# coding: utf-8
# Copyright © 2016 YunXing Zuo

import re
import numpy as np
import urllib
import json
import os
import shutil
import time
from structure import *
from high_symmetry_Kpoints import *

__author__ = 'YunXing Zuo'
__email__ = 'zuoyx@pkusz.edu.cn'
__date__ = 'Nov. 12, 2016'

def downloadjson(mid, API_KEY):
    apiStem = "https://www.materialsproject.org/rest/v1/materials/%s/vasp/cif?API_KEY=%s" % (mid, API_KEY)
    print apiStem
    c=urllib.urlopen(apiStem)
    return json.loads(c.read())

def downloadjson_bandstructure(mid, API_KEY):
    apiStem = "https://www.materialsproject.org/rest/v1/materials/%s/vasp/bandstructure?API_KEY=%s" % (mid, API_KEY)
    print apiStem
    c=urllib.urlopen(apiStem)
    return json.loads(c.read())

def crawl(lowest_index, highest_index):
    for i in range(lowest_index, highest_index):
        mid = 'mp-' + str(i)
        dict = downloadjson(mid)
        if not dict["valid_response"]:
            continue
        rootdir = os.getcwd()
        matdict = dict["response"]
        s = matdict[0]['cif']
        dir_name = 'PWmat_' + str(i)
        a = float(re.search(r'_cell_length_a\s*(.*)', s).group(1))
        b = float(re.search(r'_cell_length_b\s*(.*)', s).group(1))
        c = float(re.search(r'_cell_length_c\s*(.*)', s).group(1))
        alpha = float(re.search(r'_cell_angle_alpha\s*(.*)', s).group(1))
        beta = float(re.search(r'_cell_angle_beta\s*(.*)', s).group(1))
        gamma = float(re.search(r'_cell_angle_gamma\s*(.*)', s).group(1))
        lattice_vectors = Lattice.from_lengths_and_angles(a, b, c, alpha, beta, gamma).vectors
        pos_pattern = re.compile(r'\s*(\w*).*(\d+\.\d*)\s*(\d+\.\d*)\s*(\d+\.\d*)')
        lines = pos_pattern.findall(s)
        positions = []
        atomic_numbers = []
        for j in lines:
            atomic_numbers.append(Element(j[0]).atomic_number)
            positions.append([float(x) for x in j[1:4]])
        structure = Structure(lattice_vectors, positions, atomic_numbers)
        try:
            points = Find_Kpoints_Path(structure)
            createdir(dir_name)
            lines = []
            lines.append('{:12d}'.format(len(points)))
            lines.append('\t2\t0')
            weight = 1.
            for coord in points:
                lines.append('{0[0]:>16.8f}{0[1]:>16.8f}{0[2]:>16.8f}{1:>16.8f}'.format(coord, weight))
            with open('Path', 'w') as f:
                f.write('\n'.join(lines))
            time.sleep(0.1)
        except:
            os.chdir(rootdir)
            continue
        structure.export_to_pwmat('atom.config')
        whether_spin = True
        bandstructure = downloadjson_bandstructure(mid)
        if not bandstructure["valid_response"]:
            whther_spin = False
        else:
            whther_spin = bandstructure["response"][0]["bandstructure"]["is_spin_polarized"]
        with open('spin', 'w') as f:
            f.write(str(whether_spin))
        os.chdir(rootdir)


def createdir(childir):
    currentdir = os.getcwd()
    nextdir = os.path.join(currentdir, childir)
    os.mkdir(nextdir)
    os.chdir(nextdir)

def Find_Kpoints_Path(Structure, criterion = 1e-8, num_interval = 30):
    abc = Structure.lattice.lengths
    angles = Structure.lattice.angles
    crystal_system = Structure.get_crystal_system()
    spg = Structure.get_spacegroup().split()[0]
    hkp = HighSymmKpath(abc, angles, crystal_system, spg).high_symmetry_kpoints
    kpoints = hkp['kpoints']
    path = hkp['path']
    points = []
    for p in path:
        i = 0
        while i < len(p) - 1:
            j = i + 1
            while np.all(abs(kpoints[p[j]] - kpoints[p[i]]) < criterion):
                j += 1
            interval = (kpoints[p[j]] - kpoints[p[i]]) / num_interval
            for k in range(num_interval):
                points.append(wash(kpoints[p[i]] + k * interval))
            i += 1
        points.append(wash(kpoints[p[-1]]))
    return points
            
def wash(point, criterion = 1e-8):
    point[np.where(abs(point) < criterion)] = 0.
    return point