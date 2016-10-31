#coding:utf-8
from numpy import *
from os import listdir    # 从os模块中导入函数listdir，它可以列出给定目录的文件名
import operator    # 导入运算符模块

def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]    # 有多少个已知类别的数据点
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet    # 把inX重复dataSetSize行1列
    sqDiffMat = diffMat**2    # 数列内元素平方
    sqDistances = sqDiffMat.sum(axis=1)    # 把每一行向量相加
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()    # 从小到大的序号
    classCount={}
    for i in range(k):    # 取k个最近邻
        voteIlabel = labels[sortedDistIndicies[i]]    # 按第二个元素的次序排列
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1    # 如果classCount里没有voteIlabel，返回0。如果有，返回键voteIlabel对应的值
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]    # classCount = {'A':1, 'B':2}

def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)    # 得到文件行数
    returnMat = zeros((numberOfLines, 3))
    intermeLabel = []
    classLabelVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip()    # 截取掉所有的回车字符
        listFromLine = line.split('\t')    # 使用tab字符将整行数据分割成一个元素列表
        returnMat[index,:] = listFromLine[0:3]    # 把前三个元素存储到特征矩阵
        classLabelVector.append(int(listFromLine[-1]))
        # intermeLabel.append(listFromLine[-1])        # 使用索引值-1表示列表中的最后一列元素
        # if (intermeLabel[index] == 'largeDoses'): classLabelVector.append(3)
        # elif (intermeLabel[index] == 'smallDoses'): classLabelVector.append(2)
        # elif (intermeLabel[index] == 'didntLike'): classLabelVector.append(1)
        index += 1
    return returnMat, classLabelVector

def autoNorm(dataSet):
    minVals = dataSet.min(0)    # .min(0)每一列取出最小值组成一行，.max(0)每一行取出最小值组成一列
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m,1))
    normDataSet = normDataSet/tile(ranges, (m,1))
    return normDataSet, ranges, minVals

def datingClassTest():
    hoRatio = 0.10
    datingDataMat, datingLabels = file2matrix('datingTestSet.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)    # 10%数据用于测试
    errorCount = 0
    for i in range(numTestVecs):    # 剩余90%作为训练
        classifierResult = classify0(normMat[i,:], normMat[numTestVecs:m,:], datingLabels[numTestVecs:m], 3)
        print "the classifier came back with: %d, the real answer is: %d" % (classifierResult, datingLabels[i])
        if (classifierResult != datingLabels[i]): errorCount += 1.0
    print "the total error rate is: %f" % (errorCount/float(numTestVecs))

def classifyPerson():
    resultList = ['not at all', 'in small doses', 'in large doses']
    percentTats = float(raw_input("percentage of time spent playing video games?"))
    ffMiles = float(raw_input("frequent flier miles earned per year?"))    # raw_input()允许用户输入文本行命令并返回用户输入的命令
    iceCream = float(raw_input("liters of ice cream consumed per year?"))
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    inArr = array([ffMiles, percentTats, iceCream])
    classifierResult = classify0((inArr-minVals)/ranges, normMat, datingLabels, 3)    # 归一化
    print "You will probably like this person: ", resultList[classifierResult - 1]

def img2vector(filename):
    returnVect = zeros((1, 1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()    # 逐行读取
        for j in range(32):
            returnVect[0, 32*i+j] = int(lineStr[j])    # 把32行数据整合到1行
    return returnVect

def handwritingClassTest():
    hwLabels = []
    trainingFileList = listdir('trainingDigits')    # 把trainingDigits目录下的文件名列出来
    m = len(trainingFileList)
    trainingMat = zeros((m, 1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])    # 把类别标签提取出来
        hwLabels.append(classNumStr)
        trainingMat[i,:] = img2vector('trainingDigits/%s' % fileNameStr)
    testFileList = listdir('testDigits')
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])    # 已知正确的标签
        vectorUnderTest = img2vector('testDigits/%s' % fileNameStr)
        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)
        print "the classifier came back with: %d, the real answer is: %d" % (classifierResult, classNumStr)
        if (classifierResult != classNumStr): errorCount += 1.0
    print "\nthe total number of errors is: %d" % errorCount
    print "\nthe total error rate is: %f" % (errorCount/float(mTest))