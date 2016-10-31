# coding: utf-8
# Copyright © 2016 YunXing Zuo, WeiJi Hsiao

import numpy as np
from lattice import Lattice

__author__ = 'YunXing Zuo, WeiJi Hsiao'
__email__ = 'weiji.hsiao@gmail.com'
__date__ = 'Oct. 25, 2016'

class Kpoint(object):
	def __init__(self, rec_lattice, coordinates, is_cartesian = False, label = None):
		if isinstance(rec_lattice, Lattice):
			self.__rec_lattice = rec_lattice
		else:
			self.__rec_lattice = Lattice(rec_lattice)

		if is_cartesian:
			self.__cart_coords = np.array(coordinates)
			self.__frac_coords = self.__rec_lattice.get_frac_coords(coordinates)
		else:
			self.__frac_coords = np.array(coordinates)
			self.__cart_coords = self.__rec_lattice.get_cart_coords(coordinates)

		self.__label = label

	@property
	def rec_lattice(self):
		return self.__rec_lattice

	@property
	def rec_vectors(self):
		return self.__rec_lattice.vectors

	@property
	def frac_coords(self):
		return self.__frac_coords

	@property
	def cart_coords(self):
		return self.__cart_coords

	@property
	def label(self):
		return self.__label
