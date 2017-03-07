# coding: utf-8
# Copyright © 2016 YunXing Zuo

import numpy as np
from copy import deepcopy
from itertools import product
from structure import *
from sp_dict import sp_dict

__author__ = 'YunXing Zuo'
__email__ = 'zuoyx@pkusz.edu.cn'
__date__ = 'Dec. 8, 2016'

"""
Generate the initial resonable structures by mapping the given composition
of elements into the Wyckoff sites of selected spacegroup as well as Monte Carlo method.
"""

def bond_dist_critieron(Structure, element_A, element_B, distprec = 1.5):
    """
    True if all the distances between positions of element_A and positions of element_B are less than disprec

    Args:
        Structure: Structure class
        element_A: string of atomic symbol (e.g., "O" define the oxygen atom)
        element_B: string of atomic symbol (e.g., "O" define the oxygen atom)

    Returns:
        bool True if all the distances between positions of element_A and positions of element_B are less than disprec
    """
    positions_element_A = Structure.frac_positions[np.array(Structure.atomic_symbols) == element_A]
    positions_element_B = Structure.frac_positions[np.array(Structure.atomic_symbols) == element_B]
    for i in product(range(len(positions_element_A)), range(len(positions_element_B))):
        bond_distance = np.linalg.norm(np.dot(positions_element_A[i[0]] - positions_element_B[i[1]], Structure.lattice_vectors))
        if bond_distance == 0.0:
            continue
        elif bond_distance < distprec:
            return False
    return True

def add_atoms(pre_structure, spg_symbol, element, letter = None, position = None):
    """
    Return a new Structure class by adding atoms of given symbol assigned in the certain Wyckoff letter
    of selected spacegroup

    Args:
        pre_structure: Structure class operated
        spg_symbol: string of spacegroup selected(e.g., "Pnma")
        element: string of atomic symbol added into the structure
        letter: string of Wyckoff Letter in the specific spacegroup (e.g., "a")

    Returns:
        A new structure class
    """
    lattice = pre_structure.lattice_vectors
    atomic_symbols = pre_structure.atomic_symbols
    positions = pre_structure.frac_positions
    if letter is not None:
        new_positions = np.array(pos_gen_wyckoff_positions(spg_symbol, letter, position))
    elif position is not None:
        new_positions = np.array(SpaceGroup(spg_symbol).get_orbit(position))
    positions = np.concatenate((positions, new_positions))
    atomic_symbols.extend([element] * len(new_positions))
    return Structure(lattice, positions, atomic_symbols)

def structure_generation(spg_symbol, lattice_vectors, letters, elements, min_bond_dist = 1.5):
    """
    Get the structure class under selected spacegroup, lattice constants, candidate feasible permutation and according types pf atoms
    by adding atoms in order by the criterion of distance. (e.g., when added Co atoms in "b" site in the structure filled with Li atoms
    in "a" site, check whether distance between every Co atom and every Li atom is larger than min_bond_dist, if not, reassign Co atom)

    Args:
        spg_symbol: string of spacegroup selected(e.g., "Pnma")
        lattice_vectors: 3x3 array defines the lattice constants
        letters: list of permutation given by permutation_gen function
        elements: list of elements mapping the given Wyckoff sites
        min_bond_dist: criterion of prescreen the feasibility of a newly generated structure, larger the min_bond_dist, more reasonable structure
                       got, however, harder to obtain the result

    Returns:
        A newly generated structure class if all the distances between different atom pairs is less than min_bond_dist, 
        else, return the string "There is not satisfied structure under this circumstances!"
    """
    temp = sorted(enumerate(letters), key=lambda x: len(pos_gen_wyckoff_positions(spg_symbol, x[1])))
    sorted_letters = [x[1] for x in temp]
    sorted_index = [x[0] for x in temp]
    sorted_elements = [elements[i] for i in sorted_index]
    initial_positions = np.array(pos_gen_wyckoff_positions(spg_symbol, sorted_letters.pop(0)))
    new_structure = Structure(lattice_vectors, initial_positions, [sorted_elements.pop(0)] * len(initial_positions))
    while sorted_letters:
        j = 0
        while j < 100:
            new_structure = add_atoms(new_structure, spg_symbol, sorted_elements[0], letter = sorted_letters[0])
            satisfied = True
            for i in np.unique(new_structure.atomic_symbols):
                if not bond_dist_critieron(new_structure, i, sorted_elements[0], min_bond_dist):
                    satisfied = False
                    break
                else: continue
            if satisfied:
                sorted_letters.pop(0)
                sorted_elements.pop(0)
                break
            j += 1
        if j >= 10: break
    if sorted_letters:
        return structure_generation(spg_symbol, lattice_vectors, letters, elements, min_bond_dist)
    return new_structure

def structure_generation_for_monte_carlo(struct_dict, min_bond_dist = 1.5):
    """
    Get the structure class from the dictionary class exported from to_dict function in Structure class including spacegroup symbol
    lattice constants, and the elements, wyckoff letters and positions of independent atoms.

    Args:
        struct_dict: dictionary, exported from Structure class
        min_bond_dist: criterion of prescreen the feasibility of a newly generated structure, larger the min_bond_dist, more reasonable structure
                       got, however, harder to obtain the result
    """
    new_structure = Structure.from_dict(struct_dict)
    satisfied = True
    for i in np.unique(new_structure.atomic_symbols):
        for j in np.unique(new_structure.atomic_symbols):
            if not bond_dist_critieron(new_structure, i, j, min_bond_dist):
                satisfied = False
    return new_structure, satisfied