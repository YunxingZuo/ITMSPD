#coding:utf-8
from numpy import *

def loadDataSet():
    return [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]

def createC1(dataSet):    # C1是大小为1的所有候选项集的集合
    C1 = []
    for transaction in dataSet:    # 对每一条交易记录
        for item in transaction:    # 遍历记录中的每一个项
            if not [item] in C1:
                C1.append([item])    # 添加只包含该物品项的一个列表
    C1.sort()
    return map(frozenset, C1)    # 对C1中每个列表取frozenset

def scanD(D, Ck, minSupport):    # Ck是候选项集列表
    ssCnt = {}
    for tid in D:
        for can in Ck:
            if can.issubset(tid):    # 如果集合是记录的一部分，那么增加字典中对应的计数值
                if not ssCnt.has_key(can): ssCnt[can] = 1
                else: ssCnt[can] += 1
    numItems = float(len(D))
    retList = []
    supportData = {}
    for key in ssCnt:
        support = ssCnt[key]/numItems
        if support >= minSupport:    # 包含满足最小支持度要求的集合
            retList.insert(0, key)    # 在第0位置插入key
        supportData[key] = support
    return retList, supportData

def aprioriGen(Lk, k):    # Lk中的项集合并构成Ck
    retList = []
    lenLk = len(Lk)
    for i in range(lenLk):
        for j in range(i+1, lenLk):
            L1 = list(Lk[i])[:k-2]; L2 = list(Lk[j])[:k-2]    # 取list(Lk[i])中的前k-2个元素
            L1.sort(); L2.sort()
            if L1 == L2:    # 如果两个集合前面k-2个元素都相等，将这两个集合合成大小为k的集合
                retList.append(Lk[i] | Lk[j])
    return retList

def apriori(dataSet, minSupport = 0.5):
    C1 = createC1(dataSet)
    D = map(set, dataSet)
    L1, supportData = scanD(D, C1, minSupport)
    L = [L1]    # 满足支持度要求的大小为1的候选项集的集合，L[0] = L1
    k = 2
    while (len(L[k-2]) > 0):
        Ck = aprioriGen(L[k-2], k)    # L会包含L1，L2，L3···C2 = aprioriGen(L1, 2)
        Lk, supK = scanD(D, Ck, minSupport)    # 使用scanD()基于Ck创建Lk
        supportData.update(supK)
        L.append(Lk)    # 把L1，L2，L3一行行加进L
        k += 1
    return L, supportData

def generateRules(L, supportData, minConf = 0.7):
    bigRuleList = []
    for i in range(1, len(L)):    # 只获得有两个或更多元素的集合
        for freqSet in L[i]:    # 遍历L中的每一个频繁项集
            H1 = [frozenset([item]) for item in freqSet]    # 对每个频繁项集创建只包含单个元素集合的列表H1
            if (i > 1):
                rulesFromConseq(freqSet, H1, supportData, bigRuleList, minConf)
            else:
                calcConf(freqSet, H1, supportData, bigRuleList, minConf)    # 项集中只有两个元素，直接使用calcConf计算可信度
    return bigRuleList

def calcConf(freqSet, H, supportData, br1, minConf = 0.7):
    prunedH = []
    for conseq in H:    # 遍历所有项集计算可信度
        conf = supportData[freqSet]/supportData[freqSet - conseq]
        if conf >= minConf:
            print freqSet - conseq, '-->', conseq, 'conf: ', conf
            br1.append((freqSet - conseq, conseq, conf))
            prunedH.append(conseq)    # 保存满足最小可信度要求的规则的后件，如果本身不满足，则所有含此后件子集的后件的规则都不满足
    return prunedH

def rulesFromConseq(freqSet, H, supportData, br1, minConf = 0.7):
    m = len(H[0])    # 计算H中的频繁项集子集大小m
    if (len(freqSet) > (m+1)):    # 看该频繁项集是否大到可以移除大小为m的子集，后面calcConf要用
        Hmp1 = aprioriGen(H, m+1)    # 生成H中元素的无重复组合
        Hmp1 = calcConf(freqSet, Hmp1, supportData, br1, minConf)    # 测试这些后件的规则的可信度
        if (len(Hmp1) > 1):    # 如果不止一条规则满足要求，则继续用rulesFromConseq组合
            rulesFromConseq(freqSet, Hmp1, supportData, br1, minConf)