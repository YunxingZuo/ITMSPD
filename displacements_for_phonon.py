# coding: utf-8
# Copyright © 2016 YunXing Zuo, WeiJi Hsiao

import numpy as np
from Symmetry_Operation import *
from RDF import *

__author__ = 'YunXing Zuo, WeiJi Hsiao'
__email__ = 'weiji.hsiao@gmail.com'
__date__ = 'Oct. 25, 2016'

class phonon_calculation(object):
    def __init__(self, POSCAR):
        self._structure = POSCAR

        # there are 3x3x3/2 possibilities exculde the (0, 0, 0)
        self.directions_set = np.array([[1, 0, 0], \
                                        [0, 1, 0], \
                                        [0, 0, 1], \
                                        [1, 1, 0], \
                                        [1, 0, 1], \
                                        [0, 1, 1], \
                                        [1, -1, 0], \
                                        [1, 0, -1], \
                                        [0, 1, -1], \
                                        [1, 1, 1], \
                                        [1, 1, -1], \
                                        [1, -1, 1], \
                                        [-1, 1, 1]])

    # to identify the transformation matrix which can transfer the point to itself
    def get_site_symmetry(self, position):

        rotations = self._structure.symmetry_operations['rotations']
        translations = self._structure.symmetry_operations['translations']
        site_symmetry = []
        for r, t in zip(rotations, translations):
            symmop = SymmOp.rotations_combine_translation(r, t)
            if symmop.whether_symmetrical(position, position, self._structure.lattice_constant):
                site_symmetry.append(r)

        return np.array(site_symmetry, dtype='intc')

    """return a direction which can be rotated by the rotation matrices in the site_symmetry 
    into two directions different from itself"""
    def first_priority_direction_of_displacement(self, site_symmetry, directions = self.directions_set):
        for direction in directions:
            rot_directions = []
            for r in site_symmetry:
                rot_directions.append(np.dot(direction, r.T))
            num_sitesym = len(site_symmetry)
            for i in range(num_sitesym):
                for j in (i+1, num_sitesym):
                    mat = np.concatenate((direction, site_symmetry[i], site_symmetry[j])).reshape(3, 3)
                    if np.linalg.det(mat) != 0:
                        return i, [direction]
        return None, None

    """ return a direction which can be rotated by the rotation matrices in the site_symmetry 
    into one direction diffenrent from itself and another direction in the directions_set"""
    def second_priority_direction_of_displacement(self, site_symmetry, directions = self.directions_set):
        for direction in directions:
            rot_directions = []
            for r in site_symmetry:
                rot_directions.append(np.dot(direction, r.T))
            num_sitesym = len(site_symmetry)
            for i in range(num_sitesym):
                for another_direction in directions:
                    mat = np.concatenate((direction, site_symmetry[i], another_direction)).reshape(3, 3)
                    if np.linalg.det(mat) != 0:
                        return i, [direction, another_direction]
        return None, None

    def get_direction_of_displacement(self, site_symmetry, directions = directions_set):
        # first_priority
        num_of_ro_to_transfer, direction_of_disp = first_priority_direction_of_displacement(site_symmetry, directions)
        if direction_of_disp is not None:
            return direction_of_disp

        # second_priority
        num_of_ro_to_transfer, directions_of_disp = second_priority_direction_of_displacement(site_symmetry, directions)
        if disps is not None:
            return disps

        # last_priority
        return [directions[0], directions[1], directions[2]]

    # to see whether any rotation in the site_symmetry can transfer the direction to its minus one
    def is_minus_direction(self, direction, site_symmetry):
        is_minus = True
        for r in site_symmetry:
            rot_direction = np.dot(rot_direction, r.T)
            if (rot_direction + direction).any():
                continue
            else:
                is_minus = False
                break
        return is_minus

    # return all the directions that can be displaced of every independent atom
    def get_directions_of_displacements(self, structure = self._structure, directions = self.directions_set):
        displacements = []

        for atom_num in structure.get_independent_atoms():
            site_symmetry = self.get_site_symmetry(structure.positions[atom_num])

            for direc in get_direction_of_displacement(site_symmetry, directions_set):
                displacements.append([atom_num, direc[0], direc[1], direc[2]])
                if is_minus_direction:
                    displacements.append([atom_num, -direc[0], -direc[1], -direc[2]])

        return displacements