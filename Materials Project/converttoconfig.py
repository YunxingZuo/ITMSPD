#coding:utf-8

from numpy import *
from math import *
import urllib
import json
import os
import shutil
import time

def downloadjson(mid):    # 下载json文件，得到字典
    apiStem = "https://www.materialsproject.org/rest/v1/materials/%s/vasp/cif?API_KEY=4pyuBOFlZiNwE9f0" % mid
    print apiStem
    c=urllib.urlopen(apiStem)
    return json.loads(c.read())

def fromciftoconfig(mid, pseduo = 'ncpp-pbe'):
    dict = downloadjson(mid)
    if dict["valid_response"] == False: return -1    # 如果response不存在， 直接返回
    else:
        rootdir = os.getcwd()
        matdict = dict["response"]
        numoftype = len(mid.split('-'))
        middir = mid + " " + pseduo
        createdir(middir)
        j = 1
        for i in range(len(matdict)):
            sth = matdict[i]["cif"].split('\n')
            if sth[15].split()[0] == '_cell_length_a':    # 筛选出符合标准的
                if len(sth[24].split()) == numoftype + 1:    # 只算有特定原子的
                    id = matdict[i]["material_id"]
                    parentdir = os.getcwd()
                    createdir('%d %s' % (j, id))    # 01 mp-250 something like that
                    j += 1
                    a = float(sth[15].split()[1])
                    b = float(sth[16].split()[1])
                    c = float(sth[17].split()[1])
                    alpha = float(sth[18].split()[1])
                    beta = float(sth[19].split()[1])
                    gamma = float(sth[20].split()[1])
                    ax, ay, az, bx, by, bz, cx, cy, cz = xandyandz(alpha, beta, gamma, a, b, c)
                    length = len(sth)
                    numofatom = length - 44    # 原子总数
                    prefix(numofatom, ax, ay, az, bx, by, bz, cx, cy, cz)
                    fwadd = open('atom.config', 'a')
                    repeatatomtype = []
                    for k in range(42, length - 2):
                        array = sth[k].split()
                        atomic = atomicnumber(array[0])
                        repeatatomtype.append(array[0])
                        x = float(array[3])
                        y = float(array[4])
                        z = float(array[5])
                        fwadd.write('\t%d\t%.12f\t%.12f\t%.12f  1  1  1\n' % (atomic, x, y, z))
                        time.sleep(0.1)
                    fwadd.close()
                    atomtype = list(set(repeatatomtype))
                    addpseduo(pseduo, atomtype)
                    addincar(atomtype, numofatom, a, b, c)
                    os.chdir(parentdir)
            time.sleep(1)
        os.chdir(rootdir)
    return

def xandyandz(alpha, beta, gamma, a, b, c):    # 对cif给出的构型进行计算得到晶格矢量
    al = alpha * pi / 180
    be = beta * pi / 180
    ga = gamma * pi / 180
    ax = a
    ay = 0
    az = 0
    bx = b * cos(ga)
    by = b * sin(ga)
    bz = 0
    cx = c * cos(be)
    cy = c * ((cos(al) - cos(ga)*cos(be))/sin(ga))
    cz = sqrt(c*c - cx**2 - cy**2)
    return ax, ay, az, bx, by, bz, cx, cy, cz

def atomicnumber(element):    # atom.comfig中要用到原子序数
    elements = {'H': 1, 'He': 2, 'Li': 3, 'Be': 4, 'B': 5, 'C': 6, \
    'N': 7, 'O': 8, 'F': 9, 'Ne': 10, 'Na': 11, 'Mg': 12, 'Al': 13, \
    'Si': 14, 'P': 15, 'S': 16, 'Cl': 17, 'Ar': 18, 'K': 19, 'Ca': 20, \
    'Sc': 21, 'Ti': 22, 'V': 23, 'Cr': 24, 'Mn': 25, 'Fe': 26, 'Co': 27, \
    'Ni': 28, 'Cu': 29, 'Zn': 30, 'Ga': 31, 'Ge': 32, 'As': 33, 'Se': 34, \
    'Br': 35, 'Kr': 36, 'Rb': 37, 'Sr': 38, 'Y': 39, 'Zr': 40, 'Nb': 41, \
    'Mo': 42, 'Tc': 43, 'Ru': 44, 'Rh': 45, 'Pd': 46, 'Ag': 47, 'Cd': 48, \
    'In': 49, 'Sn': 50, 'Sb': 51, 'Te': 52, 'I': 53, 'Xe': 54, 'Cs': 55, \
    'Ba': 56, 'Lu': 71, 'Hf': 72, 'Ta': 73, 'W': 74, 'Re': 75, 'Os': 76, \
    'Ir': 77, 'Pt': 78, 'Au': 79, 'Hg': 80, 'Tl': 81, 'Pb': 82, 'Bi': 83, \
    'Po': 84, 'At': 85, 'Rn': 86}
    return elements[element]

def prefix(numofatom, ax, ay, az, bx, by, bz, cx, cy, cz):    # 对每个atom.config写个抬头
    fw = open('atom.config', 'w')
    fw.write('\t%d\n' % numofatom)
    fw.write("Lattice vector\n")
    fw.write('\t%.10f\t%.10f\t%.10f\n' % (ax, ay, az))
    fw.write('\t%.10f\t%.10f\t%.10f\n' % (bx, by, bz))
    fw.write('\t%.10f\t%.10f\t%.10f\n' % (cx, cy, cz))
    fw.write("Position, move_x, move_y, move_z\n")
    fw.close()

def createdir(childir):    # 在当前目录下创建指定名字文件夹并进入
    currentdir = os.getcwd()
    nextdir = os.path.join(currentdir, childir)
    os.mkdir(nextdir)
    os.chdir(nextdir)

def addpseduo(pseduo, atomtype):    # 添加赝势文件
    parentdir = 'D:\\pseudo\\pseudopotential'
    listname = os.listdir(parentdir)
    for i in range(len(listname)):
        if listname[i] == pseduo:
            dir = os.path.join(parentdir, listname[i])
            atom = os.listdir(dir)
            for j in range(len(atomtype)):
                for k in range(len(atom)):
                    if atomtype[j] == atom[k]:
                        shutil.copy(os.path.join(dir, atomtype[j]), os.getcwd())

def addincar(atomtype, numofatom, lx, ly, lz):    # 复制并修改etot.incar
    incar = "D:\\pseudo\\etot.input"
    shutil.copy(incar, os.getcwd())
    fw = open('etot.input', 'r+')
    content = fw.readlines()
    Xk, Yk, Zk = autokpoints(numofatom, lx, ly, lz)
    content.insert(3, '    MP_N123 = %d %d %d 0 0 0\n' % (Xk, Yk, Zk))
    number = 1 
    position = 3
    for i in range(len(atomtype)):
        content.insert(position, '    in.psp%d = %s\n' % (number, atomtype[i]))
        number += 1
        position += 1
    fw = open('etot.input', 'w+')
    fw.writelines(content)
    fw.close()

def autokpoints(numofatom, lx, ly, lz):
    numofkpoints = round(1000.0 / numofatom)
    X = ly * lz
    Y = lx * lz
    Z = lx * ly
    k = power(numofkpoints/(X * Y * Z), 1/3.0)
    Xk = int(round(X * k))
    Yk = int(round(Y * k))
    Zk = int(round(Z * k))
    return Xk, Yk, Zk