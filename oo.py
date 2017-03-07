# coding: utf-8
# Copyright © 2016 YunXing Zuo

import re
import numpy as np
import urllib
import json
from sp_dict import sp_dict
from monty.serialization import loadfn
from wyckoffss import *
from structure import *

__author__ = 'YunXing Zuo'
__email__ = 'zuoyx@pkusz.edu.cn'
__date__ = 'Nov. 12, 2016'

SYMM_DATA = loadfn('symm_data.yaml')
subgroup_dict = SYMM_DATA['maximal_subgroups']
def connect(index):
    l = []
    for k, v in subgroup_dict.items():
        if k == index:
            l.extend(v)
        elif index in v:
            l.append(k)
        else:
            continue
    if index in l:
        l.remove(index)
    return l

def spacegroup_graph():
    graph = np.zeros((230, 230))
    for i in range(1, 231):
        for j in connect(i):
            graph[i-1][j-1] = 1
    Shortest_Path = []
    for i in range(1, 231):
        Shortest_Path.append(shortest_path(i, graph))
    Shortest_Path = np.array(Shortest_Path, dtype=int)
    return Shortest_Path

def shortest_path(index, mat):
    mat[mat != 1] = 999
    np.einsum('ii->i', mat)[:] = 0
    current = index - 1
    result = mat[current].copy()
    current_distance = result[current]
    neis = np.where(mat[current] == 1)[0]
    unvisited = range(len(mat))
    while True:
        for nei in neis:
            if nei not in unvisited:
                continue
            new_distance = current_distance + 1
            if result[nei] > new_distance:
                result[nei] = new_distance
        unvisited.remove(current)
        if not unvisited: break
        candidate = list(set(unvisited).intersection(set(neis)))
        if candidate:
            current = candidate[0]
        else:
            current = unvisited[0]
        current_distance = result[current]
        neis = np.where(mat[current] == 1)[0]
    return result

def downloadjson(mid):    # 下载json文件，得到字典
    apiStem = "https://www.materialsproject.org/rest/v1/materials/%s/vasp/?API_KEY=4pyuBOFlZiNwE9f0" % mid
    print apiStem
    c=urllib.urlopen(apiStem)
    return json.loads(c.read())

def numbers_consider(mid):
    dict = downloadjson(mid)
    if dict["valid_response"] == False: return -1    # 如果response不存在， 直接返回
    else:
        matdict = dict['response']
        numoftype = len(mid.split('-'))
        number_set = []
        for i in range(len(matdict)):
            s = matdict[i]['cif']
            numofspecies = len(re.search(r'_chemical_formula_sum\s*(.*)', s).group(1).split())
            if numofspecies == numoftype:
                number_set.append(matdict[i]['spacegroup']['number'])
    return np.unique(number_set)

def shortest_path_sum(mid, index, Shortest_Path):
    index = index - 1
    numbers_set = numbers_consider(mid)
    return sum(Shortest_Path[:][index][np.unique(numbers_set) - 1])

#promising_index = 0
#j = 0
#number_set = numbers_consider(mid)
#for i in range(1, 231):
    #sum_hehe = sum(graph[:][i-1][np.unique(number_set) - 1])
    #number_sum.append(sum_hehe)
#b = zip(number_sum, range(len(number_sum)))
#b.sort(lambda x: x[0])
#c = [x[1] for x in b]
