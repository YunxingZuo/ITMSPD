#coding:utf-8
from numpy import *
from time import sleep
import json
import urllib2

def loadDataSet(fileName):
    numFeat = len(open(fileName).readline().split('\t')) - 1
    dataMat = []; labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = []
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat, labelMat

def standRegres(xArr, yArr):
    xMat = mat(xArr); yMat = mat(yArr).T    # xMat是(m*n)矩阵，yMat是列向量
    xTx = xMat.T * xMat
    if linalg.det(xTx) == 0.0:    # 判断行列式是否为0
        print "This matrix is singular, cannot do inverse"
        return
    ws = xTx.I * (xMat.T * yMat)    # 对(y-Xw)^T(y-Xw)求导得到 w=(XTX)^(-1)XTy
    return ws

def plotOriData(xArr, yArr, ws):
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(111)
    xMat = mat(xArr); yMat = mat(yArr)
    ax.scatter(xMat[:,1].flatten().A[0], yMat.T[:,0].flatten().A[0])    # 绘制原始数据，flatten变成横向量
    xCopy = xMat.copy()
    xCopy.sort(0)
    yHat = xCopy * ws
    ax.plot(xCopy[:,1], yHat)
    plt.show()

def lwlr(testPoint, xArr, yArr, k=1.0):
    xMat = mat(xArr); yMat = mat(yArr).T
    m = shape(xMat)[0]
    weights = mat(eye((m)))    # 创建对角权重矩阵，阶数等于样本点个数，为每个样本点创建一个相对当前测试点的权重
    for j in range(m):
        diffMat = testPoint - xMat[j,:]
        weights[j,j] = exp(diffMat*diffMat.T/(-2.0*k**2))
    xTx = xMat.T * (weights * xMat)
    if linalg.det(xTx) == 0.0:
        print "This matrix is singular, cannot do inverse"
        return
    ws = xTx.I * (xMat.T * (weights * yMat))
    return testPoint * ws

def lwlrTest(testArr, xArr, yArr, k=1.0):
    m = shape(testArr)[0]
    yHat = zeros(m)    # (1*m)行向量
    for i in range(m):
        yHat[i] = lwlr(testArr[i], xArr, yArr, k)
    return yHat

def plotLwlrData(xArr, yArr, yHat):
    import matplotlib.pyplot as plt
    xMat = mat(xArr)
    srtInd = xMat[:,1].argsort(0)    # 从小到大的序号
    xSort = xMat[srtInd][:,0,:]    # 按顺序排列的xMat
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(xSort[:,1], yHat[srtInd])
    ax.scatter(xMat[:,1].flatten().A[0], mat(yArr).T.flatten().A[0], s=2, c='red')
    plt.show()

def rssError(yArr, yHatArr):
    return ((yArr - yHatArr)**2).sum()

def ridgeRegres(xMat, yMat, lam = 0.2):    # 岭回归用于处理特征数多于样本数，因为此时xTx不满秩，不能求逆
    xTx = xMat.T * xMat
    denom = xTx + eye(shape(xMat)[1]) * lam    # w=(XTX+λI)^(-1)XTy
    if linalg.det(denom) == 0.0:
        print "This matrix is singular, cannot do inverse"
        return
    ws = denom.I * (xMat.T * yMat)
    return ws

def ridgeTest(xArr, yArr):
    import matplotlib.pyplot as plt
    xMat = mat(xArr); yMat = mat(yArr).T
    yMean = mean(yMat,0)    # 求列的平均值
    yMat = yMat - yMean
    xMeans = mean(xMat, 0)
    xVar = var(xMat, 0)    # 求列的平均方差
    xMat = (xMat - xMeans)/xVar    # 数据标准化
    numTestPts = 30    # 在30个λ上测试回归系数
    wMat = zeros((numTestPts, shape(xMat)[1]))
    for i in range(numTestPts):
        ws = ridgeRegres(xMat, yMat, exp(i-10))    # λ取非常小和非常大的值时分别对结果造成的影响
        wMat[i,:] = ws.T
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(wMat)
    plt.show()
    return wMat

def regularize(xMat):    # 特征按均值为0方差为1进行标准化处理
    inMat = xMat.copy()
    inMeans = mean(xMat, 0)
    inVar = var(xMat, 0)
    inMat = (inMat - inMeans)/inVar
    return inMat

def stageWise(xArr, yArr, eps=0.01, numIt=100):    # 前向逐步回归，贪心算法，每一步都尽可能减少误差
    xMat = mat(xArr); yMat = mat(yArr).T
    yMean = mean(yMat, 0)
    yMat = yMat - yMean
    xMat = regularize(xMat)
    m,n = shape(xMat)
    returnMat = zeros((numIt, n))
    ws = zeros((n,1)); wsTest = ws.copy(); wsMax = ws.copy()
    for i in range(numIt):    # 需要迭代numIt次
        print ws.T
        lowestError = inf;
        for j in range(n):
            for sign in [-1, 1]:    # 在每个特征上运行两次for循环，分别计算增加或减少该特征对误差的影响
                wsTest = ws.copy()
                wsTest[j] += eps * sign
                yTest = xMat * wsTest
                rssE = rssError(yMat.A, yTest.A)
                if rssE < lowestError:
                    lowestError = rssE
                    wsMax = wsTest
        ws = wsMax.copy()
        returnMat[i,:] = ws.T
    return returnMat

def searchForSet(retX, retY, setNum, yr, numPce, origPrc):
    sleep(10)
    myAPIstr = 'get from code.google.com'
    searchURL = 'https://www.googleapis.com/shopping/search/v1/public/products?key=%s&country=US&q=lego+%d&alt=json' \
                % (myAPIstr, setNum)
    pg = urllib2.urlopen(searchURL)
    retDict = json.loads(pg.read())
    for i in range(len(retDict['items'])):
        try:
            currItem = retDict['items'][i]
            if currItem['product']['condition'] == 'new':
                newFlag = 1
            else: newFlag = 0
            listOfInv = currItem['product']['inventories']
            for item in listOfInv:
                sellingPrice = item['price']
                if sellingPrice > origPrc * 0.5:
                    print "%d\t%d\t%d\t%f\t%f" % (yr, numPce, newFlag, origPrc, sellingPrice)
                    retX.append([yr, numPce, newFlag, origPrc])
                    retY.append(sellingPrice)
        except: print 'problem with item %d' % i

def setDataCollect(retX, retY):
    searchForSet(retX, retY, 8288, 2006, 800, 49.99)
    searchForSet(retX, retY, 10030, 2002, 3096, 269.99)
    searchForSet(retX, retY, 10179, 2007, 5195, 499.99)
    searchForSet(retX, retY, 10181, 2007, 3428, 199.99)
    searchForSet(retX, retY, 10189, 2008, 5922, 299.99)
    searchForSet(retX, retY, 10196, 2009, 3263, 249.99)

def crossValidation(xArr, yArr, numVal=10):
    m = len(yArr)
    indexList = range(m)
    errorMat = zeros((numVal, 30))
    for i in range(numVal):    # 30个λ每个λ算10次交叉验证
        trainX = []; trainY = []
        testX = []; testY = []
        random.shuffle(indexList)    # 把顺序打乱
        for j in range(m):
            if j < m*0.9:
                trainX.append(xArr[indexList[j]])    # 数据分为训练集和测试集
                trainY.append(yArr[indexList[j]])
            else:
                testX.append(xArr[indexList[j]])
                testY.append(yArr[indexList[j]])
        wMat = ridgeTest(trainX, trainY)    # (30*n)
        for k in range(30):    # 第k组w
            matTestX = mat(testX); matTrainX = mat(trainX)
            meanTrain = mean(matTrainX, 0)
            varTrain = var(matTrainX, 0)
            matTestX = (matTestX - meanTrain)/varTrain    # 用训练集的参数将测试数据标准化
            yEst = matTestX * mat(wMat[k,:]).T + mean(trainY)
            errorMat[i, k] = rssError(yEst.T.A, array(testY))
    meanErrors = mean(errorMat, 0)    # 每个w对应的10次的平均误差
    minMean = float(min(meanErrors))    # 最小误差
    bestWeights = wMat[nonzero(meanErrors == minMean)]
    xMat = mat(xArr); yMat = mat(yArr).T
    meanX = mean(xMat, 0); varX = var(xMat, 0)
    unReg = bestWeights/varX
    print "the best model from Ridge Regression is:\n", unReg
    print "with constant term: ", -1*sum(multiply(meanX, unReg)) + mean(yMat)
