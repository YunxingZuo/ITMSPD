#coding:utf-8
import matplotlib.pyplot as plt

decisionNode = dict(boxstyle = "sawtooth", fc = "0.8")
leafNode = dict(boxstyle = "round4", fc = "0.8")
arrow_args = dict(arrowstyle = "<-")

def plotNode(nodeTxt, centerPt, parentPt, nodeType):    # centerPt是指文本位置
    createPlot.ax1.annotate(nodeTxt, xy = parentPt, xycoords = 'axes fraction', xytext = centerPt, \
        textcoords = 'axes fraction', va = "center", ha = "center", bbox = nodeType, arrowprops = arrow_args)

# def createPlot():
    # fig = plt.figure(1, facecolor = 'white')
    # fig.clf()    # 清空绘图区
    # createPlot.ax1 = plt.subplot(111, frameon = False)
    # plotNode('a decision node', (0.5, 0.1), (0.1, 0.5), decisionNode)
    # plotNode('a leaf node', (0.8, 0.1), (0.3, 0.8), leafNode)
    # plt.show()

def getNumLeafs(myTree):    # 获得叶节点个数
    numLeafs = 0
    firstStr = myTree.keys()[0]    # 第一个特征的名称
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':    # 看看secondDict[key]是不是字典
            numLeafs += getNumLeafs(secondDict[key])    # 返回的是secondDcit[key]的叶节点数
        else: numLeafs += 1
    return numLeafs

def getTreeDepth(myTree):    # 获得树深度
    maxDepth = 0
    firstStr = myTree.keys()[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            thisDepth = 1 + getTreeDepth(secondDict[key])
        else: thisDepth = 1    # 如果是类标签，就是1，如果是字典，就是1+getTreeDepth(字典)
        if thisDepth > maxDepth: maxDepth = thisDepth
    return maxDepth

def retrieveTree(i):
    listOfTrees = [{'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}}, \
                {'no surfacing': {0: 'no', 1: {'flippers': {0: {'head': {0: 'no', 1: 'yes'}}, 1: 'no'}}}}]
    return listOfTrees[i]

def plotMidText(cntrPt, parentPt, txtString):    # 箭头中间标号
    xMid = (parentPt[0] - cntrPt[0])/2.0 + cntrPt[0]
    yMid = (parentPt[1] - cntrPt[1])/2.0 + cntrPt[1]
    createPlot.ax1.text(xMid, yMid, txtString)

def plotTree(myTree, parentPt, nodeTxt):
    numLeafs = getNumLeafs(myTree)    # 叶子节点数目
    depth = getTreeDepth(myTree)    # 深度
    firstStr = myTree.keys()[0]
    cntrPt = (plotTree.xOff + (1.0 + float(numLeafs))/2.0/plotTree.totalW, plotTree.yOff)
    plotMidText(cntrPt, parentPt, nodeTxt)
    plotNode(firstStr, cntrPt, parentPt, decisionNode)    # "no surfacing"应该在cntrPt位置上
    secondDict = myTree[firstStr]
    plotTree.yOff = plotTree.yOff - 1.0/plotTree.totalD
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':    # 递归
            plotTree(secondDict[key], cntrPt, str(key))
        else:
            plotTree.xOff = plotTree.xOff + 1.0/plotTree.totalW
            plotNode(secondDict[key], (plotTree.xOff, plotTree.yOff), cntrPt, leafNode)
            plotMidText((plotTree.xOff, plotTree.yOff), cntrPt, str(key))
    plotTree.yOff = plotTree.yOff + 1.0/plotTree.totalD    # 绘制完子树要把y轴倒回去

def createPlot(inTree):
    fig = plt.figure(1, facecolor = 'white')
    fig.clf()
    axprops = dict(xticks=[], yticks=[])    # x, y轴标签不显示
    createPlot.ax1 = plt.subplot(111, frameon=False, **axprops)
    plotTree.totalW = float(getNumLeafs(inTree))
    plotTree.totalD = float(getTreeDepth(inTree))
    plotTree.xOff = -0.5/plotTree.totalW; plotTree.yOff = 1.0;
    plotTree(inTree, (0.5, 1.0), '')
    plt.show()