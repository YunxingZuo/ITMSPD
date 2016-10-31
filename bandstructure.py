# coding: utf-8
# Copyright © 2016 YunXing Zuo, WeiJi Hsiao

import numpy as np
import math
import collections
from structure import Structure
from kpoint import Kpoint

__author__ = 'YunXing Zuo, WeiJi Hsiao'
__email__ = 'weiji.hsiao@gmail.com'
__date__ = 'Oct. 25, 2016'

class BandStructure(object):
	def __init__(self, kpoints, eigenvalues, rec_lattice, efermi, is_cartesian = False, labels_dict = None):
		"""
		Create a BandStructure object.

		Args:
			kpoints (List):
			eigenvalues (dict):
			rec_lattice (Lattice/3x3 array):
			efermi (float):
			is_cartesian (bool):
			labels_dict (dict):
		"""
		self.__efermi = efermi

		if labels_dict is None:
			labels_dict = {}

		self.__kpoints = []
		for k in kpoints:
			label = None
			for l in labels_dict:
				if np.linalg.norm(k - np.array(labels_dict[l])) < 0.0001:
					label = l
			self.__kpoints.append(Kpoint(rec_lattice, k, is_cartesian, label))

		self.__bands = {spin:np.array(eigenv) for spin, eigenv in eigenvalues.items()}
		self.__nbands = len(eigenvalues[1])
		self.__is_spin_polarized = len(self.__bands) == 2

	def __repr__(self):
		pass

	@property
	def efermi(self):
		return self.__efermi

	@efermi.setter
	def efermi(self, efermi):
		self.__efermi = efermi

	def is_metal(self):
		for spin, eigenv in self.__bands.items():
			for i in range(self.__nbands):
				if np.any(eigenv[i, :] < self.__efermi) and np.any(eigenv[i, :] > self.__efermi):
					return True
		return False

	def get_vbm(self):
		if self.is_metal():
			return {'band_index': [], 
			        'kpoint_index': [], 
			        'kpoint': [], 
			        'energy': None}

		max_tmpt = -float('inf')
		kpoint_index = None
		kpointvbm = None
		for spin, eigenv in self.__bands.items():
			for i, j in zip(*np.where(eigenv < self.__efermi)):
				if eigenv[i, j] > max_tmpt:
					max_tmpt = float(eigenv[i, j])
					kpoint_index = j
					kpointvbm = self.__kpoints[j]

		list_of_kpoints = []
		if kpointvbm.label is not None:
			for i in range(self.__kpoints):
				if self.__kpoints[i].label == kpointvbm.label:
					list_of_kpoints.append(i)
		else:
			list_of_kpoints.append(kpoint_index)

		list_of_bands = collections.defaultdict(list)
		for spin in self.__bands:
			for i in range(self.__nbands):
				if math.fabs(self.__bands[spin][i][kpoint_index] - max_tmpt) < 0.001:
					list_of_bands[spin].append(i)

		return {'band_index': list_of_bands,
				'kpoint_index': list_of_kpoints,
				'kpoint': kpointvbm,
				'energy': max_tmpt}

	def get_cbm(self):
		if self.is_metal():
			return {'band_index': [], 
			        'kpoint_index': [], 
			        'kpoint': [], 
			        'energy': None}

		max_tmpt = float('inf')
		kpoint_index = None
		kpointcbm = None
		for spin, eigenv in self.__bands.items():
			for i, j in zip(*np.where(eigenv > self.__efermi)):
				if eigenv[i, j] < max_tmpt:
					max_tmpt = float(eigenv[i, j])
					kpoint_index = j
					kpointcbm = self.__kpoints[j]

		list_of_kpoints = []
		if kpointcbm.label is not None:
			for i in range(self.__kpoints):
				if self.__kpoints[i].label == kpointcbm.label:
					list_of_kpoints.append(i)
		else:
			list_of_kpoints.append(kpoint_index)

		list_of_bands = collections.defaultdict(list)
		for spin in self.__bands:
			for i in range(self.__nbands):
				if math.fabs(self.__bands[spin][i][kpoint_index] - max_tmpt) < 0.001:
					list_of_bands[spin].append(i)

		return {'band_index': list_of_bands,
				'kpoint_index': list_of_kpoints,
				'kpoint': kpointcbm,
				'energy': max_tmpt}
 
	def get_kpoints(self):
		pass

	def get_structure(self):
		pass

	@staticmethod
	def import_from_vasp(filename):
		pass

	def plot(self, filename):
		pass