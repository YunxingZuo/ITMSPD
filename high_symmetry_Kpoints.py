# coding: utf-8
# Copyright © 2016 YunXing Zuo, WeiJi Hsiao

import numpy as np

from math import ceil
from math import cos
from math import sin
from math import tan
from math import pi

__author__ = 'YunXing Zuo, WeiJi Hsiao'
__email__ = 'weiji.hsiao@gmail.com'
__date__ = 'Oct. 25, 2016'

class HighSymmKpath(object):
    def __init__(self, abc, angles, lattice_system, spg_symbol):
        self._abc = abc
        self._angles = angles


        if lattice_system == "cubic":
            if "P" in spg_symbol:
                self.high_symmetry_kpoints = self.cubic()
            elif "F" in spg_symbol:
                self.high_symmetry_kpoints = self.fcc()
            elif "I" in spg_symbol:
                self.high_symmetry_kpoints = self.bcc()
            else:
                warn("Unexpected value for spg_symbol: %s" % spg_symbol)

        elif lattice_system == "tetragonal":
            if "P" in spg_symbol:
                self.high_symmetry_kpoints = self.tet()
            elif "I" in spg_symbol:
                a = self._abc[0]
                c = self._abc[2]
                if c < a:
                    self.high_symmetry_kpoints = self.bctet1(c, a)
                else:
                    self.high_symmetry_kpoints = self.bctet2(c, a)
            else:
                warn("Unexpected value for spg_symbol: %s" % spg_symbol)

        elif lattice_system == "orthorhombic":
            a, b, c = self.abc()

            if "P" in spg_symbol:
                self.high_symmetry_kpoints = self.orc()

            elif "F" in spg_symbol:
                if 1 / a ** 2 > 1 / b ** 2 + 1 / c ** 2:
                    self.high_symmetry_kpoints = self.orcf1(a, b, c)
                elif 1 / a ** 2 < 1 / b ** 2 + 1 / c ** 2:
                    self.high_symmetry_kpoints = self.orcf2(a, b, c)
                else:
                    self.high_symmetry_kpoints = self.orcf3(a, b, c)

            elif "I" in spg_symbol:
                self.high_symmetry_kpoints = self.orci(a, b, c)

            elif "C" in spg_symbol:
                self.high_symmetry_kpoints = self.orcc(a, b)
            else:
                warn("Unexpected value for spg_symbol: %s" % spg_symbol)

        elif lattice_system == "hexagonal":
            self.high_symmetry_kpoints = self.hex()

        elif lattice_system == "rhombohedral" or lattice_system == "trigonal":
            alpha = self._angles[0]
            if alpha < 90:
                self.high_symmetry_kpoints = self.rhl1(alpha * pi / 180)
            else:
                self.high_symmetry_kpoints = self.rhl2(alpha * pi / 180)

        elif lattice_system == "monoclinic":
            a, b, c = self.abc()
            alpha, beta, gamma = self.angles()

            if "P" in spg_symbol:
                self.high_symmetry_kpoints = self.mcl(b, c, alpha * pi / 180)

            elif "C" in spg_symbol:
                if gamma > 90:
                    self.high_symmetry_kpoints = self.mclc1(a, b, c, alpha * pi / 180)
                elif gamma == 90:
                    self.high_symmetry_kpoints = self.mclc2(a, b, c, alpha * pi / 180)
                elif gamma < 90:
                    if b * cos(alpha * pi / 180) / c + b ** 2 * sin(alpha * pi / 180) ** 2 / (a ** 2) < 1:
                        self.high_symmetry_kpoints = self.mclc3(a, b, c, alpha * pi / 180)
                    elif b * cos(alpha * pi / 180) / c + b ** 2 * sin(alpha * pi / 180) ** 2 / (a ** 2) == 1:
                        self.high_symmetry_kpoints = self.mclc4(a, b, c, alpha * pi / 180)
                    elif b * cos(alpha * pi / 180) / c + b ** 2 * sin(alpha * pi / 180) ** 2 / (a ** 2) > 1:
                        self.high_symmetry_kpoints = self.mclc5(a, b, c, alpha * pi / 180)
            else:
                warn("Unexpected value for spg_symbol: %s" % spg_symbol)

        elif lattice_system == "triclinic":
            alpha, beta, gamma = self.angles()
            if alpha > 90 and beta > 90 and min(alpha, beta, gamma) > 90:
                self.high_symmetry_kpoints = self.tri_1a()
            elif alpha > 90 and beta > 90 and gamma == 90:
                self.high_symmetry_kpoints = self.tri_2a()
            elif alpha < 90 and beta < 90 and max(alpha, beta, gamma) < 90:
                self.high_symmetry_kpoints = self.tri_1b()
            elif alpha < 90 and beta < 90 and gamma == 90:
                self.high_symmetry_kpoints = self.tri_2b()
            else:
                warn("Unexpected value for spg_symbol: %s" % spg_symbol)


    def abc(self):
        return self._abc[0], self._abc[1], self._abc[2]

    def angles(self):
        return self._angles[0], self._angles[1], self._angles[2]

    # A.1. Cubic (CUN, cP)
    """Convention lattice
        a1 = (a, 0, 0)
        a2 = (0, a, 0)
        a3 = (0, 0, a)"""
    def cubic(self):
        self.name = "CUB"
        kpoints = {"\Gamma": np.array([0.0, 0.0, 0.0]), "R": np.array([0.5, 0.5, 0.5]), \
        "M": np.array([0.5, 0.5, 0.0]), "X": np.array([0.0, 0.5, 0.0])}
        path = [["\Gamma", "X", "M", "\Gamma", "R", "X"], ["M", "R"]]
        return {'kpoints': kpoints, 'path': path}

    # A.2. Face-centered cubic (FCC, cF)
    """Convention lattice           Primitivelattice
        a1 = (a, 0, 0)              a1 = (0, a/2, a/2)
        a2 = (0, a, 0)              a2 = (a/2, 0, a/2)
        a3 = (0, 0, a)              a3 = (a/2, a/2, 0)"""
    def fcc(self):
        self.name = "FCC"
        kpoints = {"\Gamma": np.array([0.0, 0.0, 0.0]), "U": np.array([5.0 / 8.0, 1.0 / 4.0, 5.0 / 8.0]), \
        "K": np.array([3.0 / 8.0, 3.0 / 8.0, 3.0, 4.0]), "W": np.array([0.5, 1.0 / 4.0, 3.0 / 4.0]), \
        "L": np.array([0.5, 0.5, 0.5]), "X": np.array([0.5, 0.0, 0.5])}
        path = [['\Gamma', 'X', 'W', 'K', '\Gamma', 'L', 'U', 'W', 'L', 'K'], ['U', 'X']]
        return {'kpoints': kpoints, 'path': path}

    # A.3. Body-centered cubic (BCC, cI)
    """Convention lattice           Primitivelattice
        a1 = (a, 0, 0)              a1 = (-a/2, a/2, a/2)
        a2 = (0, a, 0)              a2 = (a/2, -a/2, a/2)
        a3 = (0, 0, a)              a3 = (a/2, a/2, -a/2)"""
    def bcc(self):
        self.name = "BCC"
        kpoints = {"\Gamma": np.array([0.0, 0.0, 0.0]), "P": np.array([1.0 / 4.0, 1.0 / 4.0, 1.0 /4.0]), \
        "H": np.array([0.5, -0.5, 0.5]), "N": np.array([0.0, 0.0, 0.5])}
        path = [['\Gamma', 'H', 'N', '\Gamma', 'P', 'H'], ['P', 'N']]
        return {'kpoints': kpoints, 'path': path}

    # A.4. Tetragonal (TET, tP)
    """Convention lattice
        a1 = (a, 0, 0)
        a2 = (0, a, 0)
        a3 = (0, 0, c)"""
    def tet(self):
        self.name = "TET"
        kpoints = {"\Gamma": np.array([0.0, 0.0, 0.0]), "R": np.array([0.0, 0.5, 0.5]), \
        "A": np.array([0.5, 0.5, 0.5]), "X": np.array([0.0, 0.5, 0.0]), \
        "M": np.array([0.5, 0.5, 0.0]), "Z": np.array([0.0, 0.0, 0.5])}
        path = [['\Gamma', 'X', 'M', '\Gamma', 'Z', 'R', 'A'], ['X', 'R'], ['M', 'A']]
        return {'kpoints': kpoints, 'path': path}

    # A.5. Body-centered tetragonal (BCT, tI)
    """Convention lattice           Primitivelattice
        a1 = (a, 0, 0)              a1 = (-a/2, a/2, c/2)
        a2 = (0, a, 0)              a2 = (a/2, -a/2, c/2)
        a3 = (0, 0, c)              a3 = (a/2, a/2, -c/2)"""
    def bctet1(self, c, a):
        self.name = "BCT1"
        eta = (1 + c ** 2 / a ** 2) / 4.0
        kpoints = {"\Gamma": np.array([0.0, 0.0, 0.0]), "X": np.array([0.0, 0.0, 0.5]), \
        "M": np.array([-0.5, 0.5, 0.5]), "Z": np.array([eta, eta, -eta]), \
        "N": np.array([0.0, 0.5, 0.0]), "Z_1": np.array([-eta, 1 - eta, eta]), \
        "P": np.array([1.0 / 4.0, 1.0 / 4.0, 1.0 / 4.0])}
        kpath = [['\Gamma', 'X', 'M', '\Gamma', 'Z', 'P', 'N', 'Z_1', 'M'], ['X', 'P']]
        return {'kpoints': kpoints, 'path': path}

    def bctet2(self, c, a):
        self.name = "BCT2"
        eta = (1 + c **2 / a ** 2) / 4.0
        zeta = a**2 / (2 * c**2)
        kpoints = {"\Gamma": np.array([0.0, 0.0, 0.0]), "X":np.array([0.0, 0.0, 0.5]), \
        "N": np.array([0.0, 0.5, 0.0]), "Y": np.array([-zeta, zeta, 0.5]), \
        "P": np.array([1.0 / 4.0, 1.0 / 4.0, 1.0 / 4.0]), "Y_1": np.array([0.5, 0.5, -zeta]), \
        "\Sigma": np.array([-eta, eta, eta]), "Z": np.array([0.5, 0.5, -0.5]), \
        "\Sigma_1": np.array([eta, 1 - eta, -eta])}
        path = [['\Gamma', 'X', 'Y', '\Sigma', '\Gamma', 'Z', '\Sigma_1', 'N', 'P', 'Y_1', 'Z'], ['X', 'P']]
        return {'kpoints': kpoints, 'path': path}

    # A.6. Orthorhombic (ORC, oP)
    """Convention lattice
        a1 = (a, 0, 0)
        a2 = (0, b, 0)
        a3 = (0, 0, c)"""
    def orc(self):
        self.name = "ORC"
        kpoints = {"\Gamma": np.array([0.0, 0.0, 0.0]), "U": np.array([0.5, 0.0, 0.5]), \
        "R": np.array([0.5, 0.5, 0.5]), "X": np.array([0.5, 0.0, 0.0]), \
        "S": np.array([0.5, 0.5, 0.0]), "Y": np.array([0.0, 0.5, 0.0]), \
        "T": np.array([0.0, 0.5, 0.5]), "Z": np.array([0.0, 0.0, 0.5])}
        path = [['\Gamma', 'X', 'S', 'Y', '\Gamma', 'Z', 'U', 'R', 'T', 'Z'], ['Y', 'T'], ['U', 'X'], ['S', 'R']]
        return {'kpoints': kpoints, 'path': path}

    # A.7. Face-centered orthorhombic (ORCF, oF)
    """Convention lattice           Primitivelattice
        a1 = (a, 0, 0)              a1 = (0, b/2, c/2)
        a2 = (0, b, 0)              a2 = (a/2, 0, c/2)
        a3 = (0, 0, c)              a3 = (a/2, b/2, 0)"""
    def orcf1(self, a, b, c):
        self.name = "ORCF1"
        zeta = (1 + a ** 2 / b ** 2 - a ** 2 / c ** 2) / 4
        eta = (1 + a ** 2 / b ** 2 + a ** 2 / c ** 2) / 4
        kpoints = {"\Gamma": np.array([0.0, 0.0, 0.0]), "X": np.array([0.0, eta, eta]), \
        "A": np.array([0.5, 0.5 + zeta, zeta]), "X_1": np.array([1.0, 1 - eta, 1 - eta]), \
        "A_1": np.array([0.5, 0.5 - zeta, 1 - zeta]), "Y": np.array([0.5, 0.0, 0.5]), \
        "L": np.array([0.5, 0.5, 0.5]), "Z": np.array([0.5, 0.5, 0.0]), \
        "T": np.array([1.0, 0.5, 0.5])}
        path = [['\Gamma', 'Y', 'T', 'Z', '\Gamma', 'X', 'A_1', 'Y'], ['T', 'X_1'], ['X', 'A', 'Z'], ['L', '\Gamma']]
        return {'kpoints': kpoints, 'path': path}

    def orcf2(self, a, b, c):
        self.name = "ORCF2"
        zeta = (1 + a ** 2 / b ** 2 - a ** 2 / c ** 2) / 4
        delta = (1 + b ** 2 / a ** 2 - b ** 2 / c ** 2) / 4
        phi = (1 + c ** 2 / b ** 2 - c ** 2/ a ** 2) / 4
        kpoints = {"\Gamma": np.array([0.0, 0.0, 0.0]), "H": np.array([1 - phi, 0.5 - phi, 0.5]), \
        "C": np.array([0.5, 0.5 - zeta, 1 - zeta]), "H_1": np.array([phi, 0.5 + phi, 0.5]), \
        "C_1": np.array([0.5, 0.5 + zeta, zeta]), "X": np.array([0.0, 0.5, 0.5]), \
        "D": np.array([0.5 - delta, 0.5, 1 - delta]), "Y": np.array([0.5, 0.0, 0.5]), \
        "D_1": np.array([0.5 + delta, 0.5, delta]), "Z": np.array([0.5, 0.5, 0.0]), \
        "L": np.array([0.5, 0.5, 0.5])}
        path = [['\Gamma', 'Y', 'C', 'D', 'X', '\Gamma', 'Z', 'D_1', 'H', 'C'], ['C_1', 'Z'], ['X', 'H_1'], ['L', '\Gamma']]
        return {'kpoints': kpoints, 'path': path}

    def orcf3(self, a, b, c):
        self.name = "ORCF3"
        zeta = (1 + a ** 2 / b ** 2 - a ** 2 / c ** 2) / 4
        eta = (1 + a ** 2 / b ** 2 + a ** 2 / c ** 2) / 4
        kpoints = {"\Gamma": np.array([0.0, 0.0, 0.0]), "X": np.array([0.0, eta, eta]), \
        "A": np.array([0.5, 0.5 + zeta, zeta]), "X_1": np.array([1.0, 1 - eta, 1 - eta]), \
        "A_1": np.array([0.5, 0.5 - zeta, 1 - zeta]), "Y": np.array([0.5, 0.0, 0.5]), \
        "L": np.array([0.5, 0.5, 0.5]), "Z": np.array([0.5, 0.5, 0.0]), \
        "T": np.array([1.0, 0.5, 0.5])}
        path = [['\Gamma', 'Y', 'T', 'Z', '\Gamma', 'X', 'A_1', 'Y'], ['X', 'A', 'Z'], ['L', '\Gamma']]
        return {'kpoints': kpoints, 'path': path}

    # A.8. Body-centered orthorhombic (ORCI, oI)
    """Convention lattice           Primitivelattice
        a1 = (a, 0, 0)              a1 = (-a/2, b/2, c/2)
        a2 = (0, b, 0)              a2 = (a/2, -b/2, c/2)
        a3 = (0, 0, c)              a3 = (a/2, b/2, -c/2)"""
    def orci(self, a, b, c):
        self.name = "ORCI"
        zeta = (1 + a ** 2 / c ** 2) / 4
        delta = (b ** 2 - a ** 2) / (4 * c **2)
        eta = (1 + b ** 2 / c ** 2) / 4
        miu = (a ** 2 + b ** 2) / (4 * c ** 2)
        kpoints = {"\Gamma": np.array([0.0, 0.0, 0.0]), "W": np.array([1.0 / 4.0, 1.0 / 4.0, 1.0 / 4.0]), \
        "L": np.array([-miu, miu, 0.5 - delta]), "X": np.array([-zeta, zeta, zeta]), \
        "L_1": np.array([miu, -miu, 0.5 + delta]), "X_1": np.array([zeta, 1 - zeta, -zeta]), \
        "L_2": np.array([0.5 - delta, 0.5 + delta, -miu]), "Y": np.array([eta, -eta, eta]), \
        "R": np.array([0.0, 0.5, 0.0]), "Y_1": np.array([1 - eta, eta, -eta]), \
        "S": np.array([0.5, 0.0, 0.0]), "Z": np.array([0.5, 0.5, -0.5]), \
        "T": np.array([0.0, 0.0, 0.5])}
        path = [['\Gamma', 'X', 'L', 'T', 'W', 'R', 'X_1', 'Z', '\Gamma', 'Y', 'S', 'W'], ['L_1', 'Y'], ['Y_1', 'Z']]
        return {'kpoints': kpoints, 'path': path}

    # A.9. C-centered orthorhombic (ORCC, oS)
    """Convention lattice           Primitivelattice
        a1 = (a, 0, 0)              a1 = (a/2, -b/2, 0)
        a2 = (0, b, 0)              a2 = (a/2, b/2, 0)
        a3 = (0, 0, c)              a3 = (0, 0, c)"""
    def orcc(self, a, b):
        self.name = "ORCC"
        zeta = (1 + a ** 2 / b ** 2) / 4
        kpoints = {"\Gamma": np.array([0.0, 0.0, 0.0]), "T": np.array([-0.5, 0.5, 0.5]), \
        "A": np.array([zeta, zeta, 0.5]), "X": np.array([zeta, zeta, 0.0]), \
        "A_1": np.array([-zeta, 1 - zeta, 0.5]), "X_1": np.array([-zeta, 1 - zeta, 0.0]), \
        "R": np.array([0.0, 0.5, 0.5]), "Y": np.array([-0.5, 0.5, 0.0]), \
        "S": np.array([0.0, 0.5, 0.0]), "Z": np.array([0.0, 0.0, 0.5])}
        path = [['\Gamma', 'X', 'S', 'R', 'A', 'Z', '\Gamma', 'Y', 'X_1', 'A_1', 'T', 'Y'], ['Z', 'T']]
        return {'kpoints': kpoints, 'path': path}

    # A.10. Hexagonal (HEX, hP)
    """Lattice
        a1 = (a/2, -(a*sqrt(3))/2, 0)
        a2 = (a/2, (a*sqrt(3))/2, 0)
        a3 = (0, 0, c)"""
    def hex(self):
        self.name = "HEX"
        kpoints = {"\Gamma": np.array([0.0, 0.0, 0.0]), "K": np.array([1.0 / 3.0, 1.0 / 3.0, 0.0]), \
        "A": np.array([0.0, 0.0, 0.5]), "L": np.array([0.5, 0.0, 0.5]), \
        "H": np.array([1.0 / 3.0, 1.0 / 3.0, 0.5]), "M": np.array([0.5, 0.0, 0.0])}
        path = [['\Gamma', 'M', 'K', '\Gamma', 'A', 'L', 'H', 'A'], ['L', 'M'], ['K', 'H']]
        return {'kpoints': kpoints, 'path': path}

    # A.11. Rhombohedral (RHL, hR)
    """Lattice
        a1 = (a*cos(α/2), -a*sin(α/2), 0)
        a2 = (a*cos(α/2), a*sin(α/2), 0)
        a3 = (a*cos(α/2)*cos(α/2), 0, a*sqrt(1 - cos(α)**2 / cos(α/2)**2))"""
    def rhl1(self, alpha):
        self.name = "RHL1"
        eta = (1 + 4 * cos(alpha)) / (2 + 4 * cos(alpha))
        nu = 3.0 / 4.0 - eta / 2
        kpoints = {"\Gamma": np.array([0.0, 0.0, 0.0]), "P": np.array([eta, nu, nu]), \
        "B": np.array([eta, 0.5, 1 - eta]), "P_1": np.array([1 - nu, 1 - nu, 1 - eta]), \
        "B_1": np.array([0.5, 1 - eta, eta -1]), "P_2": np.array([nu, nu, eta - 1]), \
        "F": np.array([0.5, 0.5, 0.0]), "Q": np.array([1 - nu, nu, 0.0]), \
        "L": np.array([0.5, 0.0, 0.0]), "X": np.array([nu, 0.0, -nu]), \
        "L_1": np.array([0.0, 0.0, -0.5]), "Z": np.array([0.5, 0.5, 0.5])}
        path = [['\Gamma', 'L', 'B_1'], ['B', 'Z', '\Gamma', 'X'], ['Q', 'F', 'P_1', 'Z'], ['L', 'P']]
        return {'kpoints': kpoints, 'path': path}

    def rhl2(self, alpha):
        self.name = "RHL2"
        eta = 1 / (2 * tan(alpha / 2) ** 2)
        nu = 3.0 / 4.0 - eta / 2
        kpoints = {"\Gamma": np.array([0.0, 0.0, 0.0]), "P_1": np.array([nu, nu - 1, nu - 1]), \
        "F": np.array([0.5, -0.5, 0.0]), "Q": np.array([eta, eta, eta]), \
        "L": np.array([0.5, 0.0, 0.0]), "Q_1": np.array([1 - eta, -eta, -eta]), \
        "P": np.array([1 - nu, -nu, 1 - nu]), "Z": np.array([0.5, -0.5, 0.5])}
        path = [['\Gamma', 'P', 'Z', 'Q', '\Gamma', 'F', 'P_1', 'Q_1', 'L', 'Z']]
        return {'kpoints': kpoints, 'path': path}

    # A.12. Monoclinic (MCL, mP)
    """Lattice
        a1 = (a, 0, 0)
        a2 = (0, b, 0)
        a3 = (0, c*cos(α), c*sin(α))"""
    def mcl(self, b, c, alpha):
        self.name = "MCL"
        eta = (1 - b * cos(alpha) / c) / (2 * sin(alpha) ** 2)
        nu = 0.5 - eta * c * cos(alpha) / b
        kpoints = {"\Gamma": np.array([0.0, 0.0, 0.0]), "H_2": np.array([0.0, eta, -nu]), \
        "A": np.array([0.5, 0.5, 0.0]), "M": np.array([0.5, eta, 1 - nu]), \
        "C": np.array([0.0, 0.5, 0.5]), "M_1": np.array([0.5, 1 - eta, nu]), \
        "D": np.array([0.5, 0.0, 0.5]), "M_2": np.array([0.5, eta, -nu]), \
        "D_1": np.array([0.5, 0.0, -0.5]), "X": np.array([0.0, 0.5, 0.0]), \
        "E": np.array([0.5, 0.5, 0.5]), "Y": np.array([0.0, 0.0, 0.5]), \
        "H": np.array([0, eta, 1 - nu]), "Y_1": np.array([0.0, 0.0, -0.5]), \
        "H_1": np.array([0.0, 1 - eta, nu]), "Z": np.array([0.5, 0.0, 0.0])}
        path = [['\Gamma', 'Y', 'H', 'C', 'E', 'M_1', 'A', 'X', 'H_1'], ['M', 'D', 'Z'], ['Y', 'D']]
        return {'kpoints': kpoints, 'path': path}

    # A.13. C-centered monoclinic (MCLC, mS)
    """Convention lattice               Primitivelattice
        a1 = (a, 0, 0)                  a1 = (a/2, b/2, 0)
        a2 = (0, b, 0)                  a2 = (-a/2, b/2, 0)
        a3 = (0, c*cos(α), c*sin(α))    a3 = (0, c*cos(α), c*sin(α))"""
    def mclc1(self, a, b, c, alpha):
        self.name = "MCLC1"
        zeta = (2 - b * cos(alpha) / c) / (4 * sin(alpha) ** 2)
        eta = 0.5 + 2 * zeta * c * cos(alpha) / b
        psi = 3.0 / 4.0 - a ** 2 / (4 * b ** 2 * sin(alpha) ** 2)
        phi = psi + (3.0 / 4.0 - psi) * b * cos(alpha) / c
        kpoints = {"\Gamma": np.array([0.0, 0.0, 0.0]), "L": np.array([0.5, 0.5, 0.5]), \
        "N": np.array([0.5, 0.0, 0.0]), "M": np.array([0.5, 0.0, 0.5]), \
        "N_1": np.array([0.0, -0.5, 0.0]), "X": np.array([1 - psi, psi - 1, 0.0]), \
        "F": np.array([1 - zeta, 1 - zeta, 1 - eta]), "X_1": np.array([psi, 1 - psi, 0.0]), \
        "F_1": np.array([zeta, zeta, eta]), "X_2": np.array([psi - 1, -psi, 0.0]), \
        "F_2": np.array([-zeta, -zeta, 1 - eta]), "Y": np.array([0.5, 0.5, 0.0]), \
        "F_3": np.array([1 - zeta, -zeta, 1 - eta]), "Y_1": np.array([-0.5, -0.5, 0.0]), \
        "I": np.array([phi, 1 - phi, 0.5]), "Z": np.array([0.0, 0.0, 0.5]), \
        "I_1": np.array([1 - phi, phi - 1, 0.5])}
        path = [['\Gamma', 'Y', 'F', 'L', 'I'], ['I_1', 'Z', 'F_1'], ['Y', 'X_1'], ['X', '\Gamma', 'N'], ['M', '\Gamma']]
        return {'kpoints': kpoints, 'path': path}

    def mclc2(self, a, b, c, alpha):
        self.name = "MCLC2"
        zeta = (2 - b * cos(alpha) / c) / (4 * sin(alpha) ** 2)
        eta = 0.5 + 2 * zeta * c * cos(alpha) / b
        psi = 3.0 / 4.0 - a ** 2 / (4 * b ** 2 * sin(alpha) ** 2)
        phi = psi + (3.0 / 4.0 - psi) * b * cos(alpha) / c
        kpoints = {"\Gamma": np.array([0.0, 0.0, 0.0]), "L": np.array([0.5, 0.5, 0.5]), \
        "N": np.array([0.5, 0.0, 0.0]), "M": np.array([0.5, 0.0, 0.5]), \
        "N_1": np.array([0.0, -0.5, 0.0]), "X": np.array([1 - psi, psi - 1, 0.0]), \
        "F": np.array([1 - zeta, 1 - zeta, 1 - eta]), "X_1": np.array([psi, 1 - psi, 0.0]), \
        "F_1": np.array([zeta, zeta, eta]), "X_2": np.array([psi - 1, -psi, 0.0]), \
        "F_2": np.array([-zeta, -zeta, 1 - eta]), "Y": np.array([0.5, 0.5, 0.0]), \
        "F_3": np.array([1 - zeta, -zeta, 1 - eta]), "Y_1": np.array([-0.5, -0.5, 0.0]), \
        "I": np.array([phi, 1 - phi, 0.5]), "Z": np.array([0.0, 0.0, 0.5]), \
        "I_1": np.array([1 - phi, phi - 1, 0.5])}
        path = [['\Gamma', 'Y', 'F', 'L', 'I'], ['I_1', 'Z', 'F_1'], ['N', '\Gamma', 'M']]
        return {'kpoints': kpoints, 'path': path}

    def mclc3(self, a, b, c, alpha):
        self.name = "MCLC3"
        miu = (1 + b ** 2 / a ** 2) / 4
        delta = b * c * cos(alpha) / (2 * a ** 2)
        zeta = miu - 1.0 / 4.0 + (1 - b * cos(alpha) / c) / (4 * sin(alpha) ** 2)
        eta = 1.0 / 2.0 + 2 * zeta * c * cos(alpha) / b
        phi = 1 + zeta - 2 * miu
        psi = eta - 2 * delta
        kpoints = {"\Gamma": np.array([0.0, 0.0, 0.0]), "N": np.array([0.5, 0.0, 0.0]), \
        "F": np.array([1 - phi, 1 - phi, 1 - psi]), "N_1": np.array([0.0, -0.5, 0.0]), \
        "F_1": np.array([phi, phi - 1, psi]), "X": np.array([0.5, -0.5, 0.0]), \
        "F_2": np.array([1 - phi, -phi, 1 - psi]), "Y": np.array([miu, miu, delta]), \
        "H": np.array([zeta, zeta, eta]), "Y_1": np.array([1 - miu, -miu, -delta]), \
        "H_1": np.array([1 - zeta, -zeta, 1 - eta]), "Y_2": np.array([-miu, -miu, -delta]), \
        "H_2": np.array([-zeta, -zeta, 1 - eta]), "Y_3": np.array([miu, miu - 1, delta]), \
        "I": np.array([0.5, -0.5, 0.5]), "Z": np.array([0.0, 0.0, 0.5]), \
        "M": np.array([0.5, 0.0, 0.5])}
        path = [['\Gamma', 'Y', 'F', 'H', 'Z', 'I', 'F_1'], ['H_1', 'Y_1', 'X', '\Gamma', 'N'], ['M', '\Gamma']]
        return {'kpoints': kpoints, 'path': path}

    def mclc4(self, a, b, c, alpha):
        self.name = "MCLC4"
        miu = (1 + b ** 2 / a ** 2) / 4
        delta = b * c * cos(alpha) / (2 * a ** 2)
        zeta = miu - 1.0 / 4.0 + (1 - b * cos(alpha) / c) / (4 * sin(alpha) ** 2)
        eta = 1.0 / 2.0 + 2 * zeta * c * cos(alpha) / b
        phi = 1 + zeta - 2 * miu
        psi = eta - 2 * delta
        kpoints = {"\Gamma": np.array([0.0, 0.0, 0.0]), "N": np.array([0.5, 0.0, 0.0]), \
        "F": np.array([1 - phi, 1 - phi, 1 - psi]), "N_1": np.array([0.0, -0.5, 0.0]), \
        "F_1": np.array([phi, phi - 1, psi]), "X": np.array([0.5, -0.5, 0.0]), \
        "F_2": np.array([1 - phi, -phi, 1 - psi]), "Y": np.array([miu, miu, delta]), \
        "H": np.array([zeta, zeta, eta]), "Y_1": np.array([1 - miu, -miu, -delta]), \
        "H_1": np.array([1 - zeta, -zeta, 1 - eta]), "Y_2": np.array([-miu, -miu, -delta]), \
        "H_2": np.array([-zeta, -zeta, 1 - eta]), "Y_3": np.array([miu, miu - 1, delta]), \
        "I": np.array([0.5, -0.5, 0.5]), "Z": np.array([0.0, 0.0, 0.5]), \
        "M": np.array([0.5, 0.0, 0.5])}
        path = [['\Gamma', 'Y', 'F', 'H', 'Z', 'I'], ['H_1', 'Y_1', 'X', '\Gamma', 'N'], ['M', '\Gamma']]
        return {'kpoints': kpoints, 'path': path}

    def mclc5(self, a, b, c, alpha):
        self.name = "MCLC5"
        zeta = (b ** 2 / a ** 2 + (1 - b * cos(alpha) / c) / (sin(alpha) ** 2)) / 4
        miu = eta / 2 + b ** 2 / (4 * a ** 2) - b * c * cos(alpha) / (2 * a ** 2)
        omega = (4 * nu - 1 - b ** 2 * sin(alpha) ** 2 / a ** 2) * c / (2 * b * cos(alpha))
        eta = 1.0 / 2.0 + 2 * zeta * c * cos(alpha) / b
        delta = zeta * c * cos(alpha) / b + omega / 2 - 1.0 / 4.0
        nu = 2 * miu - zeta
        rho = 1 - zeta * a ** 2 / b ** 2
        kpoints = {"\Gamma": np.array([0.0, 0.0, 0.0]), "M": np.array([0.5, 0.0, 0.5]), \
        "F": np.array([nu, nu, omega]), "N": np.array([0.5, 0.0, 0.0]), \
        "F_1": np.array([1 - nu, 1 - nu, 1 - omega]), "N_1": np.array([0.0, -0.5, 0.0]), \
        "F_2": np.array([nu, nu - 1, omega]), "X": np.array([0.5, -0.5, 0.0]), \
        "H": np.array([zeta, zeta, eta]), "Y": np.array([miu, miu, delta]), \
        "H_1": np.array([1 - zeta, -zeta, 1 - eta]), "Y_1": np.array([1 - miu, -miu, -delta]), \
        "H_2": np.array([-zeta, -zeta, 1 - eta]), "Y_2": np.array([-miu, -miu, -delta]), \
        "I": np.array([rho, 1 - rho, 0.5]), "Y_3": np.array([miu, miu - 1, delta]), \
        "I_1": np.array([1 - rho, rho - 1, 0.5]), "Z": np.array([0.0, 0.0, 0.5]), \
        "L": np.array([0.5, 0.5, 0.5])}
        path = [['\Gamma', 'Y', 'F', 'L', 'I'], ['I_1', 'Z', 'H', 'F_1'], ['H_1', 'Y_1', 'X', '\Gamma', 'N'], ['M', '\Gamma']]
        return {'kpoints': kpoints, 'path': path}

    # A.14. Triclinic (TRI, aP)
    """Lattice
        a1 = (a, 0, 0)
        a2 = (b*cos(γ), b*sin(γ), 0)
        a3 = (c*cos(β), c/sin(γ)*[cos(α)-cos(β)cos(γ)], c/sin(γ)*sqrt(sin(γ)**2-cos(α)**2-cos(β)**2+2*cos(α)*cos(β)*cos(γ)))"""
    def tri_1a(self):
        self.name = "TRI_1a"
        kpoints = {"\Gamma": np.array([0.0, 0.0, 0.0]), "R": np.array([0.5, 0.5, 0.5]), \
        "L": np.array([0.5, 0.5, 0.0]), "X": np.array([0.5, 0.0, 0.0]), \
        "M": np.array([0.0, 0.5, 0.5]), "Y": np.array([0.0, 0.5, 0.0]), \
        "N": np.array([0.5, 0.0, 0.5]), "Z": np.array([0.0, 0.0, 0.5])}
        path = [['X', '\Gamma', 'Y'], ['L', '\Gamma', 'Z'], ['N', '\Gamma', 'M'], ['R', '\Gamma']]
        return {'kpoints': kpoints, 'path': path}

    def tri_2a(self):
        self.name = "TRI_2a"
        kpoints = {"\Gamma": np.array([0.0, 0.0, 0.0]), "R": np.array([0.5, 0.5, 0.5]), \
        "L": np.array([0.5, 0.5, 0.0]), "X": np.array([0.5, 0.0, 0.0]), \
        "M": np.array([0.0, 0.5, 0.5]), "Y": np.array([0.0, 0.5, 0.0]), \
        "N": np.array([0.5, 0.0, 0.5]), "Z": np.array([0.0, 0.0, 0.5])}
        path = [['X', '\Gamma', 'Y'], ['L', '\Gamma', 'Z'], ['N', '\Gamma', 'M'], ['R', '\Gamma']]
        return {'kpoints': kpoints, 'path': path}

    def tri_1b(self):
        self.name = "TRI_1b"
        kpoints = {"\Gamma": np.array([0.0, 0.0, 0.0]), "R": np.array([0.0, -0.5, 0.5]), \
        "L": np.array([0.5, -0.5, 0.0]), "X": np.array([0.0, -0.5, 0.0]), \
        "M": np.array([0.0, 0.0, 0.5]), "Y": np.array([0.5, 0.0, 0.0]), \
        "N": np.array([-0.5, -0.5, 0.5]), "Z": np.array([-0.5, 0.0, 0.5])}
        path = [['X', '\Gamma', 'Y'], ['L', '\Gamma', 'Z'], ['N', '\Gamma', 'M'], ['R', '\Gamma']]
        return {'kpoints': kpoints, 'path': path}

    def tri_2b(self):
        self.name = "TRI_2b"
        kpoints = {"\Gamma": np.array([0.0, 0.0, 0.0]), "R": np.array([0.0, -0.5, 0.5]), \
        "L": np.array([0.5, -0.5, 0.0]), "X": np.array([0.0, -0.5, 0.0]), \
        "M": np.array([0.0, 0.0, 0.5]), "Y": np.array([0.5, 0.0, 0.0]), \
        "N": np.array([-0.5, -0.5, 0.5]), "Z": np.array([-0.5, 0.0, 0.5])}
        path = [['X', '\Gamma', 'Y'], ['L', '\Gamma', 'Z'], ['N', '\Gamma', 'M'], ['R', '\Gamma']]
        return {'kpoints': kpoints, 'path': path}
