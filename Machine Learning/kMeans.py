#coding:utf-8
from numpy import *

def loadDataSet(fileName):
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = map(float, curLine)
        dataMat.append(fltLine)
    return dataMat

def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2)))    # 计算向量的距离

def randCent(dataSet, k):    # 随机生成k个质心
    n = shape(dataSet)[1]    # 质心是n维
    centroids = mat(zeros((k,n)))
    for j in range(n):
        minJ = min(dataSet[:,j])
        rangeJ = float(max(dataSet[:,j] - minJ))
        centroids[:,j] = minJ + rangeJ * random.rand(k,1)    # 在每一维的最小值和最大值之间生成0到1的随机数
    return centroids

def kMeans(dataSet, k, distMeas=distEclud, createCent=randCent):
    m = shape(dataSet)[0]    # 点的个数
    clusterAssment = mat(zeros((m,2)))
    centroids = createCent(dataSet, k)
    clusterChanged = True
    while clusterChanged:    # 反复迭代，直到所有数据点的簇分配结果不再改变为止
        clusterChanged = False
        for i in range(m):    # 遍历每个点
            minDist = inf; minIndex = -1
            for j in range(k):    # 对每个点遍历所有质点
                distJI = distMeas(centroids[j,:], dataSet[i,:])
                if distJI < minDist:
                    minDist = distJI; minIndex = j    # 找到与第i个点最近的质点
            if clusterAssment[i,0] != minIndex: clusterChanged = True    # 如果任一点的簇分配结果发生变化，更新clusterChanged的标志
            clusterAssment[i,:] = minIndex, minDist**2    # 一列记录簇索引值，第二列存储误差
        print centroids
        for cent in range(k):
            ptsInClust = dataSet[nonzero(clusterAssment[:,0].A == cent)[0]]    # 通过数组过滤获得给定簇的所有点
            centroids[cent,:] = mean(ptsInClust, axis = 0)    # 沿矩阵列方向进行均值计算
    return centroids, clusterAssment

def biKmeans(dataSet, k, distMeas=distEclud):    # 二分K-均值算法，将所有点作为一个簇，然后选最大程度降低SSE值的簇进行划分
    m = shape(dataSet)[0]
    clusterAssment = mat(zeros((m,2)))
    centroid0 = mean(dataSet, axis = 0).tolist()[0]
    centList = [centroid0]
    for j in range(m):
        clusterAssment[j,1] = distMeas(mat(centroid0), dataSet[j,:])**2
    while (len(centList) < k):
        lowestSSE = inf
        for i in range(len(centList)):    # 对每个簇
            ptsInCurrCluster = dataSet[nonzero(clusterAssment[:,0].A == i)[0],:]    # 将该簇所有点看成一个小的数据集
            centroidMat, splitClustAss = kMeans(ptsInCurrCluster, 2, distMeas)    # 每个簇划分成两个簇
            sseSplit = sum(splitClustAss[:,1])
            sseNotSplit = sum(clusterAssment[nonzero(clusterAssment[:,0].A != i)[0],1])
            print "sseSplit, and notSplit: ", sseSplit, sseNotSplit
            if (sseSplit + sseNotSplit) < lowestSSE:    # 划分簇和剩余数据集误差之和作为本次划分的误差
                bestCentToSplit = i
                bestNewCents = centroidMat
                bestClustAss = splitClustAss.copy()
                lowestSSE = sseSplit + sseNotSplit
        bestClustAss[nonzero(bestClustAss[:,0].A == 1)[0], 0] == len(centList)    # 编号为1的结果簇将簇编号改为新加簇的编号
        bestClustAss[nonzero(bestClustAss[:,0].A == 0)[0], 0] == bestCentToSplit    # 编号为0的结果簇改为划分簇的编号
        print 'the bestCentToSplit is: ', bestCentToSplit
        print 'the len of bestClustAss is: ', len(bestClustAss)
        centList[bestCentToSplit] = bestNewCents[0,:].tolist()[0]    # 划分簇的质心坐标变为编号为0的质心坐标
        centList.append(bestNewCents[1,:].tolist()[0])    # 新加簇的质心坐标为编号为1的质心坐标
        clusterAssment[nonzero(clusterAssment[:,0].A == bestCentToSplit)[0],:] = bestClustAss
    return mat(centList), clusterAssment

import urllib
import json
def geoGrab(stAddress, city):
    apiStem = 'http://where.yahooapis.com/geocode?'
    params = {}
    params['flags'] = 'J'
    params['appid'] = 'ppp68N8t'
    params['location'] = '%s %s' % (stAddress, city)
    url_params = urllib.urlencode(params)
    yahooApi = apiStem + url_params
    print yahooApi
    c=urllib.urlopen(yahooApi)
    return json.loads(c.read())

from time import sleep
def massPlaceFind(fileName):
    fw = open('places.txt', 'w')
    for line in open(fileName).readlines():
        line = line.strip()
        lineArr = line.split('\t')
        retDict = geoGrab(lineArr[1], lineArr[2])
        if retDict['ResultSet']['Error'] == 0:
            lat = float(retDict['ResultSet']['Results'][0]['latitude'])
            lng = float(retDict['ResultSet']['Results'][0]['longitude'])
            print "%s\t%f\t%f" % (lineArr[0], lat, lng)
            fw.write('%s\t%f\t%f\n' % (line, lat, lng))
        else: print "error fetching"
        sleep(1)
    fw.close()