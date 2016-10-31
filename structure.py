# coding: utf-8
# Copyright © 2016 YunXing Zuo, WeiJi Hsiao

from math import pi, fabs
import numpy as np
import itertools

from lattice import Lattice
from element import Element
from Symmetry_Operation import *

import spglib

__author__ = 'YunXing Zuo, WeiJi Hsiao'
__email__ = 'weiji.hsiao@gmail.com'
__date__ = 'Oct. 25, 2016'

class Structure(object):
    def __init__(self, lattice, positions, atoms, is_cartesian = False, name = None):
        """
        Create a Structure object.

        Args:
            lattice(Lattice or 3x3 Array): The lattice either as a Lattice object or as a 3x3 array of which each raw corresponds to a lattice vector.
            frac_positions (List): A List of fractional coordinates of each atom.
            atoms (List): A List of atoms either as atomic symbols or as atomic numbers or Element objects.
            name (str): The name of the system. Default is None.

        """
        if isinstance(lattice, Lattice):
            self.__lattice = lattice
        else:
            self.__lattice = Lattice(lattice)

        if is_cartesian:
            self.__cart_positions = np.array(positions)
            self.__frac_positions = self.__lattice.get_frac_coords(positions)
        else:
            self.__frac_positions = np.array(positions)
            self.__cart_positions = self.__lattice.get_cart_coords(positions)

        self.__atoms = []
        for atom in atoms:
            if isinstance(atom, Element):
                element = atom
            else:
                element = Element(atom)
            self.__atoms.append(element)

        self.__element_species = []
        self.__num_per_species = []

        for species, atoms in itertools.groupby(self.__atoms):
            self.__element_species.append(species)
            self.__num_per_species.append(len(list(atoms)))

        # tempt = None
        # for atom in self.__atoms:
            # if tempt != atom:
                # self.__element_species.append(atom)
                # self.__num_per_species.append(1)
                # tempt = atom
            # else:
                # self.__num_per_species[-1] += 1

        if name is None:
            name = ''.join('{:s}{:d} '.format(element.atomic_symbol,num) for element, num in zip(self.__element_species, self.__num_per_species))
        self.__name = name

    def __repr__(self):
        strings = []
        strings.append('Structure of {name}'.format(name = self.__name))
        strings.append(str(self.__lattice))
        strings.append('Atoms')
        for element, num in zip(self.__element_species, self.__num_per_species):
            strings.append('{:>4s} : {:<4d}'.format(element.atomic_symbol,num))
        strings.append('Fractional Coordinates')
        for atom, position in zip(self.__atoms, self.__frac_positions):
            strings.append('{:>4s} : {:>16.8f}{:>16.8f}{:>16.8f}'.format(atom.atomic_symbol, *position))
        return '\n'.join(strings)

    def is_similar_to(self, other, tolerance = 1e-5):
        """
        Returns True if the structure is similar to the given one within a tolerance.

        Args:
            other (Structure): The structure to compare to.
            tolerance (float): The tolerance parameter to compare against the absolute difference of vector-coordinates
                               as well as frac_position-coordinates between two structures.
        """
        if self is other:
            return True
        if not isinstance(other, Structure):
            return False
        if self.number_of_atoms != other.number_of_atoms:
            return False
        if not self.lattice.is_similar_to(other.lattice, tolerance):
            return False
        for i, self_pos in enumerate(self.frac_positions):
            for j, other_pos in enumerate(other.frac_positions):
                if all([abs(diff) < tolerance for diff in np.array(self_pos - other_pos)]):
                    if self.atomic_symbols[i] != other.atomic_symbols[j]:
                        return False
                    break
            else:
                return False
        return True


    @property
    def lattice(self):
        return self.__lattice

    @property
    def lattice_vectors(self):
        return self.__lattice.vectors

    @property
    def frac_positions(self):
        return self.__frac_positions

    @property
    def cart_positions(self):
        return self.__cart_positions

    @property
    def atomic_symbols(self):
        return [atom.atomic_symbol for atom in self.__atoms]

    @property
    def atomic_numbers(self):
        return [atom.atomic_number for atom in self.__atoms]

    @property
    def number_of_atoms(self):
        return len(self.__atoms)

    @property
    def element_species(self):
        return self.__element_species

    @property
    def num_per_species(self):
        return self.__num_per_species

    def as_tuple(self):
        """
        Create a tuple for spglib input.
        """
        return (self.__lattice.vectors, np.array(self.__frac_positions), np.array(self.atomic_numbers))

    def create_supercell(self, trans_matrix):
        """
        Create a supercell.

        Args:
            trans_matrix: A matirx, of which all elements should be integers, for transformaing the lattice vectors.
                          There are several options:
                          1. A 3x3 matrix. For instance, [[2, 1, 0], [1, 1, 0], [0, 0, 1]] creates a new structure with
                             lattice vectors a' = 2a + b, b' = a + b, and c' = c, where a, b, and c are the lattice vectors
                             of the original structure.
                          2. A List of three scaling factors. For instance, [2, 2, 1] creates a new structure with dimensions
                             2a x 2b x c.
                          3. A number which scales all vectors by the same factor.

        Returns:
            Supercell as a Structure object.
        """
        trans_matrix = np.array(trans_matrix, dtype = 'intc')
        if trans_matrix.shape != (3, 3):
            trans_matrix = np.array(trans_matrix * np.eye(3), dtype = 'intc')

        frame = np.array([[0,0,0],\
                          [1,0,0],\
                          [0,1,0],\
                          [0,0,1],\
                          [1,1,0],\
                          [1,0,1],\
                          [0,1,1],\
                          [1,1,1]])
        frame_projection = np.dot(frame, trans_matrix)
        scaling_ratios = [(min(frame_projection[:, i]), max(frame_projection[:, i])) for i in range(3)]

        atomic_numbers = self.atomic_numbers
        old_position_coords = self.frac_positions
        extended_atomic_numbers = []
        extended_old_position_coords = []
        for n, position in enumerate(old_position_coords):
            for i in itertools.product(range(*scaling_ratios[0]), range(*scaling_ratios[1]), range(*scaling_ratios[2])):
                extended_atomic_numbers.append(atomic_numbers[n])
                extended_old_position_coords.append(position + np.array(i))

        new_lattice_vectors = np.dot(trans_matrix, self.lattice_vectors)
        extended_new_position_coords = np.dot(extended_old_position_coords, np.linalg.inv(trans_matrix))

        new_atomic_numbers = []
        new_position_coords = []
        for i in range(len(extended_new_position_coords)):
            if all([(0 <= coord < 1) for coord in extended_new_position_coords[i]]):
                new_atomic_numbers.append(extended_atomic_numbers[i])
                new_position_coords.append(extended_new_position_coords[i])

        return Structure(new_lattice_vectors, new_position_coords, new_atomic_numbers)

    def find_primitive_cell(self, symprec = 1e-3, angle_tolerance = 5):
        """
        Find the primitive cell of the structure.

        Returns:
            Primitive cell as a Structure object.
        """
        vectors, positions, atomic_numbers = spglib.find_primitive(self.as_tuple(), symprec = symprec, angle_tolerance = angle_tolerance)
        for i in range(len(positions)):
            for j in range(3):
                if fabs(positions[i][j] - 1) < 0.01:
                    positions[i][j] = 0
        return Structure(vectors, positions, atomic_numbers)

    def get_symmetry_dataset(self, symprec = 1e-3, angle_tolerance = 5):
        return spglib.get_symmetry_dataset(self.as_tuple(), symprec = symprec, angle_tolerance = angle_tolerance)

    def get_symmetry_operations(self, symprec = 1e-3, angle_tolerance = 5):
        return spglib.get_symmetry(self.as_tuple(), symprec = symprec, angle_tolerance = angle_tolerance)

    def get_spacegroup(self, symprec = 1e-3, angle_tolerance = 5):
        return spglib.get_spacegroup(self.as_tuple(), symprec = symprec, angle_tolerance = angle_tolerance)

    def get_pointgroup(self):
        ro = self.get_symmetry_operations()['rotations']
        if len(ro) == 0:
            return '1'
        return spglib.get_pointgroup(ro)[0]

    def get_crystal_system(self):
        n = self.get_symmetry_dataset()['number']

        f = lambda i, j: i <= n <= j
        cs = {"triclinic": (1, 2), "monoclinic": (3, 15), "orthorhombic": (16, 74), \
        "tetragonal": (75, 142), "trigonal": (143, 167), "hexagonal": (168, 194), \
        "cubic": (195, 230)}

        crystal_system = None

        for k, v in cs.items():
            if f(*v):
                crystal_system = k
                break
        return crystal_system

    def get_identical_atoms_and_operations(self, additional_symmetry_operations = None, symprec = 1e-3):
        lattice_vectors = self.lattice_vectors
        scaled_positions = self.frac_positions
        rotations = self.get_symmetry_operations()['rotations']
        translations = self.get_symmetry_operations()['translations']
        if not additional_symmetry_operations is None:
            for add_symmop in additional_symmetry_operations:
                ro = add_symmop.rotation_matrix.reshape(1, 3, 3)
                tran = add_symmop.translation_vector.reshape(1, 3)
                rotations = np.append(rotations, ro, axis = 0)
                translations = np.append(translations, tran, axis = 0)
        identical_atoms = [i for i in range(self.number_of_atoms)]
        identical_operations = {}
        for i, p in enumerate(scaled_positions):
            is_found = False
            for j in range(i):
                for r, t in zip(rotations, translations):
                    symmop = SymmOp.rotations_combine_translation(r, t)
                    is_found = symmop.whether_symmetrical(p, scaled_positions[j], lattice_vectors)
                    if is_found:
                        identical_atoms[i] = j
                        key = '{}->{}'.format(i, j)
                        value = symmop.affine_matrix
                        identical_operations[key] = value
                        break
                if is_found:
                    break
        return np.array(identical_atoms, dtype='intc'), identical_operations

    def get_independent_atoms(self, additional_symmetry_operations = None, symprec = 1e-3):
        indep_atoms = []
        identical_atoms = self.get_identical_atoms_and_operations(additional_symmetry_operations, symprec)[0]
        for i, eq in enumerate(identical_atoms):
            if i == eq:
                indep_atoms.append(i)
        return np.array(indep_atoms, dtype='intc')

    @staticmethod
    def import_from_vasp(filename):
        """
        Import structure data from a VASP POSCAR or CONTCAR file.

        Args:
            filename (str): The file to import from.

        Returns:
            A Structure object.
        """
        with open(filename) as f:
            lines = f.readlines()

            name = lines[0].strip('\n')
            scale = float(lines[1])

            vectors = []
            for i in range(2, 5):
                vector = [float(coord) * scale for coord in lines[i].split()[:3]]
                vectors.append(vector)

            lattice = Lattice(vectors)

            num_per_species = []
            for x in lines[6].split():
                try:
                    num = int(x)
                    num_per_species.append(num)
                except ValueError:
                    pass
            element_species_symbols = lines[5].split()[:len(num_per_species)]
            atoms = []
            for symbol, num in zip(element_species_symbols, num_per_species):
                atoms += [symbol] * num

            if lines[7][0].lower() == 's':
                index = 8
            else:
                index = 7

            if (lines[index][0].lower() == 'c' or lines[index][0].lower() == 'k'):
                is_cartesian = True
            else:
                is_cartesian = False
            index += 1
            positions = []
            for i in range(index, index+sum(num_per_species)):
                position = [float(coord) for coord in lines[i].split()[:3]]
                positions.append(position)
        return Structure(lattice, positions, atoms, is_cartesian, name)

    def export_to_vasp(self, filename, is_cartesian = False, scale = 1.0):
        """
        Export structure data to a VASP POSCAR file.

        Args:
            filename (str): The file to export to.
            is_cartesian (bool): Whether to switch to cartesian mod in which all the atom positions are represented as cartesian coordinates. Default is False.
            scale (float): The universal scaling factor which is used to scale all lattice vectors and all atom coordinates. Defaults to 1.0.
        """
        lines = []
        lines.append(self.__name)
        lines.append(str(scale))
        vectors = self.__lattice.vectors / scale
        for vector in vectors:
            lines.append('{:>16.8f}{:>16.8f}{:>16.8f}'.format(*vector))
        lines.append(''.join('{:>6s}'.format(element.atomic_symbol) for element in self.__element_species))
        lines.append(''.join('{:>6d}'.format(num) for num in self.__num_per_species))
        if is_cartesian:
            positions = self.cart_positions / scale
            lines.append('Cartesian')
        else:
            positions = self.frac_positions
            lines.append('Direct')
        for position in positions:
            lines.append('{:>16.8f}{:>16.8f}{:>16.8f}'.format(*position))

        with open(filename, 'w') as f:
            f.write('\n'.join(lines))

    @staticmethod
    def import_from_pwmat(filename):
        """
        Import structure data from a PWmat atom.config file.

        Args:
            filename (str): The file to import from.

        Returns:
            A Structure object.
        """
        with open(filename) as f:
            lines = f.readlines()

            number_of_atoms = int(lines[0].split()[0])

            lattice_vectors = []
            if lines[1][0].lower() == 'l':
                for i in range(2, 5):
                    lattice_vectors.append([float(x) for x in lines[i].split()[:3]])

            if lines[5][0].lower() == 'p':
                line_index = 6

            positions = []
            atomic_numbers = []
            end_line_index = line_index + number_of_atoms
            for i in range(line_index, end_line_index):
                atomic_numbers.append(int(lines[i].split()[0]))
                positions.append([float(x) for x in lines[i].split()[1:4]])

            return Structure(lattice_vectors, positions, atomic_numbers)

    def export_to_pwmat(self, filename, whether_to_move = None):
        """
        Export structure data to a PWmat atom.config file.

        Args:
            filename (str): The file to export to.
            whether_to_move (List): A List of List[imx, imy, imz] where imx, imy and imz are flags for whether to move atoms in x, y, z directions
                                    (not the lattice vector directions) to RELAX.
                                    1 means to relax that atom in that direction
                                    0 means to fix that atom in that direction
                                    Default is [[1, 1, 1], [1, 1, 1], [1, 1, 1], ...]
        """
        if whether_to_move is None:
            whether_to_move = [[1, 1, 1] for i in range(self.number_of_atoms)]

        lines = []
        lines.append('{:d}'.format(self.number_of_atoms))
        lines.append('Lattice vector')
        for vector in self.lattice_vectors:
            lines.append('{:>16.8f}{:>16.8f}{:>16.8f}'.format(*vector))
        lines.append('Position')
        for number, position, im in zip(self.atomic_numbers, self.frac_positions, whether_to_move):
            lines.append('{0:>4d}{1[0]:>16.8f}{1[1]:>16.8f}{1[2]:>16.8f}{2[0]:>6d}{2[1]:>6d}{2[2]:>6d}'.format(number, position, im))
        with open(filename, 'w') as f:
            f.write('\n'.join(lines))

    @staticmethod
    def import_from_cif(filename):
        positions = []
        atoms = []
        with open(filename) as f:
            for line in f:
                if (line.find('length_a') >= 0):
                    a = float(line.split()[1])
                    continue
                if (line.find('length_b') >= 0):
                    b = float(line.split()[1])
                    continue
                if (line.find('length_c') >= 0):
                    c = float(line.split()[1])
                    continue
                if (line.find('angle_alpha') >= 0):
                    alpha = float(line.split()[1])
                    continue
                if (line.find('angle_beta') >= 0):
                    beta = float(line.split()[1])
                    continue
                if (line.find('angle_gamma') >= 0):
                    gamma = float(line.split()[1])
                    continue
                if (line.find('Biso') >= 0):
                    positions.append([float(coord) for coord in line.split()[2:5]])
                    atoms.append(Element(line.split()[7]))
        lattice = Lattice.from_lengths_and_angles(a, b, c, alpha, beta, gamma)
        return Structure(lattice, positions, atoms)


    def export_to_cif(self, filename):
        pass