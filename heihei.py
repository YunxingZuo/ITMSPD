# coding: utf-8
# Copyright © 2016 YunXing Zuo

import numpy as np
from copy import deepcopy
from itertools import product
from structure import Structure
from wyckoff_positions_gen import pos_gen_wyckoff_positions
from sp_dict import sp_dict

__author__ = 'YunXing Zuo'
__email__ = 'zuoyx@pkusz.edu.cn'
__date__ = 'Nov. 12, 2016'

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

def add_atoms(pre_structure, spg_symbol, element, letter):
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
    new_positions = np.array(pos_gen_wyckoff_positions(spg_symbol, letter))
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
        while j < 5000:
            new_structure = add_atoms(new_structure, spg_symbol, sorted_elements[0], sorted_letters[0])
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
        if j >= 5000: break
    if sorted_letters:
        return False
    return new_structure

def identical(list_A, list_B):
    """
    True if all elements in A list are identical to elements in B list in sorted order or original order

    Args:
        list_A: list compared to another list
        list_B: list compared to another list
    """
    if len(list_A) != len(list_B):
        return False
    try:
        return np.all([sorted(list_A)[i] == sorted(list_B)[i] for i in range(len(list_A))])
    except:
        return np.all([list_A[i] == list_B[i] for i in range(len(list_A))])

def tree_gen(spg_symbol, num_of_atom, letter_candidates_symbols, letter_candidates_numbers, pre_used = []):
    """
    An iterative tree generation process of assigning certain number of atoms in the candidate sites 
    (e.g., 12 atoms assigned in the wyckoff sites of spacegroup "R-3mH"), 
    see the final outcome in the result of filter_replicate function below
    
    Args:
        spg_symbol: string of spacegroup selected (e.g., "R-3mH")
        num_of_atom: the number of atoms assigned in candidate sites
        letter_candidates_symbols: list of all string of Wyckoff letters in selected spacegroup (e.g., ['a', 'b', 'c', 'd'] for "Pnma" 
                                   resulted from the sp_dict dictionary class, usually sp_dict['Pnma'].keys())
        letter_candidates_numbers: list of all multiplicities of Wyckoff letters in selected spacegroup, mapping the 
                                   string of Wyckoff letters in letter_candidates_symbols (e.g., sp_dict['Pnma'].values())
        pre_used: list including the used Wyckoff letters during the iteration process, when all Wyckoff letters used, iteration end up

    Returns:
        A tree dictionary class indicates the feasible combination of different Wyckoff letters in case of certain number of atoms
    """
    if not pre_used:
        if num_of_atom == 0:
            return True
        qualified_candidate_symbols = np.array(letter_candidates_symbols)[np.array(letter_candidates_numbers) <= num_of_atom].tolist()
        if qualified_candidate_symbols:
            tree = {}
            for letter in qualified_candidate_symbols:
                new_num_of_atom = num_of_atom - len(pos_gen_wyckoff_positions(spg_symbol, letter))
                new_letter_candidates_numbers = [num for num in letter_candidates_numbers]
                new_letter_candidates_symbols = [sym for sym in letter_candidates_symbols]
                if identical(pos_gen_wyckoff_positions(spg_symbol, letter), pos_gen_wyckoff_positions(spg_symbol, letter)):
                    del new_letter_candidates_numbers[new_letter_candidates_symbols.index(letter)]
                    new_letter_candidates_symbols.remove(letter)
                    tree[letter] = tree_gen(spg_symbol, new_num_of_atom, new_letter_candidates_symbols, new_letter_candidates_numbers, pre_used)
                else:
                    tree[letter] = tree_gen(spg_symbol, new_num_of_atom, new_letter_candidates_symbols, new_letter_candidates_numbers, pre_used)
            return tree
        else:
            return False
    else:
        new_letter_candidates_numbers = [num for num in letter_candidates_numbers]
        new_letter_candidates_symbols = [sym for sym in letter_candidates_symbols]
        for letter in pre_used:
            if identical(pos_gen_wyckoff_positions(spg_symbol, letter), pos_gen_wyckoff_positions(spg_symbol, letter)):
                del new_letter_candidates_numbers[new_letter_candidates_symbols.index(letter)]
                new_letter_candidates_symbols.remove(letter)
        return tree_gen(spg_symbol, num_of_atom, new_letter_candidates_symbols, new_letter_candidates_numbers, [])

def list_all_dict(tree, l = []):
    """
    Transfer the tree dictionary into list according to their feasibility

    Args:
        tree: the tree class generated by tree_gen function

    Returns:
        list of all combination of different Wyckoff letters
    """
    if isinstance(tree, dict):
        result = []
        for k in tree.keys():
            a = [i for i in l]
            a.append(k)
            c = list_all_dict(tree[k], a)
            if isinstance(tree[k], bool):
                result.append(c)
            else:
                result.extend(c)
        return result
    elif not tree:
        return None
    else:
        return l

def filter_replicate(r):
    """
    Elimibate the repeated combination in the result of list_all_dict function
    """
    r = filter(None, r)
    o = []
    for i in r:
        if np.all([not identical(j, i) for j in o]):
            o.append(i)
    return o

def permutate(spg_symbol, num_of_atom, symbol_of_atom, letter_candidates_symbols, letter_candidates_numbers, letters = []):
    """
    Return a tuple of a list of all permutations and according type of atom (e.g., mapping 6 O atoms in the Wyckoff sites of spacegrop "R-3mH"
    will result in two permutations: ['a', 'b'] and ['c'])
    """
    letter_symbols = sp_dict[spg_symbol].keys()
    letter_numbers = sp_dict[spg_symbol].values()
    tree = tree_gen(spg_symbol, num_of_atom, letter_symbols, letter_numbers, letters)
    permutation = filter_replicate(list_all_dict(tree))
    s = deepcopy(permutation)
    for i in s:
        for j in range(len(i)):
            i[j] = symbol_of_atom
    return permutation, s

def permutation_gen(spg_symbol, num_of_atoms, symbol_of_atoms):
    """
    Return a tuple of a list of all permutations and according types of atoms (e.g., mapping 3 Li atoms, 3 Co atoms, 6 O atoms in the Wyckoff sites of spacegrop "R-3mH"
    will result in two permutations: ['a', 'b', 'c'] for ['Li', 'Co', 'O'] and ['b', 'a', 'c'] for ['Li', 'Co', 'O'])
    """
    if not spg_symbol in sp_dict.keys():
        raise ValueError("Bad international symbol {:s}".format(spg_symbol))
    if len(symbol_of_atoms) != len(num_of_atoms):
        raise IndexError("Wrong symbol list was input!")
    letter_candidates_symbols = sp_dict[spg_symbol].keys()
    letter_candidates_numbers = sp_dict[spg_symbol].values()
    letters = []
    letters_permutation, symbols_permutation = permutate(spg_symbol, num_of_atoms.pop(0), symbol_of_atoms.pop(0), letter_candidates_symbols, letter_candidates_numbers, letters)
    while num_of_atoms:
        next_letters = []
        next_symbols = []
        for l, s in zip(letters_permutation, symbols_permutation):
            temp_letters_permutation, temp_symbols_permutation = permutate(spg_symbol, num_of_atoms[0], symbol_of_atoms[0], letter_candidates_symbols, letter_candidates_numbers, l)
            next_letters_permutation = [np.concatenate((l, i)).tolist() for i in temp_letters_permutation]
            next_symbols_permutation = [np.concatenate((s, i)).tolist() for i in temp_symbols_permutation]
            next_letters.extend(next_letters_permutation)
            next_symbols.extend(next_symbols_permutation)
        symbol_of_atoms.pop(0)
        num_of_atoms.pop(0)
        letters_permutation = deepcopy(next_letters)
        symbols_permutation = deepcopy(next_symbols)
    return letters_permutation, symbols_permutation



def test():
    letter_permutation, symbol_permutation = permutation_gen('R-3mH', [3, 3, 6], ['Li', 'Co', 'O'])
    return letter_permutation, symbol_permutation
