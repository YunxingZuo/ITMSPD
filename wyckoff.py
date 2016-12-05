# coding: utf-8
# Copyright © 2016 YunXing Zuo, WeiJi Hsiao

__author__ = 'YunXing Zuo, WeiJi Hsiao'
__email__ = 'weiji.hsiao@gmail.com'
__date__ = 'Oct. 25, 2016'

spacegroup_dict = {1: 'P1', 2: 'P-1', 3: 'P2', 4: 'P2_1', 5: 'C2', 6: 'Pm', 7: 'Pc', 8: 'Cm', 9: 'Cc', 10: 'P2/m', \
                   11: 'P2_1/m', 12: 'C2/m', 13: 'P2/c', 14: 'P2_1/c', 15: 'C2/c', 16: 'P222', 17: 'P222_1', 18: 'P2_12_12', \
                   19: 'P2_12_12_1', 20: 'C222_1', 21: 'C222', 22: 'F222', 23: 'I222', 24: 'I2_12_12_1', 25: 'Pmm2', \
                   26: 'Pmc2_1', 27: 'Pcc2', 28: 'Pma2', 29: 'Pca2_1', 30: 'Pnc2', 31: 'Pmn2_1', 32: 'Pba2', 33: 'Pna2_1', \
                   34: 'Pnn2', 35: 'Cmm2', 36: 'Cmc2_1', 37: 'Ccc2', 38: 'Amm2', 39: 'Aem2', 40: 'Ama2', 41: 'Aea2', \
                   42: 'Fmm2', 43: 'Fdd2', 44: 'Imm2', 45: 'Iba2', 46: 'Ima2', 47: 'Pmmm', 48: 'Pnnn', 49: 'Pccm', 50: 'Pban', \
                   51: 'Pmma', 52: 'Pnna', 53: 'Pmna', 54: 'Pcca', 55: 'Pbam', 56: 'Pccn', 57: 'Pbcm', 58: 'Pnnm', 59: 'Pmmn', \
                   60: 'Pbcn', 61: 'Pbca', 62: 'Pnma', 63: 'Cmcm', 64: 'Cmce', 65: 'Cmmm', 66: 'Cccm', 67: 'Cmme', 68: 'Ccce', \
                   69: 'Fmmm', 70: 'Fddd', 71: 'Immm', 72: 'Ibam', 73: 'Ibca', 74: 'Imma', 75: 'P4', 76: 'P4_1', 77: 'P4_2', \
                   78: 'P4_3', 79: 'I4', 80: 'I4_1', 81: 'P-4', 82: 'I-4', 83: 'P4/m', 84: 'P4_2/m', 85: 'P4/n', 86: 'P4_2/n', \
                   87: 'I4/m', 88: 'I4_1/a', 89: 'P422', 90: 'P42_12', 91: 'P4_122', 92: 'P4_12_12', 93: 'P4_222', 94: 'P4_22_12', \
                   95: 'P4_322', 96: 'P4_32_12', 97: 'I422', 98: 'I4_122', 99: 'P4mm', 100: 'P4bm', 101: 'P4_2cm', 102: 'P4_2nm', \
                   103: 'P4cc', 104: 'P4nc', 105: 'P4_2mc', 106: 'P4_2bc', 107: 'I4mm', 108: 'I4cm', 109: 'I4_1md', 110: 'I4_1cd', \
                   111: 'P-42m', 112: 'P-42c', 113: 'P-42_1m', 114: 'P-42_1c', 115: 'P-4m2', 116: 'P-4c2', 117: 'P-4b2', \
                   118: 'P-4n2', 119: 'I-4m2', 120: 'I-4c2', 121: 'I-42m', 122: 'I-42d', 123: 'P4/mmm', 124: 'P4/mcc', 125: 'P4/nbm', \
                   126: 'P4/nnc', 127: 'P4/mbm', 128: 'P4/mnc', 129: 'P4/nmm', 130: 'P4/ncc', 131: 'P4_2/mmc', 132: 'P4_2/mcm', \
                   133: 'P4_2/nbc', 134: 'P4_2/nnm', 135: 'P4_2/mbc', 136: 'P4_2/mnm', 137: 'P4_2/nmc', 138: 'P4_2/ncm', \
                   139: 'I4/mmm', 140: 'I4/mcm', 141: 'I4_1/amd', 142: 'I4_1/acd', 143: 'P3', 144: 'P3_1', 145: 'P3_2', \
                   146: 'R3', 147: 'P-3', 148: 'R-3', 149: 'P312', 150: 'P321', 151: 'P3_112', 152: 'P3_121', 153: 'P3_212', \
                   154: 'P3_221', 155: 'R32', 156: 'P3m1', 157: 'P31m', 158: 'P3c1', 159: 'P31c', 160: 'R3m', 161: 'R3c', \
                   162: 'P-31m', 163: 'P-31c', 164: 'P-3m1', 165: 'P-3c1', 166: 'R-3m', 167: 'R-3c', 168: 'P6', 169: 'P6_1', \
                   170: 'P6_5', 171: 'P6_2', 172: 'P6_4', 173: 'P6_3', 174: 'P-6', 175: 'P6/m', 176: 'P6_3/m', 177: 'P622', \
                   178: 'P6_122', 179: 'P6_522', 180: 'P6_222', 181: 'P6_422', 182: 'P6_322', 183: 'P6mm', 184: 'P6cc', 185: 'P6_3cm', \
                   186: 'P6_3mc', 187: 'P-6m2', 188: 'P-6c2', 189: 'P-62m', 190: 'P-62c', 191: 'P6/mmm', 192: 'P6/mcc', \
                   193: 'P6_3/mcm', 194: 'P6_3/mmc', 195: 'P23', 196: 'F23', 197: 'I23', 198: 'P2_13', 199: 'I2_13', 200: 'Pm-3', \
                   201: 'Pn-3', 202: 'Fm-3', 203: 'Fd-3', 204: 'Im-3', 205: 'Pa-3', 206: 'Ia-3', 207: 'P432', 208: 'P4_232', \
                   209: 'F432', 210: 'F4_132', 211: 'I432', 212: 'P4_332', 213: 'P4_132', 214: 'I4_132', 215: 'P-43m', 216: 'F-43m', \
                   217: 'I-43m', 218: 'P-43n', 219: 'F-43c', 220: 'I-43d', 221: 'Pm-3m', 222: 'Pn-3n', 223: 'Pm-3n', 224: 'Pn-3m', \
                   225: 'Fm-3m', 226: 'Fm-3c', 227: 'Fd-3m', 228: 'Fd-3c', 229: 'Im-3m', 230: 'Ia-3d'}

def crystal_system(spacegroup_number):
    n = spacegroup_number

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

def create_lattice(self, a_length, b_length, c_length, lattice_system):
    eq = lambda x, y: not x-y
    ineq = lambda x, y: x-y

    if lattice_system == "cubic":
        if not all([eq(a_length, b_length), eq(a_length, c_length), eq(b_length, c_length)]):
            raise ValueError("'a == b == c' must be satisfied for cubic.")
        alpha = 90
        beta = 90
        gamma = 90
        lattice = Lattice.from_lengths_and_angles(a_length, b_length, c_length, alpha, beta, gamma)
        return lattice

    elif lattice_system == "tetragonal":
        if not all([eq(a_length, b_length), ineq(a_length, c_length), ineq(b_length, c_length)]):
            raise ValueError("'a == b != c' must be satisfied for tetragonal.")
        alpha = 90
        beta = 90
        gamma = 90
        lattice = Lattice.from_lengths_and_angles(a_length, b_length, c_length, alpha, beta, gamma)
        return lattice

    elif lattice_system == "orthorhombic":
        if not all([ineq(a_length, b_length), ineq(a_length, c_length), ineq(b_length, c_length)]):
            raise ValueError("'a != b != c' must be satisfied for orthorhombic.")
        alpha = 90
        beta = 90
        gamma = 90
        lattice = Lattice.from_lengths_and_angles(a_length, b_length, c_length, alpha, beta, gamma)
        return lattice

    elif lattice_system == "hexagonal":
        if not all([eq(a_length, b_length), ineq(a_length, c_length), ineq(b_length, c_length)]):
            raise ValueError("'a == b != c' must be satisfied for hexagonal.")
        alpha = 90
        beta = 90
        gamma = 120
        lattice = Lattice.from_lengths_and_angles(a_length, b_length, c_length, alpha, beta, gamma)
        return lattice

    elif lattice_system == "rhombohedral" or lattice_system == "trigonal":
        if not all([eq(a_length, b_length), eq(a_length, c_length), eq(b_length, c_length)]):
            raise ValueError("'a == b == c' must be satisfied for trigonal.")
        angle = random.randint(60, 120)
        while eq(angle, 90):
            angle = random.randint(60, 120)
        alpha = angle
        beta = angle
        gamma = angle
        lattice = Lattice.from_lengths_and_angles(a_length, b_length, c_length, alpha, beta, gamma)
        return lattice

    elif lattice_system == "monoclinic":
        if not all([ineq(a_length, b_length), ineq(a_length, c_length), ineq(b_length, c_length)]):
            raise ValueError("'a != b != c' must be satisfied for monoclinic.")
        alpha = 90
        gamma = 90
        beta = random.randint(45, 135)
        while eq(beta, 90):
            beta = random.randint(45, 135)
        lattice = Lattice.from_lengths_and_angles(a_length, b_length, c_length, alpha, beta, gamma)
        return lattice

    elif lattice_system == "triclinic":
        if not all([ineq(a_length, b_length), ineq(a_length, c_length), ineq(b_length, c_length)]):
            raise ValueError("'a != b != c' must be satisfied for triclinic.")
        alpha = random.randint(60, 120)
        while eq(alpha, 90):
            alpha = random.randint(45, 135)
        beta = random.randint(60, 120)
        while eq(beta, alpha) or eq(beta, 90):
            beta = random.randint(60, 120)
        gamma = random.randint(60, 120)
        while eq(gamma, beta) or eq(gamma, alpha) or eq(gamma, 90):
            gamma = random.randint(60, 120)
        lattice = Lattice.from_lengths_and_angles(a_length, b_length, c_length, alpha, beta, gamma)
        return lattice

    else:
        raise ValueError("Please make sure the name of lattice system is correct.")        