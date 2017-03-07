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

def downloadjson(mid):
    apiStem = "https://www.materialsproject.org/rest/v1/materials/%s/vasp/cif?API_KEY=4pyuBOFlZiNwE9f0" % mid
    print apiStem
    c=urllib.urlopen(apiStem)
    return json.loads(c.read())

def downloadjson_vasp(mid):
    apiStem = "https://www.materialsproject.org/rest/v1/materials/%s/vasp/?API_KEY=4pyuBOFlZiNwE9f0" % mid
    c=urllib.urlopen(apiStem)
    return json.loads(c.read())

def downloadjson_number(number):
    apiStem = "https://www.materialsproject.org/rest/v1/materials/mp-%s/vasp/cif?API_KEY=4pyuBOFlZiNwE9f0" % number
    print apiStem
    c=urllib.urlopen(apiStem)
    return json.loads(c.read())

def downloadjson_bandstructure(mid):
    apiStem = "https://www.materialsproject.org/rest/v1/materials/%s/vasp/bandstructure?API_KEY=4pyuBOFlZiNwE9f0" % mid
    print apiStem
    c=urllib.urlopen(apiStem)
    return json.loads(c.read())

def crawl_HTP(lowest_index, highest_index):
    for i in range(lowest_index, highest_index):
        rootdir = os.getcwd()
        dir_name = 'PWmat_' + str(i)
        if os.path.exists(os.path.join(rootdir, dir_name)):
            continue
        mid = 'mp-' + str(i)
        dict = downloadjson(mid)
        if not dict["valid_response"]:
            continue
        matdict = dict["response"]
        s = matdict[0]['cif']
        a = float(re.search(r'_cell_length_a\s*(.*)', s).group(1))
        b = float(re.search(r'_cell_length_b\s*(.*)', s).group(1))
        c = float(re.search(r'_cell_length_c\s*(.*)', s).group(1))
        alpha = float(re.search(r'_cell_angle_alpha\s*(.*)', s).group(1))
        beta = float(re.search(r'_cell_angle_beta\s*(.*)', s).group(1))
        gamma = float(re.search(r'_cell_angle_gamma\s*(.*)', s).group(1))
        lattice_vectors = Lattice.from_lengths_and_angles(a, b, c, alpha, beta, gamma).vectors
        pos_pattern = re.compile(r'\s*(\w*).*\d\s*(-?\d+\.\d*)\s*(-?\d+\.\d*)\s*(-?\d+\.\d*)')
        lines = pos_pattern.findall(s)
        positions = []
        atomic_numbers = []
        for j in lines:
            atomic_numbers.append(Element(j[0]).atomic_number)
            positions.append([float(x) for x in j[1:4]])
        structure = Structure(lattice_vectors, positions, atomic_numbers)
        createdir(dir_name)
        structure.export_to_pwmat('atom.config')
        whether_spin = True
        bandstructure = downloadjson_bandstructure(mid)
        if not bandstructure["valid_response"]:
            whether_spin = False
        else:
            whether_spin = bandstructure["response"][0]["bandstructure"]["is_spin_polarized"]
        with open('spin', 'w') as f:
            f.write(str(whether_spin))
        try:
            points = Find_Kpoints_Path(structure)
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
        os.chdir(rootdir)

def crawl_atom_types(mid):
    dict = downloadjson(mid)
    if dict["valid_response"] == False: return -1
    numoftypes = len(mid.split('-'))
    rootdir = os.getcwd()
    matdict = dict['response']
    for i in range(len(matdict)):
        id = matdict[i]['material_id']
        if not numoftypes == downloadjson_vasp(id)['response'][0]['nelements']:
            continue
        s = matdict[i]['cif']
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
        createdir(id)
        structure.export_to_pwmat('atom.config')
        os.chdir(rootdir)

def crawl_mp_index(index):
    dict = downloadjson(index)
    if dict["valid_response"] == False: return -1
    rootdir = os.getcwd()
    matdict = dict["response"]
    s = matdict[0]['cif']
    a = float(re.search(r'_cell_length_a\s*(.*)', s).group(1))
    b = float(re.search(r'_cell_length_b\s*(.*)', s).group(1))
    c = float(re.search(r'_cell_length_c\s*(.*)', s).group(1))
    alpha = float(re.search(r'_cell_angle_alpha\s*(.*)', s).group(1))
    beta = float(re.search(r'_cell_angle_beta\s*(.*)', s).group(1))
    gamma = float(re.search(r'_cell_angle_gamma\s*(.*)', s).group(1))
    lattice_vectors = Lattice.from_lengths_and_angles(a, b, c, alpha, beta, gamma).vectors
    pos_pattern = re.compile(r'\s*(\w*).*\d\s*(-?\d+\.\d*)\s*(-?\d+\.\d*)\s*(-?\d+\.\d*)')
    lines = pos_pattern.findall(s)
    positions = []
    atomic_numbers = []
    for j in lines:
        atomic_numbers.append(Element(j[0]).atomic_number)
        positions.append([float(x) for x in j[1:4]])
    structure = Structure(lattice_vectors, positions, atomic_numbers)
    createdir(index)
    structure.export_to_pwmat('atom.config')
    os.chdir(rootdir)

def createdir(childir):
    currentdir = os.getcwd()
    nextdir = os.path.join(currentdir, childir)
    os.mkdir(nextdir)
    os.chdir(nextdir)

# def weng():
    # with open('out') as f:
        # lines = f.readlines()
    # numbers = []
    # for i in range(len(lines)):
        # numbers.append(lines[i].split()[0])
    # spg_ints = []
    # for number in numbers:
        # try:
            # d = downloadjson_number(number)
            # s = d['response'][0]['cif']
            # a = float(re.search(r'_cell_length_a\s*(.*)', s).group(1))
            # b = float(re.search(r'_cell_length_b\s*(.*)', s).group(1))
            # c = float(re.search(r'_cell_length_c\s*(.*)', s).group(1))
            # alpha = float(re.search(r'_cell_angle_alpha\s*(.*)', s).group(1))
            # beta = float(re.search(r'_cell_angle_beta\s*(.*)', s).group(1))
            # gamma = float(re.search(r'_cell_angle_gamma\s*(.*)', s).group(1))
            # lattice_vectors = Lattice.from_lengths_and_angles(a, b, c, alpha, beta, gamma).vectors
            # pos_pattern = re.compile(r'\s*(\w*).*\d\s*(-?\d+\.\d*)\s*(-?\d+\.\d*)\s*(-?\d+\.\d*)')
            # lines = pos_pattern.findall(s)
            # positions = []
            # atomic_numbers = []
            # for j in lines:
                # atomic_numbers.append(Element(j[0]).atomic_number)
                # positions.append([float(x) for x in j[1:4]])
            # structure = Structure(lattice_vectors, positions, atomic_numbers)
            # spg_int = SpaceGroup(structure.get_spacegroup()).int_number
        # except:
            # d = downloadjson_number(number)
            # s = d['response'][0]['cif']
            # a = float(re.search(r'_cell_length_a\s*(.*)', s).group(1))
            # b = float(re.search(r'_cell_length_b\s*(.*)', s).group(1))
            # c = float(re.search(r'_cell_length_c\s*(.*)', s).group(1))
            # alpha = float(re.search(r'_cell_angle_alpha\s*(.*)', s).group(1))
            # beta = float(re.search(r'_cell_angle_beta\s*(.*)', s).group(1))
            # gamma = float(re.search(r'_cell_angle_gamma\s*(.*)', s).group(1))
            # lattice_vectors = Lattice.from_lengths_and_angles(a, b, c, alpha, beta, gamma).vectors
            # pos_pattern = re.compile(r'\s*(\w*).*\d\s*(-?\d+\.\d*)\s*(-?\d+\.\d*)\s*(-?\d+\.\d*)')
            # lines = pos_pattern.findall(s)
            # positions = []
            # atomic_numbers = []
            # for j in lines:
                # atomic_numbers.append(Element(j[0]).atomic_number)
                # positions.append([float(x) for x in j[1:4]])
            # structure = Structure(lattice_vectors, positions, atomic_numbers)
            # spg_int = SpaceGroup(structure.get_spacegroup()).int_number
        # spg_ints.append(spg_int)
    # with open('spg_ints', 'w') as f:
        # f.writelines('\n'.join(spg_ints))

# def weng2():
    # r = os.getcwd()
    # enter = os.path.join(r, 'PO4')
    # os.chdir(enter)
    # l = os.listdir(os.getcwd())
    # le = []
    # for i in range(len(l)):
        # m = l[i].split('.')[0].split('_')[1]
        # print m
        # s = Structure.import_from_pwmat(l[i])
        # spg_int = SpaceGroup(s.get_spacegroup()).int_number
        # spg = m + '\t' + str(spg_int)
        # le.append(spg)
        # lines = '\n'.join(le)
    # with open('heheheda', 'w') as f:
        # f.writelines(lines)

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
                if j >= len(p) - 1:
                    break
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
