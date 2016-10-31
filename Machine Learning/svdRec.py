#coding:utf-8
from numpy import *
from numpy import linalg as la

def loadExData():
    return [[1, 1, 1, 0, 0],
            [2, 2, 2, 0, 0],
            [1, 1, 1, 0, 0],
            [5, 5, 5, 0, 0],
            [1, 1, 0, 2, 2],
            [0, 0, 0, 3, 3],
            [0, 0, 0, 1, 1]]

def loadExData2():
    return[[0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 5],
           [0, 0, 0, 3, 0, 4, 0, 0, 0, 0, 3],
           [0, 0, 0, 0, 4, 0, 0, 1, 0, 4, 0],
           [3, 3, 4, 0, 0, 0, 0, 2, 2, 0, 0],
           [5, 4, 5, 0, 0, 0, 0, 5, 5, 0, 0],
           [0, 0, 0, 0, 5, 0, 1, 0, 0, 5, 0],
           [4, 3, 4, 0, 0, 0, 0, 5, 5, 0, 1],
           [0, 0, 0, 4, 0, 4, 0, 0, 0, 0, 4],
           [0, 0, 0, 2, 0, 2, 5, 0, 0, 1, 2],
           [0, 0, 0, 0, 5, 0, 0, 0, 0, 4, 0],
           [1, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0]]

def eulidSim(inA, inB):    # 计算欧式距离
    return 1.0/(1.0 + la.norm(inA - inB))    # 相似度=1/(1+距离)，归一化到0~1

def pearsSim(inA, inB):
    if len(inA) < 3: return 1.0    # 如果不存在三个点以上，返回1.0，因为此时两个向量完全相关
    return 0.5 + 0.5 * corrcoef(inA, inB, rowvar=0)[0][1]    # 归一化到0~1

def cosSim(inA, inB):
    num = float(inA.T*inB)
    denom = la.norm(inA) * la.norm(inB)
    return 0.5 + 0.5 * float(num/denom)

def standEst(dataMat, user, simMeas, item):    # 对某个指定用户和某个指定物品
    n = shape(dataMat)[1]    # 物品数目
    simTotal = 0.0; ratSimTotal = 0.0
    for j in range(n):
        userRating = dataMat[user, j]
        if userRating == 0: continue    # 遍历用户行中每个物品，如果某个物品评分为0，跳过该物品
        overLap = nonzero(logical_and(dataMat[:,item].A > 0, dataMat[:,j].A > 0))[0]
        # 第item列和第j列同时大于0的行数为True，否则为False
        if len(overLap) == 0: similarity = 0    # 如果这么多用户都没有同时大于0的，则相似度为0
        else: similarity = simMeas(dataMat[overLap, item], dataMat[overLap, j])
        print 'the %d and %d similarity is: %f' % (item, j, similarity)
        simTotal += similarity
        ratSimTotal += similarity * userRating    # 对未评级物品进行别的已评级物品的相似度计算，再由用户对
    if simTotal == 0: return 0                    # 已评级物品的评分给出权重
    else: return ratSimTotal/simTotal

def recommend(dataMat, user, N=3, simMeas = cosSim, estMethod = standEst):
    unratedItems = nonzero(dataMat[user,:].A == 0)[1]    # 未评级物品的列序号
    if len(unratedItems) == 0: return 'you rated everything'    # 如果不存在未评分物品，则退出函数
    itemScores = []
    for item in unratedItems:    # 在所有未评分物品上进行循环
        estimatedScore = estMethod(dataMat, user, simMeas, item)    # 产生该物品的预测得分
        itemScores.append((item, estimatedScore))    # 物品编号和预测得分值放在元素列表itemScore中
    return sorted(itemScores, key=lambda jj: jj[1], reverse=True)[:N]    # 按从大到小排序返回前N个值

def svdEst(dataMat, user, simMeas, item):
    n = shape(dataMat)[1]
    simTotal = 0.0; ratSimTotal = 0.0
    U, Sigma, VT = la.svd(dataMat)
    Sig4 = mat(eye(4) * Sigma[:4])    # 建立能量大于总能量90%的几维对角矩阵
    xformedItems = dataMat.T * U[:,:4] * Sig4.I    # 构建转换后的物品
    for j in range(n):
        userRating = dataMat[user, j]
        if userRating == 0 or j == item: continue
        similarity = simMeas(xformedItems[item,:].T, xformedItems[j,:].T)
        print 'the %d and %d similarity is: %f' % (item, j, similarity)
        simTotal += similarity
        ratSimTotal += similarity * userRating
    if simTotal == 0: return 0
    else: return ratSimTotal/simTotal

def printMat(inMat, thresh=0.8):
    for i in range(32):
        for k in range(32):
            if float(inMat[i, k] > thresh):
                print 1,
            else: print 0,
        print ' '

def imgCompress(numSV = 3, thresh = 0.8):
    myl = []
    for line in open('0_5.txt').readlines():
        newRow = []
        for i in range(32):
            newRow.append(int(line[i]))
        myl.append(newRow)
    myMat = mat(myl)
    print "****original matrix*****"
    printMat(myMat, thresh)
    U, Sigma, VT = la.svd(myMat)    # 对原图像进行svd分解
    SigRecon = mat(zeros((numSV, numSV)))
    for k in range(numSV):
        SigRecon[k, k] = Sigma[k]    # 允许基于任意给定奇异值数目来重构图像
    reconMat = U[:,:numSV] * SigRecon * VT[:numSV,:]    # 重构图像
    print "****reconstructed matrix using %d singular values*****" % numSV
    printMat(reconMat, thresh)