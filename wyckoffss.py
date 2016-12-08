# coding: utf-8
# Copyright © 2016 YunXing Zuo

import numpy as np
from groups import SpaceGroup
from numpy.random import rand

__author__ = 'YunXing Zuo'
__email__ = 'zuoyx@pkusz.edu.cn'
__date__ = 'Nov. 12, 2016'

def pos_gen_wyckoff_positions(symbol, letter):
    if symbol == 'P1':
        return sp_1_pos(letter)
    elif symbol == 'P-1':
        return sp_2_pos(letter)
    elif symbol == 'P2':
        return sp_3_pos(letter)
    elif symbol == 'P2_1':
        return sp_4_pos(letter)
    elif symbol == 'C2':
        return sp_5_pos(letter)
    elif symbol == 'Pm':
        return sp_6_pos(letter)
    elif symbol == 'Pc':
        return sp_7_pos(letter)
    elif symbol == 'Cm':
        return sp_8_pos(letter)
    elif symbol == 'Cc':
        return sp_9_pos(letter)
    elif symbol == 'P2/m':
        return sp_10_pos(letter)
    elif symbol == 'P2_1/m':
        return sp_11_pos(letter)
    elif symbol == 'C2/m':
        return sp_12_pos(letter)
    elif symbol == 'P2/c':
        return sp_13_pos(letter)
    elif symbol == 'P2_1/c':
        return sp_14_pos(letter)
    elif symbol == 'C2/c':
        return sp_15_pos(letter)
    elif symbol == 'P222':
        return sp_16_pos(letter)
    elif symbol == 'P222_1':
        return sp_17_pos(letter)
    elif symbol == 'P2_12_12':
        return sp_18_pos(letter)
    elif symbol == 'P2_12_12_1':
        return sp_19_pos(letter)
    elif symbol == 'C222_1':
        return sp_20_pos(letter)
    elif symbol == 'C222':
        return sp_21_pos(letter)
    elif symbol == 'F222':
        return sp_22_pos(letter)
    elif symbol == 'I222':
        return sp_23_pos(letter)
    elif symbol == 'I2_12_12_1':
        return sp_24_pos(letter)
    elif symbol == 'Pmm2':
        return sp_25_pos(letter)
    elif symbol == 'Pmc2_1':
        return sp_26_pos(letter)
    elif symbol == 'Pcc2':
        return sp_27_pos(letter)
    elif symbol == 'Pma2':
        return sp_28_pos(letter)
    elif symbol == 'Pca2_1':
        return sp_29_pos(letter)
    elif symbol == 'Pnc2':
        return sp_30_pos(letter)
    elif symbol == 'Pmn2_1':
        return sp_31_pos(letter)
    elif symbol == 'Pba2':
        return sp_32_pos(letter)
    elif symbol == 'Pna2_1':
        return sp_33_pos(letter)
    elif symbol == 'Pnn2':
        return sp_34_pos(letter)
    elif symbol == 'Cmm2':
        return sp_35_pos(letter)
    elif symbol == 'Cmc2_1':
        return sp_36_pos(letter)
    elif symbol == 'Ccc2':
        return sp_37_pos(letter)
    elif symbol == 'Amm2':
        return sp_38_pos(letter)
    elif symbol == 'Aem2':
        return sp_39_pos(letter)
    elif symbol == 'Ama2':
        return sp_40_pos(letter)
    elif symbol == 'Aea2':
        return sp_41_pos(letter)
    elif symbol == 'Fmm2':
        return sp_42_pos(letter)
    elif symbol == 'Fdd2':
        return sp_43_pos(letter)
    elif symbol == 'Imm2':
        return sp_44_pos(letter)
    elif symbol == 'Iba2':
        return sp_45_pos(letter)
    elif symbol == 'Ima2':
        return sp_46_pos(letter)
    elif symbol == 'Pmmm':
        return sp_47_pos(letter)
    elif symbol == 'Pnnn':
        return sp_48_pos(letter)
    elif symbol == 'Pccm':
        return sp_49_pos(letter)
    elif symbol == 'Pban':
        return sp_50_pos(letter)
    elif symbol == 'Pmma':
        return sp_51_pos(letter)
    elif symbol == 'Pnna':
        return sp_52_pos(letter)
    elif symbol == 'Pmna':
        return sp_53_pos(letter)
    elif symbol == 'Pcca':
        return sp_54_pos(letter)
    elif symbol == 'Pbam':
        return sp_55_pos(letter)
    elif symbol == 'Pccn':
        return sp_56_pos(letter)
    elif symbol == 'Pbcm':
        return sp_57_pos(letter)
    elif symbol == 'Pnnm':
        return sp_58_pos(letter)
    elif symbol == 'Pmmn':
        return sp_59_pos(letter)
    elif symbol == 'Pbcn':
        return sp_60_pos(letter)
    elif symbol == 'Pbca':
        return sp_61_pos(letter)
    elif symbol == 'Pnma':
        return sp_62_pos(letter)
    elif symbol == 'Cmcm':
        return sp_63_pos(letter)
    elif symbol == 'Cmce':
        return sp_64_pos(letter)
    elif symbol == 'Cmmm':
        return sp_65_pos(letter)
    elif symbol == 'Cccm':
        return sp_66_pos(letter)
    elif symbol == 'Cmme':
        return sp_67_pos(letter)
    elif symbol == 'Ccce':
        return sp_68_pos(letter)
    elif symbol == 'Fmmm':
        return sp_69_pos(letter)
    elif symbol == 'Fddd':
        return sp_70_pos(letter)
    elif symbol == 'Immm':
        return sp_71_pos(letter)
    elif symbol == 'Ibam':
        return sp_72_pos(letter)
    elif symbol == 'Ibca':
        return sp_73_pos(letter)
    elif symbol == 'Imma':
        return sp_74_pos(letter)
    elif symbol == 'P4':
        return sp_75_pos(letter)
    elif symbol == 'P4_1':
        return sp_76_pos(letter)
    elif symbol == 'P4_2':
        return sp_77_pos(letter)
    elif symbol == 'P4_3':
        return sp_78_pos(letter)
    elif symbol == 'I4':
        return sp_79_pos(letter)
    elif symbol == 'I4_1':
        return sp_80_pos(letter)
    elif symbol == 'P-4':
        return sp_81_pos(letter)
    elif symbol == 'I-4':
        return sp_82_pos(letter)
    elif symbol == 'P4/m':
        return sp_83_pos(letter)
    elif symbol == 'P4_2/m':
        return sp_84_pos(letter)
    elif symbol == 'P4/n':
        return sp_85_pos(letter)
    elif symbol == 'P4_2/n':
        return sp_86_pos(letter)
    elif symbol == 'I4/m':
        return sp_87_pos(letter)
    elif symbol == 'I4_1/a':
        return sp_88_pos(letter)
    elif symbol == 'P422':
        return sp_89_pos(letter)
    elif symbol == 'P42_12':
        return sp_90_pos(letter)
    elif symbol == 'P4_122':
        return sp_91_pos(letter)
    elif symbol == 'P4_12_12':
        return sp_92_pos(letter)
    elif symbol == 'P4_222':
        return sp_93_pos(letter)
    elif symbol == 'P4_22_12':
        return sp_94_pos(letter)
    elif symbol == 'P4_322':
        return sp_95_pos(letter)
    elif symbol == 'P4_32_12':
        return sp_96_pos(letter)
    elif symbol == 'I422':
        return sp_97_pos(letter)
    elif symbol == 'I4_122':
        return sp_98_pos(letter)
    elif symbol == 'P4mm':
        return sp_99_pos(letter)
    elif symbol == 'P4bm':
        return sp_100_pos(letter)
    elif symbol == 'P4_2cm':
        return sp_101_pos(letter)
    elif symbol == 'P4_2nm':
        return sp_102_pos(letter)
    elif symbol == 'P4cc':
        return sp_103_pos(letter)
    elif symbol == 'P4nc':
        return sp_104_pos(letter)
    elif symbol == 'P4_2mc':
        return sp_105_pos(letter)
    elif symbol == 'P4_2bc':
        return sp_106_pos(letter)
    elif symbol == 'I4mm':
        return sp_107_pos(letter)
    elif symbol == 'I4cm':
        return sp_108_pos(letter)
    elif symbol == 'I4_1md':
        return sp_109_pos(letter)
    elif symbol == 'I4_1cd':
        return sp_110_pos(letter)
    elif symbol == 'P-42m':
        return sp_111_pos(letter)
    elif symbol == 'P-42c':
        return sp_112_pos(letter)
    elif symbol == 'P-42_1m':
        return sp_113_pos(letter)
    elif symbol == 'P-42_1c':
        return sp_114_pos(letter)
    elif symbol == 'P-4m2':
        return sp_115_pos(letter)
    elif symbol == 'P-4c2':
        return sp_116_pos(letter)
    elif symbol == 'P-4b2':
        return sp_117_pos(letter)
    elif symbol == 'P-4n2':
        return sp_118_pos(letter)
    elif symbol == 'I-4m2':
        return sp_119_pos(letter)
    elif symbol == 'I-4c2':
        return sp_120_pos(letter)
    elif symbol == 'I-42m':
        return sp_121_pos(letter)
    elif symbol == 'I-42d':
        return sp_122_pos(letter)
    elif symbol == 'P4/mmm':
        return sp_123_pos(letter)
    elif symbol == 'P4/mcc':
        return sp_124_pos(letter)
    elif symbol == 'P4/nbm':
        return sp_125_pos(letter)
    elif symbol == 'P4/nnc':
        return sp_126_pos(letter)
    elif symbol == 'P4/mbm':
        return sp_127_pos(letter)
    elif symbol == 'P4/mnc':
        return sp_128_pos(letter)
    elif symbol == 'P4/nmm':
        return sp_129_pos(letter)
    elif symbol == 'P4/ncc':
        return sp_130_pos(letter)
    elif symbol == 'P4_2/mmc':
        return sp_131_pos(letter)
    elif symbol == 'P4_2/mcm':
        return sp_132_pos(letter)
    elif symbol == 'P4_2/nbc':
        return sp_133_pos(letter)
    elif symbol == 'P4_2/nnm':
        return sp_134_pos(letter)
    elif symbol == 'P4_2/mbc':
        return sp_135_pos(letter)
    elif symbol == 'P4_2/mnm':
        return sp_136_pos(letter)
    elif symbol == 'P4_2/nmc':
        return sp_137_pos(letter)
    elif symbol == 'P4_2/ncm':
        return sp_138_pos(letter)
    elif symbol == 'I4/mmm':
        return sp_139_pos(letter)
    elif symbol == 'I4/mcm':
        return sp_140_pos(letter)
    elif symbol == 'I4_1/amd':
        return sp_141_pos(letter)
    elif symbol == 'I4_1/acd':
        return sp_142_pos(letter)
    elif symbol == 'P3':
        return sp_143_pos(letter)
    elif symbol == 'P3_1':
        return sp_144_pos(letter)
    elif symbol == 'P3_2':
        return sp_145_pos(letter)
    elif symbol == 'R3':
        return sp_146_pos_R(letter)
    elif symbol == 'R3H':
        return sp_146_pos_H(letter)
    elif symbol == 'P-3':
        return sp_147_pos(letter)
    elif symbol == 'R-3':
        return sp_148_pos_R(letter)
    elif symbol == 'R-3H':
        return sp_148_pos_H(letter)
    elif symbol == 'P312':
        return sp_149_pos(letter)
    elif symbol == 'P321':
        return sp_150_pos(letter)
    elif symbol == 'P3_112':
        return sp_151_pos(letter)
    elif symbol == 'P3_121':
        return sp_152_pos(letter)
    elif symbol == 'P3_212':
        return sp_153_pos(letter)
    elif symbol == 'P3_221':
        return sp_154_pos(letter)
    elif symbol == 'R32':
        return sp_155_pos_R(letter)
    elif symbol == 'R32H':
        return sp_155_pos_H(letter)
    elif symbol == 'P3m1':
        return sp_156_pos(letter)
    elif symbol == 'P31m':
        return sp_157_pos(letter)
    elif symbol == 'P3c1':
        return sp_158_pos(letter)
    elif symbol == 'P31c':
        return sp_159_pos(letter)
    elif symbol == 'R3m':
        return sp_160_pos_R(letter)
    elif symbol == 'R3mH':
        return sp_160_pos_H(letter)
    elif symbol == 'R3c':
        return sp_161_pos_R(letter)
    elif symbol == 'R3cH':
        return sp_161_pos_H(letter)
    elif symbol == 'P-31m':
        return sp_162_pos(letter)
    elif symbol == 'P-31c':
        return sp_163_pos(letter)
    elif symbol == 'P-3m1':
        return sp_164_pos(letter)
    elif symbol == 'P-3c1':
        return sp_165_pos(letter)
    elif symbol == 'R-3m':
        return sp_166_pos_R(letter)
    elif symbol == 'R-3mH':
        return sp_166_pos_H(letter)
    elif symbol == 'R-3c':
        return sp_167_pos_R(letter)
    elif symbol == 'R-3cH':
        return sp_167_pos_H(letter)
    elif symbol == 'P6':
        return sp_168_pos(letter)
    elif symbol == 'P6_1':
        return sp_169_pos(letter)
    elif symbol == 'P6_5':
        return sp_170_pos(letter)
    elif symbol == 'P6_2':
        return sp_171_pos(letter)
    elif symbol == 'P6_4':
        return sp_172_pos(letter)
    elif symbol == 'P6_3':
        return sp_173_pos(letter)
    elif symbol == 'P-6':
        return sp_174_pos(letter)
    elif symbol == 'P6/m':
        return sp_175_pos(letter)
    elif symbol == 'P6_3/m':
        return sp_176_pos(letter)
    elif symbol == 'P622':
        return sp_177_pos(letter)
    elif symbol == 'P6_122':
        return sp_178_pos(letter)
    elif symbol == 'P6_522':
        return sp_179_pos(letter)
    elif symbol == 'P6_222':
        return sp_180_pos(letter)
    elif symbol == 'P6_422':
        return sp_181_pos(letter)
    elif symbol == 'P6_322':
        return sp_182_pos(letter)
    elif symbol == 'P6mm':
        return sp_183_pos(letter)
    elif symbol == 'P6cc':
        return sp_184_pos(letter)
    elif symbol == 'P6_3cm':
        return sp_185_pos(letter)
    elif symbol == 'P6_3mc':
        return sp_186_pos(letter)
    elif symbol == 'P-6m2':
        return sp_187_pos(letter)
    elif symbol == 'P-6c2':
        return sp_188_pos(letter)
    elif symbol == 'P-62m':
        return sp_189_pos(letter)
    elif symbol == 'P-62c':
        return sp_190_pos(letter)
    elif symbol == 'P6/mmm':
        return sp_191_pos(letter)
    elif symbol == 'P6/mcc':
        return sp_192_pos(letter)
    elif symbol == 'P6_3/mcm':
        return sp_193_pos(letter)
    elif symbol == 'P6_3/mmc':
        return sp_194_pos(letter)
    elif symbol == 'P23':
        return sp_195_pos(letter)
    elif symbol == 'F23':
        return sp_196_pos(letter)
    elif symbol == 'I23':
        return sp_197_pos(letter)
    elif symbol == 'P2_13':
        return sp_198_pos(letter)
    elif symbol == 'I2_13':
        return sp_199_pos(letter)
    elif symbol == 'Pm-3':
        return sp_200_pos(letter)
    elif symbol == 'Pn-3':
        return sp_201_pos(letter)
    elif symbol == 'Fm-3':
        return sp_202_pos(letter)
    elif symbol == 'Fd-3':
        return sp_203_pos(letter)
    elif symbol == 'Im-3':
        return sp_204_pos(letter)
    elif symbol == 'Pa-3':
        return sp_205_pos(letter)
    elif symbol == 'Ia-3':
        return sp_206_pos(letter)
    elif symbol == 'P432':
        return sp_207_pos(letter)
    elif symbol == 'P4_232':
        return sp_208_pos(letter)
    elif symbol == 'F432':
        return sp_209_pos(letter)
    elif symbol == 'F4_132':
        return sp_210_pos(letter)
    elif symbol == 'I432':
        return sp_211_pos(letter)
    elif symbol == 'P4_332':
        return sp_212_pos(letter)
    elif symbol == 'P4_132':
        return sp_213_pos(letter)
    elif symbol == 'I4_132':
        return sp_214_pos(letter)
    elif symbol == 'P-43m':
        return sp_215_pos(letter)
    elif symbol == 'F-43m':
        return sp_216_pos(letter)
    elif symbol == 'I-43m':
        return sp_217_pos(letter)
    elif symbol == 'P-43n':
        return sp_218_pos(letter)
    elif symbol == 'F-43c':
        return sp_219_pos(letter)
    elif symbol == 'I-43d':
        return sp_220_pos(letter)
    elif symbol == 'Pm-3m':
        return sp_221_pos(letter)
    elif symbol == 'Pn-3n':
        return sp_222_pos(letter)
    elif symbol == 'Pm-3n':
        return sp_223_pos(letter)
    elif symbol == 'Pn-3m':
        return sp_224_pos(letter)
    elif symbol == 'Fm-3m':
        return sp_225_pos(letter)
    elif symbol == 'Fm-3c':
        return sp_226_pos(letter)
    elif symbol == 'Fd-3m':
        return sp_227_pos(letter)
    elif symbol == 'Fd-3c':
        return sp_228_pos(letter)
    elif symbol == 'Im-3m':
        return sp_229_pos(letter)
    elif symbol == 'Ia-3d':
        return sp_230_pos(letter)

def sp_1_pos(letter):
    letters_selection = ['a']
    spg = SpaceGroup('P1')
    if not letter in letters_selection:
        raise ValueError("It is not a P1 wyckoff position!")
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_2_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    spg = SpaceGroup('P-1')
    if not letter in letters_selection:
        raise ValueError("It is not a P-1 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([0., 0.5, 0.])
    elif letter == 'd':
        return spg.get_orbit([0.5, 0., 0.])
    elif letter == 'e':
        return spg.get_orbit([0.5, 0.5, 0.])
    elif letter == 'f':
        return spg.get_orbit([0.5, 0., 0.5])
    elif letter == 'g':
        return spg.get_orbit([0., 0.5, 0.5])
    elif letter == 'h':
        return spg.get_orbit([0.5, 0.5, 0.5])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_3_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e']
    spg = SpaceGroup('P2')
    if not letter in letters_selection:
        raise ValueError("It is not a P2 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., rand(), 0.])
    elif letter == 'b':
        return spg.get_orbit([0., rand(), 0.5])
    elif letter == 'c':
        return spg.get_orbit([0.5, rand(), 0.])
    elif letter == 'd':
        return spg.get_orbit([0.5, rand(), 0.5])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_4_pos(letter):
    letters_selection = ['a']
    spg = SpaceGroup('P2_1')
    if not letter in letters_selection:
        raise ValueError("It is not a P2_1 wyckoff position!")
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_5_pos(letter):
    letters_selection = ['a', 'b', 'c']
    spg = SpaceGroup('C2')
    if not letter in letters_selection:
        raise ValueError("It is not a C2 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., rand(), 0.])
    elif letter == 'b':
        return spg.get_orbit([0., rand(), 0.5])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_6_pos(letter):
    letters_selection = ['a', 'b', 'c']
    spg = SpaceGroup('Pm')
    if not letter in letters_selection:
        raise ValueError("It is not a Pm wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([rand(), 0., rand()])
    elif letter == 'b':
        return spg.get_orbit([rand(), 0.5, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_7_pos(letter):
    letters_selection = ['a']
    spg = SpaceGroup('Pc')
    if not letter in letters_selection:
        raise ValueError("It is not a Pc wyckoff position!")
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_8_pos(letter):
    letters_selection = ['a', 'b']
    spg = SpaceGroup('Cm')
    if not letter in letters_selection:
        raise ValueError("It is not a Cm wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([rand(), 0., rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_9_pos(letter):
    letters_selection = ['a']
    spg = SpaceGroup('Cc')
    if not letter in letters_selection:
        raise ValueError("It is not a Cc wyckoff position!")
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_10_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
    spg = SpaceGroup('P2/m')
    if not letter in letters_selection:
        raise ValueError("It is not a P2/m wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0.5, 0.])
    elif letter == 'c':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'd':
        return spg.get_orbit([0.5, 0., 0.])
    elif letter == 'e':
        return spg.get_orbit([0.5, 0.5, 0.])
    elif letter == 'f':
        return spg.get_orbit([0., 0.5, 0.5])
    elif letter == 'g':
        return spg.get_orbit([0.5, 0., 0.5])
    elif letter == 'h':
        return spg.get_orbit([0.5, 0.5, 0.5])
    elif letter == 'i':
        return spg.get_orbit([0., rand(), 0.])
    elif letter == 'j':
        return spg.get_orbit([0.5, rand(), 0.])
    elif letter == 'k':
        return spg.get_orbit([0., rand(), 0.5])
    elif letter == 'l':
        return spg.get_orbit([0.5, rand(), 0.5])
    elif letter == 'm':
        return spg.get_orbit([rand(), 0., rand()])
    elif letter == 'n':
        return spg.get_orbit([rand(), 0.5, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_11_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f']
    spg = SpaceGroup('P2_1/m')
    if not letter in letters_selection:
        raise ValueError("It is not a P2_1/m wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0., 0.])
    elif letter == 'c':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'd':
        return spg.get_orbit([0.5, 0., 0.5])
    elif letter == 'e':
        return spg.get_orbit([rand(), 0.25, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_12_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    spg = SpaceGroup('C2/m')
    if not letter in letters_selection:
        raise ValueError("It is not a C2/m wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0.5, 0.])
    elif letter == 'c':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'd':
        return spg.get_orbit([0., 0.5, 0.5])
    elif letter == 'e':
        return spg.get_orbit([0.25, 0.25, 0.])
    elif letter == 'f':
        return spg.get_orbit([0.25, 0.25, 0.5])
    elif letter == 'g':
        return spg.get_orbit([0., rand(), 0.])
    elif letter == 'h':
        return spg.get_orbit([0., rand(), 0.5])
    elif letter == 'i':
        return spg.get_orbit([rand(), 0., rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_13_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    spg = SpaceGroup('P2/c')
    if not letter in letters_selection:
        raise ValueError("It is not a P2/c wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0.5, 0.])
    elif letter == 'c':
        return spg.get_orbit([0., 0.5, 0.])
    elif letter == 'd':
        return spg.get_orbit([0.5, 0., 0.])
    elif letter == 'e':
        return spg.get_orbit([0., rand(), 0.25])
    elif letter == 'f':
        return spg.get_orbit([0.5, rand(), 0.25])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_14_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e']
    spg = SpaceGroup('P2_1/c')
    if not letter in letters_selection:
        raise ValueError("It is not a P2_1/c wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0., 0.])
    elif letter == 'c':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'd':
        return spg.get_orbit([0.5, 0., 0.5])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_15_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f']
    spg = SpaceGroup('C2/c')
    if not letter in letters_selection:
        raise ValueError("It is not a C2/c wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0.5, 0.])
    elif letter == 'c':
        return spg.get_orbit([0.25, 0.25, 0.])
    elif letter == 'd':
        return spg.get_orbit([0.25, 0.25, 0.5])
    elif letter == 'e':
        return spg.get_orbit([0., rand(), 0.25])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_16_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u']
    spg = SpaceGroup('P222')
    if not letter in letters_selection:
        raise ValueError("It is not a P222 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0., 0.])
    elif letter == 'c':
        return spg.get_orbit([0., 0.5, 0.])
    elif letter == 'd':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'e':
        return spg.get_orbit([0.5, 0.5, 0.])
    elif letter == 'f':
        return spg.get_orbit([0.5, 0., 0.5])
    elif letter == 'g':
        return spg.get_orbit([0., 0.5, 0.5])
    elif letter == 'h':
        return spg.get_orbit([0.5, 0.5, 0.5])
    elif letter == 'i':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'j':
        return spg.get_orbit([rand(), 0., 0.5])
    elif letter == 'k':
        return spg.get_orbit([rand(), 0.5, 0.])
    elif letter == 'l':
        return spg.get_orbit([rand(), 0.5, 0.5])
    elif letter == 'm':
        return spg.get_orbit([0., rand(), 0.])
    elif letter == 'n':
        return spg.get_orbit([0., rand(), 0.5])
    elif letter == 'o':
        return spg.get_orbit([0.5, rand(), 0.])
    elif letter == 'p':
        return spg.get_orbit([0.5, rand(), 0.5])
    elif letter == 'q':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'r':
        return spg.get_orbit([0.5, 0., rand()])
    elif letter == 's':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 't':
        return spg.get_orbit([0.5, 0.5, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_17_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e']
    spg = SpaceGroup('P222_1')
    if not letter in letters_selection:
        raise ValueError("It is not a P222_1 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([rand(), 0.5, 0.])
    elif letter == 'c':
        return spg.get_orbit([0., rand(), 0.25])
    elif letter == 'd':
        return spg.get_orbit([0.5, rand(), 0.25])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_18_pos(letter):
    letters_selection = ['a', 'b', 'c']
    spg = SpaceGroup('P2_12_12')
    if not letter in letters_selection:
        raise ValueError("It is not a P2_12_12 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'b':
        return spg.get_orbit([0., 0.5, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_19_pos(letter):
    letters_selection = ['a']
    spg = SpaceGroup('P2_12_12_1')
    if not letter in letters_selection:
        raise ValueError("It is not a P2_12_12_1 wyckoff position!")
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_20_pos(letter):
    letters_selection = ['a', 'b', 'c']
    spg = SpaceGroup('C222_1')
    if not letter in letters_selection:
        raise ValueError("It is not a C222_1 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., rand(), 0.25])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_21_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    spg = SpaceGroup('C222')
    if not letter in letters_selection:
        raise ValueError("It is not a C222 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0.5, 0.])
    elif letter == 'c':
        return spg.get_orbit([0.5, 0., 0.5])
    elif letter == 'd':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'e':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'f':
        return spg.get_orbit([rand(), 0., 0.5])
    elif letter == 'g':
        return spg.get_orbit([0., rand(), 0.])
    elif letter == 'h':
        return spg.get_orbit([0., rand(), 0.5])
    elif letter == 'i':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'j':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'k':
        return spg.get_orbit([0.25, 0.25, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_22_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    spg = SpaceGroup('F222')
    if not letter in letters_selection:
        raise ValueError("It is not a F222 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([0.25, 0.25, 0.25])
    elif letter == 'd':
        return spg.get_orbit([0.25, 0.25, 0.75])
    elif letter == 'e':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'f':
        return spg.get_orbit([0., rand(), 0.])
    elif letter == 'g':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'h':
        return spg.get_orbit([0.25, 0.25, rand()])
    elif letter == 'i':
        return spg.get_orbit([0.25, rand(), 0.25])
    elif letter == 'j':
        return spg.get_orbit([rand(), 0.25, 0.25])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_23_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    spg = SpaceGroup('I222')
    if not letter in letters_selection:
        raise ValueError("It is not a I222 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0., 0.])
    elif letter == 'c':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'd':
        return spg.get_orbit([0., 0.5, 0.])
    elif letter == 'e':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'f':
        return spg.get_orbit([rand(), 0., 0.5])
    elif letter == 'g':
        return spg.get_orbit([0., rand(), 0.])
    elif letter == 'h':
        return spg.get_orbit([0.5, rand(), 0.])
    elif letter == 'i':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'j':
        return spg.get_orbit([0., 0.5, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_24_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd']
    spg = SpaceGroup('I2_12_12_1')
    if not letter in letters_selection:
        raise ValueError("It is not a I2_12_12_1 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([rand(), 0., 0.25])
    elif letter == 'b':
        return spg.get_orbit([0.25, rand(), 0.])
    elif letter == 'c':
        return spg.get_orbit([0., 0.25, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_25_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    spg = SpaceGroup('Pmm2')
    if not letter in letters_selection:
        raise ValueError("It is not a Pmm2 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'b':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'c':
        return spg.get_orbit([0.5, 0., rand()])
    elif letter == 'd':
        return spg.get_orbit([0.5, 0.5, rand()])
    elif letter == 'e':
        return spg.get_orbit([rand(), 0., rand()])
    elif letter == 'f':
        return spg.get_orbit([rand(), 0.5, rand()])
    elif letter == 'g':
        return spg.get_orbit([0., rand(), rand()])
    elif letter == 'h':
        return spg.get_orbit([0.5, rand(), rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_26_pos(letter):
    letters_selection = ['a', 'b', 'c']
    spg = SpaceGroup('Pmc2_1')
    if not letter in letters_selection:
        raise ValueError("It is not a Pmc2_1 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., rand(), rand()])
    elif letter == 'b':
        return spg.get_orbit([0.5, rand(), rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_27_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e']
    spg = SpaceGroup('Pcc2')
    if not letter in letters_selection:
        raise ValueError("It is not a Pcc2 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'b':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'c':
        return spg.get_orbit([0.5, 0., rand()])
    elif letter == 'd':
        return spg.get_orbit([0.5, 0.5, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_28_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd']
    spg = SpaceGroup('Pma2')
    if not letter in letters_selection:
        raise ValueError("It is not a Pma2 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'b':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'c':
        return spg.get_orbit([0.25, rand(), rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_29_pos(letter):
    letters_selection = ['a']
    spg = SpaceGroup('Pca2_1')
    if not letter in letters_selection:
        raise ValueError("It is not a Pca2_1 wyckoff position!")
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_30_pos(letter):
    letters_selection = ['a', 'b', 'c']
    spg = SpaceGroup('Pnc2')
    if not letter in letters_selection:
        raise ValueError("It is not a Pnc2 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0., rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_31_pos(letter):
    letters_selection = ['a', 'b']
    spg = SpaceGroup('Pmn2_1')
    if not letter in letters_selection:
        raise ValueError("It is not a Pmn2_1 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., rand(), rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_32_pos(letter):
    letters_selection = ['a', 'b', 'c']
    spg = SpaceGroup('Pba2')
    if not letter in letters_selection:
        raise ValueError("It is not a Pba2 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'b':
        return spg.get_orbit([0., 0.5, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_33_pos(letter):
    letters_selection = ['a']
    spg = SpaceGroup('Pna2_1')
    if not letter in letters_selection:
        raise ValueError("It is not a Pna2_1 wyckoff position!")
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_34_pos(letter):
    letters_selection = ['a', 'b', 'c']
    spg = SpaceGroup('Pnn2')
    if not letter in letters_selection:
        raise ValueError("It is not a Pnn2 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'b':
        return spg.get_orbit([0., 0.5, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_35_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f']
    spg = SpaceGroup('Cmm2')
    if not letter in letters_selection:
        raise ValueError("It is not a Cmm2 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'b':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'c':
        return spg.get_orbit([0.25, 0.25, rand()])
    elif letter == 'd':
        return spg.get_orbit([rand(), 0., rand()])
    elif letter == 'e':
        return spg.get_orbit([0., rand(), rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_36_pos(letter):
    letters_selection = ['a', 'b']
    spg = SpaceGroup('Cmc2_1')
    if not letter in letters_selection:
        raise ValueError("It is not a Cmc2_1 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., rand(), rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_37_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd']
    spg = SpaceGroup('Ccc2')
    if not letter in letters_selection:
        raise ValueError("It is not a Ccc2 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'b':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'c':
        return spg.get_orbit([0.25, 0.25, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_38_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f']
    spg = SpaceGroup('Amm2')
    if not letter in letters_selection:
        raise ValueError("It is not a Amm2 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0., rand()])
    elif letter == 'c':
        return spg.get_orbit([rand(), 0., rand()])
    elif letter == 'd':
        return spg.get_orbit([0., rand(), rand()])
    elif letter == 'e':
        return spg.get_orbit([0.5, rand(), rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_39_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd']
    spg = SpaceGroup('Aem2')
    if not letter in letters_selection:
        raise ValueError("It is not a Aem2 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0., rand()])
    elif letter == 'c':
        return spg.get_orbit([rand(), 0.25, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_40_pos(letter):
    letters_selection = ['a', 'b', 'c']
    spg = SpaceGroup('Ama2')
    if not letter in letters_selection:
        raise ValueError("It is not a Ama2 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'b':
        return spg.get_orbit([0.25, rand(), rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_41_pos(letter):
    letters_selection = ['a', 'b']
    spg = SpaceGroup('Aea2')
    if not letter in letters_selection:
        raise ValueError("It is not a Aea2 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_42_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e']
    spg = SpaceGroup('Fmm2')
    if not letter in letters_selection:
        raise ValueError("It is not a Fmm2 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'b':
        return spg.get_orbit([0.25, 0.25, rand()])
    elif letter == 'c':
        return spg.get_orbit([0., rand(), rand()])
    elif letter == 'd':
        return spg.get_orbit([rand(), 0., rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_43_pos(letter):
    letters_selection = ['a', 'b']
    spg = SpaceGroup('Fdd2')
    if not letter in letters_selection:
        raise ValueError("It is not a Fdd2 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_44_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e']
    spg = SpaceGroup('Imm2')
    if not letter in letters_selection:
        raise ValueError("It is not a Imm2 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'b':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'c':
        return spg.get_orbit([rand(), 0., rand()])
    elif letter == 'd':
        return spg.get_orbit([0., rand(), rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_45_pos(letter):
    letters_selection = ['a', 'b', 'c']
    spg = SpaceGroup('Iba2')
    if not letter in letters_selection:
        raise ValueError("It is not a Iba2 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'b':
        return spg.get_orbit([0., 0.5, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_46_pos(letter):
    letters_selection = ['a', 'b', 'c']
    spg = SpaceGroup('Ima2')
    if not letter in letters_selection:
        raise ValueError("It is not a Ima2 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'b':
        return spg.get_orbit([0.25, rand(), rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_47_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A']
    spg = SpaceGroup('Pmmm')
    if not letter in letters_selection:
        raise ValueError("It is not a Pmmm wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0., 0.])
    elif letter == 'c':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'd':
        return spg.get_orbit([0.5, 0., 0.5])
    elif letter == 'e':
        return spg.get_orbit([0., 0.5, 0.])
    elif letter == 'f':
        return spg.get_orbit([0.5, 0.5, 0.])
    elif letter == 'g':
        return spg.get_orbit([0., 0.5, 0.5])
    elif letter == 'h':
        return spg.get_orbit([0.5, 0.5, 0.5])
    elif letter == 'i':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'j':
        return spg.get_orbit([rand(), 0., 0.5])
    elif letter == 'k':
        return spg.get_orbit([rand(), 0.5, 0.])
    elif letter == 'l':
        return spg.get_orbit([rand(), 0.5, 0.5])
    elif letter == 'm':
        return spg.get_orbit([0., rand(), 0.])
    elif letter == 'n':
        return spg.get_orbit([0., rand(), 0.5])
    elif letter == 'o':
        return spg.get_orbit([0.5, rand(), 0.])
    elif letter == 'p':
        return spg.get_orbit([0.5, rand(), 0.5])
    elif letter == 'q':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'r':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 's':
        return spg.get_orbit([0.5, 0., rand()])
    elif letter == 't':
        return spg.get_orbit([0.5, 0.5, rand()])
    elif letter == 'u':
        return spg.get_orbit([0., rand(), rand()])
    elif letter == 'v':
        return spg.get_orbit([0.5, rand(), rand()])
    elif letter == 'w':
        return spg.get_orbit([rand(), 0., rand()])
    elif letter == 'x':
        return spg.get_orbit([rand(), 0.5, rand()])
    elif letter == 'y':
        return spg.get_orbit([rand(), rand(), 0.])
    elif letter == 'z':
        return spg.get_orbit([rand(), rand(), 0.5])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_48_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    spg = SpaceGroup('Pnnn')
    if not letter in letters_selection:
        raise ValueError("It is not a Pnnn wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0., 0.])
    elif letter == 'c':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'd':
        return spg.get_orbit([0., 0.5, 0.])
    elif letter == 'e':
        return spg.get_orbit([0.25, 0.25, 0.25])
    elif letter == 'f':
        return spg.get_orbit([0.75, 0.75, 0.75])
    elif letter == 'g':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'h':
        return spg.get_orbit([rand(), 0., 0.5])
    elif letter == 'i':
        return spg.get_orbit([0., rand(), 0.])
    elif letter == 'j':
        return spg.get_orbit([0.5, rand(), 0.])
    elif letter == 'k':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'l':
        return spg.get_orbit([0., 0.5, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_49_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r']
    spg = SpaceGroup('Pccm')
    if not letter in letters_selection:
        raise ValueError("It is not a Pccm wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0.5, 0.])
    elif letter == 'c':
        return spg.get_orbit([0., 0.5, 0.])
    elif letter == 'd':
        return spg.get_orbit([0.5, 0., 0.])
    elif letter == 'e':
        return spg.get_orbit([0., 0., 0.25])
    elif letter == 'f':
        return spg.get_orbit([0.5, 0., 0.25])
    elif letter == 'g':
        return spg.get_orbit([0., 0.5, 0.25])
    elif letter == 'h':
        return spg.get_orbit([0.5, 0.5, 0.25])
    elif letter == 'i':
        return spg.get_orbit([rand(), 0., 0.25])
    elif letter == 'j':
        return spg.get_orbit([rand(), 0.5, 0.25])
    elif letter == 'k':
        return spg.get_orbit([0., rand(), 0.25])
    elif letter == 'l':
        return spg.get_orbit([0.5, rand(), 0.25])
    elif letter == 'm':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'n':
        return spg.get_orbit([0.5, 0.5, rand()])
    elif letter == 'o':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'p':
        return spg.get_orbit([0.5, 0., rand()])
    elif letter == 'q':
        return spg.get_orbit([rand(), rand(), 0.])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_50_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    spg = SpaceGroup('Pban')
    if not letter in letters_selection:
        raise ValueError("It is not a Pban wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0., 0.])
    elif letter == 'c':
        return spg.get_orbit([0.5, 0., 0.5])
    elif letter == 'd':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'e':
        return spg.get_orbit([0.25, 0.25, 0.])
    elif letter == 'f':
        return spg.get_orbit([0.25, 0.25, 0.5])
    elif letter == 'g':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'h':
        return spg.get_orbit([rand(), 0., 0.5])
    elif letter == 'i':
        return spg.get_orbit([0., rand(), 0.])
    elif letter == 'j':
        return spg.get_orbit([0., rand(), 0.5])
    elif letter == 'k':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'l':
        return spg.get_orbit([0., 0.5, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_51_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    spg = SpaceGroup('Pmma')
    if not letter in letters_selection:
        raise ValueError("It is not a Pmma wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0.5, 0.])
    elif letter == 'c':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'd':
        return spg.get_orbit([0., 0.5, 0.5])
    elif letter == 'e':
        return spg.get_orbit([0.25, 0., rand()])
    elif letter == 'f':
        return spg.get_orbit([0.25, 0.5, rand()])
    elif letter == 'g':
        return spg.get_orbit([0., rand(), 0.])
    elif letter == 'h':
        return spg.get_orbit([0., rand(), 0.5])
    elif letter == 'i':
        return spg.get_orbit([rand(), 0., rand()])
    elif letter == 'j':
        return spg.get_orbit([rand(), 0.5, rand()])
    elif letter == 'k':
        return spg.get_orbit([0.25, rand(), rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_52_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e']
    spg = SpaceGroup('Pnna')
    if not letter in letters_selection:
        raise ValueError("It is not a Pnna wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([0.25, 0., rand()])
    elif letter == 'd':
        return spg.get_orbit([rand(), 0.25, 0.25])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_53_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    spg = SpaceGroup('Pmna')
    if not letter in letters_selection:
        raise ValueError("It is not a Pmna wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0., 0.])
    elif letter == 'c':
        return spg.get_orbit([0.5, 0.5, 0.])
    elif letter == 'd':
        return spg.get_orbit([0., 0.5, 0.])
    elif letter == 'e':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'f':
        return spg.get_orbit([rand(), 0.5, 0.])
    elif letter == 'g':
        return spg.get_orbit([0.25, rand(), 0.25])
    elif letter == 'h':
        return spg.get_orbit([0., rand(), rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_54_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f']
    spg = SpaceGroup('Pcca')
    if not letter in letters_selection:
        raise ValueError("It is not a Pcca wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0.5, 0.])
    elif letter == 'c':
        return spg.get_orbit([0., rand(), 0.25])
    elif letter == 'd':
        return spg.get_orbit([0.25, 0., rand()])
    elif letter == 'e':
        return spg.get_orbit([0.25, 0.5, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_55_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    spg = SpaceGroup('Pbam')
    if not letter in letters_selection:
        raise ValueError("It is not a Pbam wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([0., 0.5, 0.])
    elif letter == 'd':
        return spg.get_orbit([0., 0.5, 0.5])
    elif letter == 'e':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'f':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'g':
        return spg.get_orbit([rand(), rand(), 0.])
    elif letter == 'h':
        return spg.get_orbit([rand(), rand(), 0.5])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_56_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e']
    spg = SpaceGroup('Pccn')
    if not letter in letters_selection:
        raise ValueError("It is not a Pccn wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([0.25, 0.25, rand()])
    elif letter == 'd':
        return spg.get_orbit([0.25, 0.75, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_57_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e']
    spg = SpaceGroup('Pbcm')
    if not letter in letters_selection:
        raise ValueError("It is not a Pbcm wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0., 0.])
    elif letter == 'c':
        return spg.get_orbit([rand(), 0.25, 0.])
    elif letter == 'd':
        return spg.get_orbit([rand(), rand(), 0.25])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_58_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    spg = SpaceGroup('Pnnm')
    if not letter in letters_selection:
        raise ValueError("It is not a Pnnm wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([0., 0.5, 0.])
    elif letter == 'd':
        return spg.get_orbit([0., 0.5, 0.5])
    elif letter == 'e':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'f':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'g':
        return spg.get_orbit([rand(), rand(), 0.])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_59_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    spg = SpaceGroup('Pmmn')
    if not letter in letters_selection:
        raise ValueError("It is not a Pmmn wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'b':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'c':
        return spg.get_orbit([0.25, 0.25, 0.])
    elif letter == 'd':
        return spg.get_orbit([0.25, 0.25, 0.5])
    elif letter == 'e':
        return spg.get_orbit([0., rand(), rand()])
    elif letter == 'f':
        return spg.get_orbit([rand(), 0., rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_60_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd']
    spg = SpaceGroup('Pbcn')
    if not letter in letters_selection:
        raise ValueError("It is not a Pbcn wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0.5, 0.])
    elif letter == 'c':
        return spg.get_orbit([0., rand(), 0.25])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_61_pos(letter):
    letters_selection = ['a', 'b', 'c']
    spg = SpaceGroup('Pbca')
    if not letter in letters_selection:
        raise ValueError("It is not a Pbca wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_62_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd']
    spg = SpaceGroup('Pnma')
    if not letter in letters_selection:
        raise ValueError("It is not a Pnma wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([rand(), 0.25, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_63_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    spg = SpaceGroup('Cmcm')
    if not letter in letters_selection:
        raise ValueError("It is not a Cmcm wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0.5, 0.])
    elif letter == 'c':
        return spg.get_orbit([0., rand(), 0.25])
    elif letter == 'd':
        return spg.get_orbit([0.25, 0.25, 0.])
    elif letter == 'e':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'f':
        return spg.get_orbit([0., rand(), rand()])
    elif letter == 'g':
        return spg.get_orbit([rand(), rand(), 0.25])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_64_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    spg = SpaceGroup('Cmce')
    if not letter in letters_selection:
        raise ValueError("It is not a Cmce wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0., 0.])
    elif letter == 'c':
        return spg.get_orbit([0.25, 0.25, 0.])
    elif letter == 'd':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'e':
        return spg.get_orbit([0.25, rand(), 0.25])
    elif letter == 'f':
        return spg.get_orbit([0., rand(), rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_65_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r']
    spg = SpaceGroup('Cmmm')
    if not letter in letters_selection:
        raise ValueError("It is not a Cmmm wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0., 0.])
    elif letter == 'c':
        return spg.get_orbit([0.5, 0., 0.5])
    elif letter == 'd':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'e':
        return spg.get_orbit([0.25, 0.25, 0.])
    elif letter == 'f':
        return spg.get_orbit([0.25, 0.25, 0.5])
    elif letter == 'g':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'h':
        return spg.get_orbit([rand(), 0., 0.5])
    elif letter == 'i':
        return spg.get_orbit([0., rand(), 0.])
    elif letter == 'j':
        return spg.get_orbit([0., rand(), 0.5])
    elif letter == 'k':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'l':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'm':
        return spg.get_orbit([0.25, 0.25, rand()])
    elif letter == 'n':
        return spg.get_orbit([0., rand(), rand()])
    elif letter == 'o':
        return spg.get_orbit([rand(), 0., rand()])
    elif letter == 'p':
        return spg.get_orbit([rand(), rand(), 0.])
    elif letter == 'q':
        return spg.get_orbit([rand(), rand(), 0.5])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_66_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    spg = SpaceGroup('Cccm')
    if not letter in letters_selection:
        raise ValueError("It is not a Cccm wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.25])
    elif letter == 'b':
        return spg.get_orbit([0., 0.5, 0.25])
    elif letter == 'c':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'd':
        return spg.get_orbit([0., 0.5, 0.])
    elif letter == 'e':
        return spg.get_orbit([0.25, 0.25, 0.])
    elif letter == 'f':
        return spg.get_orbit([0.25, 0.75, 0.])
    elif letter == 'g':
        return spg.get_orbit([rand(), 0., 0.25])
    elif letter == 'h':
        return spg.get_orbit([0., rand(), 0.25])
    elif letter == 'i':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'j':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'k':
        return spg.get_orbit([0.25, 0.25, rand()])
    elif letter == 'l':
        return spg.get_orbit([rand(), rand(), 0.])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_67_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
    spg = SpaceGroup('Cmme')
    if not letter in letters_selection:
        raise ValueError("It is not a Cmme wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0.25, 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0.25, 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'd':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'e':
        return spg.get_orbit([0.25, 0.25, 0.])
    elif letter == 'f':
        return spg.get_orbit([0.25, 0.25, 0.5])
    elif letter == 'g':
        return spg.get_orbit([0., 0.25, rand()])
    elif letter == 'h':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'i':
        return spg.get_orbit([rand(), 0., 0.5])
    elif letter == 'j':
        return spg.get_orbit([0.25, rand(), 0.])
    elif letter == 'k':
        return spg.get_orbit([0.25, rand(), 0.5])
    elif letter == 'l':
        return spg.get_orbit([0.25, 0., rand()])
    elif letter == 'm':
        return spg.get_orbit([0., rand(), rand()])
    elif letter == 'n':
        return spg.get_orbit([rand(), 0.25, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_68_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    spg = SpaceGroup('Ccce')
    if not letter in letters_selection:
        raise ValueError("It is not a Ccce wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([0.25, 0., 0.25])
    elif letter == 'd':
        return spg.get_orbit([0., 0.25, 0.25])
    elif letter == 'e':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'f':
        return spg.get_orbit([0., rand(), 0.])
    elif letter == 'g':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'h':
        return spg.get_orbit([0.25, 0.25, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_69_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    spg = SpaceGroup('Fmmm')
    if not letter in letters_selection:
        raise ValueError("It is not a Fmmm wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([0., 0.25, 0.25])
    elif letter == 'd':
        return spg.get_orbit([0.25, 0., 0.25])
    elif letter == 'e':
        return spg.get_orbit([0.25, 0.25, 0.])
    elif letter == 'f':
        return spg.get_orbit([0.25, 0.25, 0.25])
    elif letter == 'g':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'h':
        return spg.get_orbit([0., rand(), 0.])
    elif letter == 'i':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'j':
        return spg.get_orbit([0.25, 0.25, rand()])
    elif letter == 'k':
        return spg.get_orbit([0.25, rand(), 0.25])
    elif letter == 'l':
        return spg.get_orbit([rand(), 0.25, 0.25])
    elif letter == 'm':
        return spg.get_orbit([0., rand(), rand()])
    elif letter == 'n':
        return spg.get_orbit([rand(), 0., rand()])
    elif letter == 'o':
        return spg.get_orbit([rand(), rand(), 0.])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_70_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    spg = SpaceGroup('Fddd')
    if not letter in letters_selection:
        raise ValueError("It is not a Fddd wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([0.125, 0.125, 0.125])
    elif letter == 'd':
        return spg.get_orbit([0.625, 0.625, 0.625])
    elif letter == 'e':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'f':
        return spg.get_orbit([0., rand(), 0.])
    elif letter == 'g':
        return spg.get_orbit([0., 0., rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_71_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
    spg = SpaceGroup('Immm')
    if not letter in letters_selection:
        raise ValueError("It is not a Immm wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0.5, 0.5])
    elif letter == 'c':
        return spg.get_orbit([0.5, 0.5, 0.])
    elif letter == 'd':
        return spg.get_orbit([0.5, 0., 0.5])
    elif letter == 'e':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'f':
        return spg.get_orbit([rand(), 0.5, 0.])
    elif letter == 'g':
        return spg.get_orbit([0., rand(), 0.])
    elif letter == 'h':
        return spg.get_orbit([0., rand(), 0.5])
    elif letter == 'i':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'j':
        return spg.get_orbit([0.5, 0., rand()])
    elif letter == 'k':
        return spg.get_orbit([0.25, 0.25, 0.25])
    elif letter == 'l':
        return spg.get_orbit([0., rand(), rand()])
    elif letter == 'm':
        return spg.get_orbit([rand(), 0., rand()])
    elif letter == 'n':
        return spg.get_orbit([rand(), rand(), 0.])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_72_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    spg = SpaceGroup('Ibam')
    if not letter in letters_selection:
        raise ValueError("It is not a Ibam wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.25])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0., 0.25])
    elif letter == 'c':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'd':
        return spg.get_orbit([0.5, 0., 0.])
    elif letter == 'e':
        return spg.get_orbit([0.25, 0.25, 0.25])
    elif letter == 'f':
        return spg.get_orbit([rand(), 0., 0.25])
    elif letter == 'g':
        return spg.get_orbit([0., rand(), 0.25])
    elif letter == 'h':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'i':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'j':
        return spg.get_orbit([rand(), rand(), 0.])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_73_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f']
    spg = SpaceGroup('Ibca')
    if not letter in letters_selection:
        raise ValueError("It is not a Ibca wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0.25, 0.25, 0.25])
    elif letter == 'c':
        return spg.get_orbit([rand(), 0., 0.25])
    elif letter == 'd':
        return spg.get_orbit([0.25, rand(), 0.])
    elif letter == 'e':
        return spg.get_orbit([0., 0.25, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_74_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    spg = SpaceGroup('Imma')
    if not letter in letters_selection:
        raise ValueError("It is not a Imma wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([0.25, 0.25, 0.25])
    elif letter == 'd':
        return spg.get_orbit([0.25, 0.25, 0.75])
    elif letter == 'e':
        return spg.get_orbit([0., 0.25, rand()])
    elif letter == 'f':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'g':
        return spg.get_orbit([0.25, rand(), 0.25])
    elif letter == 'h':
        return spg.get_orbit([0., rand(), rand()])
    elif letter == 'i':
        return spg.get_orbit([rand(), 0.25, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_75_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd']
    spg = SpaceGroup('P4')
    if not letter in letters_selection:
        raise ValueError("It is not a P4 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0.5, rand()])
    elif letter == 'c':
        return spg.get_orbit([0., 0.5, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_76_pos(letter):
    letters_selection = ['a']
    spg = SpaceGroup('P4_1')
    if not letter in letters_selection:
        raise ValueError("It is not a P4_1 wyckoff position!")
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_77_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd']
    spg = SpaceGroup('P4_2')
    if not letter in letters_selection:
        raise ValueError("It is not a P4_2 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0.5, rand()])
    elif letter == 'c':
        return spg.get_orbit([0., 0.5, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_78_pos(letter):
    letters_selection = ['a']
    spg = SpaceGroup('P4_3')
    if not letter in letters_selection:
        raise ValueError("It is not a P4_3 wyckoff position!")
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_79_pos(letter):
    letters_selection = ['a', 'b', 'c']
    spg = SpaceGroup('I4')
    if not letter in letters_selection:
        raise ValueError("It is not a I4 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'b':
        return spg.get_orbit([0., 0.5, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_80_pos(letter):
    letters_selection = ['a', 'b']
    spg = SpaceGroup('I4_1')
    if not letter in letters_selection:
        raise ValueError("It is not a I4_1 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_81_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    spg = SpaceGroup('P-4')
    if not letter in letters_selection:
        raise ValueError("It is not a P-4 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([0.5, 0.5, 0.])
    elif letter == 'd':
        return spg.get_orbit([0.5, 0.5, 0.5])
    elif letter == 'e':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'f':
        return spg.get_orbit([0.5, 0.5, rand()])
    elif letter == 'g':
        return spg.get_orbit([0., 0.5, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_82_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    spg = SpaceGroup('I-4')
    if not letter in letters_selection:
        raise ValueError("It is not a I-4 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([0., 0.5, 0.25])
    elif letter == 'd':
        return spg.get_orbit([0., 0.5, 0.75])
    elif letter == 'e':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'f':
        return spg.get_orbit([0., 0.5, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_83_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    spg = SpaceGroup('P4/m')
    if not letter in letters_selection:
        raise ValueError("It is not a P4/m wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([0.5, 0.5, 0.])
    elif letter == 'd':
        return spg.get_orbit([0.5, 0.5, 0.5])
    elif letter == 'e':
        return spg.get_orbit([0., 0.5, 0.])
    elif letter == 'f':
        return spg.get_orbit([0., 0.5, 0.5])
    elif letter == 'g':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'h':
        return spg.get_orbit([0.5, 0.5, rand()])
    elif letter == 'i':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'j':
        return spg.get_orbit([rand(), rand(), 0.])
    elif letter == 'k':
        return spg.get_orbit([rand(), rand(), 0.5])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_84_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    spg = SpaceGroup('P4_2/m')
    if not letter in letters_selection:
        raise ValueError("It is not a P4_2/m wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0.5, 0.])
    elif letter == 'c':
        return spg.get_orbit([0., 0.5, 0.])
    elif letter == 'd':
        return spg.get_orbit([0., 0.5, 0.5])
    elif letter == 'e':
        return spg.get_orbit([0., 0., 0.25])
    elif letter == 'f':
        return spg.get_orbit([0.5, 0.5, 0.25])
    elif letter == 'g':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'h':
        return spg.get_orbit([0.5, 0.5, rand()])
    elif letter == 'i':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'j':
        return spg.get_orbit([rand(), rand(), 0.])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_85_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    spg = SpaceGroup('P4/n')
    if not letter in letters_selection:
        raise ValueError("It is not a P4/n wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'd':
        return spg.get_orbit([0.25, 0.25, 0.])
    elif letter == 'e':
        return spg.get_orbit([0.25, 0.25, 0.5])
    elif letter == 'f':
        return spg.get_orbit([0., 0., rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_86_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    spg = SpaceGroup('P4_2/n')
    if not letter in letters_selection:
        raise ValueError("It is not a P4_2/n wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([0.25, 0.25, 0.25])
    elif letter == 'd':
        return spg.get_orbit([0.25, 0.25, 0.75])
    elif letter == 'e':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'f':
        return spg.get_orbit([0., 0., rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_87_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    spg = SpaceGroup('I4/m')
    if not letter in letters_selection:
        raise ValueError("It is not a I4/m wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([0., 0.5, 0.])
    elif letter == 'd':
        return spg.get_orbit([0., 0.5, 0.25])
    elif letter == 'e':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'f':
        return spg.get_orbit([0.25, 0.25, 0.25])
    elif letter == 'g':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'h':
        return spg.get_orbit([rand(), rand(), 0.])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_88_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f']
    spg = SpaceGroup('I4_1/a')
    if not letter in letters_selection:
        raise ValueError("It is not a I4_1/a wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([0., 0.25, 0.125])
    elif letter == 'd':
        return spg.get_orbit([0., 0.25, 0.625])
    elif letter == 'e':
        return spg.get_orbit([0., 0., rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_89_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    spg = SpaceGroup('P422')
    if not letter in letters_selection:
        raise ValueError("It is not a P422 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([0.5, 0.5, 0.])
    elif letter == 'd':
        return spg.get_orbit([0.5, 0.5, 0.5])
    elif letter == 'e':
        return spg.get_orbit([0.5, 0., 0.])
    elif letter == 'f':
        return spg.get_orbit([0.5, 0., 0.5])
    elif letter == 'g':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'h':
        return spg.get_orbit([0.5, 0.5, rand()])
    elif letter == 'i':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'j':
        x = rand()
        return spg.get_orbit([x, x, 0.])
    elif letter == 'k':
        x = rand()
        return spg.get_orbit([x, x, 0.5])
    elif letter == 'l':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'm':
        return spg.get_orbit([rand(), 0.5, 0.5])
    elif letter == 'n':
        return spg.get_orbit([rand(), 0., 0.5])
    elif letter == 'o':
        return spg.get_orbit([rand(), 0.5, 0.])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_90_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    spg = SpaceGroup('P42_12')
    if not letter in letters_selection:
        raise ValueError("It is not a P42_12 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'd':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'e':
        x = rand()
        return spg.get_orbit([x, x, 0.])
    elif letter == 'f':
        x = rand()
        return spg.get_orbit([x, x, 0.5])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_91_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd']
    spg = SpaceGroup('P4_122')
    if not letter in letters_selection:
        raise ValueError("It is not a P4_122 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., rand(), 0.])
    elif letter == 'b':
        return spg.get_orbit([0.5, rand(), 0.])
    elif letter == 'c':
        x = rand()
        return spg.get_orbit([x, x, 0.375])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_92_pos(letter):
    letters_selection = ['a', 'b']
    spg = SpaceGroup('P4_12_12')
    if not letter in letters_selection:
        raise ValueError("It is not a P4_12_12 wyckoff position!")
    elif letter == 'a':
        x = rand()
        return spg.get_orbit([x, x, 0.])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_93_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    spg = SpaceGroup('P4_222')
    if not letter in letters_selection:
        raise ValueError("It is not a P4_222 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0.5, 0.])
    elif letter == 'c':
        return spg.get_orbit([0., 0.5, 0.])
    elif letter == 'd':
        return spg.get_orbit([0., 0.5, 0.5])
    elif letter == 'e':
        return spg.get_orbit([0., 0., 0.25])
    elif letter == 'f':
        return spg.get_orbit([0.5, 0.5, 0.25])
    elif letter == 'g':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'h':
        return spg.get_orbit([0.5, 0.5, rand()])
    elif letter == 'i':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'j':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'k':
        return spg.get_orbit([rand(), 0.5, 0.5])
    elif letter == 'l':
        return spg.get_orbit([rand(), 0., 0.5])
    elif letter == 'm':
        return spg.get_orbit([rand(), 0.5, 0.])
    elif letter == 'n':
        x = rand()
        return spg.get_orbit([x, x, 0.25])
    elif letter == 'o':
        x = rand()
        return spg.get_orbit([x, x, 0.75])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_94_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    spg = SpaceGroup('P4_22_12')
    if not letter in letters_selection:
        raise ValueError("It is not a P4_22_12 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'd':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'e':
        x = rand()
        return spg.get_orbit([x, x, 0.])
    elif letter == 'f':
        x = rand()
        return spg.get_orbit([x, x, 0.5])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_95_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd']
    spg = SpaceGroup('P4_322')
    if not letter in letters_selection:
        raise ValueError("It is not a P4_322 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., rand(), 0.])
    elif letter == 'b':
        return spg.get_orbit([0.5, rand(), 0.])
    elif letter == 'c':
        x = rand()
        return spg.get_orbit([x, x, 0.625])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_96_pos(letter):
    letters_selection = ['a', 'b']
    spg = SpaceGroup('P4_32_12')
    if not letter in letters_selection:
        raise ValueError("It is not a P4_32_12 wyckoff position!")
    elif letter == 'a':
        x = rand()
        return spg.get_orbit([x, x, 0.])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_97_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    spg = SpaceGroup('I422')
    if not letter in letters_selection:
        raise ValueError("It is not a I422 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([0., 0.5, 0.])
    elif letter == 'd':
        return spg.get_orbit([0., 0.5, 0.25])
    elif letter == 'e':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'f':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'g':
        x = rand()
        return spg.get_orbit([x, x, 0.])
    elif letter == 'h':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'i':
        return spg.get_orbit([rand(), 0., 0.5])
    elif letter == 'j':
        x = rand()
        return spg.get_orbit([x, x - 0.5 if x >= 0.5 else x + 0.5, 0.25])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_98_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    spg = SpaceGroup('I4_122')
    if not letter in letters_selection:
        raise ValueError("It is not a I4_122 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'd':
        x = rand()
        return spg.get_orbit([x, x, 0.])
    elif letter == 'e':
        x = rand()
        return spg.get_orbit([-x, x, 0.])
    elif letter == 'f':
        return spg.get_orbit([rand(), 0.25, 0.125])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_99_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    spg = SpaceGroup('P4mm')
    if not letter in letters_selection:
        raise ValueError("It is not a P4mm wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0.5, rand()])
    elif letter == 'c':
        return spg.get_orbit([0.5, 0., rand()])
    elif letter == 'd':
        x = rand()
        return spg.get_orbit([x, x, rand()])
    elif letter == 'e':
        return spg.get_orbit([rand(), 0., rand()])
    elif letter == 'f':
        return spg.get_orbit([rand(), 0.5, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_100_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd']
    spg = SpaceGroup('P4bm')
    if not letter in letters_selection:
        raise ValueError("It is not a P4bm wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0., rand()])
    elif letter == 'c':
        x = rand()
        return spg.get_orbit([x, x - 0.5 if x >= 0.5 else x + 0.5, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_101_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e']
    spg = SpaceGroup('P4_2cm')
    if not letter in letters_selection:
        raise ValueError("It is not a P4_2cm wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0.5, rand()])
    elif letter == 'c':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'd':
        x = rand()
        return spg.get_orbit([x, x, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_102_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd']
    spg = SpaceGroup('P4_2nm')
    if not letter in letters_selection:
        raise ValueError("It is not a P4_2nm wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'b':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'c':
        x = rand()
        return spg.get_orbit([x, x, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_103_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd']
    spg = SpaceGroup('P4cc')
    if not letter in letters_selection:
        raise ValueError("It is not a P4cc wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0.5, rand()])
    elif letter == 'c':
        return spg.get_orbit([0., 0.5, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_104_pos(letter):
    letters_selection = ['a', 'b', 'c']
    spg = SpaceGroup('P4nc')
    if not letter in letters_selection:
        raise ValueError("It is not a P4nc wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'b':
        return spg.get_orbit([0., 0.5, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_105_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f']
    spg = SpaceGroup('P4_2mc')
    if not letter in letters_selection:
        raise ValueError("It is not a P4_2mc wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0.5, rand()])
    elif letter == 'c':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'd':
        return spg.get_orbit([rand(), 0., rand()])
    elif letter == 'e':
        return spg.get_orbit([rand(), 0.5, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_106_pos(letter):
    letters_selection = ['a', 'b', 'c']
    spg = SpaceGroup('P4_2bc')
    if not letter in letters_selection:
        raise ValueError("It is not a P4_2bc wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'b':
        return spg.get_orbit([0., 0.5, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_107_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e']
    spg = SpaceGroup('I4mm')
    if not letter in letters_selection:
        raise ValueError("It is not a I4mm wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'b':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'c':
        x = rand()
        return spg.get_orbit([x, x, rand()])
    elif letter == 'd':
        return spg.get_orbit([rand(), 0., rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_108_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd']
    spg = SpaceGroup('I4cm')
    if not letter in letters_selection:
        raise ValueError("It is not a I4cm wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0., rand()])
    elif letter == 'c':
        x = rand()
        return spg.get_orbit([x, x - 0.5 if x >= 0.5 else x + 0.5, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_109_pos(letter):
    letters_selection = ['a', 'b', 'c']
    spg = SpaceGroup('I4_1md')
    if not letter in letters_selection:
        raise ValueError("It is not a I4_1md wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'b':
        return spg.get_orbit([0., rand(), rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_110_pos(letter):
    letters_selection = ['a', 'b']
    spg = SpaceGroup('I4_1cd')
    if not letter in letters_selection:
        raise ValueError("It is not a I4_1cd wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_111_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
    spg = SpaceGroup('P-42m')
    if not letter in letters_selection:
        raise ValueError("It is not a P-42m wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0.5, 0.5])
    elif letter == 'c':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'd':
        return spg.get_orbit([0.5, 0.5, 0.])
    elif letter == 'e':
        return spg.get_orbit([0.5, 0., 0.])
    elif letter == 'f':
        return spg.get_orbit([0.5, 0., 0.5])
    elif letter == 'g':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'h':
        return spg.get_orbit([0.5, 0.5, rand()])
    elif letter == 'i':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'j':
        return spg.get_orbit([rand(), 0.5, 0.5])
    elif letter == 'k':
        return spg.get_orbit([rand(), 0., 0.5])
    elif letter == 'l':
        return spg.get_orbit([rand(), 0.5, 0.])
    elif letter == 'm':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'n':
        x = rand()
        return spg.get_orbit([x, x, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_112_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
    spg = SpaceGroup('P-42c')
    if not letter in letters_selection:
        raise ValueError("It is not a P-42c wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.25])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0., 0.25])
    elif letter == 'c':
        return spg.get_orbit([0.5, 0.5, 0.25])
    elif letter == 'd':
        return spg.get_orbit([0., 0.5, 0.25])
    elif letter == 'e':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'f':
        return spg.get_orbit([0.5, 0.5, 0.])
    elif letter == 'g':
        return spg.get_orbit([rand(), 0., 0.25])
    elif letter == 'h':
        return spg.get_orbit([0.5, rand(), 0.25])
    elif letter == 'i':
        return spg.get_orbit([rand(), 0.5, 0.25])
    elif letter == 'j':
        return spg.get_orbit([0., rand(), 0.25])
    elif letter == 'k':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'l':
        return spg.get_orbit([0.5, 0.5, rand()])
    elif letter == 'm':
        return spg.get_orbit([0., 0.5, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_113_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f']
    spg = SpaceGroup('P-42_1m')
    if not letter in letters_selection:
        raise ValueError("It is not a P-42_1m wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'd':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'e':
        x = rand()
        return spg.get_orbit([x, x - 0.5 if x >= 0.5 else x + 0.5, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_114_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e']
    spg = SpaceGroup('P-42_1c')
    if not letter in letters_selection:
        raise ValueError("It is not a P-42_1c wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'd':
        return spg.get_orbit([0., 0.5, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_115_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    spg = SpaceGroup('P-4m2')
    if not letter in letters_selection:
        raise ValueError("It is not a P-4m2 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0.5, 0.])
    elif letter == 'c':
        return spg.get_orbit([0.5, 0.5, 0.5])
    elif letter == 'd':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'e':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'f':
        return spg.get_orbit([0.5, 0.5, rand()])
    elif letter == 'g':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'h':
        x = rand()
        return spg.get_orbit([x, x, 0.])
    elif letter == 'i':
        x = rand()
        return spg.get_orbit([x, x, 0.5])
    elif letter == 'j':
        return spg.get_orbit([rand(), 0., rand()])
    elif letter == 'k':
        return spg.get_orbit([rand(), 0.5, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_116_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    spg = SpaceGroup('P-4c2')
    if not letter in letters_selection:
        raise ValueError("It is not a P-4c2 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.25])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0.5, 0.25])
    elif letter == 'c':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'd':
        return spg.get_orbit([0.5, 0.5, 0.])
    elif letter == 'e':
        x = rand()
        return spg.get_orbit([x, x, 0.25])
    elif letter == 'f':
        x = rand()
        return spg.get_orbit([x, x, 0.75])
    elif letter == 'g':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'h':
        return spg.get_orbit([0.5, 0.5, rand()])
    elif letter == 'i':
        return spg.get_orbit([0., 0.5, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_117_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    spg = SpaceGroup('P-4b2')
    if not letter in letters_selection:
        raise ValueError("It is not a P-4b2 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([0., 0.5, 0.])
    elif letter == 'd':
        return spg.get_orbit([0., 0.5, 0.5])
    elif letter == 'e':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'f':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'g':
        x = rand()
        return spg.get_orbit([x, x - 0.5 if x >= 0.5 else x + 0.5, 0.])
    elif letter == 'h':
        x = rand()
        return spg.get_orbit([x, x - 0.5 if x >= 0.5 else x + 0.5, 0.5])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_118_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    spg = SpaceGroup('P-4n2')
    if not letter in letters_selection:
        raise ValueError("It is not a P-4n2 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([0., 0.5, 0.25])
    elif letter == 'd':
        return spg.get_orbit([0., 0.5, 0.75])
    elif letter == 'e':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'f':
        x = rand()
        return spg.get_orbit([x, -x + 0.5 if x <= 0.5 else -x + 1.5, 0.25])
    elif letter == 'g':
        x = rand()
        return spg.get_orbit([x, x - 0.5 if x >= 0.5 else x + 0.5, 0.])
    elif letter == 'h':
        return spg.get_orbit([0., 0.5, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_119_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    spg = SpaceGroup('I-4m2')
    if not letter in letters_selection:
        raise ValueError("It is not a I-4m2 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([0., 0.5, 0.25])
    elif letter == 'd':
        return spg.get_orbit([0., 0.5, 0.75])
    elif letter == 'e':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'f':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'g':
        x = rand()
        return spg.get_orbit([x, x, 0.])
    elif letter == 'h':
        x = rand()
        return spg.get_orbit([x, x - 0.5 if x >= 0.5 else x + 0.5, 0.25])
    elif letter == 'i':
        return spg.get_orbit([rand(), 0., rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_120_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    spg = SpaceGroup('I-4c2')
    if not letter in letters_selection:
        raise ValueError("It is not a I-4c2 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.25])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'c':
        return spg.get_orbit([0., 0.5, 0.25])
    elif letter == 'd':
        return spg.get_orbit([0., 0.5, 0.])
    elif letter == 'e':
        x = rand()
        return spg.get_orbit([x, x, 0.25])
    elif letter == 'f':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'g':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'h':
        x = rand()
        return spg.get_orbit([x, x - 0.5 if x >= 0.5 else x + 0.5, 0.])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_121_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    spg = SpaceGroup('I-42m')
    if not letter in letters_selection:
        raise ValueError("It is not a I-42m wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([0., 0.5, 0.])
    elif letter == 'd':
        return spg.get_orbit([0., 0.5, 0.25])
    elif letter == 'e':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'f':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'g':
        return spg.get_orbit([rand(), 0., 0.5])
    elif letter == 'h':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'i':
        x = rand()
        return spg.get_orbit([x, x, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_122_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e']
    spg = SpaceGroup('I-42d')
    if not letter in letters_selection:
        raise ValueError("It is not a I-42d wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'd':
        return spg.get_orbit([rand(), 0.25, 0.125])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_123_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u']
    spg = SpaceGroup('P4/mmm')
    if not letter in letters_selection:
        raise ValueError("It is not a P4/mmm wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([0.5, 0.5, 0.])
    elif letter == 'd':
        return spg.get_orbit([0.5, 0.5, 0.5])
    elif letter == 'e':
        return spg.get_orbit([0., 0.5, 0.5])
    elif letter == 'f':
        return spg.get_orbit([0., 0.5, 0.])
    elif letter == 'g':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'h':
        return spg.get_orbit([0.5, 0.5, rand()])
    elif letter == 'i':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'j':
        x = rand()
        return spg.get_orbit([x, x, 0.])
    elif letter == 'k':
        x = rand()
        return spg.get_orbit([x, x, 0.5])
    elif letter == 'l':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'm':
        return spg.get_orbit([rand(), 0., 0.5])
    elif letter == 'n':
        return spg.get_orbit([rand(), 0.5, 0.])
    elif letter == 'o':
        return spg.get_orbit([rand(), 0.5, 0.5])
    elif letter == 'p':
        return spg.get_orbit([rand(), rand(), 0.])
    elif letter == 'q':
        return spg.get_orbit([rand(), rand(), 0.5])
    elif letter == 'r':
        x = rand()
        return spg.get_orbit([x, x, rand()])
    elif letter == 's':
        return spg.get_orbit([rand(), 0., rand()])
    elif letter == 't':
        return spg.get_orbit([rand(), 0.5, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_124_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
    spg = SpaceGroup('P4/mcc')
    if not letter in letters_selection:
        raise ValueError("It is not a P4/mcc wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.25])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'c':
        return spg.get_orbit([0.5, 0.5, 0.25])
    elif letter == 'd':
        return spg.get_orbit([0.5, 0.5, 0.])
    elif letter == 'e':
        return spg.get_orbit([0., 0.5, 0.])
    elif letter == 'f':
        return spg.get_orbit([0., 0.5, 0.25])
    elif letter == 'g':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'h':
        return spg.get_orbit([0.5, 0.5, rand()])
    elif letter == 'i':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'j':
        x = rand()
        return spg.get_orbit([x, x, 0.25])
    elif letter == 'k':
        return spg.get_orbit([rand(), 0., 0.25])
    elif letter == 'l':
        return spg.get_orbit([rand(), 0.5, 0.25])
    elif letter == 'm':
        return spg.get_orbit([rand(), rand(), 0.])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_125_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
    spg = SpaceGroup('P4/nbm')
    if not letter in letters_selection:
        raise ValueError("It is not a P4/nbm wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([0., 0.5, 0.])
    elif letter == 'd':
        return spg.get_orbit([0., 0.5, 0.5])
    elif letter == 'e':
        return spg.get_orbit([0.25, 0.25, 0.])
    elif letter == 'f':
        return spg.get_orbit([0.25, 0.25, 0.5])
    elif letter == 'g':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'h':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'i':
        x = rand()
        return spg.get_orbit([x, x, 0.])
    elif letter == 'j':
        x = rand()
        return spg.get_orbit([x, x, 0.5])
    elif letter == 'k':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'l':
        return spg.get_orbit([rand(), 0., 0.5])
    elif letter == 'm':
        x = rand()
        return spg.get_orbit([x, x - 0.5 if x >= 0.5 else x + 0.5, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_126_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    spg = SpaceGroup('P4/nnc')
    if not letter in letters_selection:
        raise ValueError("It is not a P4/nnc wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([0.5, 0., 0.])
    elif letter == 'd':
        return spg.get_orbit([0.5, 0., 0.25])
    elif letter == 'e':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'f':
        return spg.get_orbit([0.25, 0.25, 0.25])
    elif letter == 'g':
        return spg.get_orbit([0.5, 0., rand()])
    elif letter == 'h':
        x = rand()
        return spg.get_orbit([x, x, 0.])
    elif letter == 'i':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'j':
        return spg.get_orbit([rand(), 0., 0.5])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_127_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    spg = SpaceGroup('P4/mbm')
    if not letter in letters_selection:
        raise ValueError("It is not a P4/mbm wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([0., 0.5, 0.5])
    elif letter == 'd':
        return spg.get_orbit([0., 0.5, 0.])
    elif letter == 'e':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'f':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'g':
        x = rand()
        return spg.get_orbit([x, x - 0.5 if x >= 0.5 else x + 0.5, 0.])
    elif letter == 'h':
        x = rand()
        return spg.get_orbit([x, x - 0.5 if x >= 0.5 else x + 0.5, 0.5])
    elif letter == 'i':
        return spg.get_orbit([rand(), rand(), 0.])
    elif letter == 'j':
        return spg.get_orbit([rand(), rand(), 0.5])
    elif letter == 'k':
        x = rand()
        return spg.get_orbit([x, x - 0.5 if x >= 0.5 else x + 0.5, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_128_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    spg = SpaceGroup('P4/mnc')
    if not letter in letters_selection:
        raise ValueError("It is not a P4/mnc wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([0., 0.5, 0.])
    elif letter == 'd':
        return spg.get_orbit([0., 0.5, 0.25])
    elif letter == 'e':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'f':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'g':
        x = rand()
        return spg.get_orbit([x, x - 0.5 if x >= 0.5 else x + 0.5, 0.25])
    elif letter == 'h':
        return spg.get_orbit([rand(), rand(), 0.])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_129_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    spg = SpaceGroup('P4/nmm')
    if not letter in letters_selection:
        raise ValueError("It is not a P4/nmm wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'd':
        return spg.get_orbit([0.25, 0.25, 0.])
    elif letter == 'e':
        return spg.get_orbit([0.25, 0.25, 0.5])
    elif letter == 'f':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'g':
        x = rand()
        return spg.get_orbit([x, x, 0.])
    elif letter == 'h':
        x = rand()
        return spg.get_orbit([x, x, 0.5])
    elif letter == 'i':
        return spg.get_orbit([0., rand(), rand()])
    elif letter == 'j':
        x = rand()
        return spg.get_orbit([x, x - 0.5 if x >= 0.5 else x + 0.5, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_130_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    spg = SpaceGroup('P4/ncc')
    if not letter in letters_selection:
        raise ValueError("It is not a P4/ncc wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.25])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'c':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'd':
        return spg.get_orbit([0.25, 0.25, 0.])
    elif letter == 'e':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'f':
        x = rand()
        return spg.get_orbit([x, x, 0.25])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_131_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r']
    spg = SpaceGroup('P4_2/mmc')
    if not letter in letters_selection:
        raise ValueError("It is not a P4_2/mmc wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0.5, 0.])
    elif letter == 'c':
        return spg.get_orbit([0., 0.5, 0.])
    elif letter == 'd':
        return spg.get_orbit([0., 0.5, 0.5])
    elif letter == 'e':
        return spg.get_orbit([0., 0., 0.25])
    elif letter == 'f':
        return spg.get_orbit([0.5, 0.5, 0.25])
    elif letter == 'g':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'h':
        return spg.get_orbit([0.5, 0.5, rand()])
    elif letter == 'i':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'j':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'k':
        return spg.get_orbit([rand(), 0.5, 0.5])
    elif letter == 'l':
        return spg.get_orbit([rand(), 0., 0.5])
    elif letter == 'm':
        return spg.get_orbit([rand(), 0.5, 0.])
    elif letter == 'n':
        x = rand()
        return spg.get_orbit([x, x, 0.25])
    elif letter == 'o':
        return spg.get_orbit([0., rand(), rand()])
    elif letter == 'p':
        return spg.get_orbit([0.5, rand(), rand()])
    elif letter == 'q':
        return spg.get_orbit([rand(), rand(), 0.])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_132_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    spg = SpaceGroup('P4_2/mcm')
    if not letter in letters_selection:
        raise ValueError("It is not a P4_2/mcm wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.25])
    elif letter == 'c':
        return spg.get_orbit([0.5, 0.5, 0.])
    elif letter == 'd':
        return spg.get_orbit([0.5, 0.5, 0.25])
    elif letter == 'e':
        return spg.get_orbit([0., 0.5, 0.25])
    elif letter == 'f':
        return spg.get_orbit([0., 0.5, 0.])
    elif letter == 'g':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'h':
        return spg.get_orbit([0.5, 0.5, rand()])
    elif letter == 'i':
        x = rand()
        return spg.get_orbit([x, x, 0.])
    elif letter == 'j':
        x = rand()
        return spg.get_orbit([x, x, 0.5])
    elif letter == 'k':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'l':
        return spg.get_orbit([rand(), 0., 0.25])
    elif letter == 'm':
        return spg.get_orbit([rand(), 0.5, 0.25])
    elif letter == 'n':
        return spg.get_orbit([rand(), rand(), 0.])
    elif letter == 'o':
        x = rand()
        return spg.get_orbit([x, x, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_133_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    spg = SpaceGroup('P4_2/nbc')
    if not letter in letters_selection:
        raise ValueError("It is not a P4_2/nbc wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0.5, 0.25])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.25])
    elif letter == 'c':
        return spg.get_orbit([0., 0.5, 0.])
    elif letter == 'd':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'e':
        return spg.get_orbit([0.25, 0.25, 0.25])
    elif letter == 'f':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'g':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'h':
        return spg.get_orbit([rand(), 0., 0.25])
    elif letter == 'i':
        return spg.get_orbit([rand(), 0., 0.75])
    elif letter == 'j':
        x = rand()
        return spg.get_orbit([x, x - 0.5 if x >= 0.5 else x + 0.5, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_134_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
    spg = SpaceGroup('P4_2/nnm')
    if not letter in letters_selection:
        raise ValueError("It is not a P4_2/nnm wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([0., 0.5, 0.])
    elif letter == 'd':
        return spg.get_orbit([0., 0.5, 0.25])
    elif letter == 'e':
        return spg.get_orbit([0.25, 0.25, 0.25])
    elif letter == 'f':
        return spg.get_orbit([0.75, 0.75, 0.75])
    elif letter == 'g':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'h':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'i':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'j':
        return spg.get_orbit([rand(), 0., 0.5])
    elif letter == 'k':
        x = rand()
        return spg.get_orbit([x, x - 0.5 if x >= 0.5 else x + 0.5, 0.25])
    elif letter == 'l':
        x = rand()
        return spg.get_orbit([x, x - 0.5 if x >= 0.5 else x + 0.5, 0.75])
    elif letter == 'm':
        x = rand()
        return spg.get_orbit([x, x, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_135_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    spg = SpaceGroup('P4_2/mbc')
    if not letter in letters_selection:
        raise ValueError("It is not a P4_2/mbc wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.25])
    elif letter == 'c':
        return spg.get_orbit([0., 0.5, 0.])
    elif letter == 'd':
        return spg.get_orbit([0., 0.5, 0.25])
    elif letter == 'e':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'f':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'g':
        x = rand()
        return spg.get_orbit([x, x - 0.5 if x >= 0.5 else x + 0.5, 0.25])
    elif letter == 'h':
        return spg.get_orbit([rand(), rand(), 0.])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_136_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    spg = SpaceGroup('P4_2/mnm')
    if not letter in letters_selection:
        raise ValueError("It is not a P4_2/mnm wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([0., 0.5, 0.])
    elif letter == 'd':
        return spg.get_orbit([0., 0.5, 0.25])
    elif letter == 'e':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'f':
        x = rand()
        return spg.get_orbit([x, x, 0.])
    elif letter == 'g':
        x = rand()
        return spg.get_orbit([x, 1 - x, 0.])
    elif letter == 'h':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'i':
        return spg.get_orbit([rand(), rand(), 0.])
    elif letter == 'j':
        x = rand()
        return spg.get_orbit([x, x, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_137_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    spg = SpaceGroup('P4_2/nmc')
    if not letter in letters_selection:
        raise ValueError("It is not a P4_2/nmc wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'd':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'e':
        return spg.get_orbit([0.25, 0.25, 0.25])
    elif letter == 'f':
        x = rand()
        return spg.get_orbit([x, x, 0.])
    elif letter == 'g':
        return spg.get_orbit([0., rand(), rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_138_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    spg = SpaceGroup('P4_2/ncm')
    if not letter in letters_selection:
        raise ValueError("It is not a P4_2/ncm wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.25])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'c':
        return spg.get_orbit([0.25, 0.25, 0.25])
    elif letter == 'd':
        return spg.get_orbit([0.25, 0.25, 0.75])
    elif letter == 'e':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'f':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'g':
        x = rand()
        return spg.get_orbit([x, x, 0.25])
    elif letter == 'h':
        x = rand()
        return spg.get_orbit([x, x, 0.75])
    elif letter == 'i':
        x = rand()
        return spg.get_orbit([x, x - 0.5 if x >= 0.5 else x + 0.5, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_139_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
    spg = SpaceGroup('I4/mmm')
    if not letter in letters_selection:
        raise ValueError("It is not a I4/mmm wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([0., 0.5, 0.])
    elif letter == 'd':
        return spg.get_orbit([0., 0.5, 0.25])
    elif letter == 'e':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'f':
        return spg.get_orbit([0.25, 0.25, 0.25])
    elif letter == 'g':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'h':
        x = rand()
        return spg.get_orbit([x, x, 0.])
    elif letter == 'i':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'j':
        return spg.get_orbit([rand(), 0.5, 0.])
    elif letter == 'k':
        x = rand()
        return spg.get_orbit([x, x - 0.5 if x >= 0.5 else x + 0.5, 0.25])
    elif letter == 'l':
        return spg.get_orbit([rand(), rand(), 0.])
    elif letter == 'm':
        x = rand()
        return spg.get_orbit([x, x, rand()])
    elif letter == 'n':
        return spg.get_orbit([0., rand(), rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_140_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    spg = SpaceGroup('I4/mcm')
    if not letter in letters_selection:
        raise ValueError("It is not a I4/mcm wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.25])
    elif letter == 'b':
        return spg.get_orbit([0., 0.5, 0.25])
    elif letter == 'c':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'd':
        return spg.get_orbit([0., 0.5, 0.])
    elif letter == 'e':
        return spg.get_orbit([0.25, 0.25, 0.25])
    elif letter == 'f':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'g':
        return spg.get_orbit([0., 0.5, rand()])
    elif letter == 'h':
        x = rand()
        return spg.get_orbit([x, x - 0.5 if x >= 0.5 else x + 0.5, 0.])
    elif letter == 'i':
        x = rand()
        return spg.get_orbit([x, x, 0.25])
    elif letter == 'j':
        return spg.get_orbit([rand(), 0., 0.25])
    elif letter == 'k':
        return spg.get_orbit([rand(), rand(), 0.])
    elif letter == 'l':
        x = rand()
        return spg.get_orbit([x, x - 0.5 if x >= 0.5 else x + 0.5, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_141_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    spg = SpaceGroup('I4_1/amd')
    if not letter in letters_selection:
        raise ValueError("It is not a I4_1/amd wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([0., 0.25, 0.125])
    elif letter == 'd':
        return spg.get_orbit([0., 0.25, 0.625])
    elif letter == 'e':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'f':
        return spg.get_orbit([rand(), 0.25, 0.125])
    elif letter == 'g':
        x = rand()
        return spg.get_orbit([x, x, 0.])
    elif letter == 'h':
        return spg.get_orbit([0., rand(), rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_142_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    spg = SpaceGroup('I4_1/acd')
    if not letter in letters_selection:
        raise ValueError("It is not a I4_1/acd wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.25])
    elif letter == 'c':
        return spg.get_orbit([0., 0.25, 0.125])
    elif letter == 'd':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'e':
        return spg.get_orbit([0.25, rand(), 0.125])
    elif letter == 'f':
        x = rand()
        return spg.get_orbit([x, x, 0.25])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_143_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd']
    spg = SpaceGroup('P3')
    if not letter in letters_selection:
        raise ValueError("It is not a P3 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'b':
        return spg.get_orbit([1./3, 2./3, rand()])
    elif letter == 'c':
        return spg.get_orbit([2./3, 1./3, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_144_pos(letter):
    letters_selection = ['a']
    spg = SpaceGroup('P3_1')
    if not letter in letters_selection:
        raise ValueError("It is not a P3_1 wyckoff position!")
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_145_pos(letter):
    letters_selection = ['a']
    spg = SpaceGroup('P3_2')
    if not letter in letters_selection:
        raise ValueError("It is not a P3_2 wyckoff position!")
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_146_pos_R(letter):
    letters_selection = ['a', 'b']
    spg = SpaceGroup('R3')
    if not letter in letters_selection:
        raise ValueError("It is not a R3 wyckoff position!")
    elif letter == 'a':
        x = rand()
        return spg.get_orbit([x, x, x])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_146_pos_H(letter):
    letters_selection = ['a', 'b']
    spg = SpaceGroup('R3H')
    if not letter in letters_selection:
        raise ValueError("It is not a R3H wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_147_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    spg = SpaceGroup('P-3')
    if not letter in letters_selection:
        raise ValueError("It is not a P-3 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'd':
        return spg.get_orbit([1./3, 2./3, rand()])
    elif letter == 'e':
        return spg.get_orbit([0.5, 0., 0.])
    elif letter == 'f':
        return spg.get_orbit([0.5, 0., 0.5])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_148_pos_R(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f']
    spg = SpaceGroup('R-3')
    if not letter in letters_selection:
        raise ValueError("It is not a R-3 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0.5, 0.5])
    elif letter == 'c':
        x = rand()
        return spg.get_orbit([x, x, x])
    elif letter == 'd':
        return spg.get_orbit([0.5, 0., 0.])
    elif letter == 'e':
        return spg.get_orbit([0., 0.5, 0.5])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_148_pos_H(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f']
    spg = SpaceGroup('R-3')
    if not letter in letters_selection:
        raise ValueError("It is not a R-3 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'd':
        return spg.get_orbit([0.5, 0., 0.5])
    elif letter == 'e':
        return spg.get_orbit([0.5, 0., 0.])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_149_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    spg = SpaceGroup('P312')
    if not letter in letters_selection:
        raise ValueError("It is not a P312 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([1./3, 2./3, 0.])
    elif letter == 'd':
        return spg.get_orbit([1./3, 2./3, 0.5])
    elif letter == 'e':
        return spg.get_orbit([2./3, 1./3, 0.])
    elif letter == 'f':
        return spg.get_orbit([2./3, 1./3, 0.5])
    elif letter == 'g':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'h':
        return spg.get_orbit([1./3, 2./3, rand()])
    elif letter == 'i':
        return spg.get_orbit([2./3, 1./3, rand()])
    elif letter == 'j':
        x = rand()
        return spg.get_orbit([x, 1 - x, 0.])
    elif letter == 'k':
        x = rand()
        return spg.get_orbit([x, 1 - x, 0.5])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_150_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    spg = SpaceGroup('P321')
    if not letter in letters_selection:
        raise ValueError("It is not a P321 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'd':
        return spg.get_orbit([1./3, 2./3, rand()])
    elif letter == 'e':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'f':
        return spg.get_orbit([rand(), 0., 0.5])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_151_pos(letter):
    letters_selection = ['a', 'b', 'c']
    spg = SpaceGroup('P3_112')
    if not letter in letters_selection:
        raise ValueError("It is not a P3_112 wyckoff position!")
    elif letter == 'a':
        x = rand()
        return spg.get_orbit([x, 1 - x, 1./3])
    elif letter == 'b':
        x = rand()
        return spg.get_orbit([x, 1 - x, 5./6])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_152_pos(letter):
    letters_selection = ['a', 'b', 'c']
    spg = SpaceGroup('P3_121')
    if not letter in letters_selection:
        raise ValueError("It is not a P3_121 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([rand(), 0., 1./3])
    elif letter == 'b':
        return spg.get_orbit([rand(), 0., 5./6])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_153_pos(letter):
    letters_selection = ['a', 'b', 'c']
    spg = SpaceGroup('P3_212')
    if not letter in letters_selection:
        raise ValueError("It is not a P3_212 wyckoff position!")
    elif letter == 'a':
        x = rand()
        return spg.get_orbit([x, 1 - x, 2./3])
    elif letter == 'b':
        x = rand()
        return spg.get_orbit([x, 1 - x, 1./6])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_154_pos(letter):
    letters_selection = ['a', 'b', 'c']
    spg = SpaceGroup('P3_221')
    if not letter in letters_selection:
        raise ValueError("It is not a P3_221 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([rand(), 0., 2./3])
    elif letter == 'b':
        return spg.get_orbit([rand(), 0., 1./6])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_155_pos_R(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f']
    spg = SpaceGroup('R32')
    if not letter in letters_selection:
        raise ValueError("It is not a R32 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0.5, 0.5])
    elif letter == 'c':
        x = rand()
        return spg.get_orbit([x, x, x])
    elif letter == 'd':
        y = rand()
        return spg.get_orbit([0., y, 1 - y])
    elif letter == 'e':
        y = rand()
        return spg.get_orbit([0.5, y, 1 - y])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_155_pos_H(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f']
    spg = SpaceGroup('R32H')
    if not letter in letters_selection:
        raise ValueError("It is not a R32H wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'd':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'e':
        return spg.get_orbit([rand(), 0., 0.5])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_156_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e']
    spg = SpaceGroup('P3m1')
    if not letter in letters_selection:
        raise ValueError("It is not a P3m1 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'b':
        return spg.get_orbit([1./3, 2./3, rand()])
    elif letter == 'c':
        return spg.get_orbit([2./3, 1./3, rand()])
    elif letter == 'd':
        x = rand()
        return spg.get_orbit([x, 1 - x, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_157_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd']
    spg = SpaceGroup('P31m')
    if not letter in letters_selection:
        raise ValueError("It is not a P31m wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'b':
        return spg.get_orbit([1./3, 2./3, rand()])
    elif letter == 'c':
        return spg.get_orbit([rand(), 0., rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_158_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd']
    spg = SpaceGroup('P3c1')
    if not letter in letters_selection:
        raise ValueError("It is not a P3c1 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'b':
        return spg.get_orbit([1./3, 2./3, rand()])
    elif letter == 'c':
        return spg.get_orbit([2./3, 1./3, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_159_pos(letter):
    letters_selection = ['a', 'b', 'c']
    spg = SpaceGroup('P31c')
    if not letter in letters_selection:
        raise ValueError("It is not a P31c wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'b':
        return spg.get_orbit([1./3, 2./3, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_160_pos_R(letter):
    letters_selection = ['a', 'b', 'c']
    spg = SpaceGroup('R3m')
    if not letter in letters_selection:
        raise ValueError("It is not a R3m wyckoff position!")
    elif letter == 'a':
        x = rand()
        return spg.get_orbit([x, x, x])
    elif letter == 'b':
        x = rand()
        return spg.get_orbit([x, x, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_160_pos_H(letter):
    letters_selection = ['a', 'b', 'c']
    spg = SpaceGroup('R3mH')
    if not letter in letters_selection:
        raise ValueError("It is not a R3mH wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'b':
        x = rand()
        return spg.get_orbit([x, 1 - x, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_161_pos_R(letter):
    letters_selection = ['a', 'b']
    spg = SpaceGroup('R3c')
    if not letter in letters_selection:
        raise ValueError("It is not a R3c wyckoff position!")
    elif letter == 'a':
        x = rand()
        return spg.get_orbit([x, x, x])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_161_pos_H(letter):
    letters_selection = ['a', 'b']
    spg = SpaceGroup('R3cH')
    if not letter in letters_selection:
        raise ValueError("It is not a R3cH wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_162_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    spg = SpaceGroup('P-31m')
    if not letter in letters_selection:
        raise ValueError("It is not a P-31m wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([1./3, 2./3, 0.])
    elif letter == 'd':
        return spg.get_orbit([1./3, 2./3, 0.5])
    elif letter == 'e':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'f':
        return spg.get_orbit([0.5, 0., 0.])
    elif letter == 'g':
        return spg.get_orbit([0.5, 0., 0.5])
    elif letter == 'h':
        return spg.get_orbit([1./3, 2./3, rand()])
    elif letter == 'i':
        x = rand()
        return spg.get_orbit([x, 1 - x, 0.])
    elif letter == 'j':
        x = rand()
        return spg.get_orbit([x, 1 - x, 0.5])
    elif letter == 'k':
        return spg.get_orbit([rand(), 0., rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_163_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    spg = SpaceGroup('P-31c')
    if not letter in letters_selection:
        raise ValueError("It is not a P-31c wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.25])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'c':
        return spg.get_orbit([1./3, 2./3, 0.25])
    elif letter == 'd':
        return spg.get_orbit([2./3, 1./3, 0.25])
    elif letter == 'e':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'f':
        return spg.get_orbit([1./3, 2./3, rand()])
    elif letter == 'g':
        return spg.get_orbit([0.5, 0., 0.])
    elif letter == 'h':
        x = rand()
        return spg.get_orbit([x, 1 - x, 0.25])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_164_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    spg = SpaceGroup('P-3m1')
    if not letter in letters_selection:
        raise ValueError("It is not a P-3m1 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'd':
        return spg.get_orbit([1./3, 2./3, rand()])
    elif letter == 'e':
        return spg.get_orbit([0.5, 0., 0.])
    elif letter == 'f':
        return spg.get_orbit([0.5, 0., 0.5])
    elif letter == 'g':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'h':
        return spg.get_orbit([rand(), 0., 0.5])
    elif letter == 'i':
        x = rand()
        return spg.get_orbit([x, 1 - x, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_165_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    spg = SpaceGroup('P-3c1')
    if not letter in letters_selection:
        raise ValueError("It is not a P-3c1 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.25])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'c':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'd':
        return spg.get_orbit([1./3, 2./3, rand()])
    elif letter == 'e':
        return spg.get_orbit([0.5, 0., 0.])
    elif letter == 'f':
        return spg.get_orbit([rand(), 0., 0.25])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_166_pos_R(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    spg = SpaceGroup('R-3m')
    if not letter in letters_selection:
        raise ValueError("It is not a R-3m wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0.5, 0.5])
    elif letter == 'c':
        x = rand()
        return spg.get_orbit([x, x, x])
    elif letter == 'd':
        return spg.get_orbit([0.5, 0., 0.])
    elif letter == 'e':
        return spg.get_orbit([0., 0.5, 0.5])
    elif letter == 'f':
        x = rand()
        return spg.get_orbit([x, 1 - x, 0.])
    elif letter == 'g':
        x = rand()
        return spg.get_orbit([x, 1 - x, 0.5])
    elif letter == 'h':
        x = rand()
        return spg.get_orbit([x, x, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_166_pos_H(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    spg = SpaceGroup('R-3mH')
    if not letter in letters_selection:
        raise ValueError("It is not a R-3mH wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'd':
        return spg.get_orbit([0.5, 0., 0.5])
    elif letter == 'e':
        return spg.get_orbit([0.5, 0., 0.])
    elif letter == 'f':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'g':
        return spg.get_orbit([rand(), 0., 0.5])
    elif letter == 'h':
        x = rand()
        return spg.get_orbit([x, 1 - x, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_167_pos_R(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f']
    spg = SpaceGroup('R-3c')
    if not letter in letters_selection:
        raise ValueError("It is not a R-3c wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0.25, 0.25, 0.25])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'c':
        x = rand()
        return spg.get_orbit([x, x, x])
    elif letter == 'd':
        return spg.get_orbit([0.5, 0., 0.])
    elif letter == 'e':
        x = rand()
        return spg.get_orbit([x, -x + 0.5 if x <= 0.5 else -x + 1.5, 0.25])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_167_pos_H(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f']
    spg = SpaceGroup('R-3cH')
    if not letter in letters_selection:
        raise ValueError("It is not a R-3cH wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.25])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'c':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'd':
        return spg.get_orbit([0.5, 0., 0.])
    elif letter == 'e':
        return spg.get_orbit([rand(), 0., 0.25])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_168_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd']
    spg = SpaceGroup('P6')
    if not letter in letters_selection:
        raise ValueError("It is not a P6 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'b':
        return spg.get_orbit([1./3, 2./3, rand()])
    elif letter == 'c':
        return spg.get_orbit([0.5, 0., rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_169_pos(letter):
    letters_selection = ['a']
    spg = SpaceGroup('P6_1')
    if not letter in letters_selection:
        raise ValueError("It is not a P6_1 wyckoff position!")
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_170_pos(letter):
    letters_selection = ['a']
    spg = SpaceGroup('P6_5')
    if not letter in letters_selection:
        raise ValueError("It is not a P6_5 wyckoff position!")
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_171_pos(letter):
    letters_selection = ['a', 'b', 'c']
    spg = SpaceGroup('P6_2')
    if not letter in letters_selection:
        raise ValueError("It is not a P6_2 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0.5, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_172_pos(letter):
    letters_selection = ['a', 'b', 'c']
    spg = SpaceGroup('P6_4')
    if not letter in letters_selection:
        raise ValueError("It is not a P6_4 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0.5, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_173_pos(letter):
    letters_selection = ['a', 'b', 'c']
    spg = SpaceGroup('P6_3')
    if not letter in letters_selection:
        raise ValueError("It is not a P6_3 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'b':
        return spg.get_orbit([1./3, 2./3, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_174_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    spg = SpaceGroup('P-6')
    if not letter in letters_selection:
        raise ValueError("It is not a P-6 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([1./3, 2./3, 0.])
    elif letter == 'd':
        return spg.get_orbit([1./3, 2./3, 0.5])
    elif letter == 'e':
        return spg.get_orbit([2./3, 1./3, 0.])
    elif letter == 'f':
        return spg.get_orbit([2./3, 1./3, 0.5])
    elif letter == 'g':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'h':
        return spg.get_orbit([1./3, 2./3, rand()])
    elif letter == 'i':
        return spg.get_orbit([2./3, 1./3, rand()])
    elif letter == 'j':
        return spg.get_orbit([rand(), rand(), 0.])
    elif letter == 'k':
        return spg.get_orbit([rand(), rand(), 0.5])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_175_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    spg = SpaceGroup('P6/m')
    if not letter in letters_selection:
        raise ValueError("It is not a P6/m wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([1./3, 2./3, 0.])
    elif letter == 'd':
        return spg.get_orbit([1./3, 2./3, 0.5])
    elif letter == 'e':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'f':
        return spg.get_orbit([0.5, 0., 0.])
    elif letter == 'g':
        return spg.get_orbit([0.5, 0., 0.5])
    elif letter == 'h':
        return spg.get_orbit([1./3, 2./3, rand()])
    elif letter == 'i':
        return spg.get_orbit([0.5, 0., rand()])
    elif letter == 'j':
        return spg.get_orbit([rand(), rand(), 0.])
    elif letter == 'k':
        return spg.get_orbit([rand(), rand(), 0.5])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_176_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    spg = SpaceGroup('P6_3/m')
    if not letter in letters_selection:
        raise ValueError("It is not a P6_3/m wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.25])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'c':
        return spg.get_orbit([1./3, 2./3, 0.25])
    elif letter == 'd':
        return spg.get_orbit([2./3, 1./3, 0.25])
    elif letter == 'e':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'f':
        return spg.get_orbit([1./3, 2./3, rand()])
    elif letter == 'g':
        return spg.get_orbit([0.5, 0., 0.])
    elif letter == 'h':
        return spg.get_orbit([rand(), rand(), 0.25])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_177_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
    spg = SpaceGroup('P622')
    if not letter in letters_selection:
        raise ValueError("It is not a P622 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([1./3, 2./3, 0.])
    elif letter == 'd':
        return spg.get_orbit([1./3, 2./3, 0.5])
    elif letter == 'e':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'f':
        return spg.get_orbit([0.5, 0., 0.])
    elif letter == 'g':
        return spg.get_orbit([0.5, 0., 0.5])
    elif letter == 'h':
        return spg.get_orbit([1./3, 2./3, rand()])
    elif letter == 'i':
        return spg.get_orbit([0.5, 0., rand()])
    elif letter == 'j':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'k':
        return spg.get_orbit([rand(), 0., 0.5])
    elif letter == 'l':
        x = rand()
        return spg.get_orbit([x, 1 - x, 0.])
    elif letter == 'm':
        x = rand()
        return spg.get_orbit([x, 1 - x, 0.5])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_178_pos(letter):
    letters_selection = ['a', 'b', 'c']
    spg = SpaceGroup('P6_122')
    if not letter in letters_selection:
        raise ValueError("It is not a P6_122 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'b':
        x = rand()
        return spg.get_orbit([x, 2 * x, 0.25])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_179_pos(letter):
    letters_selection = ['a', 'b', 'c']
    spg = SpaceGroup('P6_522')
    if not letter in letters_selection:
        raise ValueError("It is not a P6_522 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'b':
        x = rand()
        return spg.get_orbit([x, 2 * x, 0.75])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_180_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    spg = SpaceGroup('P6_222')
    if not letter in letters_selection:
        raise ValueError("It is not a P6_222 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([0.5, 0., 0.])
    elif letter == 'd':
        return spg.get_orbit([0.5, 0., 0.5])
    elif letter == 'e':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'f':
        return spg.get_orbit([0.5, 0., rand()])
    elif letter == 'g':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'h':
        return spg.get_orbit([rand(), 0., 0.5])
    elif letter == 'i':
        x = rand()
        return spg.get_orbit([x, 2 * x, 0.])
    elif letter == 'j':
        x = rand()
        return spg.get_orbit([x, 2 * x, 0.5])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_181_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    spg = SpaceGroup('P6_422')
    if not letter in letters_selection:
        raise ValueError("It is not a P6_422 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([0.5, 0., 0.])
    elif letter == 'd':
        return spg.get_orbit([0.5, 0., 0.5])
    elif letter == 'e':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'f':
        return spg.get_orbit([0.5, 0., rand()])
    elif letter == 'g':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'h':
        return spg.get_orbit([rand(), 0., 0.5])
    elif letter == 'i':
        x = rand()
        return spg.get_orbit([x, 2 * x, 0.])
    elif letter == 'j':
        x = rand()
        return spg.get_orbit([x, 2 * x, 0.5])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_182_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    spg = SpaceGroup('P6_322')
    if not letter in letters_selection:
        raise ValueError("It is not a P6_322 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.25])
    elif letter == 'c':
        return spg.get_orbit([1./3, 2./3, 0.25])
    elif letter == 'd':
        return spg.get_orbit([1./3, 2./3, 0.75])
    elif letter == 'e':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'f':
        return spg.get_orbit([1./3, 2./3, rand()])
    elif letter == 'g':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'h':
        x = rand()
        return spg.get_orbit([x, 2 * x, 0.25])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_183_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f']
    spg = SpaceGroup('P6mm')
    if not letter in letters_selection:
        raise ValueError("It is not a P6mm wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'b':
        return spg.get_orbit([1./3, 2./3, rand()])
    elif letter == 'c':
        return spg.get_orbit([0.5, 0., rand()])
    elif letter == 'd':
        return spg.get_orbit([rand(), 0., rand()])
    elif letter == 'e':
        x = rand()
        return spg.get_orbit([x, 1 - x, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_184_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd']
    spg = SpaceGroup('P6cc')
    if not letter in letters_selection:
        raise ValueError("It is not a P6cc wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'b':
        return spg.get_orbit([1./3, 2./3, rand()])
    elif letter == 'c':
        return spg.get_orbit([0.5, 0., rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_185_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd']
    spg = SpaceGroup('P6_3cm')
    if not letter in letters_selection:
        raise ValueError("It is not a P6_3cm wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'b':
        return spg.get_orbit([1./3, 2./3, rand()])
    elif letter == 'c':
        return spg.get_orbit([rand(), 0., rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_186_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd']
    spg = SpaceGroup('P6_3mc')
    if not letter in letters_selection:
        raise ValueError("It is not a P6_3mc wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'b':
        return spg.get_orbit([1./3, 2./3, rand()])
    elif letter == 'c':
        x = rand()
        return spg.get_orbit([x, 1 - x, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_187_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
    spg = SpaceGroup('P-6m2')
    if not letter in letters_selection:
        raise ValueError("It is not a P-6m2 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([1./3, 2./3, 0.])
    elif letter == 'd':
        return spg.get_orbit([1./3, 2./3, 0.5])
    elif letter == 'e':
        return spg.get_orbit([2./3, 1./3, 0.])
    elif letter == 'f':
        return spg.get_orbit([2./3, 1./3, 0.5])
    elif letter == 'g':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'h':
        return spg.get_orbit([1./3, 2./3, rand()])
    elif letter == 'i':
        return spg.get_orbit([2./3, 1./3, rand()])
    elif letter == 'j':
        x = rand()
        return spg.get_orbit([x, 1 - x, 0.])
    elif letter == 'k':
        x = rand()
        return spg.get_orbit([x, 1 - x, 0.5])
    elif letter == 'l':
        return spg.get_orbit([rand(), rand(), 0.])
    elif letter == 'm':
        return spg.get_orbit([rand(), rand(), 0.5])
    elif letter == 'n':
        x = rand()
        return spg.get_orbit([x, 1 - x, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_188_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    spg = SpaceGroup('P-6c2')
    if not letter in letters_selection:
        raise ValueError("It is not a P-6c2 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.25])
    elif letter == 'c':
        return spg.get_orbit([1./3, 2./3, 0.])
    elif letter == 'd':
        return spg.get_orbit([1./3, 2./3, 0.25])
    elif letter == 'e':
        return spg.get_orbit([2./3, 1./3, 0.])
    elif letter == 'f':
        return spg.get_orbit([2./3, 1./3, 0.25])
    elif letter == 'g':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'h':
        return spg.get_orbit([1./3, 2./3, rand()])
    elif letter == 'i':
        return spg.get_orbit([2./3, 1./3, rand()])
    elif letter == 'j':
        x = rand()
        return spg.get_orbit([x, 1 - x, 0.])
    elif letter == 'k':
        return spg.get_orbit([rand(), rand(), 0.25])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_189_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    spg = SpaceGroup('P-62m')
    if not letter in letters_selection:
        raise ValueError("It is not a P-62m wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([1./3, 2./3, 0.])
    elif letter == 'd':
        return spg.get_orbit([1./3, 2./3, 0.5])
    elif letter == 'e':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'f':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'g':
        return spg.get_orbit([rand(), 0., 0.5])
    elif letter == 'h':
        return spg.get_orbit([1./3, 2./3, rand()])
    elif letter == 'i':
        return spg.get_orbit([rand(), 0., rand()])
    elif letter == 'j':
        return spg.get_orbit([rand(), rand(), 0.])
    elif letter == 'k':
        return spg.get_orbit([rand(), rand(), 0.5])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_190_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    spg = SpaceGroup('P-62c')
    if not letter in letters_selection:
        raise ValueError("It is not a P-62c wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.25])
    elif letter == 'c':
        return spg.get_orbit([1./3, 2./3, 0.25])
    elif letter == 'd':
        return spg.get_orbit([2./3, 1./3, 0.25])
    elif letter == 'e':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'f':
        return spg.get_orbit([1./3, 2./3, rand()])
    elif letter == 'g':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'h':
        return spg.get_orbit([rand(), rand(), 0.25])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_191_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r']
    spg = SpaceGroup('P6/mmm')
    if not letter in letters_selection:
        raise ValueError("It is not a P6/mmm wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.5])
    elif letter == 'c':
        return spg.get_orbit([1./3, 2./3, 0.])
    elif letter == 'd':
        return spg.get_orbit([1./3, 2./3, 0.5])
    elif letter == 'e':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'f':
        return spg.get_orbit([0.5, 0., 0.])
    elif letter == 'g':
        return spg.get_orbit([0.5, 0., 0.5])
    elif letter == 'h':
        return spg.get_orbit([1./3, 2./3, rand()])
    elif letter == 'i':
        return spg.get_orbit([0.5, 0., rand()])
    elif letter == 'j':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'k':
        return spg.get_orbit([rand(), 0., 0.5])
    elif letter == 'l':
        x = rand()
        return spg.get_orbit([x, 2 * x, 0.])
    elif letter == 'm':
        x = rand()
        return spg.get_orbit([x, 2 * x, 0.5])
    elif letter == 'n':
        return spg.get_orbit([rand(), 0., rand()])
    elif letter == 'o':
        x = rand()
        return spg.get_orbit([x, 2 * x, rand()])
    elif letter == 'p':
        return spg.get_orbit([rand(), rand(), 0.])
    elif letter == 'q':
        return spg.get_orbit([rand(), rand(), 0.5])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_192_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    spg = SpaceGroup('P6/mcc')
    if not letter in letters_selection:
        raise ValueError("It is not a P6/mcc wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.25])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'c':
        return spg.get_orbit([1./3, 2./3, 0.25])
    elif letter == 'd':
        return spg.get_orbit([1./3, 2./3, 0.])
    elif letter == 'e':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'f':
        return spg.get_orbit([0.5, 0., 0.25])
    elif letter == 'g':
        return spg.get_orbit([0.5, 0., 0.])
    elif letter == 'h':
        return spg.get_orbit([1./3, 2./3, rand()])
    elif letter == 'i':
        return spg.get_orbit([0.5, 0., rand()])
    elif letter == 'j':
        return spg.get_orbit([rand(), 0., 0.25])
    elif letter == 'k':
        x = rand()
        return spg.get_orbit([x, 2 * x, 0.25])
    elif letter == 'l':
        return spg.get_orbit([rand(), rand(), 0.])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_193_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    spg = SpaceGroup('P6_3/mcm')
    if not letter in letters_selection:
        raise ValueError("It is not a P6_3/mcm wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.25])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'c':
        return spg.get_orbit([1./3, 2./3, 0.25])
    elif letter == 'd':
        return spg.get_orbit([1./3, 2./3, 0.])
    elif letter == 'e':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'f':
        return spg.get_orbit([0.5, 0., 0.])
    elif letter == 'g':
        return spg.get_orbit([rand(), 0., 0.25])
    elif letter == 'h':
        return spg.get_orbit([1./3, 2./3, rand()])
    elif letter == 'i':
        x = rand()
        return spg.get_orbit([x, 2 * x, 0.])
    elif letter == 'j':
        return spg.get_orbit([rand(), rand(), 0.25])
    elif letter == 'k':
        return spg.get_orbit([rand(), 0., rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_194_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    spg = SpaceGroup('P6_3/mmc')
    if not letter in letters_selection:
        raise ValueError("It is not a P6_3/mmc wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.25])
    elif letter == 'c':
        return spg.get_orbit([1./3, 2./3, 0.25])
    elif letter == 'd':
        return spg.get_orbit([1./3, 2./3, 0.75])
    elif letter == 'e':
        return spg.get_orbit([0., 0., rand()])
    elif letter == 'f':
        return spg.get_orbit([1./3, 2./3, rand()])
    elif letter == 'g':
        return spg.get_orbit([0.5, 0., 0.])
    elif letter == 'h':
        x = rand()
        return spg.get_orbit([x, 2 * x, 0.25])
    elif letter == 'i':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'j':
        return spg.get_orbit([rand(), rand(), 0.25])
    elif letter == 'k':
        x = rand()
        return spg.get_orbit([x, 2 * x, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_195_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    spg = SpaceGroup('P23')
    if not letter in letters_selection:
        raise ValueError("It is not a P23 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0.5, 0.5])
    elif letter == 'c':
        return spg.get_orbit([0., 0.5, 0.5])
    elif letter == 'd':
        return spg.get_orbit([0.5, 0., 0.])
    elif letter == 'e':
        x = rand()
        return spg.get_orbit([x, x, x])
    elif letter == 'f':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'g':
        return spg.get_orbit([rand(), 0., 0.5])
    elif letter == 'h':
        return spg.get_orbit([rand(), 0.5, 0.])
    elif letter == 'i':
        return spg.get_orbit([rand(), 0.5, 0.5])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_196_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    spg = SpaceGroup('F23')
    if not letter in letters_selection:
        raise ValueError("It is not a F23 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0.5, 0.5])
    elif letter == 'c':
        return spg.get_orbit([0.25, 0.25, 0.25])
    elif letter == 'd':
        return spg.get_orbit([0.75, 0.75, 0.75])
    elif letter == 'e':
        x = rand()
        return spg.get_orbit([x, x, x])
    elif letter == 'f':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'g':
        return spg.get_orbit([rand(), 0.25, 0.25])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_197_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f']
    spg = SpaceGroup('I23')
    if not letter in letters_selection:
        raise ValueError("It is not a I23 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0.5, 0.5])
    elif letter == 'c':
        x = rand()
        return spg.get_orbit([x, x, x])
    elif letter == 'd':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'e':
        return spg.get_orbit([rand(), 0.5, 0.])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_198_pos(letter):
    letters_selection = ['a', 'b']
    spg = SpaceGroup('P2_13')
    if not letter in letters_selection:
        raise ValueError("It is not a P2_13 wyckoff position!")
    elif letter == 'a':
        x = rand()
        return spg.get_orbit([x, x, x])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_199_pos(letter):
    letters_selection = ['a', 'b', 'c']
    spg = SpaceGroup('I2_13')
    if not letter in letters_selection:
        raise ValueError("It is not a I2_13 wyckoff position!")
    elif letter == 'a':
        x = rand()
        return spg.get_orbit([x, x, x])
    elif letter == 'b':
        return spg.get_orbit([rand(), 0., 0.25])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_200_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    spg = SpaceGroup('Pm-3')
    if not letter in letters_selection:
        raise ValueError("It is not a Pm-3 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0.5, 0.5])
    elif letter == 'c':
        return spg.get_orbit([0., 0.5, 0.5])
    elif letter == 'd':
        return spg.get_orbit([0.5, 0., 0.])
    elif letter == 'e':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'f':
        return spg.get_orbit([rand(), 0., 0.5])
    elif letter == 'g':
        return spg.get_orbit([rand(), 0.5, 0.])
    elif letter == 'h':
        return spg.get_orbit([rand(), 0.5, 0.5])
    elif letter == 'i':
        x = rand()
        return spg.get_orbit([x, x, x])
    elif letter == 'j':
        return spg.get_orbit([0., rand(), rand()])
    elif letter == 'k':
        return spg.get_orbit([0.5, rand(), rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_201_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    spg = SpaceGroup('Pn-3')
    if not letter in letters_selection:
        raise ValueError("It is not a Pn-3 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0.25, 0.25, 0.25])
    elif letter == 'c':
        return spg.get_orbit([0.75, 0.75, 0.75])
    elif letter == 'd':
        return spg.get_orbit([0., 0.5, 0.5])
    elif letter == 'e':
        x = rand()
        return spg.get_orbit([x, x, x])
    elif letter == 'f':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'g':
        return spg.get_orbit([rand(), 0.5, 0.])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_202_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    spg = SpaceGroup('Fm-3')
    if not letter in letters_selection:
        raise ValueError("It is not a Fm-3 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0.5, 0.5])
    elif letter == 'c':
        return spg.get_orbit([0.25, 0.25, 0.25])
    elif letter == 'd':
        return spg.get_orbit([0., 0.25, 0.25])
    elif letter == 'e':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'f':
        x = rand()
        return spg.get_orbit([x, x, x])
    elif letter == 'g':
        return spg.get_orbit([rand(), 0.25, 0.25])
    elif letter == 'h':
        return spg.get_orbit([0., rand(), rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_203_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    spg = SpaceGroup('Fd-3')
    if not letter in letters_selection:
        raise ValueError("It is not a Fd-3 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0.5, 0.5])
    elif letter == 'c':
        return spg.get_orbit([0.125, 0.125, 0.125])
    elif letter == 'd':
        return spg.get_orbit([0.625, 0.625, 0.625])
    elif letter == 'e':
        x = rand()
        return spg.get_orbit([x, x, x])
    elif letter == 'f':
        return spg.get_orbit([rand(), 0., 0.])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_204_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    spg = SpaceGroup('Im-3')
    if not letter in letters_selection:
        raise ValueError("It is not a Im-3 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0.5, 0.5])
    elif letter == 'c':
        return spg.get_orbit([0.25, 0.25, 0.25])
    elif letter == 'd':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'e':
        return spg.get_orbit([rand(), 0., 0.5])
    elif letter == 'f':
        x = rand()
        return spg.get_orbit([x, x, x])
    elif letter == 'g':
        return spg.get_orbit([0., rand(), rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_205_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd']
    spg = SpaceGroup('Pa-3')
    if not letter in letters_selection:
        raise ValueError("It is not a Pa-3 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0.5, 0.5])
    elif letter == 'c':
        x = rand()
        return spg.get_orbit([x, x, x])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_206_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e']
    spg = SpaceGroup('Ia-3')
    if not letter in letters_selection:
        raise ValueError("It is not a Ia-3 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0.25, 0.25, 0.25])
    elif letter == 'c':
        x = rand()
        return spg.get_orbit([x, x, x])
    elif letter == 'd':
        return spg.get_orbit([rand(), 0., 0.25])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_207_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    spg = SpaceGroup('P432')
    if not letter in letters_selection:
        raise ValueError("It is not a P432 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0.5, 0.5])
    elif letter == 'c':
        return spg.get_orbit([0., 0.5, 0.5])
    elif letter == 'd':
        return spg.get_orbit([0.5, 0., 0.])
    elif letter == 'e':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'f':
        return spg.get_orbit([rand(), 0.5, 0.5])
    elif letter == 'g':
        return spg.get_orbit([x, x, x])
    elif letter == 'h':
        return spg.get_orbit([rand(), 0.5, 0.])
    elif letter == 'i':
        y = rand()
        return spg.get_orbit([0., y, y])
    elif letter == 'j':
        y = rand()
        return spg.get_orbit([0.5, y, y])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_208_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    spg = SpaceGroup('P4_232')
    if not letter in letters_selection:
        raise ValueError("It is not a P4_232 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0.25, 0.25, 0.25])
    elif letter == 'c':
        return spg.get_orbit([0.75, 0.75, 0.75])
    elif letter == 'd':
        return spg.get_orbit([0., 0.5, 0.5])
    elif letter == 'e':
        return spg.get_orbit([0.25, 0., 0.5])
    elif letter == 'f':
        return spg.get_orbit([0.25, 0.5, 0.])
    elif letter == 'g':
        x = rand()
        return spg.get_orbit([x, x, x])
    elif letter == 'h':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'i':
        return spg.get_orbit([rand(), 0., 0.5])
    elif letter == 'j':
        return spg.get_orbit([rand(), 0.5, 0.])
    elif letter == 'k':
        y = rand()
        return spg.get_orbit([0.25, y, -y + 0.5 if y <= 0.5 else -y + 1.5])
    elif letter == 'l':
        y = rand()
        return spg.get_orbit([0.25, y, y - 0.5 if y >= 0.5 else y + 0.5])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_209_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    spg = SpaceGroup('F432')
    if not letter in letters_selection:
        raise ValueError("It is not a F432 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0.5, 0.5])
    elif letter == 'c':
        return spg.get_orbit([0.25, 0.25, 0.25])
    elif letter == 'd':
        return spg.get_orbit([0., 0.25, 0.25])
    elif letter == 'e':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'f':
        x = rand()
        return spg.get_orbit([x, x, x])
    elif letter == 'g':
        y = rand()
        return spg.get_orbit([0., y, y])
    elif letter == 'h':
        y = rand()
        return spg.get_orbit([0.5, y, y])
    elif letter == 'i':
        return spg.get_orbit([rand(), 0.25, 0.25])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_210_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    spg = SpaceGroup('F4_132')
    if not letter in letters_selection:
        raise ValueError("It is not a F4_132 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0.5, 0.5])
    elif letter == 'c':
        return spg.get_orbit([0.125, 0.125, 0.125])
    elif letter == 'd':
        return spg.get_orbit([0.625, 0.625, 0.625])
    elif letter == 'e':
        x = rand()
        return spg.get_orbit([x, x, x])
    elif letter == 'f':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'g':
        y = rand()
        return spg.get_orbit([0.125, y, -y + 0.25 if y <= 0.25 else -y + 1.25])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_211_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    spg = SpaceGroup('I432')
    if not letter in letters_selection:
        raise ValueError("It is not a I432 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0.5, 0.5])
    elif letter == 'c':
        return spg.get_orbit([0.25, 0.25, 0.25])
    elif letter == 'd':
        return spg.get_orbit([0.25, 0.5, 0.])
    elif letter == 'e':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'f':
        x = rand()
        return spg.get_orbit([x, x, x])
    elif letter == 'g':
        return spg.get_orbit([rand(), 0.5, 0.])
    elif letter == 'h':
        y = rand()
        return spg.get_orbit([0., y, y])
    elif letter == 'i':
        y = rand()
        return spg.get_orbit([0.25, y, -y + 0.5 if y <= 0.5 else -y + 1.5])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_212_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e']
    spg = SpaceGroup('P4_332')
    if not letter in letters_selection:
        raise ValueError("It is not a P4_332 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0.125, 0.125, 0.125])
    elif letter == 'b':
        return spg.get_orbit([0.625, 0.625, 0.625])
    elif letter == 'c':
        x = rand()
        return spg.get_orbit([x, x, x])
    elif letter == 'd':
        y = rand()
        return spg.get_orbit([0.125, y, -y + 0.25 if y <= 0.25 else -y + 1.25])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_213_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e']
    spg = SpaceGroup('P4_132')
    if not letter in letters_selection:
        raise ValueError("It is not a P4_132 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0.375, 0.375, 0.375])
    elif letter == 'b':
        return spg.get_orbit([0.875, 0.875, 0.875])
    elif letter == 'c':
        x = rand()
        return spg.get_orbit([x, x, x])
    elif letter == 'd':
        y = rand()
        return spg.get_orbit([0.125, y, y + 0.25 if y < 0.75 else y - 0.75])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_214_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    spg = SpaceGroup('I4_132')
    if not letter in letters_selection:
        raise ValueError("It is not a I4_132 wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0.125, 0.125, 0.125])
    elif letter == 'b':
        return spg.get_orbit([0.875, 0.875, 0.875])
    elif letter == 'c':
        return spg.get_orbit([0.125, 0., 0.25])
    elif letter == 'd':
        return spg.get_orbit([0.625, 0., 0.25])
    elif letter == 'e':
        x = rand()
        return spg.get_orbit([x, x, x])
    elif letter == 'f':
        return spg.get_orbit([rand(), 0., 0.25])
    elif letter == 'g':
        y = rand()
        return spg.get_orbit([0.125, y, y + 0.25 if y < 0.75 else y - 0.75])
    elif letter == 'h':
        y = rand()
        return spg.get_orbit([0.125, y, -y + 0.25 if y <= 0.25 else -y + 1.25])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_215_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    spg = SpaceGroup('P-43m')
    if not letter in letters_selection:
        raise ValueError("It is not a P-43m wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0.5, 0.5])
    elif letter == 'c':
        return spg.get_orbit([0., 0.5, 0.5])
    elif letter == 'd':
        return spg.get_orbit([0.5, 0., 0.])
    elif letter == 'e':
        x = rand()
        return spg.get_orbit([x, x, x])
    elif letter == 'f':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'g':
        return spg.get_orbit([rand(), 0.5, 0.5])
    elif letter == 'h':
        return spg.get_orbit([rand(), 0.5, 0.])
    elif letter == 'i':
        x = rand()
        return spg.get_orbit([x, x, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_216_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    spg = SpaceGroup('F-43m')
    if not letter in letters_selection:
        raise ValueError("It is not a F-43m wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0.5, 0.5])
    elif letter == 'c':
        return spg.get_orbit([0.25, 0.25, 0.25])
    elif letter == 'd':
        return spg.get_orbit([0.75, 0.75, 0.75])
    elif letter == 'e':
        x = rand()
        return spg.get_orbit([x, x, x])
    elif letter == 'f':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'g':
        return spg.get_orbit([rand(), 0.25, 0.25])
    elif letter == 'h':
        x = rand()
        return spg.get_orbit([x, x, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_217_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    spg = SpaceGroup('I-43m')
    if not letter in letters_selection:
        raise ValueError("It is not a I-43m wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0.5, 0.5])
    elif letter == 'c':
        x = rand()
        return spg.get_orbit([x, x, x])
    elif letter == 'd':
        return spg.get_orbit([0.25, 0.5, 0.])
    elif letter == 'e':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'f':
        return spg.get_orbit([rand(), 0.5, 0.])
    elif letter == 'g':
        x = rand()
        return spg.get_orbit([x, x, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_218_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    spg = SpaceGroup('P-43n')
    if not letter in letters_selection:
        raise ValueError("It is not a P-43n wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0.5, 0.5])
    elif letter == 'c':
        return spg.get_orbit([0.25, 0.5, 0.])
    elif letter == 'd':
        return spg.get_orbit([0.25, 0., 0.5])
    elif letter == 'e':
        x = rand()
        return spg.get_orbit([x, x, x])
    elif letter == 'f':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'g':
        return spg.get_orbit([rand(), 0.5, 0.])
    elif letter == 'h':
        return spg.get_orbit([rand(), 0., 0.5])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_219_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    spg = SpaceGroup('F-43c')
    if not letter in letters_selection:
        raise ValueError("It is not a F-43c wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0.25, 0.25, 0.25])
    elif letter == 'c':
        return spg.get_orbit([0., 0.25, 0.25])
    elif letter == 'd':
        return spg.get_orbit([0.25, 0., 0.])
    elif letter == 'e':
        x = rand()
        return spg.get_orbit([x, x, x])
    elif letter == 'f':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'g':
        return spg.get_orbit([rand(), 0.25, 0.25])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_220_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e']
    spg = SpaceGroup('I-43d')
    if not letter in letters_selection:
        raise ValueError("It is not a I-43d wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0.375, 0., 0.25])
    elif letter == 'b':
        return spg.get_orbit([0.875, 0., 0.25])
    elif letter == 'c':
        x = rand()
        return spg.get_orbit([x, x, x])
    elif letter == 'd':
        return spg.get_orbit([rand(), 0., 0.25])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_221_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
    spg = SpaceGroup('Pm-3m')
    if not letter in letters_selection:
        raise ValueError("It is not a Pm-3m wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0.5, 0.5])
    elif letter == 'c':
        return spg.get_orbit([0., 0.5, 0.5])
    elif letter == 'd':
        return spg.get_orbit([0.5, 0., 0.])
    elif letter == 'e':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'f':
        return spg.get_orbit([rand(), 0.5, 0.5])
    elif letter == 'g':
        x = rand()
        return spg.get_orbit([x, x, x])
    elif letter == 'h':
        return spg.get_orbit([rand(), 0.5, 0.])
    elif letter == 'i':
        y = rand()
        return spg.get_orbit([0., y, y])
    elif letter == 'j':
        y = rand()
        return spg.get_orbit([0.5, y, y])
    elif letter == 'k':
        return spg.get_orbit([0., rand(), rand()])
    elif letter == 'l':
        return spg.get_orbit([0.5, rand(), rand()])
    elif letter == 'm':
        x = rand()
        return spg.get_orbit([x, x, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_222_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    spg = SpaceGroup('Pn-3n')
    if not letter in letters_selection:
        raise ValueError("It is not a Pn-3n wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0.5, 0.5])
    elif letter == 'c':
        return spg.get_orbit([0.25, 0.25, 0.25])
    elif letter == 'd':
        return spg.get_orbit([0.25, 0., 0.5])
    elif letter == 'e':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'f':
        x = rand()
        return spg.get_orbit([x, x, x])
    elif letter == 'g':
        return spg.get_orbit([rand(), 0., 0.5])
    elif letter == 'h':
        y = rand()
        return spg.get_orbit([0., y, y])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_223_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    spg = SpaceGroup('Pm-3n')
    if not letter in letters_selection:
        raise ValueError("It is not a Pm-3n wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0.5, 0.5])
    elif letter == 'c':
        return spg.get_orbit([0.25, 0., 0.5])
    elif letter == 'd':
        return spg.get_orbit([0.25, 0.5, 0.])
    elif letter == 'e':
        return spg.get_orbit([0.25, 0.25, 0.25])
    elif letter == 'f':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'g':
        return spg.get_orbit([rand(), 0., 0.5])
    elif letter == 'h':
        return spg.get_orbit([rand(), 0.5, 0.])
    elif letter == 'i':
        x = rand()
        return spg.get_orbit([x, x, x])
    elif letter == 'j':
        y = rand()
        return spg.get_orbit([0.25, y, y - 0.5 if y >= 0.5 else y + 0.5])
    elif letter == 'k':
        return spg.get_orbit([0., rand(), rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_224_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    spg = SpaceGroup('Pn-3m')
    if not letter in letters_selection:
        raise ValueError("It is not a Pn-3m wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0.25, 0.25, 0.25])
    elif letter == 'c':
        return spg.get_orbit([0.75, 0.75, 0.75])
    elif letter == 'd':
        return spg.get_orbit([0., 0.5, 0.5])
    elif letter == 'e':
        x = rand()
        return spg.get_orbit([x, x, x])
    elif letter == 'f':
        return spg.get_orbit([0.25, 0., 0.5])
    elif letter == 'g':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'h':
        return spg.get_orbit([rand(), 0., 0.5])
    elif letter == 'i':
        y = rand()
        return spg.get_orbit([0.25, y, -y + 0.5 if y <= 0.5 else -y + 1.5])
    elif letter == 'j':
        y = rand()
        return spg.get_orbit([0.25, y, y - 0.5 if y >= 0.5 else y + 0.5])
    elif letter == 'k':
        x = rand()
        return spg.get_orbit([x, x, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_225_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    spg = SpaceGroup('Fm-3m')
    if not letter in letters_selection:
        raise ValueError("It is not a Fm-3m wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0.5, 0.5])
    elif letter == 'c':
        return spg.get_orbit([0.25, 0.25, 0.25])
    elif letter == 'd':
        return spg.get_orbit([0., 0.25, 0.25])
    elif letter == 'e':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'f':
        x = rand()
        return spg.get_orbit([x, x, x])
    elif letter == 'g':
        return spg.get_orbit([rand(), 0.25, 0.25])
    elif letter == 'h':
        y = rand()
        return spg.get_orbit([0., y, y])
    elif letter == 'i':
        y = rand()
        return spg.get_orbit([0.5, y, y])
    elif letter == 'j':
        return spg.get_orbit([0., rand(), rand()])
    elif letter == 'k':
        x = rand()
        return spg.get_orbit([x, x, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_226_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    spg = SpaceGroup('Fm-3c')
    if not letter in letters_selection:
        raise ValueError("It is not a Fm-3c wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0.25, 0.25, 0.25])
    elif letter == 'b':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'c':
        return spg.get_orbit([0.25, 0., 0.])
    elif letter == 'd':
        return spg.get_orbit([0., 0.25, 0.25])
    elif letter == 'e':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'f':
        return spg.get_orbit([rand(), 0.25, 0.25])
    elif letter == 'g':
        x = rand()
        return spg.get_orbit([x, x, x])
    elif letter == 'h':
        y = rand()
        return spg.get_orbit([0.25, y, y])
    elif letter == 'i':
        return spg.get_orbit([0., rand(), rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_227_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    spg = SpaceGroup('Fd-3m')
    if not letter in letters_selection:
        raise ValueError("It is not a Fd-3m wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0.5, 0.5, 0.5])
    elif letter == 'c':
        return spg.get_orbit([0.125, 0.125, 0.125])
    elif letter == 'd':
        return spg.get_orbit([0.625, 0.625, 0.625])
    elif letter == 'e':
        x = rand()
        return spg.get_orbit([x, x, x])
    elif letter == 'f':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'g':
        x = rand()
        return spg.get_orbit([x, x, rand()])
    elif letter == 'h':
        y = rand()
        return spg.get_orbit([0.125, y, -y + 0.25 if y <= 0.25 else -y + 1.25])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_228_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    spg = SpaceGroup('Fd-3c')
    if not letter in letters_selection:
        raise ValueError("It is not a Fd-3c wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0.125, 0.125, 0.125])
    elif letter == 'c':
        return spg.get_orbit([0.375, 0.375, 0.375])
    elif letter == 'd':
        return spg.get_orbit([0.25, 0., 0.])
    elif letter == 'e':
        x = rand()
        return spg.get_orbit([x, x, x])
    elif letter == 'f':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'g':
        y = rand()
        return spg.get_orbit([0.125, y, -y + 0.25 if y <= 0.25 else -y + 1.25])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_229_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    spg = SpaceGroup('Im-3m')
    if not letter in letters_selection:
        raise ValueError("It is not a Im-3m wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0., 0.5, 0.5])
    elif letter == 'c':
        return spg.get_orbit([0.25, 0.25, 0.25])
    elif letter == 'd':
        return spg.get_orbit([0.25, 0., 0.5])
    elif letter == 'e':
        return spg.get_orbit([rand(), 0., 0.])
    elif letter == 'f':
        x = rand()
        return spg.get_orbit([x, x, x])
    elif letter == 'g':
        return spg.get_orbit([rand(), 0., 0.5])
    elif letter == 'h':
        y = rand()
        return spg.get_orbit([0., y, y])
    elif letter == 'i':
        y = rand()
        return spg.get_orbit([0.25, y, -y + 0.5 if y <= 0.5 else -y + 1.5])
    elif letter == 'j':
        return spg.get_orbit([0., rand(), rand()])
    elif letter == 'k':
        x = rand()
        return spg.get_orbit([x, x, rand()])
    else:
        return spg.get_orbit([rand(), rand(), rand()])

def sp_230_pos(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    spg = SpaceGroup('Ia-3d')
    if not letter in letters_selection:
        raise ValueError("It is not a Ia-3d wyckoff position!")
    elif letter == 'a':
        return spg.get_orbit([0., 0., 0.])
    elif letter == 'b':
        return spg.get_orbit([0.125, 0.125, 0.125])
    elif letter == 'c':
        return spg.get_orbit([0.125, 0., 0.25])
    elif letter == 'd':
        return spg.get_orbit([0.375, 0., 0.25])
    elif letter == 'e':
        x = rand()
        return spg.get_orbit([x, x, x])
    elif letter == 'f':
        return spg.get_orbit([rand(), 0., 0.25])
    elif letter == 'g':
        y = rand()
        return spg.get_orbit([0.125, y, -y + 0.25 if y <= 0.25 else -y + 1.25])
    else:
        return spg.get_orbit([rand(), rand(), rand()])
