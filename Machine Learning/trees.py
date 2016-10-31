#coding:utf-8
from math import log
import operator

def calcShannonEnt(dataSet):    # 香农熵H=-Σ p(x)log2p(x)
    numEntries = len(dataSet)    # 行数
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]    # 创建一个数据字典，它的键值是最后一列数值
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0    # 如果当前键值不存在，则扩展字典并将当前键值加入字典
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt

def createDataSet():
    dataSet = [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels

def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:    # axis是特征值的位置，如果有满足要求的特征值
            reducedFeatVec = featVec[:axis]    # 则将满足要求的列表除特征值外添加到新创建的列表中
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1    # 特征的个数
    baseEntropy = calcShannonEnt(dataSet)    # 原始香农熵
    bestInfoGain = 0.0; bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]    # 将数据集中所有第i个特征值抽取出来
        uniqueVals = set(featList)    # 包含featList中所有不同的值
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy    # 信息增益是熵的减少或是数据无序度的减少
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature

def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys(): classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(), key = operator.itemgetter(1), reverse = True)
    return sortedClassCount[0][0]

def createTree(dataSet, labels):    # 把决策树看成嵌套叶子节点信息的字典数据
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):    # 所有类标签完全相同，则直接返回该类标签
        return classList[0]
    if len(dataSet[0]) == 1:    # 使用完所有特征仍不能将数据完全划分，则返回出现次数最多的类别
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatlabel = labels[bestFeat]
    myTree = {bestFeatlabel:{}}    # 嵌套开始
    del(labels[bestFeat])    # 特征一经使用就舍弃
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]    # 直接复制
        myTree[bestFeatlabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
    return myTree

def classify(inputTree, featLabels, testVec):
    firstStr = inputTree.keys()[0]
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)    # 将标签字符串转换为索引
    for key in secondDict.keys():
        if testVec[featIndex] == key:
            if type(secondDict[key]).__name__ == 'dict':
                classLabel = classify(secondDict[key], featLabels, testVec)
            else: classLabel = secondDict[key]
    return classLabel

def storeTree(inputTree, filename):    # 使用pickle模块存储决策树
    import pickle
    fw = open(filename, 'w')
    pickle.dump(inputTree, fw)
    fw.close()

def grabTree(filename):
    import pickle
    fr = open(filename)
    return pickle.load(fr)

def lensestest(filename):
    fr = open(filename)
    lenses = [inst.strip().split('\t') for inst in fr.readlines()]
    lensesLabels = ['age', 'prescript', 'astigmatic', 'tearRate']
    lensesTree = createTree(lenses, lensesLabels)
    return lensesTree