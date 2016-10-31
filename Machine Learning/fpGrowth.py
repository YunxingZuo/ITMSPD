#coding:utf-8
from numpy import *

class treeNode:
    def __init__(self, nameValue, numOccur, parentNode):
        self.name = nameValue
        self.count = numOccur
        self.nodeLink = None    # 链接相似的元素
        self.parent = parentNode    # 父节点
        self.children = {}

    def inc(self, numOccur):
        self.count += numOccur

    def disp(self, ind=1):
        print '  '*ind, self.name, ' ', self.count
        for child in self.children.values():
            child.disp(ind+1)

def createTree(dataSet, minSup = 1):
    headerTable = {}
    for trans in dataSet:    # trans是键值
        for item in trans:    # dataSet[trans]是trans出现的次数，此处item是字母
            headerTable[item] = headerTable.get(item, 0) + dataSet[trans]    # 如果item在字典中返回item的值，否则返回0
    for k in headerTable.keys():
        if headerTable[k] < minSup:
            del(headerTable[k])    # 移除不满足最小支持度的单元素项
    freqItemSet = set(headerTable.keys())
    if len(freqItemSet) == 0: return None, None
    for k in headerTable:
        headerTable[k] = [headerTable[k], None]    # headerTable = {'e': [1, None]...'z': [5, None]}
    retTree = treeNode('Null Set', 1, None)
    for tranSet, count in dataSet.items():    # items()返回(key, value)
        localD = {}
        for item in tranSet:
            if item in freqItemSet:
                localD[item] = headerTable[item][0]    # localD和headerTable相同
        if len(localD) > 0:    # 对第一条tranSet，orderedItems = ['z', 'x', 's'...] 按键值排序后只取键
            orderedItems = [v[0] for v in sorted(localD.items(), key=lambda p: p[1], reverse=True)]
            updateTree(orderedItems, retTree, headerTable, count)
    return retTree, headerTable

def updateTree(items, inTree, headerTable, count):
    if items[0] in inTree.children:    # 测试事务中的第一个元素项是否作为子节点存在
        inTree.children[items[0]].inc(count)    # 如果存在，更新该元素项的计数，头指针表该元素项指向的节点也不变
    else:
        inTree.children[items[0]] = treeNode(items[0], count, inTree)    # 不存在则创建一个新的子节点添加到树中
        if headerTable[items[0]][1] == None:
            headerTable[items[0]][1] = inTree.children[items[0]]    # {···'x': [4, treeNode('x', 1, treeNode('z', 1, retTree))]···}
        else:
            updateHeader(headerTable[items[0]][1], inTree.children[items[0]])
    if len(items) > 1:    # 对这个tranSet中的剩余单元素项迭代调用updateTree，每次调用时去掉列表中第一个元素
        updateTree(items[1::], inTree.children[items[0]], headerTable, count)

def updateHeader(nodeToTest, targetNode):    # 假设'x'指向node1，node2，node3，uH(1,2)时node1没有nodeLink，
    while (nodeToTest.nodeLink != None):    # 此时node1的nodeLink等于node2，uH(1,3)时node1有nodeLink，此时
        nodeToTest = nodeToTest.nodeLink    # node1被node2取代，node2没有nodeLink，故node2的nodeLink等于
    nodeToTest.nodeLink = targetNode    # node3

def loadSimpDat():
    simpDat = [['r', 'z', 'h', 'j', 'p'], \
                ['z', 'y', 'x', 'w', 'v', 'u', 't', 's'], \
                ['z'], \
                ['r', 'x', 'n', 'o', 's'], \
                ['y', 'r', 'x', 'z', 'q', 't', 'p'], \
                ['y', 'z', 'x', 'e', 'q', 's', 't', 'm']]
    return simpDat

def createInitSet(dataSet):    # 从列表到字典
    retDict = {}
    for trans in dataSet:
        retDict[frozenset(trans)] = 1
    return retDict

def ascendTree(leafNode, prefixPath):    # 得到前缀路径加本身
    if leafNode.parent != None:
        prefixPath.append(leafNode.name)
        ascendTree(leafNode.parent, prefixPath)

def findPrefixPath(basePat, treeNode):    # 使用头指针表来指向该类型的第一个元素项，该元素项会链接到后续元素项
    condPats = {}
    while treeNode != None:
        prefixPath = []
        ascendTree(treeNode, prefixPath)
        if len(prefixPath) > 1:
            condPats[frozenset(prefixPath[1:])] = treeNode.count    # 把本身去掉，只留下前缀路径
        treeNode = treeNode.nodeLink
    return condPats

def mineTree(inTree, headerTable, minSup, preFix, freqItemList):
    bigL = [v[0] for v in sorted(headerTable.items(), key=lambda p: p[1])]    # 对头指针表中的元素项按出现频率从小到大排序
    for basePat in bigL:
        newFreqSet = preFix.copy()
        newFreqSet.add(basePat)
        freqItemList.append(newFreqSet)
        condPattBases = findPrefixPath(basePat, headerTable[basePat][1])    # 创键前缀路径
        myCondTree, myHead = createTree(condPattBases, minSup)    # 遍历所有前缀路径得到headerTable
        if myHead != None:
            print 'conditional tree for: ', newFreqSet
            myCondTree.disp(1)
            mineTree(myCondTree, myHead, minSup, newFreqSet, freqItemList)    # 用新的headerTable迭代
