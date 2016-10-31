#coding:utf-8
from numpy import *

def loadDataSet(fileName):
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = map(float, curLine)    # 将每行映射成浮点数
        dataMat.append(fltLine)
    return dataMat

def binSplitDataSet(dataSet, feature, value):    # nonzero返回非零的坐标
    mat0 = dataSet[nonzero(dataSet[:,feature] > value)[0],:][0]
    mat1 = dataSet[nonzero(dataSet[:,feature] <= value)[0],:][0]
    return mat0, mat1

def regLeaf(dataSet):
    return mean(dataSet[:,1])

def regErr(dataSet):
    return var(dataSet[:,1]) * shape(dataSet)[0]    # 返回目标变量的总方差

def chooseBestSplit(dataSet, leafType=regLeaf, errType=regErr, ops=(1,4)):    # 提前终止条件即预剪、
    tolS = ops[0]; tolN = ops[1]    # tolS是允许的最小误差下降值，tolN是切分的最少样本数
    if len(set(dataSet[:,-1].T.tolist()[0])) == 1:    # 统计不同剩余特征值的数目，如果为1，不需要再切分
        return None, leafType(dataSet)    # 返回的也就是那个特征值
    m,n = shape(dataSet)
    S = errType(dataSet)
    bestS = inf; bestIndex = 0; bestValue = 0
    for featIndex in range(n-1):    # 对每个特征
        for splitVal in set(dataSet[:,featIndex]):    # 对每个不同的特征值 
            mat0, mat1 = binSplitDataSet(dataSet, featIndex, splitVal)
            if (shape(mat0)[0] < tolN) or (shape(mat1)[0] < tolN): continue    # 如果子集太小，也不应该切分
            newS = errType(mat0) + errType(mat1)
            if newS < bestS:
                bestIndex = featIndex
                bestValue = splitVal
                bestS = newS
    if (S - bestS) < tolS:    # 切分数据集后效果提升不够大，不应该进行切分操作
        return None, leafType(dataSet)
    mat0, mat1 = binSplitDataSet(dataSet, bestIndex, bestValue)
    if (shape(mat0)[0] < tolN) or (shape(mat1) < tolN):
        return None, leafType(dataSet)
    return bestIndex, bestValue

def createTree(dataSet, leafType=regLeaf, errType=regErr, ops=(1,4)):
    feat, val = chooseBestSplit(dataSet, leafType, errType, ops)
    if feat == None: return val    # 满足停止条件，返回某类模型的值，回归树返回常数，模型树返回线性方程
    retTree = {}
    retTree['spInd'] = feat
    retTree['spVal'] = val
    lSet, rSet = binSplitDataSet(dataSet, feat, val)
    retTree['left'] = createTree(lSet, leafType, errType, ops)
    retTree['right'] = createTree(rSet, leafType, errType, ops)
    return retTree

def isTree(obj):    # 判断obj是不是树
    return (type(obj).__name__ == 'dict')

def getMean(tree):    # 对树进行塌陷处理
    if isTree(tree['right']): tree['right'] = getMean(tree['right'])
    if isTree(tree['left']): tree['left'] = getMean(tree['left'])
    return (tree['left'] + tree['right'])/2.0

def prune(tree, testData):
    if shape(testData)[0] == 0: return getMean(tree)    # 没有测试数据则对树进行塌陷处理
    if (isTree(tree['right']) or isTree(tree['left'])):
        lSet, rSet = binSplitDataSet(testData, tree['spInd'], tree['spVal'])
    if isTree(tree['left']): tree['left'] = prune(tree['left'], lSet)
    if isTree(tree['right']): tree['right'] = prune(tree['right'], rSet)
    if not isTree(tree['left']) and not isTree(tree['right']):
        lSet, rSet = binSplitDataSet(testData, tree['spInd'], tree['spVal'])
        errorNoMerge = sum(power(lSet[:,-1] - tree['left'], 2)) \
                    + sum(power(rSet[:,-1] - tree['right'], 2))    # 计算不合并的误差
        treeMean = (tree['left'] + tree['right'])/2.0
        errorMerge = sum(power(testData[:,-1] - treeMean, 2))    # 计算合并的误差
        if errorMerge < errorNoMerge:    # 如果合并降低误差，则把叶节点合并
            print "merging"
            return treeMean
        else: return tree    # 否则直接返回原树
    else: return tree    # 如果在比较误差后得不到左边和右边都是叶节点时，不用考虑，直接返回原树

def linearSolve(dataSet):
    m,n = shape(dataSet)
    X = mat(ones((m,n))); Y = mat(ones((m,1)))
    X[:,1:n] = dataSet[:,0:n-1]; Y = mat(dataSet[:,-1])    # X的第1列都是1，dataSet中数据格式化
    xTx = X.T * X
    if linalg.det(xTx) == 0.0:
        raise NameError('This matrix is singular, cannot do inverse, \n\ try increasing the second value of ops')
    ws = xTx.I * (X.T * Y)
    return ws, X, Y

def modelLeaf(dataSet):    # 负责生成叶节点线性片段，特征是ws
    ws, X, Y = linearSolve(dataSet)
    return ws

def modelErr(dataSet):
    ws, X, Y = linearSolve(dataSet)
    yHat = X * ws
    return sum(power(Y - yHat, 2))

def regTreeEval(model, inDat):    # 对回归树叶节点进行预测
    return float(model)

def modelTreeEval(model, inDat):    # 对模型树叶节点进行预测
    n = shape(inDat)[1]
    X = mat(ones((1, n+1)))
    X[:,1:n+1] = inDat    # inDat是一个n列行向量，在原数据矩阵上增加第0列
    return float(X*model)

# 自顶向下遍历整棵树，直到命中叶节点，一旦到达叶节点，在输入数据上调用modelEval()函数
def treeForeCast(tree, inData, modelEval=regTreeEval):    # 对回归树叶节点进行预测用regTreeEval，对模型树叶节点进行预测用modelTreeEval
    if not isTree(tree): return modelEval(tree, inData)    # 如果不是树，直接返回预测值
    if inData[tree['spInd']] > tree['spVal']:    # 看看inData属于给定tree的哪个叶节点
        if isTree(tree['left']):
            return treeForeCast(tree['left'], inData, modelEval)
        else:
            return modelEval(tree['left'], inData)
    else:
        if isTree(tree['right']):
            return treeForeCast(tree['right'], inData, modelEval)
        else:
            return modelEval(tree['right'], inData)


def createForeCast(tree, testData, modelEval=regTreeEval):
    m = len(testData)
    yHat = mat(zeros((m,1)))
    for i in range(m):
        yHat[i,0] = treeForeCast(tree, mat(testData[i]), modelEval)
    return yHat