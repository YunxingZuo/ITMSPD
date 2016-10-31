# coding: utf-8
# Copyright © 2016 YunXing Zuo, WeiJi Hsiao

from math import pi, sin, cos
import numpy as np
import itertools
from scipy.spatial import Voronoi

__author__ = 'YunXing Zuo, WeiJi Hsiao'
__email__ = 'weiji.hsiao@gmail.com'
__date__ = 'Oct. 25, 2016'

class Lattice(object):
    def __init__(self,vectors):
        """
        Create a Lattice object.
        Args:
            vectors (Array/List): A Array or a List corresponds to the lattice vectors.
        """
        self.__vectors = np.array(vectors, dtype = np.float64).reshape((3,3))
        self.__lengths = np.zeros(3)
        for i in range(3):
            self.__lengths[i] = np.sqrt(np.sum(x * x for x in self.__vectors[i]))
        self.__angles = np.zeros(3)
        for i in range(3):
            j = (i + 1) % 3
            k = (i + 2) % 3
            cos_angle = np.dot(self.__vectors[j], self.__vectors[k]) / (self.__lengths[j] * self.__lengths[k])
            self.__angles[i] = np.arccos(cos_angle) * 180.0 / pi
        self.__volume = np.dot(self.__vectors[0], np.cross(self.__vectors[1], self.__vectors[2]))

    def __repr__(self):
        strings = ['Lattice',
                   '  lengths : {:>16.8f}{:>16.8f}{:>16.8f}'.format(*self.__lengths),
                   '  angles  : {:>16.8f}{:>16.8f}{:>16.8f}'.format(*self.__angles),
                   '  volume  : {:16.8f}'.format(self.__volume),
                   '  vector1 : {:>16.8f}{:>16.8f}{:>16.8f}'.format(*self.__vectors[0]),
                   '  vector2 : {:>16.8f}{:>16.8f}{:>16.8f}'.format(*self.__vectors[1]),
                   '  vector3 : {:>16.8f}{:>16.8f}{:>16.8f}'.format(*self.__vectors[2])]
        return '\n'.join(strings)

    def is_similar_to(self, other, tolerance = 1e-5):
        """
        Returns True if the lattice is similar to the given one within a tolerance.

        Args:
            other (Lattice): The lattice to compare to.
            tolerance (float): The tolerance parameter to compare against the absolute difference of vector-coordinates between two lattices.
        """
        if self is other:
            return True
        if not isinstance(other, Lattice):
            return False
        for i in range(3):
            if any([abs(diff) >= tolerance for diff in np.array(self.vectors[i] - other.vectors[i])]):
                return False
        return True

    @staticmethod
    def from_lengths_and_angles(a, b, c, alpha, beta, gamma, is_radius = False):
        """
        Create a Lattice object from a set of lengths and angles.
        Args:
            a (float):
            b (float):
            c (float):
            alpha (float):
            beta (float):
            gamma (float):
            is_radius (bool): Whether the angles comes in radius. Default is False.
        """
        if not is_radius:
            al = alpha * pi / 180
            be = beta * pi / 180
            ga = gamma * pi / 180
        else:
            al = alpha
            be = beta
            ga = gamma
        ax = a
        ay = 0
        az = 0
        bx = b * cos(ga)
        by = b * sin(ga)
        bz = 0
        cx = c * cos(be)
        cy = c * ((cos(al) - cos(ga)*cos(be))/sin(ga))
        cz = np.sqrt(c*c - cx**2 - cy**2)
        return Lattice([[ax, ay, az], [bx, by, bz], [cx, cy, cz]])
    
    @property
    def vectors(self):
        return self.__vectors
    
    @property
    def lengths(self):
        return self.__lengths
    
    @property
    def angles(self):
        return self.__angles
    
    @property
    def volume(self):
        return self.__volume
    
    @property
    def a(self):
        return self.__lengths[0]
    
    @property
    def b(self):
        return self.__lengths[1]
    
    @property
    def c(self):
        return self.__lengths[2]
    
    @property
    def alpha(self):
        return self.__angles[0]
    
    @property
    def beta(self):
        return self.__angles[1]
    
    @property
    def gamma(self):
        return self.__angles[2]

    def get_cart_coords(self, frac_coords):
        return np.dot(frac_coords, self.__vectors)

    def get_frac_coords(self, cart_coords):
        return np.dot(cart_coords, np.linalg.inv(self.__vectors))

    @property
    def reciprocal_lattice(self):
        rec_lattice = []
        for i in range(3):
            j = (i + 1) % 3
            k = (i + 2) % 3
            rec_lattice.append(2 * pi * np.cross(self.__vectors[j], self.__vectors[k]) / self.__volume)
        return Lattice(rec_lattice)

    @property
    def reciprocal_lattice_crystallographic(self):
        """
        Returns the *crystallographic* reciprocal lattice, i.e., no factor of
        2 * pi.
        """
        return Lattice(self.reciprocal_lattice.vectors / (2 * np.pi))

    def get_wigner_seitz_cell(self):
        """
        Get the Wigner-Seitz Cell of the lattice.

        Returns:
            A List of List of coordinates.
        """
        vector1 = self.__vectors[0]
        vector2 = self.__vectors[1]
        vector3 = self.__vectors[2]

        points = []
        for i, j, k in itertools.product([-1, 0, 1], [-1, 0, 1], [-1, 0, 1]):
            points.append(i * vector1 + j * vector2 + k * vector3)
        vor = Voronoi(points)
        ws_cell = []
        for r in vor.ridge_dict:
            if r[0] == 12 or r[1] == 13:
                ws_cell.append([vor.vertices[i] for i in vor.ridge_dict[r]])
        return ws_cell

    def get_brillouin_zone(self):
        """
        Get the Brillouin Zone of the lattice.
        """
        return self.reciprocal_lattice.get_wigner_seitz_cell()