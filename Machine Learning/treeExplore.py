#coding:utf-8
from numpy import *

from Tkinter import *
import regTrees

import matplotlib
matplotlib.use('TkAgg')    # 设定后端为TkAgg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg    # 将TkAgg和Matplotlib图链接起来
from matplotlib.figure import Figure

def reDraw(tolS, tolN):
    reDraw.f.clf()    # 清空之前的图像
    reDraw.a = reDraw.f.add_subplot(111)
    if chkBtnVar.get():    # 检查复选框是否选中，选中构建模型树，没选中构建回归树
        if tolN < 2: tolN = 2
        myTree = regTrees.createTree(reDraw.rawDat, regTrees.modelLeaf, regTrees.modelErr, (tolS, tolN))
        yHat = regTrees.createForeCast(myTree, reDraw.testDat, regTrees.modelTreeEval)
    else:
        myTree = regTrees.createTree(reDraw.rawDat, ops=(tolS, tolN))
        yHat = regTrees.createForeCast(myTree, reDraw.testDat)
    reDraw.a.scatter(reDraw.rawDat[:,0], reDraw.rawDat[:,1], s=5)
    reDraw.a.plot(reDraw.testDat, yHat, linewidth=2.0)
    reDraw.canvas.show()

def getInputs():
    try: tolN = int(tolNentry.get())    # 得到用户输入的文本，try：可以把输入文本解析成整数就继续执行
    except:    # 如果不能识别则输出错误信息，同时清空输入框并恢复默认值
        tolN = 10
        print "enter Integer for tolN"
        tolNentry.delete(0, END)
        tolNentry.insert(0, '10')
    try: tolS = float(tolSentry.get())
    except:
        tolS = 1.0
        print "enter Float for tolS"
        tolSentry.delete(0, END)
        tolSentry.insert(0, '1.0')
    return tolN, tolS

def drawNewTree():
    tolN, tolS = getInputs()
    reDraw(tolS, tolN)

root = Tk()    # 创造根部件

reDraw.f = Figure(figsize=(5,4), dpi=100)    # 插入标签，用.grid()方法设定行和列的位置
reDraw.canvas = FigureCanvasTkAgg(reDraw.f, master=root)
reDraw.canvas.show()
reDraw.canvas.get_tk_widget().grid(row=0, columnspan=3)

Label(root, text="tolN").grid(row=1, column=0)    # 设定columnspan和rowspan的值允许小部件跨行或跨列
tolNentry = Entry(root)    # 文本输入框
tolNentry.grid(row=1, column=1)
tolNentry.insert(0, '10')
Label(root, text="tolS").grid(row=2, column=0)
tolSentry = Entry(root)
tolSentry.grid(row=2, column=1)
tolSentry.insert(0, '1.0')    # 在有人点击ReDraw按钮时就会调用drawNewTree函数
Button(root, text="ReDraw", command=drawNewTree).grid(row=1, column=2, rowspan=3)

chkBtnVar = IntVar()
chkBtn = Checkbutton(root, text="Model Tree", variable = chkBtnVar)    # 为了读取Checkbutton状态要创建一个变量
chkBtn.grid(row=3, column=0, columnspan=2)

reDraw.rawDat = mat(regTrees.loadDataSet('sine.txt'))
reDraw.testDat = arange(min(reDraw.rawDat[:,0]), max(reDraw.rawDat[:,0]), 0.01)    # 测试集的点分布均匀

reDraw(1.0, 10)

root.mainloop()