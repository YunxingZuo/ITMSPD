# coding: utf-8
# Copyright ? 2016 YunXing Zuo

import numpy as np

__author__ = 'YunXing Zuo'
__email__ = 'zuoyx@pkusz.edu.cn'
__date__ = 'Dec. 22, 2016'

def wyckoff_parameter(symbol, letter):
    if symbol in 'P1':
        return sp_1_parameter(letter)
    elif symbol in 'P-1':
        return sp_2_parameter(letter)
    elif symbol in 'P2':
        return sp_3_parameter(letter)
    elif symbol in 'P2_1':
        return sp_4_parameter(letter)
    elif symbol in 'C2':
        return sp_5_parameter(letter)
    elif symbol in 'Pm':
        return sp_6_parameter(letter)
    elif symbol in 'Pc':
        return sp_7_parameter(letter)
    elif symbol in 'Cm':
        return sp_8_parameter(letter)
    elif symbol in 'Cc':
        return sp_9_parameter(letter)
    elif symbol in 'P2/m':
        return sp_10_parameter(letter)
    elif symbol in 'P2_1/m':
        return sp_11_parameter(letter)
    elif symbol in 'C2/m':
        return sp_12_parameter(letter)
    elif symbol in 'P2/c':
        return sp_13_parameter(letter)
    elif symbol in 'P2_1/c':
        return sp_14_parameter(letter)
    elif symbol in 'C2/c':
        return sp_15_parameter(letter)
    elif symbol in 'P222':
        return sp_16_parameter(letter)
    elif symbol in 'P222_1':
        return sp_17_parameter(letter)
    elif symbol in 'P2_12_12':
        return sp_18_parameter(letter)
    elif symbol in 'P2_12_12_1':
        return sp_19_parameter(letter)
    elif symbol in 'C222_1':
        return sp_20_parameter(letter)
    elif symbol in 'C222':
        return sp_21_parameter(letter)
    elif symbol in 'F222':
        return sp_22_parameter(letter)
    elif symbol in 'I222':
        return sp_23_parameter(letter)
    elif symbol in 'I2_12_12_1':
        return sp_24_parameter(letter)
    elif symbol in 'Pmm2':
        return sp_25_parameter(letter)
    elif symbol in 'Pmc2_1':
        return sp_26_parameter(letter)
    elif symbol in 'Pcc2':
        return sp_27_parameter(letter)
    elif symbol in 'Pma2':
        return sp_28_parameter(letter)
    elif symbol in 'Pca2_1':
        return sp_29_parameter(letter)
    elif symbol in 'Pnc2':
        return sp_30_parameter(letter)
    elif symbol in 'Pmn2_1':
        return sp_31_parameter(letter)
    elif symbol in 'Pba2':
        return sp_32_parameter(letter)
    elif symbol in 'Pna2_1':
        return sp_33_parameter(letter)
    elif symbol in 'Pnn2':
        return sp_34_parameter(letter)
    elif symbol in 'Cmm2':
        return sp_35_parameter(letter)
    elif symbol in 'Cmc2_1':
        return sp_36_parameter(letter)
    elif symbol in 'Ccc2':
        return sp_37_parameter(letter)
    elif symbol in 'Amm2':
        return sp_38_parameter(letter)
    elif symbol in 'Aem2':
        return sp_39_parameter(letter)
    elif symbol in 'Ama2':
        return sp_40_parameter(letter)
    elif symbol in 'Aea2':
        return sp_41_parameter(letter)
    elif symbol in 'Fmm2':
        return sp_42_parameter(letter)
    elif symbol in 'Fdd2':
        return sp_43_parameter(letter)
    elif symbol in 'Imm2':
        return sp_44_parameter(letter)
    elif symbol in 'Iba2':
        return sp_45_parameter(letter)
    elif symbol in 'Ima2':
        return sp_46_parameter(letter)
    elif symbol in 'Pmmm':
        return sp_47_parameter(letter)
    elif symbol in 'Pnnn':
        return sp_48_parameter(letter)
    elif symbol in 'Pccm':
        return sp_49_parameter(letter)
    elif symbol in 'Pban':
        return sp_50_parameter(letter)
    elif symbol in 'Pmma':
        return sp_51_parameter(letter)
    elif symbol in 'Pnna':
        return sp_52_parameter(letter)
    elif symbol in 'Pmna':
        return sp_53_parameter(letter)
    elif symbol in 'Pcca':
        return sp_54_parameter(letter)
    elif symbol in 'Pbam':
        return sp_55_parameter(letter)
    elif symbol in 'Pccn':
        return sp_56_parameter(letter)
    elif symbol in 'Pbcm':
        return sp_57_parameter(letter)
    elif symbol in 'Pnnm':
        return sp_58_parameter(letter)
    elif symbol in 'Pmmn':
        return sp_59_parameter(letter)
    elif symbol in 'Pbcn':
        return sp_60_parameter(letter)
    elif symbol in 'Pbca':
        return sp_61_parameter(letter)
    elif symbol in 'Pnma':
        return sp_62_parameter(letter)
    elif symbol in 'Cmcm':
        return sp_63_parameter(letter)
    elif symbol in 'Cmce':
        return sp_64_parameter(letter)
    elif symbol in 'Cmmm':
        return sp_65_parameter(letter)
    elif symbol in 'Cccm':
        return sp_66_parameter(letter)
    elif symbol in 'Cmme':
        return sp_67_parameter(letter)
    elif symbol in 'Ccce':
        return sp_68_parameter(letter)
    elif symbol in 'Fmmm':
        return sp_69_parameter(letter)
    elif symbol in 'Fddd':
        return sp_70_parameter(letter)
    elif symbol in 'Immm':
        return sp_71_parameter(letter)
    elif symbol in 'Ibam':
        return sp_72_parameter(letter)
    elif symbol in 'Ibca':
        return sp_73_parameter(letter)
    elif symbol in 'Imma':
        return sp_74_parameter(letter)
    elif symbol in 'P4':
        return sp_75_parameter(letter)
    elif symbol in 'P4_1':
        return sp_76_parameter(letter)
    elif symbol in 'P4_2':
        return sp_77_parameter(letter)
    elif symbol in 'P4_3':
        return sp_78_parameter(letter)
    elif symbol in 'I4':
        return sp_79_parameter(letter)
    elif symbol in 'I4_1':
        return sp_80_parameter(letter)
    elif symbol in 'P-4':
        return sp_81_parameter(letter)
    elif symbol in 'I-4':
        return sp_82_parameter(letter)
    elif symbol in 'P4/m':
        return sp_83_parameter(letter)
    elif symbol in 'P4_2/m':
        return sp_84_parameter(letter)
    elif symbol in 'P4/n':
        return sp_85_parameter(letter)
    elif symbol in 'P4_2/n':
        return sp_86_parameter(letter)
    elif symbol in 'I4/m':
        return sp_87_parameter(letter)
    elif symbol in 'I4_1/a':
        return sp_88_parameter(letter)
    elif symbol in 'P422':
        return sp_89_parameter(letter)
    elif symbol in 'P42_12':
        return sp_90_parameter(letter)
    elif symbol in 'P4_122':
        return sp_91_parameter(letter)
    elif symbol in 'P4_12_12':
        return sp_92_parameter(letter)
    elif symbol in 'P4_222':
        return sp_93_parameter(letter)
    elif symbol in 'P4_22_12':
        return sp_94_parameter(letter)
    elif symbol in 'P4_322':
        return sp_95_parameter(letter)
    elif symbol in 'P4_32_12':
        return sp_96_parameter(letter)
    elif symbol in 'I422':
        return sp_97_parameter(letter)
    elif symbol in 'I4_122':
        return sp_98_parameter(letter)
    elif symbol in 'P4mm':
        return sp_99_parameter(letter)
    elif symbol in 'P4bm':
        return sp_100_parameter(letter)
    elif symbol in 'P4_2cm':
        return sp_101_parameter(letter)
    elif symbol in 'P4_2nm':
        return sp_102_parameter(letter)
    elif symbol in 'P4cc':
        return sp_103_parameter(letter)
    elif symbol in 'P4nc':
        return sp_104_parameter(letter)
    elif symbol in 'P4_2mc':
        return sp_105_parameter(letter)
    elif symbol in 'P4_2bc':
        return sp_106_parameter(letter)
    elif symbol in 'I4mm':
        return sp_107_parameter(letter)
    elif symbol in 'I4cm':
        return sp_108_parameter(letter)
    elif symbol in 'I4_1md':
        return sp_109_parameter(letter)
    elif symbol in 'I4_1cd':
        return sp_110_parameter(letter)
    elif symbol in 'P-42m':
        return sp_111_parameter(letter)
    elif symbol in 'P-42c':
        return sp_112_parameter(letter)
    elif symbol in 'P-42_1m':
        return sp_113_parameter(letter)
    elif symbol in 'P-42_1c':
        return sp_114_parameter(letter)
    elif symbol in 'P-4m2':
        return sp_115_parameter(letter)
    elif symbol in 'P-4c2':
        return sp_116_parameter(letter)
    elif symbol in 'P-4b2':
        return sp_117_parameter(letter)
    elif symbol in 'P-4n2':
        return sp_118_parameter(letter)
    elif symbol in 'I-4m2':
        return sp_119_parameter(letter)
    elif symbol in 'I-4c2':
        return sp_120_parameter(letter)
    elif symbol in 'I-42m':
        return sp_121_parameter(letter)
    elif symbol in 'I-42d':
        return sp_122_parameter(letter)
    elif symbol in 'P4/mmm':
        return sp_123_parameter(letter)
    elif symbol in 'P4/mcc':
        return sp_124_parameter(letter)
    elif symbol in 'P4/nbm':
        return sp_125_parameter(letter)
    elif symbol in 'P4/nnc':
        return sp_126_parameter(letter)
    elif symbol in 'P4/mbm':
        return sp_127_parameter(letter)
    elif symbol in 'P4/mnc':
        return sp_128_parameter(letter)
    elif symbol in 'P4/nmm':
        return sp_129_parameter(letter)
    elif symbol in 'P4/ncc':
        return sp_130_parameter(letter)
    elif symbol in 'P4_2/mmc':
        return sp_131_parameter(letter)
    elif symbol in 'P4_2/mcm':
        return sp_132_parameter(letter)
    elif symbol in 'P4_2/nbc':
        return sp_133_parameter(letter)
    elif symbol in 'P4_2/nnm':
        return sp_134_parameter(letter)
    elif symbol in 'P4_2/mbc':
        return sp_135_parameter(letter)
    elif symbol in 'P4_2/mnm':
        return sp_136_parameter(letter)
    elif symbol in 'P4_2/nmc':
        return sp_137_parameter(letter)
    elif symbol in 'P4_2/ncm':
        return sp_138_parameter(letter)
    elif symbol in 'I4/mmm':
        return sp_139_parameter(letter)
    elif symbol in 'I4/mcm':
        return sp_140_parameter(letter)
    elif symbol in 'I4_1/amd':
        return sp_141_parameter(letter)
    elif symbol in 'I4_1/acd':
        return sp_142_parameter(letter)
    elif symbol in 'P3':
        return sp_143_parameter(letter)
    elif symbol in 'P3_1':
        return sp_144_parameter(letter)
    elif symbol in 'P3_2':
        return sp_145_parameter(letter)
    elif symbol in 'R3':
        return sp_146_parameter_R(letter)
    elif symbol in 'R3H':
        return sp_146_parameter_H(letter)
    elif symbol in 'P-3':
        return sp_147_parameter(letter)
    elif symbol in 'R-3':
        return sp_148_parameter_R(letter)
    elif symbol in 'R-3H':
        return sp_148_parameter_H(letter)
    elif symbol in 'P312':
        return sp_149_parameter(letter)
    elif symbol in 'P321':
        return sp_150_parameter(letter)
    elif symbol in 'P3_112':
        return sp_151_parameter(letter)
    elif symbol in 'P3_121':
        return sp_152_parameter(letter)
    elif symbol in 'P3_212':
        return sp_153_parameter(letter)
    elif symbol in 'P3_221':
        return sp_154_parameter(letter)
    elif symbol in 'R32':
        return sp_155_parameter_R(letter)
    elif symbol in 'R32H':
        return sp_155_parameter_H(letter)
    elif symbol in 'P3m1':
        return sp_156_parameter(letter)
    elif symbol in 'P31m':
        return sp_157_parameter(letter)
    elif symbol in 'P3c1':
        return sp_158_parameter(letter)
    elif symbol in 'P31c':
        return sp_159_parameter(letter)
    elif symbol in 'R3m':
        return sp_160_parameter_R(letter)
    elif symbol in 'R3mH':
        return sp_160_parameter_H(letter)
    elif symbol in 'R3c':
        return sp_161_parameter_R(letter)
    elif symbol in 'R3cH':
        return sp_161_parameter_H(letter)
    elif symbol in 'P-31m':
        return sp_162_parameter(letter)
    elif symbol in 'P-31c':
        return sp_163_parameter(letter)
    elif symbol in 'P-3m1':
        return sp_164_parameter(letter)
    elif symbol in 'P-3c1':
        return sp_165_parameter(letter)
    elif symbol in 'R-3m':
        return sp_166_parameter_R(letter)
    elif symbol in 'R-3mH':
        return sp_166_parameter_H(letter)
    elif symbol in 'R-3c':
        return sp_167_parameter_R(letter)
    elif symbol in 'R-3cH':
        return sp_167_parameter_H(letter)
    elif symbol in 'P6':
        return sp_168_parameter(letter)
    elif symbol in 'P6_1':
        return sp_169_parameter(letter)
    elif symbol in 'P6_5':
        return sp_170_parameter(letter)
    elif symbol in 'P6_2':
        return sp_171_parameter(letter)
    elif symbol in 'P6_4':
        return sp_172_parameter(letter)
    elif symbol in 'P6_3':
        return sp_173_parameter(letter)
    elif symbol in 'P-6':
        return sp_174_parameter(letter)
    elif symbol in 'P6/m':
        return sp_175_parameter(letter)
    elif symbol in 'P6_3/m':
        return sp_176_parameter(letter)
    elif symbol in 'P622':
        return sp_177_parameter(letter)
    elif symbol in 'P6_122':
        return sp_178_parameter(letter)
    elif symbol in 'P6_522':
        return sp_179_parameter(letter)
    elif symbol in 'P6_222':
        return sp_180_parameter(letter)
    elif symbol in 'P6_422':
        return sp_181_parameter(letter)
    elif symbol in 'P6_322':
        return sp_182_parameter(letter)
    elif symbol in 'P6mm':
        return sp_183_parameter(letter)
    elif symbol in 'P6cc':
        return sp_184_parameter(letter)
    elif symbol in 'P6_3cm':
        return sp_185_parameter(letter)
    elif symbol in 'P6_3mc':
        return sp_186_parameter(letter)
    elif symbol in 'P-6m2':
        return sp_187_parameter(letter)
    elif symbol in 'P-6c2':
        return sp_188_parameter(letter)
    elif symbol in 'P-62m':
        return sp_189_parameter(letter)
    elif symbol in 'P-62c':
        return sp_190_parameter(letter)
    elif symbol in 'P6/mmm':
        return sp_191_parameter(letter)
    elif symbol in 'P6/mcc':
        return sp_192_parameter(letter)
    elif symbol in 'P6_3/mcm':
        return sp_193_parameter(letter)
    elif symbol in 'P6_3/mmc':
        return sp_194_parameter(letter)
    elif symbol in 'P23':
        return sp_195_parameter(letter)
    elif symbol in 'F23':
        return sp_196_parameter(letter)
    elif symbol in 'I23':
        return sp_197_parameter(letter)
    elif symbol in 'P2_13':
        return sp_198_parameter(letter)
    elif symbol in 'I2_13':
        return sp_199_parameter(letter)
    elif symbol in 'Pm-3':
        return sp_200_parameter(letter)
    elif symbol in 'Pn-3':
        return sp_201_parameter(letter)
    elif symbol in 'Fm-3':
        return sp_202_parameter(letter)
    elif symbol in 'Fd-3':
        return sp_203_parameter(letter)
    elif symbol in 'Im-3':
        return sp_204_parameter(letter)
    elif symbol in 'Pa-3':
        return sp_205_parameter(letter)
    elif symbol in 'Ia-3':
        return sp_206_parameter(letter)
    elif symbol in 'P432':
        return sp_207_parameter(letter)
    elif symbol in 'P4_232':
        return sp_208_parameter(letter)
    elif symbol in 'F432':
        return sp_209_parameter(letter)
    elif symbol in 'F4_132':
        return sp_210_parameter(letter)
    elif symbol in 'I432':
        return sp_211_parameter(letter)
    elif symbol in 'P4_332':
        return sp_212_parameter(letter)
    elif symbol in 'P4_132':
        return sp_213_parameter(letter)
    elif symbol in 'I4_132':
        return sp_214_parameter(letter)
    elif symbol in 'P-43m':
        return sp_215_parameter(letter)
    elif symbol in 'F-43m':
        return sp_216_parameter(letter)
    elif symbol in 'I-43m':
        return sp_217_parameter(letter)
    elif symbol in 'P-43n':
        return sp_218_parameter(letter)
    elif symbol in 'F-43c':
        return sp_219_parameter(letter)
    elif symbol in 'I-43d':
        return sp_220_parameter(letter)
    elif symbol in 'Pm-3m':
        return sp_221_parameter(letter)
    elif symbol in 'Pn-3n':
        return sp_222_parameter(letter)
    elif symbol in 'Pm-3n':
        return sp_223_parameter(letter)
    elif symbol in 'Pn-3m':
        return sp_224_parameter(letter)
    elif symbol in 'Fm-3m':
        return sp_225_parameter(letter)
    elif symbol in 'Fm-3c':
        return sp_226_parameter(letter)
    elif symbol in 'Fd-3m':
        return sp_227_parameter(letter)
    elif symbol in 'Fd-3c':
        return sp_228_parameter(letter)
    elif symbol in 'Im-3m':
        return sp_229_parameter(letter)
    elif symbol in 'Ia-3d':
        return sp_230_parameter(letter)

parameter = [np.array([True, True, True]), np.array([True, True, False]), np.array([True, False, True]), np.array([False, True, True]), \
             np.array([True, False, False]), np.array([False, True, False]), np.array([False, False, True]), np.array([False, False, False])]

def sp_1_parameter(letter):
    letters_selection = ['a']
    if not letter in letters_selection:
        raise ValueError("It is not a P1 wyckoff position!")
    else:
        return parameter[0]

def sp_2_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    if not letter in letters_selection:
        raise ValueError("It is not a P-1 wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
        return parameter[7]
    else:
        return parameter[0]

def sp_3_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e']
    if not letter in letters_selection:
        raise ValueError("It is not a P2 wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[5]
    else:
        return parameter[0]

def sp_4_parameter(letter):
    letters_selection = ['a']
    if not letter in letters_selection:
        raise ValueError("It is not a P2_1 wyckoff position!")
    else:
        return parameter[0]

def sp_5_parameter(letter):
    letters_selection = ['a', 'b', 'c']
    if not letter in letters_selection:
        raise ValueError("It is not a C2 wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[5]
    else:
        return parameter[0]

def sp_6_parameter(letter):
    letters_selection = ['a', 'b', 'c']
    if not letter in letters_selection:
        raise ValueError("It is not a Pm wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[2]
    else:
        return parameter[0]

def sp_7_parameter(letter):
    letters_selection = ['a']
    if not letter in letters_selection:
        raise ValueError("It is not a Pc wyckoff position!")
    else:
        return parameter[0]

def sp_8_parameter(letter):
    letters_selection = ['a', 'b']
    if not letter in letters_selection:
        raise ValueError("It is not a Cm wyckoff position!")
    elif letter in ['a']:
        return parameter[2]
    else:
        return parameter[0]

def sp_9_parameter(letter):
    letters_selection = ['a']
    if not letter in letters_selection:
        raise ValueError("It is not a Cc wyckoff position!")
    else:
        return parameter[0]

def sp_10_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
    if not letter in letters_selection:
        raise ValueError("It is not a P2/m wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
        return parameter[7]
    elif letter in ['i', 'j', 'k', 'l']:
        return parameter[5]
    elif letter in ['m', 'n']:
        return parameter[2]
    else:
        return parameter[0]

def sp_11_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f']
    if not letter in letters_selection:
        raise ValueError("It is not a P2_1/m wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e']:
        return parameter[2]
    else:
        return parameter[0]

def sp_12_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    if not letter in letters_selection:
        raise ValueError("It is not a C2/m wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd', 'e', 'f']:
        return parameter[7]
    elif letter in ['g', 'h']:
        return parameter[5]
    elif letter in ['i']:
        return parameter[2]
    else:
        return parameter[0]

def sp_13_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    if not letter in letters_selection:
        raise ValueError("It is not a P2/c wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'f']:
        return parameter[5]
    else:
        return parameter[0]

def sp_14_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e']
    if not letter in letters_selection:
        raise ValueError("It is not a P2_1/c wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    else:
        return parameter[0]

def sp_15_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f']
    if not letter in letters_selection:
        raise ValueError("It is not a C2/c wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e']:
        return parameter[5]
    else:
        return parameter[0]

def sp_16_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u']
    if not letter in letters_selection:
        raise ValueError("It is not a P222 wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
        return parameter[7]
    elif letter in ['i', 'j', 'k', 'l']:
        return parameter[4]
    elif letter in ['m', 'n', 'o', 'p']:
        return parameter[5]
    elif letter in ['q', 'r', 's', 't']:
        return parameter[6]
    else:
        return parameter[0]

def sp_17_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e']
    if not letter in letters_selection:
        raise ValueError("It is not a P222_1 wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[4]
    elif letter in ['c', 'd']:
        return parameter[5]
    else:
        return parameter[0]

def sp_18_parameter(letter):
    letters_selection = ['a', 'b', 'c']
    if not letter in letters_selection:
        raise ValueError("It is not a P2_12_12 wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[6]
    else:
        return parameter[0]

def sp_19_parameter(letter):
    letters_selection = ['a']
    if not letter in letters_selection:
        raise ValueError("It is not a P2_12_12_1 wyckoff position!")
    else:
        return parameter[0]

def sp_20_parameter(letter):
    letters_selection = ['a', 'b', 'c']
    if not letter in letters_selection:
        raise ValueError("It is not a C222_1 wyckoff position!")
    elif letter in ['a']:
        return parameter[4]
    elif letter in ['b']:
        return parameter[5]
    else:
        return parameter[0]

def sp_21_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    if not letter in letters_selection:
        raise ValueError("It is not a C222 wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'f']:
        return parameter[4]
    elif letter in ['g', 'h']:
        return parameter[5]
    elif letter in ['i', 'j', 'k']:
        return parameter[6]
    else:
        return parameter[0]

def sp_22_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    if not letter in letters_selection:
        raise ValueError("It is not a F222 wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'j']:
        return parameter[4]
    elif letter in ['f', 'i']:
        return parameter[5]
    elif letter in ['g', 'h']:
        return parameter[6]
    else:
        return parameter[0]

def sp_23_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    if not letter in letters_selection:
        raise ValueError("It is not a I222 wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'f']:
        return parameter[4]
    elif letter in ['g', 'h']:
        return parameter[5]
    elif letter in ['i', 'j']:
        return parameter[6]
    else:
        return parameter[0]

def sp_24_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd']
    if not letter in letters_selection:
        raise ValueError("It is not a I2_12_12_1 wyckoff position!")
    elif letter in ['a']:
        return parameter[4]
    elif letter in ['b']:
        return parameter[5]
    elif letter in ['c']:
        return parameter[6]
    else:
        return parameter[0]

def sp_25_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    if not letter in letters_selection:
        raise ValueError("It is not a Pmm2 wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[6]
    elif letter in ['e', 'f']:
        return parameter[2]
    elif letter in ['g', 'h']:
        return parameter[3]
    else:
        return parameter[0]

def sp_26_parameter(letter):
    letters_selection = ['a', 'b', 'c']
    if not letter in letters_selection:
        raise ValueError("It is not a Pmc2_1 wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[3]
    else:
        return parameter[0]

def sp_27_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e']
    if not letter in letters_selection:
        raise ValueError("It is not a Pcc2 wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[6]
    else:
        return parameter[0]

def sp_28_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd']
    if not letter in letters_selection:
        raise ValueError("It is not a Pma2 wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[6]
    elif letter in ['c']:
        return parameter[3]
    else:
        return parameter[0]

def sp_29_parameter(letter):
    letters_selection = ['a']
    if not letter in letters_selection:
        raise ValueError("It is not a Pca2_1 wyckoff position!")
    else:
        return parameter[0]

def sp_30_parameter(letter):
    letters_selection = ['a', 'b', 'c']
    if not letter in letters_selection:
        raise ValueError("It is not a Pnc2 wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[6]
    else:
        return parameter[0]

def sp_31_parameter(letter):
    letters_selection = ['a', 'b']
    if not letter in letters_selection:
        raise ValueError("It is not a Pmn2_1 wyckoff position!")
    elif letter in ['a']:
        return parameter[3]
    else:
        return parameter[0]

def sp_32_parameter(letter):
    letters_selection = ['a', 'b', 'c']
    if not letter in letters_selection:
        raise ValueError("It is not a Pba2 wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[6]
    else:
        return parameter[0]

def sp_33_parameter(letter):
    letters_selection = ['a']
    if not letter in letters_selection:
        raise ValueError("It is not a Pna2_1 wyckoff position!")
    else:
        return parameter[0]

def sp_34_parameter(letter):
    letters_selection = ['a', 'b', 'c']
    if not letter in letters_selection:
        raise ValueError("It is not a Pnn2 wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[6]
    else:
        return parameter[0]

def sp_35_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f']
    if not letter in letters_selection:
        raise ValueError("It is not a Cmm2 wyckoff position!")
    elif letter in ['a', 'b', 'c']:
        return parameter[6]
    elif letter in ['d']:
        return parameter[2]
    elif letter in ['e']:
        return parameter[3]
    else:
        return parameter[0]

def sp_36_parameter(letter):
    letters_selection = ['a', 'b']
    if not letter in letters_selection:
        raise ValueError("It is not a Cmc2_1 wyckoff position!")
    elif letter in ['a']:
        return parameter[3]
    else:
        return parameter[0]

def sp_37_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd']
    if not letter in letters_selection:
        raise ValueError("It is not a Ccc2 wyckoff position!")
    elif letter in ['a', 'b', 'c']:
        return parameter[6]
    else:
        return parameter[0]

def sp_38_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f']
    if not letter in letters_selection:
        raise ValueError("It is not a Amm2 wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[6]
    elif letter in ['c']:
        return parameter[2]
    elif letter in ['d', 'e']:
        return parameter[3]
    else:
        return parameter[0]

def sp_39_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd']
    if not letter in letters_selection:
        raise ValueError("It is not a Aem2 wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[6]
    elif letter in ['c']:
        return parameter[2]
    else:
        return parameter[0]

def sp_40_parameter(letter):
    letters_selection = ['a', 'b', 'c']
    if not letter in letters_selection:
        raise ValueError("It is not a Ama2 wyckoff position!")
    elif letter in ['a']:
        return parameter[6]
    elif letter in ['b']:
        return parameter[3]
    else:
        return parameter[0]

def sp_41_parameter(letter):
    letters_selection = ['a', 'b']
    if not letter in letters_selection:
        raise ValueError("It is not a Aea2 wyckoff position!")
    elif letter in ['a']:
        return parameter[6]
    else:
        return parameter[0]

def sp_42_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e']
    if not letter in letters_selection:
        raise ValueError("It is not a Fmm2 wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[6]
    elif letter in ['c']:
        return parameter[3]
    elif letter in ['d']:
        return parameter[2]
    else:
        return parameter[0]

def sp_43_parameter(letter):
    letters_selection = ['a', 'b']
    if not letter in letters_selection:
        raise ValueError("It is not a Fdd2 wyckoff position!")
    elif letter in ['a']:
        return parameter[6]
    else:
        return parameter[0]

def sp_44_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e']
    if not letter in letters_selection:
        raise ValueError("It is not a Imm2 wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[6]
    elif letter in ['c']:
        return parameter[2]
    elif letter in ['d']:
        return parameter[3]
    else:
        return parameter[0]

def sp_45_parameter(letter):
    letters_selection = ['a', 'b', 'c']
    if not letter in letters_selection:
        raise ValueError("It is not a Iba2 wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[6]
    else:
        return parameter[0]

def sp_46_parameter(letter):
    letters_selection = ['a', 'b', 'c']
    if not letter in letters_selection:
        raise ValueError("It is not a Ima2 wyckoff position!")
    elif letter in 'a':
        return parameter[6]
    elif letter in 'b':
        return parameter[3]
    else:
        return parameter[0]

def sp_47_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A']
    if not letter in letters_selection:
        raise ValueError("It is not a Pmmm wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
        return parameter[7]
    elif letter in ['i', 'j', 'k', 'l']:
        return parameter[4]
    elif letter in ['m', 'n', 'o', 'p']:
        return parameter[5]
    elif letter in ['q', 'r', 's', 't']:
        return parameter[6]
    elif letter in ['u', 'v']:
        return parameter[3]
    elif letter in ['w', 'x']:
        return parameter[2]
    elif letter in ['y', 'z']:
        return parameter[1]
    else:
        return parameter[0]

def sp_48_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    if not letter in letters_selection:
        raise ValueError("It is not a Pnnn wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd', 'e', 'f']:
        return parameter[7]
    elif letter in ['g', 'h']:
        return parameter[4]
    elif letter in ['i', 'j']:
        return parameter[5]
    elif letter in ['k', 'l']:
        return parameter[6]
    else:
        return parameter[0]

def sp_49_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r']
    if not letter in letters_selection:
        raise ValueError("It is not a Pccm wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
        return parameter[7]
    elif letter in ['i', 'j']:
        return parameter[4]
    elif letter in ['k', 'l']:
        return parameter[5]
    elif letter in ['m', 'n', 'o', 'p']:
        return parameter[6]
    elif letter in ['q']:
        return parameter[1]
    else:
        return parameter[0]

def sp_50_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    if not letter in letters_selection:
        raise ValueError("It is not a Pban wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd', 'e', 'f']:
        return parameter[7]
    elif letter in ['g', 'h']:
        return parameter[4]
    elif letter in ['i', 'j']:
        return parameter[5]
    elif letter in ['k', 'l']:
        return parameter[6]
    else:
        return parameter[0]

def sp_51_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    if not letter in letters_selection:
        raise ValueError("It is not a Pmma wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'f']:
        return parameter[6]
    elif letter in ['g', 'h']:
        return parameter[5]
    elif letter in ['i', 'j']:
        return parameter[2]
    elif letter in ['k']:
        return parameter[3]
    else:
        return parameter[0]

def sp_52_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e']
    if not letter in letters_selection:
        raise ValueError("It is not a Pnna wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[7]
    elif letter in ['c']:
        return parameter[6]
    elif letter in ['d']:
        return parameter[4]
    else:
        return parameter[0]

def sp_53_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    if not letter in letters_selection:
        raise ValueError("It is not a Pmna wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'f']:
        return parameter[4]
    elif letter in ['g']:
        return parameter[5]
    elif letter in ['h']:
        return parameter[3]
    else:
        return parameter[0]

def sp_54_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f']
    if not letter in letters_selection:
        raise ValueError("It is not a Pcca wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[7]
    elif letter in ['c']:
        return parameter[5]
    elif letter in ['d', 'e']:
        return parameter[6]
    else:
        return parameter[0]

def sp_55_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    if not letter in letters_selection:
        raise ValueError("It is not a Pbam wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'f']:
        return parameter[6]
    elif letter in ['g', 'h']:
        return parameter[1]
    else:
        return parameter[0]

def sp_56_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e']
    if not letter in letters_selection:
        raise ValueError("It is not a Pccn wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[7]
    elif letter in ['c', 'd']:
        return parameter[6]
    else:
        return parameter[0]

def sp_57_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e']
    if not letter in letters_selection:
        raise ValueError("It is not a Pbcm wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[7]
    elif letter in ['c']:
        return parameter[4]
    elif letter in ['d']:
        return parameter[1]
    else:
        return parameter[0]

def sp_58_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    if not letter in letters_selection:
        raise ValueError("It is not a Pnnm wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'f']:
        return parameter[6]
    elif letter in ['g']:
        return parameter[1]
    else:
        return parameter[0]

def sp_59_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    if not letter in letters_selection:
        raise ValueError("It is not a Pmmn wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[6]
    elif letter in ['c', 'd']:
        return parameter[7]
    elif letter in ['e']:
        return parameter[3]
    elif letter in ['f']:
        return parameter[2]
    else:
        return parameter[0]

def sp_60_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd']
    if not letter in letters_selection:
        raise ValueError("It is not a Pbcn wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[7]
    elif letter in ['c']:
        return parameter[5]
    else:
        return parameter[0]

def sp_61_parameter(letter):
    letters_selection = ['a', 'b', 'c']
    if not letter in letters_selection:
        raise ValueError("It is not a Pbca wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[7]
    else:
        return parameter[0]

def sp_62_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd']
    if not letter in letters_selection:
        raise ValueError("It is not a Pnma wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[7]
    elif letter in ['c']:
        return parameter[2]
    else:
        return parameter[0]

def sp_63_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    if not letter in letters_selection:
        raise ValueError("It is not a Cmcm wyckoff position!")
    elif letter in ['a', 'b', 'd']:
        return parameter[7]
    elif letter in ['c']:
        return parameter[5]
    elif letter in ['e']:
        return parameter[4]
    elif letter in ['f']:
        return parameter[3]
    elif letter in ['g']:
        return parameter[1]
    else:
        return parameter[0]

def sp_64_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    if not letter in letters_selection:
        raise ValueError("It is not a Cmce wyckoff position!")
    elif letter in ['a', 'b', 'c']:
        return parameter[7]
    elif letter in ['d']:
        return parameter[4]
    elif letter in ['e']:
        return parameter[5]
    elif letter in ['f']:
        return parameter[3]
    else:
        return parameter[0]

def sp_65_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r']
    if not letter in letters_selection:
        raise ValueError("It is not a Cmmm wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd', 'e', 'f']:
        return parameter[7]
    elif letter in ['g', 'h']:
        return parameter[4]
    elif letter in ['i', 'j']:
        return parameter[5]
    elif letter in ['k', 'l', 'm']:
        return parameter[6]
    elif letter in ['n']:
        return parameter[3]
    elif letter in ['o']:
        return parameter[2]
    elif letter in ['p', 'q']:
        return parameter[1]
    else:
        return parameter[0]

def sp_66_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    if not letter in letters_selection:
        raise ValueError("It is not a Cccm wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd', 'e', 'f']:
        return parameter[7]
    elif letter in ['g']:
        return parameter[4]
    elif letter in ['h']:
        return parameter[5]
    elif letter in ['i', 'j', 'k']:
        return parameter[6]
    elif letter in ['l']:
        return parameter[1]
    else:
        return parameter[0]

def sp_67_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
    if not letter in letters_selection:
        raise ValueError("It is not a Cmme wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd', 'e', 'f']:
        return parameter[7]
    elif letter in ['g', 'l']:
        return parameter[6]
    elif letter in ['h', 'i']:
        return parameter[4]
    elif letter in ['j', 'k']:
        return parameter[5]
    elif letter in ['m']:
        return parameter[3]
    elif letter in ['n']:
        return parameter[2]
    else:
        return parameter[0]

def sp_68_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    if not letter in letters_selection:
        raise ValueError("It is not a Ccce wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e']:
        return parameter[4]
    elif letter in ['f']:
        return parameter[5]
    elif letter in ['g', 'h']:
        return parameter[6]
    else:
        return parameter[0]

def sp_69_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    if not letter in letters_selection:
        raise ValueError("It is not a Fmmm wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd', 'e', 'f']:
        return parameter[7]
    elif letter in ['g', 'l']:
        return parameter[4]
    elif letter in ['h', 'k']:
        return parameter[5]
    elif letter in ['i', 'j']:
        return parameter[6]
    elif letter in ['m']:
        return parameter[3]
    elif letter in ['n']:
        return parameter[2]
    elif letter in ['o']:
        return parameter[1]
    else:
        return parameter[0]

def sp_70_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    if not letter in letters_selection:
        raise ValueError("It is not a Fddd wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e']:
        return parameter[4]
    elif letter in ['f']:
        return parameter[5]
    elif letter in ['g']:
        return parameter[6]
    else:
        return parameter[0]

def sp_71_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
    if not letter in letters_selection:
        raise ValueError("It is not a Immm wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd', 'k']:
        return parameter[7]
    elif letter in ['e', 'f']:
        return parameter[4]
    elif letter in ['g', 'h']:
        return parameter[5]
    elif letter in ['i', 'j']:
        return parameter[6]
    elif letter in ['l']:
        return parameter[3]
    elif letter in ['m']:
        return parameter[2]
    elif letter in ['n']:
        return parameter[1]
    else:
        return parameter[0]

def sp_72_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    if not letter in letters_selection:
        raise ValueError("It is not a Ibam wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd', 'e']:
        return parameter[7]
    elif letter in ['f']:
        return parameter[4]
    elif letter in ['g']:
        return parameter[5]
    elif letter in ['h', 'i']:
        return parameter[6]
    elif letter in ['j']:
        return parameter[1]
    else:
        return parameter[0]

def sp_73_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f']
    if not letter in letters_selection:
        raise ValueError("It is not a Ibca wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[7]
    elif letter in ['c']:
        return parameter[4]
    elif letter in ['d']:
        return parameter[5]
    elif letter in ['e']:
        return parameter[6]
    else:
        return parameter[0]

def sp_74_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    if not letter in letters_selection:
        raise ValueError("It is not a Imma wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e']:
        return parameter[6]
    elif letter in ['f']:
        return parameter[4]
    elif letter in ['g']:
        return parameter[5]
    elif letter in ['h']:
        return parameter[3]
    elif letter in ['i']:
        return parameter[2]
    else:
        return parameter[0]

def sp_75_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd']
    if not letter in letters_selection:
        raise ValueError("It is not a P4 wyckoff position!")
    elif letter in ['a', 'b', 'c']:
        return parameter[6]
    else:
        return parameter[0]

def sp_76_parameter(letter):
    letters_selection = ['a']
    if not letter in letters_selection:
        raise ValueError("It is not a P4_1 wyckoff position!")
    else:
        return parameter[0]

def sp_77_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd']
    if not letter in letters_selection:
        raise ValueError("It is not a P4_2 wyckoff position!")
    elif letter in ['a', 'b', 'c']:
        return parameter[6]
    else:
        return parameter[0]

def sp_78_parameter(letter):
    letters_selection = ['a']
    if not letter in letters_selection:
        raise ValueError("It is not a P4_3 wyckoff position!")
    else:
        return parameter[0]

def sp_79_parameter(letter):
    letters_selection = ['a', 'b', 'c']
    if not letter in letters_selection:
        raise ValueError("It is not a I4 wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[6]
    else:
        return parameter[0]

def sp_80_parameter(letter):
    letters_selection = ['a', 'b']
    if not letter in letters_selection:
        raise ValueError("It is not a I4_1 wyckoff position!")
    elif letter in ['a']:
        return parameter[6]
    else:
        return parameter[0]

def sp_81_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    if not letter in letters_selection:
        raise ValueError("It is not a P-4 wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'f', 'g']:
        return parameter[6]
    else:
        return parameter[0]

def sp_82_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    if not letter in letters_selection:
        raise ValueError("It is not a I-4 wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'f'] :
        return parameter[6]
    else:
        return parameter[0]

def sp_83_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    if not letter in letters_selection:
        raise ValueError("It is not a P4/m wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd', 'e', 'f']:
        return parameter[7]
    elif letter in ['g', 'h', 'i']:
        return parameter[6]
    elif letter in ['j', 'k']:
        return parameter[1]
    else:
        return parameter[0]

def sp_84_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    if not letter in letters_selection:
        raise ValueError("It is not a P4_2/m wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd', 'e', 'f']:
        return parameter[7]
    elif letter in ['g', 'h', 'i']:
        return parameter[6]
    elif letter in ['j']:
        return parameter[1]
    else:
        return parameter[0]

def sp_85_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    if not letter in letters_selection:
        raise ValueError("It is not a P4/n wyckoff position!")
    elif letter in ['a', 'b', 'd', 'e']:
        return parameter[7]
    elif letter in ['c', 'f']:
        return parameter[6]
    else:
        return parameter[0]

def sp_86_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    if not letter in letters_selection:
        raise ValueError("It is not a P4_2/n wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'f']:
        return parameter[6]
    else:
        return parameter[0]

def sp_87_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    if not letter in letters_selection:
        raise ValueError("It is not a I4/m wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd', 'f']:
        return parameter[7]
    elif letter in ['e', 'g']:
        return parameter[6]
    elif letter in ['h']:
        return parameter[1]
    else:
        return parameter[0]

def sp_88_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f']
    if not letter in letters_selection:
        raise ValueError("It is not a I4_1/a wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e']:
        return parameter[6]
    else:
        return parameter[0]

def sp_89_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    if not letter in letters_selection:
        raise ValueError("It is not a P422 wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd', 'e', 'f']:
        return parameter[7]
    elif letter in ['g', 'h', 'i']:
        return parameter[6]
    elif letter in ['j', 'k', 'l', 'm', 'n', 'o']:
        return parameter[4]
    else:
        return parameter[0]

def sp_90_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    if not letter in letters_selection:
        raise ValueError("It is not a P42_12 wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[7]
    elif letter in ['c', 'd']:
        return parameter[6]
    elif letter in ['e', 'f']:
        return parameter[4]
    else:
        return parameter[0]

def sp_91_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd']
    if not letter in letters_selection:
        raise ValueError("It is not a P4_122 wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[5]
    elif letter in ['c']:
        return parameter[4]
    else:
        return parameter[0]

def sp_92_parameter(letter):
    letters_selection = ['a', 'b']
    if not letter in letters_selection:
        raise ValueError("It is not a P4_12_12 wyckoff position!")
    elif letter in ['a']:
        return parameter[1]
    else:
        return parameter[0]

def sp_93_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    if not letter in letters_selection:
        raise ValueError("It is not a P4_222 wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd', 'e', 'f']:
        return parameter[7]
    elif letter in ['g', 'h', 'i']:
        return parameter[6]
    elif letter in ['j', 'k', 'l', 'm', 'n', 'o']:
        return parameter[4]
    else:
        return parameter[0]

def sp_94_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    if not letter in letters_selection:
        raise ValueError("It is not a P4_22_12 wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[7]
    elif letter in ['c', 'd']:
        return parameter[6]
    elif letter in ['e', 'f']:
        return parameter[4]
    else:
        return parameter[0]

def sp_95_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd']
    if not letter in letters_selection:
        raise ValueError("It is not a P4_322 wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[5]
    elif letter in ['c']:
        return parameter[4]
    else:
        return parameter[0]

def sp_96_parameter(letter):
    letters_selection = ['a', 'b']
    if not letter in letters_selection:
        raise ValueError("It is not a P4_32_12 wyckoff position!")
    elif letter in ['a']:
        return parameter[1]
    else:
        return parameter[0]

def sp_97_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    if not letter in letters_selection:
        raise ValueError("It is not a I422 wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'f']:
        return parameter[6]
    elif letter in ['g', 'h', 'i', 'j']:
        return parameter[4]
    else:
        return parameter[0]

def sp_98_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    if not letter in letters_selection:
        raise ValueError("It is not a I4_122 wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[7]
    elif letter in ['c']:
        return parameter[6]
    elif letter in ['d', 'e', 'f']:
        return parameter[4]
    else:
        return parameter[0]

def sp_99_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    if not letter in letters_selection:
        raise ValueError("It is not a P4mm wyckoff position!")
    elif letter in ['a', 'b', 'c']:
        return parameter[6]
    elif letter in ['d', 'e', 'f']:
        return parameter[2]
    else:
        return parameter[0]

def sp_100_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd']
    if not letter in letters_selection:
        raise ValueError("It is not a P4bm wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[6]
    elif letter in ['c']:
        return parameter[2]
    else:
        return parameter[0]

def sp_101_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e']
    if not letter in letters_selection:
        raise ValueError("It is not a P4_2cm wyckoff position!")
    elif letter in ['a', 'b', 'c']:
        return parameter[6]
    elif letter in ['d']:
        return parameter[2]
    else:
        return parameter[0]

def sp_102_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd']
    if not letter in letters_selection:
        raise ValueError("It is not a P4_2nm wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[6]
    elif letter in 'c':
        return parameter[2]
    else:
        return parameter[0]

def sp_103_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd']
    if not letter in letters_selection:
        raise ValueError("It is not a P4cc wyckoff position!")
    elif letter in ['a', 'b', 'c']:
        return parameter[6]
    else:
        return parameter[0]

def sp_104_parameter(letter):
    letters_selection = ['a', 'b', 'c']
    if not letter in letters_selection:
        raise ValueError("It is not a P4nc wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[6]
    else:
        return parameter[0]

def sp_105_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f']
    if not letter in letters_selection:
        raise ValueError("It is not a P4_2mc wyckoff position!")
    elif letter in ['a', 'b', 'c']:
        return parameter[6]
    elif letter in ['d', 'e']:
        return parameter[2]
    else:
        return parameter[0]

def sp_106_parameter(letter):
    letters_selection = ['a', 'b', 'c']
    if not letter in letters_selection:
        raise ValueError("It is not a P4_2bc wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[6]
    else:
        return parameter[0]

def sp_107_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e']
    if not letter in letters_selection:
        raise ValueError("It is not a I4mm wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[6]
    elif letter in ['c', 'd']:
        return parameter[2]
    else:
        return parameter[0]

def sp_108_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd']
    if not letter in letters_selection:
        raise ValueError("It is not a I4cm wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[6]
    elif letter in ['c']:
        return parameter[2]
    else:
        return parameter[0]

def sp_109_parameter(letter):
    letters_selection = ['a', 'b', 'c']
    if not letter in letters_selection:
        raise ValueError("It is not a I4_1md wyckoff position!")
    elif letter in ['a']:
        return parameter[6]
    elif letter in ['b']:
        return parameter[3]
    else:
        return parameter[0]

def sp_110_parameter(letter):
    letters_selection = ['a', 'b']
    if not letter in letters_selection:
        raise ValueError("It is not a I4_1cd wyckoff position!")
    elif letter in ['a']:
        return parameter[6]
    else:
        return parameter[0]

def sp_111_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
    if not letter in letters_selection:
        raise ValueError("It is not a P-42m wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd', 'e', 'f']:
        return parameter[7]
    elif letter in ['g', 'h', 'm']:
        return parameter[6]
    elif letter in ['i', 'j', 'k', 'l']:
        return parameter[4]
    elif letter in ['n']:
        return parameter[2]
    else:
        return parameter[0]

def sp_112_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
    if not letter in letters_selection:
        raise ValueError("It is not a P-42c wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd', 'e', 'f']:
        return parameter[7]
    elif letter in ['g', 'i']:
        return parameter[4]
    elif letter in ['h', 'j']:
        return parameter[5]
    elif letter in ['k', 'l', 'm']:
        return parameter[6]
    else:
        return parameter[0]

def sp_113_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f']
    if not letter in letters_selection:
        raise ValueError("It is not a P-42_1m wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[7]
    elif letter in ['c', 'd']:
        return parameter[6]
    elif letter in ['e']:
        return parameter[2]
    else:
        return parameter[0]

def sp_114_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e']
    if not letter in letters_selection:
        raise ValueError("It is not a P-42_1c wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[7]
    elif letter in ['c', 'd']:
        return parameter[6]
    else:
        return parameter[0]

def sp_115_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    if not letter in letters_selection:
        raise ValueError("It is not a P-4m2 wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'f', 'g']:
        return parameter[6]
    elif letter in ['h', 'i']:
        return parameter[4]
    elif letter in ['j', 'k']:
        return parameter[2]
    else:
        return parameter[0]

def sp_116_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    if not letter in letters_selection:
        raise ValueError("It is not a P-4c2 wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'f']:
        return parameter[4]
    elif letter in ['g', 'h', 'i']:
        return parameter[6]
    else:
        return parameter[0]

def sp_117_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    if not letter in letters_selection:
        raise ValueError("It is not a P-4b2 wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'f']:
        return parameter[6]
    elif letter in ['g', 'h']:
        return parameter[4]
    else:
        return parameter[0]

def sp_118_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    if not letter in letters_selection:
        raise ValueError("It is not a P-4n2 wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'h']:
        return parameter[6]
    elif letter in ['f', 'g']:
        return parameter[4]
    else:
        return parameter[0]

def sp_119_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    if not letter in letters_selection:
        raise ValueError("It is not a I-4m2 wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'f']:
        return parameter[6]
    elif letter in ['g', 'h']:
        return parameter[4]
    elif letter in ['i']:
        return parameter[2]
    else:
        return parameter[0]

def sp_120_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    if not letter in letters_selection:
        raise ValueError("It is not a I-4c2 wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'h']:
        return parameter[4]
    elif letter in ['f', 'g']:
        return parameter[6]
    else:
        return parameter[0]

def sp_121_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    if not letter in letters_selection:
        raise ValueError("It is not a I-42m wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'h']:
        return parameter[6]
    elif letter in ['f', 'g']:
        return parameter[4]
    elif letter in ['i']:
        return parameter[2]
    else:
        return parameter[0]

def sp_122_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e']
    if not letter in letters_selection:
        raise ValueError("It is not a I-42d wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[7]
    elif letter in ['c']:
        return parameter[6]
    elif letter in ['d']:
        return parameter[4]
    else:
        return parameter[0]

def sp_123_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u']
    if not letter in letters_selection:
        raise ValueError("It is not a P4/mmm wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd', 'e', 'f']:
        return parameter[7]
    elif letter in ['g', 'h', 'i']:
        return parameter[6]
    elif letter in ['j', 'k', 'l', 'm', 'n', 'o']:
        return parameter[4]
    elif letter in ['p', 'q']:
        return parameter[1]
    elif letter in ['r', 's', 't']:
        return parameter[2]
    else:
        return parameter[0]

def sp_124_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
    if not letter in letters_selection:
        raise ValueError("It is not a P4/mcc wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd', 'e', 'f']:
        return parameter[7]
    elif letter in ['g', 'h', 'i']:
        return parameter[6]
    elif letter in ['j', 'k', 'l']:
        return parameter[4]
    elif letter in ['m']:
        return parameter[1]
    else:
        return parameter[0]

def sp_125_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
    if not letter in letters_selection:
        raise ValueError("It is not a P4/nbm wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd', 'e', 'f']:
        return parameter[7]
    elif letter in ['g', 'h']:
        return parameter[6]
    elif letter in ['i', 'j', 'k', 'l']:
        return parameter[4]
    elif letter in ['m']:
        return parameter[2]
    else:
        return parameter[0]

def sp_126_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    if not letter in letters_selection:
        raise ValueError("It is not a P4/nnc wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd', 'f']:
        return parameter[7]
    elif letter in ['e', 'g']:
        return parameter[6]
    elif letter in ['h', 'i', 'j']:
        return parameter[4]
    else:
        return parameter[0]

def sp_127_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    if not letter in letters_selection:
        raise ValueError("It is not a P4/mbm wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'f']:
        return parameter[6]
    elif letter in ['g', 'h']:
        return parameter[4]
    elif letter in ['i', 'j']:
        return parameter[1]
    elif letter in ['k']:
        return parameter[2]
    else:
        return parameter[0]

def sp_128_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    if not letter in letters_selection:
        raise ValueError("It is not a P4/mnc wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'f']:
        return parameter[6]
    elif letter in ['g']:
        return parameter[4]
    elif letter in ['h']:
        return parameter[1]
    else:
        return parameter[0]

def sp_129_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    if not letter in letters_selection:
        raise ValueError("It is not a P4/nmm wyckoff position!")
    elif letter in ['a', 'b', 'd', 'e']:
        return parameter[7]
    elif letter in ['c', 'f']:
        return parameter[6]
    elif letter in ['g', 'h']:
        return parameter[4]
    elif letter in ['i']:
        return parameter[3]
    elif letter in ['j']:
        return parameter[2]
    else:
        return parameter[0]

def sp_130_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    if not letter in letters_selection:
        raise ValueError("It is not a P4/ncc wyckoff position!")
    elif letter in ['a', 'b', 'd']:
        return parameter[7]
    elif letter in ['c', 'e']:
        return parameter[6]
    elif letter in 'f':
        return parameter[4]
    else:
        return parameter[0]

def sp_131_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r']
    if not letter in letters_selection:
        raise ValueError("It is not a P4_2/mmc wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd', 'e', 'f']:
        return parameter[7]
    elif letter in ['g', 'h', 'i']:
        return parameter[6]
    elif letter in ['j', 'k', 'l', 'm', 'n']:
        return parameter[4]
    elif letter in ['o', 'p']:
        return parameter[3]
    elif letter in ['q']:
        return parameter[1]
    else:
        return parameter[0]

def sp_132_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    if not letter in letters_selection:
        raise ValueError("It is not a P4_2/mcm wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd', 'e', 'f']:
        return parameter[7]
    elif letter in ['g', 'h']:
        return parameter[6]
    elif letter in ['i', 'j', 'l', 'm']:
        return parameter[4]
    elif letter in ['k']:
        return parameter[6]
    elif letter in ['n']:
        return parameter[1]
    elif letter in ['o']:
        return parameter[2]
    else:
        return parameter[0]

def sp_133_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    if not letter in letters_selection:
        raise ValueError("It is not a P4_2/nbc wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd', 'e']:
        return parameter[7]
    elif letter in ['f', 'g']:
        return parameter[6]
    elif letter in ['h', 'i', 'j']:
        return parameter[4]
    else:
        return parameter[0]

def sp_134_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
    if not letter in letters_selection:
        raise ValueError("It is not a P4_2/nnm wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd', 'e', 'f']:
        return parameter[7]
    elif letter in ['g', 'h']:
        return parameter[6]
    elif letter in ['i', 'j', 'k', 'l']:
        return parameter[4]
    elif letter in ['m']:
        return parameter[2]
    else:
        return parameter[0]

def sp_135_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    if not letter in letters_selection:
        raise ValueError("It is not a P4_2/mbc wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'f']:
        return parameter[6]
    elif letter in ['g']:
        return parameter[4]
    elif letter in ['h']:
        return parameter[1]
    else:
        return parameter[0]

def sp_136_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    if not letter in letters_selection:
        raise ValueError("It is not a P4_2/mnm wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'h']:
        return parameter[6]
    elif letter in ['f', 'g']:
        return parameter[4]
    elif letter in ['i']:
        return parameter[1]
    elif letter in ['j']:
        return parameter[2]
    else:
        return parameter[0]

def sp_137_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    if not letter in letters_selection:
        raise ValueError("It is not a P4_2/nmc wyckoff position!")
    elif letter in ['a', 'b', 'e']:
        return parameter[7]
    elif letter in ['c', 'd']:
        return parameter[6]
    elif letter in ['f']:
        return parameter[4]
    elif letter in ['g']:
        return parameter[3]
    else:
        return parameter[0]

def sp_138_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    if not letter in letters_selection:
        raise ValueError("It is not a P4_2/ncm wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'f']:
        return parameter[6]
    elif letter in ['g', 'h']:
        return parameter[4]
    elif letter in ['i']:
        return parameter[2]
    else:
        return parameter[0]

def sp_139_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
    if not letter in letters_selection:
        raise ValueError("It is not a I4/mmm wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd', 'f']:
        return parameter[7]
    elif letter in ['e', 'g']:
        return parameter[6]
    elif letter in ['h', 'i', 'j', 'k']:
        return parameter[4]
    elif letter in ['l']:
        return parameter[1]
    elif letter in ['m']:
        return parameter[2]
    elif letter in ['n']:
        return parameter[3]
    else:
        return parameter[0]

def sp_140_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    if not letter in letters_selection:
        raise ValueError("It is not a I4/mcm wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd', 'e']:
        return parameter[7]
    elif letter in ['f', 'g']:
        return parameter[6]
    elif letter in ['h', 'i', 'j']:
        return parameter[4]
    elif letter in ['k']:
        return parameter[1]
    elif letter in ['l']:
        return parameter[2]
    else:
        return parameter[0]

def sp_141_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    if not letter in letters_selection:
        raise ValueError("It is not a I4_1/amd wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e']:
        return parameter[6]
    elif letter in ['f', 'g']:
        return parameter[4]
    elif letter in ['h']:
        return parameter[3]
    else:
        return parameter[0]

def sp_142_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    if not letter in letters_selection:
        raise ValueError("It is not a I4_1/acd wyckoff position!")
    elif letter in ['a', 'b', 'c']:
        return parameter[7]
    elif letter in ['d']:
        return parameter[6]
    elif letter in ['e']:
        return parameter[5]
    elif letter in ['f']:
        return parameter[4]
    else:
        return parameter[0]

def sp_143_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd']
    if not letter in letters_selection:
        raise ValueError("It is not a P3 wyckoff position!")
    elif letter in ['a', 'b', 'c']:
        return parameter[6]
    else:
        return parameter[0]

def sp_144_parameter(letter):
    letters_selection = ['a']
    if not letter in letters_selection:
        raise ValueError("It is not a P3_1 wyckoff position!")
    else:
        return parameter[0]

def sp_145_parameter(letter):
    letters_selection = ['a']
    if not letter in letters_selection:
        raise ValueError("It is not a P3_2 wyckoff position!")
    else:
        return parameter[0]

def sp_146_R_parameter(letter):
    letters_selection = ['a', 'b']
    if not letter in letters_selection:
        raise ValueError("It is not a R3 wyckoff position!")
    elif letter in ['a']:
        return parameter[4]
    else:
        return parameter[0]

def sp_146_H_parameter(letter):
    letters_selection = ['a', 'b']
    if not letter in letters_selection:
        raise ValueError("It is not a R3H wyckoff position!")
    elif letter in ['a']:
        return parameter[6]
    else:
        return parameter[0]

def sp_147_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    if not letter in letters_selection:
        raise ValueError("It is not a P-3 wyckoff position!")
    elif letter in ['a', 'b', 'e', 'f']:
        return parameter[7]
    elif letter in ['c', 'd']:
        return parameter[6]
    else:
        return parameter[0]

def sp_148_R_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f']
    if not letter in letters_selection:
        raise ValueError("It is not a R-3 wyckoff position!")
    elif letter in ['a', 'b', 'd', 'e']:
        return parameter[7]
    elif letter in ['c']:
        return parameter[4]
    else:
        return parameter[0]

def sp_148_H_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f']
    if not letter in letters_selection:
        raise ValueError("It is not a R-3 wyckoff position!")
    elif letter in ['a', 'b', 'd', 'e']:
        return parameter[7]
    elif letter in ['c']:
        return parameter[6]
    else:
        return parameter[0]

def sp_149_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    if not letter in letters_selection:
        raise ValueError("It is not a P312 wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd', 'e', 'f']:
        return parameter[7]
    elif letter in ['g', 'h', 'i']:
        return parameter[6]
    elif letter in ['j', 'k']:
        return parameter[4]
    else:
        return parameter[0]

def sp_150_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    if not letter in letters_selection:
        raise ValueError("It is not a P321 wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[7]
    elif letter in ['c', 'd']:
        return parameter[6]
    elif letter in ['e', 'f']:
        return parameter[4]
    else:
        return parameter[0]

def sp_151_parameter(letter):
    letters_selection = ['a', 'b', 'c']
    if not letter in letters_selection:
        raise ValueError("It is not a P3_112 wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[4]
    else:
        return parameter[0]

def sp_152_parameter(letter):
    letters_selection = ['a', 'b', 'c']
    if not letter in letters_selection:
        raise ValueError("It is not a P3_121 wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[4]
    else:
        return parameter[0]

def sp_153_parameter(letter):
    letters_selection = ['a', 'b', 'c']
    if not letter in letters_selection:
        raise ValueError("It is not a P3_212 wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[4]
    else:
        return parameter[0]

def sp_154_parameter(letter):
    letters_selection = ['a', 'b', 'c']
    if not letter in letters_selection:
        raise ValueError("It is not a P3_221 wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[4]
    else:
        return parameter[0]

def sp_155_R_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f']
    if not letter in letters_selection:
        raise ValueError("It is not a R32 wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[7]
    elif letter in ['c']:
        return parameter[4]
    elif letter in ['d', 'e']:
        return parameter[5]
    else:
        return parameter[0]

def sp_155_H_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f']
    if not letter in letters_selection:
        raise ValueError("It is not a R32H wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[7]
    elif letter in ['c']:
        return parameter[6]
    elif letter in ['d', 'e']:
        return parameter[4]
    else:
        return parameter[0]

def sp_156_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e']
    if not letter in letters_selection:
        raise ValueError("It is not a P3m1 wyckoff position!")
    elif letter in ['a', 'b', 'c']:
        return parameter[6]
    elif letter in ['d']:
        return parameter[2]
    else:
        return parameter[0]

def sp_157_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd']
    if not letter in letters_selection:
        raise ValueError("It is not a P31m wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[6]
    elif letter in ['c']:
        return parameter[2]
    else:
        return parameter[0]

def sp_158_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd']
    if not letter in letters_selection:
        raise ValueError("It is not a P3c1 wyckoff position!")
    elif letter in ['a', 'b', 'c']:
        return parameter[6]
    else:
        return parameter[0]

def sp_159_parameter(letter):
    letters_selection = ['a', 'b', 'c']
    if not letter in letters_selection:
        raise ValueError("It is not a P31c wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[6]
    else:
        return parameter[0]

def sp_160_R_parameter(letter):
    letters_selection = ['a', 'b', 'c']
    if not letter in letters_selection:
        raise ValueError("It is not a R3m wyckoff position!")
    elif letter in ['a']:
        return parameter[4]
    elif letter in ['b']:
        return parameter[2]
    else:
        return parameter[0]

def sp_160_H_parameter(letter):
    letters_selection = ['a', 'b', 'c']
    if not letter in letters_selection:
        raise ValueError("It is not a R3mH wyckoff position!")
    elif letter in ['a']:
        return parameter[6]
    elif letter in ['b']:
        return parameter[2]
    else:
        return parameter[0]

def sp_161_R_parameter(letter):
    letters_selection = ['a', 'b']
    if not letter in letters_selection:
        raise ValueError("It is not a R3c wyckoff position!")
    elif letter in ['a']:
        return parameter[4]
    else:
        return parameter[0]

def sp_161_H_parameter(letter):
    letters_selection = ['a', 'b']
    if not letter in letters_selection:
        raise ValueError("It is not a R3cH wyckoff position!")
    elif letter in ['a']:
        return parameter[6]
    else:
        return parameter[0]

def sp_162_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    if not letter in letters_selection:
        raise ValueError("It is not a P-31m wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd', 'f', 'g']:
        return parameter[7]
    elif letter in ['e', 'h']:
        return parameter[6]
    elif letter in ['i', 'j']:
        return parameter[4]
    elif letter in ['k']:
        return parameter[2]
    else:
        return parameter[0]

def sp_163_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    if not letter in letters_selection:
        raise ValueError("It is not a P-31c wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd', 'g']:
        return parameter[7]
    elif letter in ['e', 'f']:
        return parameter[6]
    elif letter in ['h']:
        return parameter[4]
    else:
        return parameter[0]

def sp_164_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    if not letter in letters_selection:
        raise ValueError("It is not a P-3m1 wyckoff position!")
    elif letter in ['a', 'b', 'e', 'f']:
        return parameter[7]
    elif letter in ['c', 'd']:
        return parameter[6]
    elif letter in ['g', 'h']:
        return parameter[4]
    elif letter in ['i']:
        return parameter[2]
    else:
        return parameter[0]

def sp_165_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    if not letter in letters_selection:
        raise ValueError("It is not a P-3c1 wyckoff position!")
    elif letter in ['a', 'b', 'e']:
        return parameter[7]
    elif letter in ['c', 'd']:
        return parameter[6]
    elif letter in ['f']:
        return parameter[4]
    else:
        return parameter[0]

def sp_166_R_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    if not letter in letters_selection:
        raise ValueError("It is not a R-3m wyckoff position!")
    elif letter in ['a', 'b', 'd', 'e']:
        return parameter[7]
    elif letter in ['c', 'f', 'g']:
        return parameter[4]
    elif letter in ['h']:
        return parameter[2]
    else:
        return parameter[0]

def sp_166_H_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    if not letter in letters_selection:
        raise ValueError("It is not a R-3mH wyckoff position!")
    elif letter in ['a', 'b', 'd', 'e']:
        return parameter[7]
    elif letter in ['c']:
        return parameter[6]
    elif letter in ['f', 'g']:
        return parameter[4]
    elif letter in ['h']:
        return parameter[2]
    else:
        return parameter[0]

def sp_167_parameter_R(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f']
    if not letter in letters_selection:
        raise ValueError("It is not a R-3c wyckoff position!")
    elif letter in ['a', 'b', 'd']:
        return parameter[7]
    elif letter in ['c', 'e']:
        return parameter[4]
    else:
        return parameter[0]

def sp_167_parameter_H(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f']
    if not letter in letters_selection:
        raise ValueError("It is not a R-3cH wyckoff position!")
    elif letter in ['a', 'b', 'd']:
        return parameter[7]
    elif letter in ['c']:
        return parameter[6]
    elif letter in ['e']:
        return parameter[4]
    else:
        return parameter[0]

def sp_168_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd']
    if not letter in letters_selection:
        raise ValueError("It is not a P6 wyckoff position!")
    elif letter in ['a', 'b', 'c']:
        return parameter[6]
    else:
        return parameter[0]

def sp_169_parameter(letter):
    letters_selection = ['a']
    if not letter in letters_selection:
        raise ValueError("It is not a P6_1 wyckoff position!")
    else:
        return parameter[0]

def sp_170_parameter(letter):
    letters_selection = ['a']
    if not letter in letters_selection:
        raise ValueError("It is not a P6_5 wyckoff position!")
    else:
        return parameter[0]

def sp_171_parameter(letter):
    letters_selection = ['a', 'b', 'c']
    if not letter in letters_selection:
        raise ValueError("It is not a P6_2 wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[6]
    else:
        return parameter[0]

def sp_172_parameter(letter):
    letters_selection = ['a', 'b', 'c']
    if not letter in letters_selection:
        raise ValueError("It is not a P6_4 wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[6]
    else:
        return parameter[0]

def sp_173_parameter(letter):
    letters_selection = ['a', 'b', 'c']
    if not letter in letters_selection:
        raise ValueError("It is not a P6_3 wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[6]
    else:
        return parameter[0]

def sp_174_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    if not letter in letters_selection:
        raise ValueError("It is not a P-6 wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd', 'e', 'f']:
        return parameter[7]
    elif letter in ['g', 'h', 'i']:
        return parameter[6]
    elif letter in ['j', 'k']:
        return parameter[1]
    else:
        return parameter[0]

def sp_175_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    if not letter in letters_selection:
        raise ValueError("It is not a P6/m wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd', 'f', 'g']:
        return parameter[7]
    elif letter in ['e', 'h', 'i']:
        return parameter[6]
    elif letter in ['j', 'k']:
        return parameter[1]
    else:
        return parameter[0]

def sp_176_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    if not letter in letters_selection:
        raise ValueError("It is not a P6_3/m wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd', 'g']:
        return parameter[7]
    elif letter in ['e', 'f']:
        return parameter[6]
    elif letter in ['h']:
        return parameter[1]
    else:
        return parameter[0]

def sp_177_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
    if not letter in letters_selection:
        raise ValueError("It is not a P622 wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd', 'f', 'g']:
        return parameter[7]
    elif letter in ['e', 'h', 'i']:
        return parameter[6]
    elif letter in ['j', 'k', 'l', 'm']:
        return parameter[4]
    else:
        return parameter[0]

def sp_178_parameter(letter):
    letters_selection = ['a', 'b', 'c']
    if not letter in letters_selection:
        raise ValueError("It is not a P6_122 wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[4]
    else:
        return parameter[0]

def sp_179_parameter(letter):
    letters_selection = ['a', 'b', 'c']
    if not letter in letters_selection:
        raise ValueError("It is not a P6_522 wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[4]
    else:
        return parameter[0]

def sp_180_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    if not letter in letters_selection:
        raise ValueError("It is not a P6_222 wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'f']:
        return parameter[6]
    elif letter in ['g', 'h', 'i', 'j']:
        return parameter[4]
    else:
        return parameter[0]

def sp_181_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    if not letter in letters_selection:
        raise ValueError("It is not a P6_422 wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'f']:
        return parameter[6]
    elif letter in ['g', 'h', 'i', 'j']:
        return parameter[4]
    else:
        return parameter[0]

def sp_182_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    if not letter in letters_selection:
        raise ValueError("It is not a P6_322 wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'f']:
        return parameter[6]
    elif letter in ['g', 'h']:
        return parameter[4]
    else:
        return parameter[0]

def sp_183_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f']
    if not letter in letters_selection:
        raise ValueError("It is not a P6mm wyckoff position!")
    elif letter in ['a', 'b', 'c']:
        return parameter[6]
    elif letter in ['d', 'e']:
        return parameter[2]
    else:
        return parameter[0]

def sp_184_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd']
    if not letter in letters_selection:
        raise ValueError("It is not a P6cc wyckoff position!")
    elif letter in ['a', 'b', 'c']:
        return parameter[6]
    else:
        return parameter[0]

def sp_185_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd']
    if not letter in letters_selection:
        raise ValueError("It is not a P6_3cm wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[6]
    elif letter in ['c']:
        return parameter[2]
    else:
        return parameter[0]

def sp_186_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd']
    if not letter in letters_selection:
        raise ValueError("It is not a P6_3mc wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[6]
    elif letter in ['c']:
        return parameter[2]
    else:
        return parameter[0]

def sp_187_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
    if not letter in letters_selection:
        raise ValueError("It is not a P-6m2 wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd', 'e', 'f']:
        return parameter[7]
    elif letter in ['g', 'h', 'i']:
        return parameter[6]
    elif letter in ['j', 'k']:
        return parameter[4]
    elif letter in ['l', 'm']:
        return parameter[1]
    elif letter in ['n']:
        return parameter[2]
    else:
        return parameter[0]

def sp_188_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    if not letter in letters_selection:
        raise ValueError("It is not a P-6c2 wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd', 'e', 'f']:
        return parameter[7]
    elif letter in ['g', 'h', 'i']:
        return parameter[6]
    elif letter in ['j']:
        return parameter[4]
    elif letter in ['k']:
        return parameter[1]
    else:
        return parameter[0]

def sp_189_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    if not letter in letters_selection:
        raise ValueError("It is not a P-62m wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'h']:
        return parameter[6]
    elif letter in ['f', 'g']:
        return parameter[4]
    elif letter in ['i']:
        return parameter[2]
    elif letter in ['j', 'k']:
        return parameter[1]
    else:
        return parameter[0]

def sp_190_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    if not letter in letters_selection:
        raise ValueError("It is not a P-62c wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'f']:
        return parameter[6]
    elif letter in ['g']:
        return parameter[4]
    elif letter in ['h']:
        return parameter[1]
    else:
        return parameter[0]

def sp_191_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r']
    if not letter in letters_selection:
        raise ValueError("It is not a P6/mmm wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd', 'f', 'g']:
        return parameter[7]
    elif letter in ['e', 'h', 'i']:
        return parameter[6]
    elif letter in ['j', 'k', 'l', 'm']:
        return parameter[4]
    elif letter in ['n', 'o']:
        return parameter[2]
    elif letter in ['p', 'q']:
        return parameter[1]
    else:
        return parameter[0]

def sp_192_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    if not letter in letters_selection:
        raise ValueError("It is not a P6/mcc wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd', 'f', 'g']:
        return parameter[7]
    elif letter in ['e', 'h', 'i']:
        return parameter[6]
    elif letter in ['j', 'k']:
        return parameter[4]
    elif letter in ['l']:
        return parameter[1]
    else:
        return parameter[0]

def sp_193_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    if not letter in letters_selection:
        raise ValueError("It is not a P6_3/mcm wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd', 'f']:
        return parameter[7]
    elif letter in ['e', 'h']:
        return parameter[6]
    elif letter in ['g', 'i']:
        return parameter[4]
    elif letter in ['j']:
        return parameter[1]
    elif letter in ['k']:
        return parameter[2]
    else:
        return parameter[0]

def sp_194_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    if not letter in letters_selection:
        raise ValueError("It is not a P6_3/mmc wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd', 'g']:
        return parameter[7]
    elif letter in ['e', 'f']:
        return parameter[6]
    elif letter in ['h', 'i']:
        return parameter[4]
    elif letter in ['j']:
        return parameter[1]
    elif letter in ['k']:
        return parameter[2]
    else:
        return parameter[0]

def sp_195_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    if not letter in letters_selection:
        raise ValueError("It is not a P23 wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'f', 'g', 'h', 'i']:
        return parameter[4]
    else:
        return parameter[0]

def sp_196_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    if not letter in letters_selection:
        raise ValueError("It is not a F23 wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'f', 'g']:
        return parameter[4]
    else:
        return parameter[0]

def sp_197_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f']
    if not letter in letters_selection:
        raise ValueError("It is not a I23 wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[7]
    elif letter in ['c', 'd', 'e']:
        return parameter[4]
    else:
        return parameter[0]

def sp_198_parameter(letter):
    letters_selection = ['a', 'b']
    if not letter in letters_selection:
        raise ValueError("It is not a P2_13 wyckoff position!")
    elif letter in ['a']:
        return parameter[4]
    else:
        return parameter[0]

def sp_199_parameter(letter):
    letters_selection = ['a', 'b', 'c']
    if not letter in letters_selection:
        raise ValueError("It is not a I2_13 wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[4]
    else:
        return parameter[0]

def sp_200_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    if not letter in letters_selection:
        raise ValueError("It is not a Pm-3 wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'f', 'g', 'h', 'i']:
        return parameter[4]
    elif letter in ['j', 'k']:
        return parameter[3]
    else:
        return parameter[0]

def sp_201_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    if not letter in letters_selection:
        raise ValueError("It is not a Pn-3 wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'f', 'g']:
        return parameter[4]
    else:
        return parameter[0]

def sp_202_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    if not letter in letters_selection:
        raise ValueError("It is not a Fm-3 wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'f', 'g']:
        return parameter[4]
    elif letter in ['h']:
        return parameter[3]
    else:
        return parameter[0]

def sp_203_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    if not letter in letters_selection:
        raise ValueError("It is not a Fd-3 wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'f']:
        return parameter[4]
    else:
        return parameter[0]

def sp_204_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    if not letter in letters_selection:
        raise ValueError("It is not a Im-3 wyckoff position!")
    elif letter in ['a', 'b', 'c']:
        return parameter[7]
    elif letter in ['d', 'e', 'f']:
        return parameter[4]
    elif letter in ['g']:
        return parameter[3]
    else:
        return parameter[0]

def sp_205_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd']
    if not letter in letters_selection:
        raise ValueError("It is not a Pa-3 wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[7]
    elif letter in ['c']:
        return parameter[4]
    else:
        return parameter[0]

def sp_206_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e']
    if not letter in letters_selection:
        raise ValueError("It is not a Ia-3 wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[7]
    elif letter in ['c', 'd']:
        return parameter[4]
    else:
        return parameter[0]

def sp_207_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    if not letter in letters_selection:
        raise ValueError("It is not a P432 wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'f', 'g', 'h']:
        return parameter[4]
    elif letter in ['i', 'j']:
        return parameter[5]
    else:
        return parameter[0]

def sp_208_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    if not letter in letters_selection:
        raise ValueError("It is not a P4_232 wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd', 'e', 'f']:
        return parameter[7]
    elif letter in ['g', 'h', 'i', 'j']:
        return parameter[4]
    elif letter in ['k', 'l']:
        return parameter[5]
    else:
        return parameter[0]

def sp_209_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    if not letter in letters_selection:
        raise ValueError("It is not a F432 wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'f', 'i']:
        return parameter[4]
    elif letter in ['g', 'h']:
        return parameter[5]
    else:
        return parameter[0]

def sp_210_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    if not letter in letters_selection:
        raise ValueError("It is not a F4_132 wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'f']:
        return parameter[4]
    elif letter in ['g']:
        return parameter[5]
    else:
        return parameter[0]

def sp_211_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    if not letter in letters_selection:
        raise ValueError("It is not a I432 wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'f', 'g']:
        return parameter[4]
    elif letter in ['h', 'i']:
        return parameter[5]
    else:
        return parameter[0]

def sp_212_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e']
    if not letter in letters_selection:
        raise ValueError("It is not a P4_332 wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[7]
    elif letter in ['c']:
        return parameter[4]
    elif letter in ['d']:
        return parameter[5]
    else:
        return parameter[0]

def sp_213_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e']
    if not letter in letters_selection:
        raise ValueError("It is not a P4_132 wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[7]
    elif letter in ['c']:
        return parameter[4]
    elif letter in ['d']:
        return parameter[5]
    else:
        return parameter[0]

def sp_214_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    if not letter in letters_selection:
        raise ValueError("It is not a I4_132 wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'f']:
        return parameter[4]
    elif letter in ['g', 'h']:
        return parameter[5]
    else:
        return parameter[0]

def sp_215_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    if not letter in letters_selection:
        raise ValueError("It is not a P-43m wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'f', 'g', 'h']:
        return parameter[4]
    elif letter in ['i']:
        return parameter[2]
    else:
        return parameter[0]

def sp_216_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    if not letter in letters_selection:
        raise ValueError("It is not a F-43m wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'f', 'g']:
        return parameter[4]
    elif letter in ['h']:
        return parameter[2]
    else:
        return parameter[0]

def sp_217_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    if not letter in letters_selection:
        raise ValueError("It is not a I-43m wyckoff position!")
    elif letter in ['a', 'b', 'd']:
        return parameter[7]
    elif letter in ['c', 'e', 'f']:
        return parameter[4]
    elif letter in ['g']:
        return parameter[2]
    else:
        return parameter[0]

def sp_218_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    if not letter in letters_selection:
        raise ValueError("It is not a P-43n wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'f', 'g', 'h']:
        return parameter[4]
    else:
        return parameter[0]

def sp_219_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    if not letter in letters_selection:
        raise ValueError("It is not a F-43c wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'f', 'g']:
        return parameter[4]
    else:
        return parameter[0]

def sp_220_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e']
    if not letter in letters_selection:
        raise ValueError("It is not a I-43d wyckoff position!")
    elif letter in ['a', 'b']:
        return parameter[7]
    elif letter in ['c', 'd']:
        return parameter[4]
    else:
        return parameter[0]

def sp_221_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
    if not letter in letters_selection:
        raise ValueError("It is not a Pm-3m wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'f', 'g', 'h']:
        return parameter[4]
    elif letter in ['i', 'j']:
        return parameter[5]
    elif letter in ['k', 'l']:
        return parameter[3]
    elif letter in ['m']:
        return parameter[2]
    else:
        return parameter[0]

def sp_222_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    if not letter in letters_selection:
        raise ValueError("It is not a Pn-3n wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'f', 'g']:
        return parameter[4]
    elif letter in ['h']:
        return parameter[5]
    else:
        return parameter[0]

def sp_223_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    if not letter in letters_selection:
        raise ValueError("It is not a Pm-3n wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd', 'e']:
        return parameter[7]
    elif letter in ['f', 'g', 'h', 'i']:
        return parameter[4]
    elif letter in ['j']:
        return parameter[5]
    elif letter in ['k']:
        return parameter[3]
    else:
        return parameter[0]

def sp_224_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    if not letter in letters_selection:
        raise ValueError("It is not a Pn-3m wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd', 'f']:
        return parameter[7]
    elif letter in ['e', 'g', 'h']:
        return parameter[4]
    elif letter in ['i', 'j']:
        return parameter[5]
    elif letter in ['k']:
        return parameter[2]
    else:
        return parameter[0]

def sp_225_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    if not letter in letters_selection:
        raise ValueError("It is not a Fm-3m wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'f', 'g']:
        return parameter[4]
    elif letter in ['h', 'i']:
        return parameter[5]
    elif letter in ['j']:
        return parameter[3]
    elif letter in ['k']:
        return parameter[2]
    else:
        return parameter[0]

def sp_226_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    if not letter in letters_selection:
        raise ValueError("It is not a Fm-3c wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'f', 'g']:
        return parameter[4]
    elif letter in ['h']:
        return parameter[5]
    elif letter in ['i']:
        return parameter[3]
    else:
        return parameter[0]

def sp_227_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    if not letter in letters_selection:
        raise ValueError("It is not a Fd-3m wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'f']:
        return parameter[4]
    elif letter in ['g']:
        return parameter[2]
    elif letter in ['h']:
        return parameter[5]
    else:
        return parameter[0]

def sp_228_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    if not letter in letters_selection:
        raise ValueError("It is not a Fd-3c wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'f']:
        return parameter[4]
    elif letter in ['g']:
        return parameter[5]
    else:
        return parameter[0]

def sp_229_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    if not letter in letters_selection:
        raise ValueError("It is not a Im-3m wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'f', 'g']:
        return parameter[4]
    elif letter in ['h', 'i']:
        return parameter[5]
    elif letter in ['j']:
        return parameter[3]
    elif letter in ['k']:
        return parameter[2]
    else:
        return parameter[0]

def sp_230_parameter(letter):
    letters_selection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    if not letter in letters_selection:
        raise ValueError("It is not a Ia-3d wyckoff position!")
    elif letter in ['a', 'b', 'c', 'd']:
        return parameter[7]
    elif letter in ['e', 'f']:
        return parameter[4]
    elif letter in ['g']:
        return parameter[5]
    else:
        return parameter[0]