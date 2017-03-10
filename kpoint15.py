# coding: utf-8
# Copyright © 2016 YunXing Zuo

import numpy as np
import json
import os
from structure import *
from high_symmetry_Kpoints import *

def trans_from_30_to_15(num_interval = 15):
    rootdir = os.getcwd()
    l = os.listdir(rootdir)
    for i in l:
        print i
        directory = os.path.join(rootdir, i)
        if os.path.isdir(directory):
            os.chdir(directory)
#            path15file = os.path.join(directory, 'Path15')
#            if os.path.exists(path15file):
#                os.chdir(rootdir)
#                continue
            s = Structure.import_from_pwmat('atom.config')
            points = Find_Kpoints_Path(s, num_interval = num_interval)
            lines = []
            lines.append('{:12d}'.format(len(points)))
            lines.append('\t2\t0')
            weight = 1.
            for coord in points:
                lines.append('{0[0]:>16.8f}{0[1]:>16.8f}{0[2]:>16.8f}{1:>16.8f}'.format(coord, weight))
            with open('Path15', 'w') as f:
                f.write('\n'.join(lines))
#            write_high = Find_Kpoints_Path(s, num_interval = num_interval)
#            lines = []
#            for w in write_high:
#	        lines.append('\t%d\t%s' % (w[0], w[1]))
#            with open('write_high', 'w') as f:
#                f.write('\n'.join(lines))
            os.chdir(rootdir)
        else:
            continue

def Find_Kpoints_Path(Structure, criterion = 1e-8, num_interval = 30):
    hkp = HighSymmKpath(Structure).high_symmetry_kpoints
    kpoints = hkp['kpoints']
    path = hkp['path']
    points = []
    for p in path:
        i = 0
        while i < len(p) - 1:
            j = i + 1
            while np.all(abs(kpoints[p[j]] - kpoints[p[i]]) < criterion):
                if j >= len(p) - 1:
                    break
                j += 1
            interval = (kpoints[p[j]] - kpoints[p[i]]) / num_interval
            for k in range(num_interval):
                points.append(wash(kpoints[p[i]] + k * interval))
            i += 1
        points.append(wash(kpoints[p[-1]]))
    write_high = []
    index = 0
    for i in range(len(path)):
        if i > 0:
            index += 1
        for j in range(len(path[i])):
            if j == 0:
                index = index
            else:
                index += num_interval
            write_high.append([index, path[i][j]])
    return points

def wash(point, criterion = 1e-8):
    point[np.where(abs(point) < criterion)] = 0.
    return point
