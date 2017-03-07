# coding: utf-8

from structure import *
from heihei import *
import os

def generate100(spg_symbol, lattice, num_atoms, spe_atoms, num_individual = 50):
    parentdir = os.getcwd()
    letter_candidate_symbols = sp_dict[spg_symbol].keys()
    letter_candidate_numbers = sp_dict[spg_symbol].values()
    letter_permutation, symbol_permutation = permutation_gen(spg_symbol, num_atoms, spe_atoms, letter_candidate_symbols, letter_candidate_numbers)
    number = 0
    useless_index = []
    while number < num_individual:
        print number
        index = int(round(rand() * len(letter_permutation)))
        while index in useless_index:
            index = int(round(rand() * len(letter_permutation)))
        structure = structure_generation(spg_symbol, lattice, letter_permutation[index], symbol_permutation[index])
        if not structure:
            useless_index.append(index)
        else:
            createdir(str(number))
            structure.export_to_pwmat('atom.config')
            os.chdir(parentdir)
            number += 1
    return useless_index


def createdir(childir):
    currentdir = os.getcwd()
    nextdir = os.path.join(currentdir, childir)
    os.mkdir(nextdir)
    os.chdir(nextdir)
