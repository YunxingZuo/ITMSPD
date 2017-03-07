# coding: utf-8

import numpy as np
from numpy.random import uniform, rand
from heiheihei import *
from wyckoffss import *
from wyckoff_parameters import *

bv_dict = {'Ag1': {'O-2': 1.805, 'S-2': 2.119, 'F-1': 1.80, 'Cl-1': 2.09}, \
           'Al3': {'O-2': 1.651, 'S-2': 2.13, 'Se-2': 2.27, 'Te-2': 2.48, 'F-1': 1.545, 'Cl-1': 2.032, 'Br-1': 2.20, 'I-1': 2.41, 'N-3': 1.79, 'P-3': 2.24, 'As-3': 2.30, 'H-1': 1.45}, \
           'As3': {'O-2': 1.789, 'S-2': 2.272, 'F-1': 1.70, 'Cl-1': 2.16, 'C-4': 1.93}, 'As5': {'O-2': 1.767, 'F-1': 1.620, 'Cl-1': 2.14}, \
           'C4': {'O-2': 1.390, 'C4': 1.54, 'S-2': 1.80, 'F-1': 1.32, 'Cl-1': 1.76, 'Br-1': 1.91, 'N-3': 1.442}, \
           'Cd2': {'O-2': 1.904, 'S-2': 2.304, 'Se-2': 2.40, 'Te-2': 2.59, 'F-1': 1.811, 'Cl-1': 2.23, 'Br-1': 2.35, 'I-1': 2.57, 'N-3': 1.96, 'P-3': 2.34, 'As-3': 2.43, 'H-1': 1.66}, \
           'Co2': {'O-2': 1.692, 'S-2': 1.94, 'F-1': 1.64, 'Cl-1': 2.01}, 'Co3': {'O-2': 1.70, 'S-2': 2.02, 'F-1': 1.62, 'Cl-1': 2.05, 'N-3': 1.69, 'C2': 1.634}, 'Co4': {'O-2': 1.72, 'F-1': 1.55}, \
           'Cr2': {'O-2': 1.73, 'F-1': 1.67, 'Cl-1': 2.09, 'Br-1': 2.26, 'I-1': 2.48, 'N-3': 1.80}, 'Cr3': {'O-2': 1.724, 'S-2': 2.162, 'F-1': 1.64, 'Cl-1': 2.08, 'Br-1': 2.28, 'N-3': 1.78}, \
           'Cr4': {'O-2': 1.783, 'F-1': 1.56}, 'Cr6': {'O-2': 1.794, 'F-1': 1.74, 'Cl-1': 2.12}, \
           'Cu1': {'O-2': 1.504, 'S-2': 1.811, 'Se-2': 1.90, 'F-1': 1.6, 'Cl-1': 1.858, 'Br-1': 2.03, 'I-1': 2.155, 'N-3': 1.520, 'P-3': 1.774, 'As-3': 1.856, 'C-4': 1.446}, \
           'Cu2': {'O-2': 1.679, 'S-2': 2.054, 'Se-2': 2.02, 'Te-2': 2.27, 'F-1': 1.594, 'Cl-1': 2.00, 'Br-1': 1.99, 'I-1': 2.16, 'N-3': 1.61, 'P-3': 1.97, 'As-3': 2.08, 'C-4': 1.72, 'H-1': 1.21}, \
           'Fe2': {'O-2': 1.713, 'S-2': 2.125, 'F-1': 1.65, 'Cl-1': 2.06, 'Br-1': 2.21, 'I-1': 2.47, 'N-3': 1.769}, \
           'Fe3': {'O-2': 1.759, 'S-2': 2.149, 'F-1': 1.679, 'Cl-1': 2.09, 'Br-1': 2.22, 'N-3': 1.815, 'C2': 1.689}, \
           'Ga3': {'O-2': 1.730, 'S-2': 2.163, 'F-1': 1.62, 'Cl-1': 2.07, 'Br-1': 2.20, 'I-1': 2.46}, \
           'Ge4': {'O-2': 1.748, 'S-2': 2.217, 'Se-2': 2.35, 'F-1': 1.66, 'Cl-1': 2.14}, 'Hg1': {'O-2': 1.90, 'F-1': 1.81, 'Cl-1': 2.28}, \
           'Hg2': {'O-2': 1.93, 'S-2': 2.308, 'F-1': 1.90, 'Cl-1': 2.25, 'Br-1': 2.38, 'I-1': 2.62}, 'I5': {'O-2': 1.992, 'F-1': 1.90}, \
           'I7': {'O-2': 1.93, 'F-1': 1.83, 'Cl-1': 2.31}, 'In3': {'O-2': 1.902, 'S-2': 2.370, 'F-1': 1.792, 'Cl-1': 2.28, 'Br-1': 2.51, 'I-1': 2.63}, \
           'K1': {'O-2': 2.132, 'S-2': 2.59, 'Se-2': 2.72, 'Te-2': 2.93, 'F-1': 1.992, 'Cl-1': 2.519, 'Br-1': 2.66, 'I-1': 2.88, 'N-3': 2.26, 'P-3': 2.64, 'As-3': 2.83}, \
           'Li1': {'O-2': 1.466, 'S-2': 1.94, 'Se-2': 2.09, 'Te-2': 2.30, 'F-1': 1.360, 'Cl-1': 1.91, 'Br-1': 2.02, 'I-1': 2.22, 'N-3': 1.61}, \
           'Mg2': {'O-2': 1.693, 'S-2': 2.18, 'Se-2': 2.32, 'Te-2': 2.53, 'F-1': 1.578, 'Cl-1': 2.08, 'Br-1': 2.28, 'I-1': 2.46, 'N-3': 1.85, 'P-3': 2.29, 'As-3': 2.38}, \
           'Mn2': {'O-2': 1.790, 'S-2': 2.22, 'F-1': 1.698, 'Cl-1': 2.133, 'Br-1': 2.34, 'I-2': 2.52, 'N-3': 1.849}, \
           'Mn3': {'O-2': 1.760, 'F-1': 1.66, 'Cl-1': 2.14, 'N-3': 1.837}, 'Mn4': {'O-2': 1.753, 'F-1': 1.71, 'Cl-1': 2.13, 'N-3': 1.822}, \
           'Mo4': {'O-2': 1.886, 'S-2': 2.235, 'F-1': 1.80, 'N-3': 2.043}, 'Mo6': {'O-2': 1.907, 'S-2': 2.331, 'F-1': 1.81, 'Cl-1': 2.28, 'N-3': 2.009}, \
           'N3': {'O-2': 1.361, 'S-2': 1.73, 'F-1': 1.37, 'Cl-1': 1.75}, 'N5': {'O-2': 1.432, 'F-1': 1.36, 'Cl-1': 1.80}, \
           'Na1': {'O-2': 1.803, 'S-2': 2.28, 'Se-2': 2.41, 'Te-2': 2.64, 'F-1': 1.677, 'Cl-1': 2.15, 'Br-1': 2.33, 'I-1': 2.56, 'N-3': 1.93, 'P-3': 2.36, 'As-3': 2.53, 'H-1': 1.68}, \
           'Nb5': {'O-2': 1.911, 'F-1': 1.87, 'Cl-1': 2.27, 'I-1': 2.77}, 'Ni3': {'O-2': 1.75, 'S-2': 2.040, 'F-1': 1.58, 'N-3': 1.731}, \
           'Ni2': {'O-2': 1.675, 'S-2': 1.937, 'F-1': 1.596, 'Cl-1': 2.02, 'Br-1': 2.20, 'I-1': 2.40, 'N-3': 1.647}, \
           'P3': {'O-2': 1.655, 'S-2': 2.12, 'Se-2': 2.24}, 'P5': {'O-2': 1.617, 'S-2': 2.145, 'F-1': 1.54, 'Cl-1': 2.02, 'N-3': 1.704}, \
           'Pb2': {'O-2': 2.112, 'S-2': 2.541, 'Se-2': 2.69, 'F-1': 2.03, 'Cl-1': 2.53, 'Br-1': 2.68, 'I-1': 2.83, 'N-3': 2.18}, \
           'Pb4': {'O-2': 2.042, 'F-1': 1.94, 'Cl-1': 2.43}, 'Ru4': {'O-2': 1.834, 'S-2': 2.21, 'F-1': 1.74, 'Cl-1': 2.21}, \
           'S2': {'O-2': 1.74, 'S-2': 2.03, 'N-2': 1.597, 'N-3': 1.682}, 'S4': {'O-2': 1.644, 'S-4': 2.35, 'F-1': 1.60, 'Cl-1': 2.02, 'N-3': 1.762}, \
           'S6': {'O-2': 1.624, 'F-1': 1.56, 'Cl-1': 2.03, 'N-3': 1.72}, 'Sb3': {'O-2': 1.955, 'S-2': 2.474, 'Se-2': 2.60, 'F-1': 1.90, 'Cl-1': 2.35, 'Br-1': 2.51, 'I-1': 2.76, 'N-3': 2.108}, \
           'Sb5': {'O-2': 1.912, 'F-1': 1.797, 'Cl-1': 2.30, 'Br-1': 2.48}, 'Sc3': {'O-2': 1.849, 'S-2': 2.321, 'Se-2': 2.44, 'Te-2': 2.64, 'F-1': 1.76, 'Cl-1': 2.23, 'Br-1': 2.38, 'I-1': 2.59, 'N-3': 1.98, 'P-3': 2.40, 'As-3': 2.48, 'H-1': 1.68}, \
           'Se2': {'S-2': 2.21, 'Se-2': 2.33}, 'Se4': {'O-2': 1.811, 'F-1': 1.73, 'Cl-1': 2.22, 'Br-1': 2.43}, 'Se6': {'O-2': 1.788, 'F-1': 1.69, 'Cl-1': 2.16, 'N-3': 1.90}, \
           'Si4': {'O-2': 1.624, 'S-2': 2.126, 'Se-2': 2.26, 'Te-2': 2.49, 'F-1': 1.58, 'Cl-1': 2.03, 'Br-1': 2.20, 'I-1': 2.41, 'C-4': 1.883, 'N-3': 1.724, 'P-3': 2.23, 'As-3': 2.31, 'H-1': 1.47}, \
           'Sn2': {'O-2': 1.984, 'S-2': 2.423, 'Se-2': 2.476, 'Te-2': 2.747, 'F-1': 1.925, 'Cl-1': 2.36, 'Br-1': 2.50, 'I-1': 2.752, 'N-3': 2.046, 'P-3': 2.488, 'As-3': 2.585, 'C-4': 2.077}, \
           'Sn4': {'O-2': 1.905, 'S-2': 2.399, 'Se-2': 2.524, 'F-1': 1.843, 'Cl-1': 2.276, 'Br-1': 2.444, 'I-1': 2.70, 'N-3': 2.024}, \
           'Ta4': {'O-2': 2.29}, 'Ta5': {'O-2': 1.92, 'S-2': 2.47, 'F-1': 1.88, 'Cl-1': 2.30}, 'Te4': {'O-2': 1.977, 'S-2': 2.44, 'F-1': 1.87, 'Cl-1': 2.37, 'Br-1': 2.55, 'I-1': 2.782}, \
           'Te6': {'O-2': 1.917, 'F-1': 1.82, 'Cl-1': 2.30}, 'Ti2': {'F-1': 2.15, 'Cl-1': 2.31, 'Br-1': 2.49}, 'Ti3': {'O-2': 1.791, 'S-2': 2.11, 'F-1': 1.723, 'Cl-1': 2.17, 'I-1': 2.52}, \
           'Ti4': {'O-2': 1.815, 'S-2': 2.29, 'F-1': 1.76, 'Cl-1': 2.19, 'Br-1': 2.36}, 'V2': {'O-2': 1.70, 'S-2': 2.11, 'F-1': 2.16, 'Cl-1': 2.44}, \
           'V3': {'O-2': 1.743, 'S-2': 2.185, 'F-1': 1.702, 'Cl-1': 2.19, 'N-3': 1.813}, 'V4': {'O-2': 1.784, 'S-2': 2.226, 'F-1': 1.70, 'Cl-1': 2.16, 'N-3': 1.875}, \
           'V5': {'O-2': 1.803, 'S-2': 2.25, 'F-1': 1.70, 'Cl-1': 2.16}, 'Zn2': {'O-2': 1.704, 'S-2': 2.09, 'Se-2': 2.22, 'Te-2': 2.45, 'F-1': 1.62, 'Cl-1': 2.01, 'Br-1': 2.15, 'I-1': 2.36, 'N-3': 1.77, 'P-3': 2.15, 'As-3': 2.24, 'H-1': 1.42}, \
           'Zr2': {'O-2': 2.34, 'F-1': 2.24, 'Cl-1': 2.58}, 'Zr4': {'O-2': 1.928, 'S-2': 2.41, 'Se-2': 2.53, 'Te-2': 2.67, 'F-1': 1.846, 'Cl-1': 2.33, 'Br-1': 2.48, 'I-1': 2.69, 'N-3': 2.11, 'P-3': 2.52, 'As-3': 2.57, 'H-1': 1.79}, \
           'As-3': {'Al3': 2.30, 'Cd2': 2.43, 'Cu1': 1.856, 'Cu2': 2.08, 'K1': 2.83, 'Mg2': 2.38, 'Na1': 2.53, 'Sc3': 2.48, 'Si4': 2.585, 'Sn2': 2.585, 'Zn2': 2.24, 'Zr2': 2.57}, \
           'Br-1': {'Al3': 2.20, 'C4': 1.91, 'Cd2': 2.35, 'Cr2': 2.26, 'Cr3': 2.28, 'Cu1': 2.03, 'Cu2': 1.99, 'Fe2': 2.21, 'Fe3': 2.22, 'Ga3': 2.20, 'Hg2': 2.38, 'In3': 2.51, 'K1': 2.66, \
                    'Li1': 2.02, 'Mg2': 2.28, 'Mn2': 2.34, 'Na1': 2.33, 'Ni2': 2.20, 'Pb2': 2.68, 'Sb3': 2.51, 'Sb5': 2.48, 'Sc3': 2.38, 'Se4': 2.43, 'Si4': 2.20, 'Sn4': 2.444, 'Zn2': 2.15, 'Zr4': 2.48}, \
           'Cl-1': {'Ag1': 2.09, 'Al3': 2.032, 'As3': 2.16, 'As5': 2.14, 'C4': 1.76, 'Cd2': 2.23, 'Co2': 2.01, 'Co3': 2.05, 'Cr2': 2.09, 'Cr3': 2.08, 'Cr6': 2.12, 'Cu1': 1.858, 'Cu2': 2.00, \
                    'Fe2': 2.06, 'Fe3': 2.09, 'Ga3': 2.07, 'Ge4': 2.14, 'Hg1': 2.28, 'Hg2': 2.25, 'I7': 2.31, 'In3': 2.28, 'K1': 2.519, 'Li1': 1.91, 'Mg2': 2.08, 'Mn2': 2.133, 'Mn3': 2.14, \
                    'Mn4': 2.13, 'Mo6': 2.28, 'N3': 1.75, 'N5': 1.80, 'Na1': 2.15, 'Nb5': 2.27, 'Ni2': 2.02, 'P5': 2.02, 'Pb2': 2.53, 'Pb4': 2.43, 'Ru4': 2.21, 'S4': 2.02, 'S6': 2.03, \
                    'Sb3': 2.35, 'Sb5': 2.30, 'Sc3': 2.23, 'Se4': 2.22, 'Se6': 2.16, 'Si4': 2.03, 'Sn2': 2.36, 'Sn4': 2.276, 'Ta5': 2.30, 'Te4': 2.37, 'Te6': 2.30, 'Ti2': 2.31, 'Ti3': 2.17, \
                    'Ti4': 2.19, 'V2': 2.44, 'V3': 2.19, 'V4': 2.16, 'V5': 2.16, 'Zn2': 2.01, 'Zr2': 2.58, 'Zr4': 2.33}, \
           'F-1': {'Ag1': 1.80, 'Al3': 1.545, 'As3': 1.70, 'As5': 1.620, 'C4': 1.32, 'Cd2': 1.811, 'Co2': 1.64, 'Co3': 1.62, 'Co4': 1.55, 'Cr2': 1.67, 'Cr3': 1.64, 'Cr4': 1.56, 'Cr6': 1.74, \
                   'Cu1': 1.6, 'Cu2': 1.594, 'Fe2': 1.65, 'Fe3': 1.679, 'Ga3': 1.62, 'Ge4': 1.66, 'Hg1': 1.81, 'Hg2': 1.90, 'I5': 1.90, 'I7': 1.83, 'In3': 1.792, 'Li1': 1.360, 'Mg2': 1.578, \
                   'Mn2': 1.698, 'Mn3': 1.66, 'Mn4': 1.71, 'Mo4': 1.80, 'Mo6': 1.81, 'N3': 1.37, 'N5': 1.36, 'Na1': 1.677, 'Nb5': 1.87, 'Ni3': 1.58, 'Ni2': 1.596, 'P5': 1.54, 'Pb2': 2.03, \
                   'Pb4': 1.94, 'Ru4': 1.74, 'S4': 1.60, 'S6': 1.56, 'Sb3': 1.90, 'Sb5': 1.797, 'Sc3': 1.76, 'Se4': 1.73, 'Se6': 1.69, 'Si4': 1.58, 'Sn2': 1.925, 'Sn4': 1.843, 'Ta5': 1.88, \
                   'Te4': 1.87, 'Te6': 1.82, 'Ti2': 2.15, 'Ti3': 1.723, 'Ti4': 1.76, 'V2': 2.16, 'V3': 1.702, 'V4': 1.70, 'V5': 1.70, 'Zn2': 1.62, 'Zr2': 2.24, 'Zr4': 1.846}, \
           'H-1': {'Al3': 1.45, 'Cd2': 1.66, 'Cu2': 1.21, 'Na1': 1.68, 'Sc3': 1.68, 'Si4': 1.47, 'Zn2': 1.42, 'Zr4': 1.79}, \
           'I-1': {'Al3': 2.41, 'Cd2': 2.57, 'Cr2': 2.48, 'Cu1': 2.155, 'Cu2': 2.16, 'Fe2': 2.47, 'Ga3': 2.46, 'Hg2': 2.62, 'In3': 2.63, 'K1': 2.88, 'Li1': 2.22, 'Mg2': 2.46, 'Mn2': 2.52, \
                   'Na1': 2.56, 'Nb5': 2.77, 'Ni2': 2.40, 'Pb2': 2.83, 'Sb3': 2.76, 'Si4': 2.41, 'Sn2': 2.752, 'Sn4': 2.70, 'Te4': 2.782, 'Ti3': 2.52, 'Zn2': 2.36, 'Zr4': 2.69}, \
           'N-3': {'Al3': 1.79, 'C4': 1.442, 'Cd2': 1.96, 'Co3': 1.69, 'Cr2': 1.80, 'Cr3': 1.78, 'Cu1': 1.520, 'Cu2': 1.61, 'Fe2': 1.769, 'Fe3': 1.815, 'K1': 2.26, 'Li1': 1.61, \
                   'Mg2': 1.85, 'Mn2': 1.849, 'Mn3': 1.837, 'Mn4': 1.822, 'Mo4': 2.043, 'Mo6': 2.009, 'N-3': 1.44, 'Na1': 1.93, 'Ni3': 1.731, 'Ni2': 1.647, 'P5': 1.704, 'Pb2': 2.18, \
                   'S2': 1.682, 'S4': 1.762, 'S6': 1.72, 'Sb3': 2.108, 'Sc3': 1.98, 'Se6': 1.90, 'Si4': 1.724, 'Sn2': 2.046, 'Sn4': 2.024, 'V3': 1.813, 'V4': 1.875, 'Zn2': 1.77, 'Zr4': 2.11}, \
           'O-2': {'Ag1': 1.805, 'Al3': 1.651, 'As3': 1.789, 'As5': 1.767, 'C4': 1.390, 'Cd2': 1.904, 'Co2': 1.692, 'Co3': 1.70, 'Co4': 1.72, 'Cr2': 1.73, 'Cr3': 1.724, 'Cr4': 1.783, \
                   'Cr6': 1.794, 'Cu1': 1.504, 'Cu2': 1.679, 'Fe2': 1.713, 'Fe3': 1.759, 'Ga3': 1.730, 'Ge4': 1.748, 'Hg1': 1.90, 'Hg2': 1.93, 'I5': 1.992, 'I7': 1.93, 'In3': 1.902, \
                   'K1': 2.132, 'Li1': 1.466, 'Mg2': 1.693, 'Mn2': 1.790, 'Mn3': 1.760, 'Mn4': 1.753, 'Mo4': 1.886, 'Mo6': 1.907, 'N3': 1.361, 'N5': 1.432, 'Na1': 1.803, 'Nb5': 1.911, \
                   'Ni3': 1.75, 'Ni2': 1.675, 'P3': 1.655, 'P5': 1.617, 'Pb2': 2.112, 'Pb4': 2.042, 'Ru4': 1.834, 'S2': 1.74, 'S4': 1.644, 'S6': 1.624, 'Sb3': 1.955, 'Sb5': 1.912, \
                   'Sc3': 1.849, 'Se4': 1.811, 'Se6': 1.788, 'Si4': 1.624, 'Sn2': 1.984, 'Sn4': 1.905, 'Ta4': 2.29, 'Ta5': 1.92, 'Te4': 1.977, 'Te6': 1.917, 'Ti3': 1.791, 'Ti4': 1.815, \
                   'V2': 1.70, 'V3': 1.743, 'V4': 1.784, 'V5': 1.803, 'Zn2': 1.704, 'Zr2': 2.34, 'Zr4': 1.928}, \
           'P-3': {'Al3': 2.24, 'Cd2': 2.34, 'Cu1': 1.774, 'Cu2': 1.97, 'K1': 2.64, 'Mg2': 2.29, 'Na1': 2.36, 'Sc3': 2.40, 'Si4': 2.23, 'Sn2': 2.488, 'Zn2': 2.15, 'Zr4': 2.52}, \
           'S-2': {'Ag1': 2.119, 'Al3': 2.13, 'As3': 2.272, 'C4': 1.80, 'Cd2': 2.304, 'Co2': 1.94, 'Co3': 2.02, 'Cr3': 2.162, 'Cu1': 1.811, 'Cu2': 2.054, 'Fe2': 2.125, 'Fe3': 2.149, \
                   'Ga3': 2.163, 'Ge4': 2.217, 'Hg2': 2.308, 'In3': 2.370, 'K1': 2.59, 'Li1': 1.94, 'Mg2': 2.18, 'Mn2': 2.22, 'N3': 1.73, 'Na1': 2.28, 'Ni3': 2.040, 'Ni2': 1.937, \
                   'P5': 2.145, 'Pb2': 2.541, 'Ru4': 2.21, 'S2': 2.03, 'Sb3': 2.474, 'Sc3': 2.321, 'Se2': 2.21, 'Si4': 2.126, 'Sn2': 2.423, 'Sn4': 2.399, 'Ta5': 2.47, 'Te4': 2.44, \
                   'Ti4': 2.29, 'V2': 2.11, 'V3': 2.185, 'V4': 2.226, 'V5': 2.25, 'Zn2': 2.09, 'Zr4': 2.41}, \
           'Se-2': {'Al3': 2.27, 'Cd2': 2.40, 'Cu1': 1.90, 'Cu2': 2.02, 'Ge4': 2.35, 'K1': 2.72, 'Li1': 2.09, 'Mg2': 2.32, 'Na1': 2.41, 'P3': 2.24, 'Pb2': 2.69, 'Sb3': 2.60, \
                    'Sc3': 2.44, 'Se2': 2.33, 'Si4': 2.26, 'Sn2': 2.476, 'Sn4': 2.524, 'Zn2': 2.22, 'Zr4': 2.53}, \
           'Te-2': {'Al3': 2.48, 'Cd2': 2.59, 'Cu2': 2.27, 'K1': 2.93, 'Li1': 2.30, 'Mg2': 2.53, 'Na1': 2.64, 'Sc3': 2.64, 'Si4': 2.49, 'Sn2': 2.747, 'Zn2': 2.45, 'Zr4': 2.67}}

def symbol_abs_error(structure, bv_dict, symbol, expected_valence, cutoff):
    abs_error = 0
    indices_excluded = np.arange(len(structure.frac_positions))[np.array(structure.atomic_symbols) == symbol]
    for center in structure.cart_positions[np.array(structure.atomic_symbols) == symbol]:
        positions_in_sphere, distances_in_sphere, indices_in_sphere = structure.lattice.get_points_in_sphere(structure.frac_positions, center, cutoff)
        bond_valence = 0
        for d, i in zip(distances_in_sphere, indices_in_sphere):
            if i in indices_excluded:
                continue
            elif structure.atomic_symbols[i] in bv_dict.keys():
                R_0 = bv_dict[structure.atomic_symbols[i]]
                bond_valence += S(R_0, d)
            else:
                continue
        abs_error += abs(bond_valence - expected_valence)
    return abs_error

def S(R_0, r):
    return np.exp((R_0 - r) / 0.37)

def bv_mean_error_criterion(structure, element_valence):
    mapping = {}
    for element, valence in element_valence.items():
        mapping[element] = element + str(valence)
    total_error = 0
    for symbol in np.unique(structure.atomic_symbols):
        bv_para = {}
        for k, v in mapping.items():
            if bv_dict[mapping[symbol]].has_key(v):
                bv_para[k] = bv_dict[mapping[symbol]][v]
        total_error += symbol_abs_error(structure, bv_para, symbol, abs(element_valence[symbol]), cutoff = 10)
    return total_error / len(structure.frac_positions)

def func(structure, element_valence, limits = [], errors = [], limit = 0, bond_dist = 1.8, radius = 0.05, criterion = 0.2, times = 200):
    error = bv_mean_error_criterion(structure, element_valence)
    print error
    errors.append(error)
    limits.append(limit)
    if error < criterion or limit > times:
        return structure, limits, errors, error, limit
    struct_dict = structure.to_dict()
    fitted_positions = [v[2] for v in struct_dict['atoms'].values()]
    satisfied = False
    while not satisfied:
        relaxed_positions = []
        for disturb in fitted_positions:
            relaxed_positions.append(disturb + np.array([uniform(-1, 1), uniform(-1, 1), uniform(-1, 1)]) * radius)
        for pos, k in zip(relaxed_positions, struct_dict['atoms']):
            struct_dict['atoms'][k][2] = pos
        new_structure, satisfied = structure_generation_for_monte_carlo(struct_dict, min_bond_dist = bond_dist)
    limit += 1
    print limit
    new_error = bv_mean_error_criterion(new_structure, element_valence)
    if new_error < error:
        structure = new_structure
        return func(structure, element_valence, limits, errors, limit, bond_dist, radius, criterion, times)
    else:
        probility = normal_distribution(new_error, error, 0.02)
        if rand() < probility:
            structure = new_structure
            return func(structure, element_valence, limits, errors, limit, bond_dist, radius, criterion, times)
        else:
            return func(structure, element_valence, limits, errors, limit, bond_dist, radius, criterion, times)

def normal_distribution(x, mu, sigma):
    return 0.5 * np.exp(-(x - mu) ** 2 / (2 * sigma ** 2))

def get_parameters(structure):
    l = []
    struct_dict = structure.to_dict()
    spg = struct_dict['spg']
    for i in struct_dict['atoms']:
        wy_le = struct_dict['atoms'][i][1]
        l.extend(struct_dict['atoms'][i][2][wyckoff_parameter(spg, wy_le)])
    return l

def from_parameters(l, struct_dict):
    iterator = 0
    spg = struct_dict['spg']
    for i in struct_dict['atoms']:
        wy_le = struct_dict['atoms'][i][1]
        parameter = struct_dict['atoms'][i][2][wyckoff_parameter(spg, wy_le)]
        struct_dict['atoms'][i][2][wyckoff_parameter(spg, wy_le)] = np.array(l[iterator : iterator + len(parameter)])
        iterator += len(parameter)
    return struct_dict
