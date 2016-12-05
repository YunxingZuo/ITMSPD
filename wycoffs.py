# coding: utf-8
# Copyright © 2016 YunXing Zuo

import numpy as np

__author__ = 'YunXing Zuo'
__email__ = 'zuoyx@pkusz.edu.cn'
__date__ = 'Nov. 12, 2016'

def special_positions(symbol, multiplicity, pos):
    if symbol == 'P1':
        return sp_1(multiplicity, pos)
    elif symbol == 'P-1':
        return sp_2(multiplicity, pos)
    elif symbol == 'P2':
        if not sp_3_b(multiplicity, pos):
            return sp_3_c(multiplicity, pos)
        else:
            return sp_3_b(multiplicity, pos)
    elif symbol == 'P2_1':
        if not sp_4_b(multiplicity, pos):
            return sp_4_c(multiplicity, pos)
        else:
            return sp_4_b(multiplicity, pos)
    elif symbol == 'C2':
        if not sp_5_b(multiplicity, pos):
            return sp_5_c(multiplicity, pos)
        else:
            return sp_5_b(multiplicity, pos)
    elif symbol == 'Pm':
        if not sp_6_b(multiplicity, pos):
            return sp_6_c(multiplicity, pos)
        else:
            return sp_6_b(multiplicity, pos)
    elif symbol == 'Pc':
        if not sp_7_b(multiplicity, pos):
            return sp_7_c(multiplicity, pos)
        else:
            return sp_7_b(multiplicity, pos)
    elif symbol == 'Cm':
        if not sp_8_b(multiplicity, pos):
            return sp_8_c(multiplicity, pos)
        else:
            return sp_8_b(multiplicity, pos)
    elif symbol == 'Cc':
        if not sp_9_b(multiplicity, pos):
            return sp_9_c(multiplicity, pos)
        else:
            return sp_9_b(multiplicity, pos)
    elif symbol == 'P2/m':
        if not sp_10_b(multiplicity, pos):
            return sp_10_c(multiplicity, pos)
        else:
            return sp_10_b(multiplicity, pos)
    elif symbol == 'P2_1/m':
        if not sp_11_b(multiplicity, pos):
            return sp_11_c(multiplicity, pos)
        else:
            return sp_11_b(multiplicity, pos)
    elif symbol == 'C2/m':
        if not sp_12_b(multiplicity, pos):
            return sp_12_c(multiplicity, pos)
        else:
            return sp_12_b(multiplicity, pos)
    elif symbol == 'P2/c':
        if not sp_13_b(multiplicity, pos):
            return sp_13_c(multiplicity, pos)
        else:
            return sp_13_b(multiplicity, pos)
    elif symbol == 'P2_1/c':
        if not sp_14_b(multiplicity, pos):
            return sp_14_c(multiplicity, pos)
        else:
            return sp_14_b(multiplicity, pos)
    elif symbol == 'C2/c':
        if not sp_15_b(multiplicity, pos):
            return sp_15_c(multiplicity, pos)
        else:
            return sp_15_b(multiplicity, pos)
    elif symbol == 'P222':
        return sp_16(multiplicity, pos)
    elif symbol == 'P222_1':
        return sp_17(multiplicity, pos)
    elif symbol == 'P2_12_12':
        return sp_18(multiplicity, pos)
    elif symbol == 'P2_12_12_1':
        return sp_19(multiplicity, pos)
    elif symbol == 'C222_1':
        return sp_20(multiplicity, pos)
    elif symbol == 'C222':
        return sp_21(multiplicity, pos)
    elif symbol == 'F222':
        return sp_22(multiplicity, pos)
    elif symbol == 'I222':
        return sp_23(multiplicity, pos)
    elif symbol == 'I2_12_12_1':
        return sp_24(multiplicity, pos)
    elif symbol == 'Pmm2':
        return sp_25(multiplicity, pos)
    elif symbol == 'Pmc2_1':
        return sp_26(multiplicity, pos)
    elif symbol == 'Pcc2':
        return sp_27(multiplicity, pos)
    elif symbol == 'Pma2':
        return sp_28(multiplicity, pos)
    elif symbol == 'Pca2_1':
        return sp_29(multiplicity, pos)
    elif symbol == 'Pnc2':
        return sp_30(multiplicity, pos)
    elif symbol == 'Pmn2_1':
        return sp_31(multiplicity, pos)
    elif symbol == 'Pba2':
        return sp_32(multiplicity, pos)
    elif symbol == 'Pna2_1':
        return sp_33(multiplicity, pos)
    elif symbol == 'Pnn2':
        return sp_34(multiplicity, pos)
    elif symbol == 'Cmm2':
        return sp_35(multiplicity, pos)
    elif symbol == 'Cmc2_1':
        return sp_36(multiplicity, pos)
    elif symbol == 'Ccc2':
        return sp_37(multiplicity, pos)
    elif symbol == 'Amm2':
        return sp_38(multiplicity, pos)
    elif symbol == 'Aem2':
        return sp_39(multiplicity, pos)
    elif symbol == 'Ama2':
        return sp_40(multiplicity, pos)
    elif symbol == 'Aea2':
        return sp_41(multiplicity, pos)
    elif symbol == 'Fmm2':
        return sp_42(multiplicity, pos)
    elif symbol == 'Fdd2':
        return sp_43(multiplicity, pos)
    elif symbol == 'Imm2':
        return sp_44(multiplicity, pos)
    elif symbol == 'Iba2':
        return sp_45(multiplicity, pos)
    elif symbol == 'Ima2':
        return sp_46(multiplicity, pos)
    elif symbol == 'Pmmm':
        return sp_47(multiplicity, pos)
    elif symbol == 'Pnnn':
        if not sp_48(multiplicity, pos):
            return sp_48_s(multiplicity, pos)
        else:
            return sp_48(multiplicity, pos)
    elif symbol == 'Pccm':
        return sp_49(multiplicity, pos)
    elif symbol == 'Pban':
        if not sp_50(multiplicity, pos):
            return sp_50_s(multiplicity, pos)
        else:
            return sp_50(multiplicity, pos)
    elif symbol == 'Pmma':
        return sp_51(multiplicity, pos)
    elif symbol == 'Pnna':
        return sp_52(multiplicity, pos)
    elif symbol == 'Pmna':
        return sp_53(multiplicity, pos)
    elif symbol == 'Pcca':
        return sp_54(multiplicity, pos)
    elif symbol == 'Pbam':
        return sp_55(multiplicity, pos)
    elif symbol == 'Pccn':
        return sp_56(multiplicity, pos)
    elif symbol == 'Pbcm':
        return sp_57(multiplicity, pos)
    elif symbol == 'Pnnm':
        return sp_58(multiplicity, pos)
    elif symbol == 'Pmmn':
        if not sp_59(multiplicity, pos):
            return sp_59_s(multiplicity, pos)
        else:
            return sp_59(multiplicity, pos)
    elif symbol == 'Pbcn':
        return sp_60(multiplicity, pos)
    elif symbol == 'Pbca':
        return sp_61(multiplicity, pos)
    elif symbol == 'Pnma':
        return sp_62(multiplicity, pos)
    elif symbol == 'Cmcm':
        return sp_63(multiplicity, pos)
    elif symbol == 'Cmce':
        return sp_64(multiplicity, pos)
    elif symbol == 'Cmmm':
        return sp_65(multiplicity, pos)
    elif symbol == 'Cccm':
        return sp_66(multiplicity, pos)
    elif symbol == 'Cmme':
        return sp_67(multiplicity, pos)
    elif symbol == 'Ccce':
        if not sp_68(multiplicity, pos):
            return sp_68_s(multiplicity, pos)
        else:
            return sp_68(multiplicity, pos)
    elif symbol == 'Fmmm':
        return sp_69(multiplicity, pos)
    elif symbol == 'Fddd':
        if not sp_70(multiplicity, pos):
            return sp_70_s(multiplicity, pos)
        else:
            return sp_70(multiplicity, pos)
    elif symbol == 'Immm':
        return sp_71(multiplicity, pos)
    elif symbol == 'Ibam':
        return sp_72(multiplicity, pos)
    elif symbol == 'Ibca':
        return sp_73(multiplicity, pos)
    elif symbol == 'Imma':
        return sp_74(multiplicity, pos)
    elif symbol == 'P4':
        return sp_75(multiplicity, pos)
    elif symbol == 'P4_1':
        return sp_76(multiplicity, pos)
    elif symbol == 'P4_2':
        return sp_77(multiplicity, pos)
    elif symbol == 'P4_3':
        return sp_78(multiplicity, pos)
    elif symbol == 'I4':
        return sp_79(multiplicity, pos)
    elif symbol == 'I4_1':
        return sp_80(multiplicity, pos)
    elif symbol == 'P-4':
        return sp_81(multiplicity, pos)
    elif symbol == 'I-4':
        return sp_82(multiplicity, pos)
    elif symbol == 'P4/m':
        return sp_83(multiplicity, pos)
    elif symbol == 'P4_2/m':
        return sp_84(multiplicity, pos)
    elif symbol == 'P4/n':
        if not sp_85(multiplicity, pos):
            return sp_85_s(multiplicity, pos)
        else:
            return sp_85(multiplicity, pos)
    elif symbol == 'P4_2/n':
        if not sp_86(multiplicity, pos):
            return sp_86_s(multiplicity, pos)
        else:
            return sp_86(multiplicity, pos)
    elif symbol == 'I4/m':
        return sp_87(multiplicity, pos)
    elif symbol == 'I4_1/a':
        if not sp_88(multiplicity, pos):
            return sp_88_s(multiplicity, pos)
        else:
            return sp_88(multiplicity, pos)
    elif symbol == 'P422':
        return sp_89(multiplicity, pos)
    elif symbol == 'P42_12':
        return sp_90(multiplicity, pos)
    elif symbol == 'P4_122':
        return sp_91(multiplicity, pos)
    elif symbol == 'P4_12_12':
        return sp_92(multiplicity, pos)
    elif symbol == 'P4_222':
        return sp_93(multiplicity, pos)
    elif symbol == 'P4_22_12':
        return sp_94(multiplicity, pos)
    elif symbol == 'P4_322':
        return sp_95(multiplicity, pos)
    elif symbol == 'P4_32_12':
        return sp_96(multiplicity, pos)
    elif symbol == 'I422':
        return sp_97(multiplicity, pos)
    elif symbol == 'I4_122':
        return sp_98(multiplicity, pos)
    elif symbol == 'P4mm':
        return sp_99(multiplicity, pos)
    elif symbol == 'P4bm':
        return sp_100(multiplicity, pos)
    elif symbol == 'P4_2cm':
        return sp_101(multiplicity, pos)
    elif symbol == 'P4_2nm':
        return sp_102(multiplicity, pos)
    elif symbol == 'P4cc':
        return sp_103(multiplicity, pos)
    elif symbol == 'P4nc':
        return sp_104(multiplicity, pos)
    elif symbol == 'P4_2mc':
        return sp_105(multiplicity, pos)
    elif symbol == 'P4_2bc':
        return sp_106(multiplicity, pos)
    elif symbol == 'I4mm':
        return sp_107(multiplicity, pos)
    elif symbol == 'I4cm':
        return sp_108(multiplicity, pos)
    elif symbol == 'I4_1md':
        return sp_109(multiplicity, pos)
    elif symbol == 'I4_1cd':
        return sp_110(multiplicity, pos)
    elif symbol == 'P-42m':
        return sp_111(multiplicity, pos)
    elif symbol == 'P-42c':
        return sp_112(multiplicity, pos)
    elif symbol == 'P-42_1m':
        return sp_113(multiplicity, pos)
    elif symbol == 'P-42_1c':
        return sp_114(multiplicity, pos)
    elif symbol == 'P-4m2':
        return sp_115(multiplicity, pos)
    elif symbol == 'P-4c2':
        return sp_116(multiplicity, pos)
    elif symbol == 'P-4b2':
        return sp_117(multiplicity, pos)
    elif symbol == 'P-4n2':
        return sp_118(multiplicity, pos)
    elif symbol == 'I-4m2':
        return sp_119(multiplicity, pos)
    elif symbol == 'I-4c2':
        return sp_120(multiplicity, pos)
    elif symbol == 'I-42m':
        return sp_121(multiplicity, pos)
    elif symbol == 'I-42d':
        return sp_122(multiplicity, pos)
    elif symbol == 'P4/mmm':
        return sp_123(multiplicity, pos)
    elif symbol == 'P4/mcc':
        return sp_124(multiplicity, pos)
    elif symbol == 'P4/nbm':
        if not sp_125(multiplicity, pos):
            return sp_125_s(multiplicity, pos)
        else:
            return sp_125(multiplicity, pos)
    elif symbol == 'P4/nnc':
        if not sp_126(multiplicity, pos):
            return sp_126_s(multiplicity, pos)
        else:
            return sp_126(multiplicity, pos)
    elif symbol == 'P4/mbm':
        return sp_127(multiplicity, pos)
    elif symbol == 'P4/mnc':
        return sp_128(multiplicity, pos)
    elif symbol == 'P4/nmm':
        if not sp_129(multiplicity, pos):
            return sp_129_s(multiplicity, pos)
        else:
            return sp_129(multiplicity, pos)
    elif symbol == 'P4/ncc':
        if not sp_130(multiplicity, pos):
            return sp_130_s(multiplicity, pos)
        else:
            return sp_130(multiplicity, pos)
    elif symbol == 'P4_2/mmc':
        return sp_131(multiplicity, pos)
    elif symbol == 'P4_2/mcm':
        return sp_132(multiplicity, pos)
    elif symbol == 'P4_2/nbc':
        if not sp_133(multiplicity, pos):
            return sp_133_s(multiplicity, pos)
        else:
            return sp_133(multiplicity, pos)
    elif symbol == 'P4_2/nnm':
        if not sp_134(multiplicity, pos):
            return sp_134_s(multiplicity, pos)
        else:
            return sp_134(multiplicity, pos)
    elif symbol == 'P4_2/mbc':
        return sp_135(multiplicity, pos)
    elif symbol == 'P4_2/mnm':
        return sp_136(multiplicity, pos)
    elif symbol == 'P4_2/nmc':
        if not sp_137(multiplicity, pos):
            return sp_137_s(multiplicity, pos)
        else:
            return sp_137(multiplicity, pos)
    elif symbol == 'P4_2/ncm':
        if not sp_138(multiplicity, pos):
            return sp_138_s(multiplicity, pos)
        else:
            return sp_138(multiplicity, pos)
    elif symbol == 'I4/mmm':
        return sp_139(multiplicity, pos)
    elif symbol == 'I4/mcm':
        return sp_140(multiplicity, pos)
    elif symbol == 'I4_1/amd':
        if not sp_141(multiplicity, pos):
            return sp_141_s(multiplicity, pos)
        else:
            return sp_141(multiplicity, pos)
    elif symbol == 'I4_1/acd':
        if not sp_142(multiplicity, pos):
            return sp_142_s(multiplicity, pos)
        else:
            return sp_142(multiplicity, pos)
    elif symbol == 'P3':
        return sp_143(multiplicity, pos)
    elif symbol == 'P3_1':
        return sp_144(multiplicity, pos)
    elif symbol == 'P3_2':
        return sp_145(multiplicity, pos)
    elif symbol == 'R3':
        return sp_146_R(multiplicity, pos)
    elif symbol == 'R3H':
        return sp_146_H(multiplicity, pos)
    elif symbol == 'P-3':
        return sp_147(multiplicity, pos)
    elif symbol == 'R-3':
        return sp_148_R(multiplicity, pos)
    elif symbol == 'R-3H':
            return sp_148_H(multiplicity, pos)
    elif symbol == 'P312':
        return sp_149(multiplicity, pos)
    elif symbol == 'P321':
        return sp_150(multiplicity, pos)
    elif symbol == 'P3_112':
        return sp_151(multiplicity, pos)
    elif symbol == 'P3_121':
        return sp_152(multiplicity, pos)
    elif symbol == 'P3_212':
        return sp_153(multiplicity, pos)
    elif symbol == 'P3_221':
        return sp_154(multiplicity, pos)
    elif symbol == 'R32':
        return sp_155_R(multiplicity, pos)
    elif symbol == 'R32H':
        return sp_155_H(multiplicity, pos)
    elif symbol == 'P3m1':
        return sp_156(multiplicity, pos)
    elif symbol == 'P31m':
        return sp_157(multiplicity, pos)
    elif symbol == 'P3c1':
        return sp_158(multiplicity, pos)
    elif symbol == 'P31c':
        return sp_159(multiplicity, pos)
    elif symbol == 'R3m':
        return sp_160_R(multiplicity, pos)
    elif symbol == 'R3mH':
        return sp_160_H(multiplicity, pos)
    elif symbol == 'R3c':
        return sp_161_R(multiplicity, pos)
    elif symbol == 'R3cH':
        return sp_161_H(multiplicity, pos)
    elif symbol == 'P-31m':
        return sp_162(multiplicity, pos)
    elif symbol == 'P-31c':
        return sp_163(multiplicity, pos)
    elif symbol == 'P-3m1':
        return sp_164(multiplicity, pos)
    elif symbol == 'P-3c1':
        return sp_165(multiplicity, pos)
    elif symbol == 'R-3m':
        return sp_166_R(multiplicity, pos)
    elif symbol == 'R-3mH':
        return sp_166_H(multiplicity, pos)
    elif symbol == 'R-3c':
        return sp_167_R(multiplicity, pos)
    elif symbol == 'R-3cH':
        return sp_167_H(multiplicity, pos)
    elif symbol == 'P6':
        return sp_168(multiplicity, pos)
    elif symbol == 'P6_1':
        return sp_169(multiplicity, pos)
    elif symbol == 'P6_5':
        return sp_170(multiplicity, pos)
    elif symbol == 'P6_2':
        return sp_171(multiplicity, pos)
    elif symbol == 'P6_4':
        return sp_172(multiplicity, pos)
    elif symbol == 'P6_3':
        return sp_173(multiplicity, pos)
    elif symbol == 'P-6':
        return sp_174(multiplicity, pos)
    elif symbol == 'P6/m':
        return sp_175(multiplicity, pos)
    elif symbol == 'P6_3/m':
        return sp_176(multiplicity, pos)
    elif symbol == 'P622':
        return sp_177(multiplicity, pos)
    elif symbol == 'P6_122':
        return sp_178(multiplicity, pos)
    elif symbol == 'P6_522':
        return sp_179(multiplicity, pos)
    elif symbol == 'P6_222':
        return sp_180(multiplicity, pos)
    elif symbol == 'P6_422':
        return sp_181(multiplicity, pos)
    elif symbol == 'P6_322':
        return sp_182(multiplicity, pos)
    elif symbol == 'P6mm':
        return sp_183(multiplicity, pos)
    elif symbol == 'P6cc':
        return sp_184(multiplicity, pos)
    elif symbol == 'P6_3cm':
        return sp_185(multiplicity, pos)
    elif symbol == 'P6_3mc':
        return sp_186(multiplicity, pos)
    elif symbol == 'P-6m2':
        return sp_187(multiplicity, pos)
    elif symbol == 'P-6c2':
        return sp_188(multiplicity, pos)
    elif symbol == 'P-62m':
        return sp_189(multiplicity, pos)
    elif symbol == 'P-62c':
        return sp_190(multiplicity, pos)
    elif symbol == 'P6/mmm':
        return sp_191(multiplicity, pos)
    elif symbol == 'P6/mcc':
        return sp_192(multiplicity, pos)
    elif symbol == 'P6_3/mcm':
        return sp_193(multiplicity, pos)
    elif symbol == 'P6_3/mmc':
        return sp_194(multiplicity, pos)
    elif symbol == 'P23':
        return sp_195(multiplicity, pos)
    elif symbol == 'F23':
        return sp_196(multiplicity, pos)
    elif symbol == 'I23':
        return sp_197(multiplicity, pos)
    elif symbol == 'P2_13':
        return sp_198(multiplicity, pos)
    elif symbol == 'I2_13':
        return sp_199(multiplicity, pos)
    elif symbol == 'Pm-3':
        return sp_200(multiplicity, pos)
    elif symbol == 'Pn-3':
        if not sp_201(multiplicity, pos):
            return sp_201_s(multiplicity, pos)
        else:
            return sp_201(multiplicity, pos)
    elif symbol == 'Fm-3':
        return sp_202(multiplicity, pos)
    elif symbol == 'Fd-3':
        if not sp_203(multiplicity, pos):
            return sp_203_s(multiplicity, pos)
        else:
            return sp_203(multiplicity, pos)
    elif symbol == 'Im-3':
        return sp_204(multiplicity, pos)
    elif symbol == 'Pa-3':
        return sp_205(multiplicity, pos)
    elif symbol == 'Ia-3':
        return sp_206(multiplicity, pos)
    elif symbol == 'P432':
        return sp_207(multiplicity, pos)
    elif symbol == 'P4_232':
        return sp_208(multiplicity, pos)
    elif symbol == 'F432':
        return sp_209(multiplicity, pos)
    elif symbol == 'F4_132':
        return sp_210(multiplicity, pos)
    elif symbol == 'I432':
        return sp_211(multiplicity, pos)
    elif symbol == 'P4_332':
        return sp_212(multiplicity, pos)
    elif symbol == 'P4_132':
        return sp_213(multiplicity, pos)
    elif symbol == 'I4_132':
        return sp_214(multiplicity, pos)
    elif symbol == 'P-43m':
        return sp_215(multiplicity, pos)
    elif symbol == 'F-43m':
        return sp_216(multiplicity, pos)
    elif symbol == 'I-43m':
        return sp_217(multiplicity, pos)
    elif symbol == 'P-43n':
        return sp_218(multiplicity, pos)
    elif symbol == 'F-43c':
        return sp_219(multiplicity, pos)
    elif symbol == 'I-43d':
        return sp_220(multiplicity, pos)
    elif symbol == 'Pm-3m':
        return sp_221(multiplicity, pos)
    elif symbol == 'Pn-3n':
        if not sp_222(multiplicity, pos):
            return sp_222_s(multiplicity, pos)
        else:
            return sp_222(multiplicity, pos)
    elif symbol == 'Pm-3n':
        return sp_223(multiplicity, pos)
    elif symbol == 'Pn-3m':
        if not sp_224(multiplicity, pos):
            return sp_224_s(multiplicity, pos)
        else:
            return sp_224(multiplicity, pos)
    elif symbol == 'Fm-3m':
        return sp_225(multiplicity, pos)
    elif symbol == 'Fm-3c':
        return sp_226(multiplicity, pos)
    elif symbol == 'Fd-3m':
        if not sp_227(multiplicity, pos):
            return sp_227_s(multiplicity, pos)
        else:
            return sp_227(multiplicity, pos)
    elif symbol == 'Fd-3c':
        if not sp_228(multiplicity, pos):
            return sp_228_s(multiplicity, pos)
        else:
            return sp_228(multiplicity, pos)
    elif symbol == 'Im-3m':
        return sp_229(multiplicity, pos)
    elif symbol == 'Ia-3d':
        return sp_230(multiplicity, pos)

def sp_1(multiplicity, pos):
    if multiplicity != 1:
        raise ValueError("It is not a P1 system!")
    else:
        return 'a'

def sp_2(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 1 and multiplicity != 2:
        raise ValueError("It is not a P-1 system!")
    elif multiplicity == 1:
        symbol_set = np.array(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5], [0., 0.5, 0.], [0.5, 0., 0.], [0.5, 0.5, 0.], [0.5, 0., 0.5], [0., 0.5, 0.5], [0.5, 0.5, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'i'

def sp_3_b(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 1 and multiplicity != 2:
        raise ValueError("It is not a P2 system!")
    elif multiplicity == 1:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0., pos[1], 0.], [0., pos[1], 0.5], [0.5, pos[1], 0.], [0.5, pos[1], 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'e'

def sp_3_c(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 1 and multiplicity != 2:
        raise ValueError("It is not a P2 system!")
    elif multiplicity == 1:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0., 0., pos[2]], [0.5, 0., pos[2]], [0., 0.5, pos[2]], [0.5, 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'e'

def sp_4_b(multiplicity, pos):
    if multiplicity != 2:
        raise ValueError("It is not a P2_1 system!")
    else:
        return 'a'

def sp_4_c(multiplicity, pos):
    if multiplicity != 2:
        raise ValueError("It is not a P2_1 system!")
    else:
        return 'a'

def sp_5_b(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4:
        raise ValueError("It is not a C2 system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., pos[1], 0.], [0., pos[1], 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'c'

def sp_5_c(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4:
        raise ValueError("It is not a C2 system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., pos[2]], [0.5, 0., pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'c'

def sp_6_b(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 1 and multiplicity != 2:
        raise ValueError("It is not a Pm system!")
    elif multiplicity == 1:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[pos[0], 0., pos[2]], [pos[0], 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'c'

def sp_6_c(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 1 and multiplicity != 2:
        raise ValueError("It is not a Pm system!")
    elif multiplicity == 1:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[pos[0], pos[1], 0.], [pos[0], pos[1], 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'c'

def sp_7_b(multiplicity, pos):
    if multiplicity != 2:
        raise ValueError("It is not a Pc system!")
    else:
        return 'a'

def sp_7_c(multiplicity, pos):
    if multiplicity != 2:
        raise ValueError("It is not a Pc system!")
    else:
        return 'a'

def sp_8_b(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4:
        raise ValueError("It is not a Cm system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a'])
        bool_set = map(f, [[pos[0], 0., pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'b'

def sp_8_c(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4:
        raise ValueError("It is not a Cm system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a'])
        bool_set = map(f, [[pos[0], pos[1], 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'b'

def sp_9_b(multiplicity, pos):
    if multiplicity != 4:
        raise ValueError("It is not a Cc system!")
    else:
        return 'a'

def sp_9_c(multiplicity, pos):
    if multiplicity != 4:
        raise ValueError("It is not a Cc system!")
    else:
        return 'a'

def sp_10_b(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 1 and multiplicity != 2 and multiplicity != 4:
        raise ValueError("It is not a P2/m system!")
    elif multiplicity == 1:
        symbol_set = np.array(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
        bool_set = map(f, [[0., 0., 0.], [0., 0.5, 0.], [0., 0., 0.5], [0.5, 0., 0.], [0.5, 0.5, 0.], [0., 0.5, 0.5], [0.5, 0., 0.5], [0.5, 0.5, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 2:
        symbol_set = np.array(['i', 'j', 'k', 'l', 'm', 'n'])
        bool_set = map(f, [[0., pos[1], 0.], [0.5, pos[1], 0.], [0., pos[1], 0.5], [0.5, pos[1], 0.5], [pos[0], 0., pos[2]], [pos[0], 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'o'

def sp_10_c(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 1 and multiplicity != 2 and multiplicity != 4:
        raise ValueError("It is not a P2/m system!")
    elif multiplicity == 1:
        symbol_set = np.array(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5], [0.5, 0., 0.], [0., 0.5, 0.], [0., 0.5, 0.5], [0.5, 0., 0.5], [0.5, 0.5, 0.], [0.5, 0.5, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 2:
        symbol_set = np.array(['i', 'j', 'k', 'l', 'm', 'n'])
        bool_set = map(f, [[0., 0., pos[2]], [0., 0.5, pos[2]], [0.5, 0., pos[2]], [0.5, 0.5, pos[2]], [pos[0], pos[1], 0.], [pos[0], pos[1], 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'o'

def sp_11_b(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4:
        raise ValueError("It is not a P2_1/m system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c', 'd', 'e'])
        bool_set = map(f, [[0., 0., 0.], [0.5, 0., 0.], [0., 0., 0.5], [0.5, 0., 0.5], [pos[0], 0.25, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'f'

def sp_11_c(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4:
        raise ValueError("It is not a P2_1/m system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c', 'd', 'e'])
        bool_set = map(f, [[0., 0., 0.], [0., 0.5, 0.], [0.5, 0., 0.], [0.5, 0.5, 0.], [pos[0], pos[1], 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'f'

def sp_12_b(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a C2/m system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0., 0., 0.], [0., 0.5, 0.], [0., 0., 0.5], [0., 0.5, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['e', 'f', 'g', 'h', 'i'])
        bool_set = map(f, [[0.25, 0.25, 0.], [0.25, 0.25, 0.5], [0., pos[1], 0.], [0., pos[1], 0.5], [pos[0], 0., pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'j'

def sp_12_c(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a C2/m system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5], [0.5, 0., 0.], [0.5, 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['e', 'f', 'g', 'h', 'i'])
        bool_set = map(f, [[0., 0.25, 0.25], [0.5, 0.25, 0.25], [0., 0., pos[2]], [0.5, 0., pos[2]], [pos[0], pos[1], 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'j'

def sp_13_b(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4:
        raise ValueError("It is not a P2/c system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c', 'd', 'e', 'f'])
        bool_set = map(f, [[0., 0., 0.], [0.5, 0.5, 0.], [0., 0.5, 0.], [0.5, 0., 0.], [0., pos[1], 0.25], [0.5, pos[1], 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'g'

def sp_13_c(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4:
        raise ValueError("It is not a P2/c system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c', 'd', 'e', 'f'])
        bool_set = map(f, [[0., 0., 0.], [0., 0.5, 0.5], [0., 0., 0.5], [0., 0.5, 0.], [0.25, 0., pos[2]], [0.25, 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'g'

def sp_14_b(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4:
        raise ValueError("It is not a P2_1/c system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0., 0., 0.], [0.5, 0., 0.], [0., 0., 0.5], [0.5, 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'e'

def sp_14_c(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4:
        raise ValueError("It is not a P2_1/c system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0., 0., 0.], [0., 0.5, 0.], [0.5, 0., 0.], [0.5, 0.5, 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'e'

def sp_15_b(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a C2/c system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b', 'c', 'd', 'e'])
        bool_set = map(f, [[0., 0., 0.], [0., 0.5, 0.], [0.25, 0.25, 0.], [0.25, 0.25, 0.5], [0., pos[1], 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'f'

def sp_15_c(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a C2/c system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b', 'c', 'd', 'e'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5], [0., 0.25, 0.25], [0.5, 0.25, 0.25], [0.25, 0., pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'f'

def sp_16(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 1 and multiplicity != 2 and multiplicity != 4:
        raise ValueError("It is not a P222 system!")
    elif multiplicity == 1:
        symbol_set = np.array(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
        bool_set = map(f, [[0., 0., 0.], [0.5, 0., 0.], [0., 0.5, 0.], [0., 0., 0.5], [0.5, 0.5, 0.], [0.5, 0., 0.5], [0., 0.5, 0.5], [0.5, 0.5, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 2:
        symbol_set = np.array(['i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'])
        bool_set = map(f, [[pos[0], 0., 0.], [pos[0], 0., 0.5], [pos[0], 0.5, 0.], [pos[0], 0.5, 0.5], [0., pos[1], 0.], [0., pos[1], 0.5], \
        [0.5, pos[1], 0.], [0.5, pos[1], 0.5], [0., 0., pos[2]], [0.5, 0., pos[2]], [0., 0.5, pos[2]], [0.5, 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        return 'u'

def sp_17(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4:
        raise ValueError("It is not a P222_1 system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[pos[0], 0., 0.], [pos[0], 0.5, 0.], [0., pos[1], 0.25], [0.5, pos[1], 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'e'

def sp_18(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4:
        raise ValueError("It is not a P2_12_12 system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., pos[2]], [0., 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'c'

def sp_19(multiplicity, pos):
    if multiplicity != 4:
        raise ValueError("It is not a P2_12_12_1 system!")
    else:
        return 'a'

def sp_20(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a C222_1 system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[pos[0], 0., 0.], [0., pos[1], 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'c'

def sp_21(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a C222 system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0., 0., 0.], [0., 0.5, 0.], [0.5, 0., 0.5], [0., 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['e', 'f', 'g', 'h', 'i', 'j', 'k'])
        bool_set = map(f, [[pos[0], 0., 0.], [pos[0], 0., 0.5], [0., pos[1], 0.], [0., pos[1], 0.5], [0., 0., pos[2]], [0., 0.5, pos[2]], [0.25, 0.25, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'l'

def sp_22(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8 and multiplicity != 16:
        raise ValueError("It is not a F222 system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5], [0.25, 0.25, 0.25], [0.25, 0.25, 0.75]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['e', 'f', 'g', 'h', 'i', 'j'])
        bool_set = map(f, [[pos[0], 0., 0.], [0., pos[1], 0.], [0., 0., pos[2]], [0.25, 0.25, pos[2]], [0.25, pos[1], 0.25], [pos[0], 0.25, 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'k'

def sp_23(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a I222 system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0., 0., 0.], [0.5, 0., 0.], [0., 0., 0.5], [0., 0.5, 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['e', 'f', 'g', 'h', 'i', 'j'])
        bool_set = map(f, [[pos[0], 0., 0.], [pos[0], 0., 0.5], [0., pos[1], 0.], [0.5, pos[1], 0.], [0., 0., pos[2]], [0., 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'k'

def sp_24(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a I2_12_12_1 system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b', 'c'])
        bool_set = map(f, [[pos[0], 0., 0.25], [0.25, pos[1], 0.], [0., 0.25, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'd'

def sp_25(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 1 and multiplicity != 2 and multiplicity != 4:
        raise ValueError("It is not a Pmm2 system!")
    elif multiplicity == 1:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0., 0., pos[2]], [0., 0.5, pos[2]], [0.5, 0., pos[2]], [0.5, 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 2:
        symbol_set = np.array(['e', 'f', 'g', 'h'])
        bool_set = map(f, [[pos[0], 0., pos[2]], [pos[0], 0.5, pos[2]], [0., pos[1], pos[2]], [0.5, pos[1], pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'i'

def sp_26(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4:
        raise ValueError("It is not a Pmc2_1 system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., pos[1], pos[2]], [0.5, pos[1], pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'c'

def sp_27(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4:
        raise ValueError("It is not a Pcc2 system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0., 0., pos[2]], [0., 0.5, pos[2]], [0.5, 0., pos[2]], [0.5, 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'e'

def sp_28(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4:
        raise ValueError("It is not a Pma2 system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c'])
        bool_set = map(f, [[0., 0., pos[2]], [0., 0.5, pos[2]], [0.25, pos[1], pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'd'

def sp_29(multiplicity, pos):
    if multiplicity != 4:
        raise ValueError("It is not a Pca2_1 system!")
    else:
        return 'a'

def sp_30(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4:
        raise ValueError("It is not a Pnc2 system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., pos[2]], [0.5, 0., pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'c'

def sp_31(multiplicity, pos):
    if multiplicity != 2 and multiplicity != 4:
        raise ValueError("It is not a Pmn2_1 system!")
    elif multiplicity == 2:
        return 'a'
    else:
        return 'b'

def sp_32(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4:
        raise ValueError("It is not a Pba2 system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., pos[2]], [0., 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'c'

def sp_33(multiplicity, pos):
    if multiplicity != 4:
        raise ValueError("It is not a Pna2_1 system!")
    else:
        return 'a'

def sp_34(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4:
        raise ValueError("It is not a Pnn2 system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., pos[2]], [0., 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'c'

def sp_35(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a Cmm2 system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., pos[2]], [0., 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['c', 'd', 'e'])
        bool_set = map(f, [[0.25, 0.25, pos[2]], [pos[0], 0., pos[2]], [0., pos[1], pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'f'

def sp_36(multiplicity, pos):
    if multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a Cmc2_1 system!")
    elif multiplicity == 4:
        return 'a'
    else:
        return 'b'

def sp_37(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a Ccc2 system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b', 'c'])
        bool_set = map(f, [[0., 0., pos[2]], [0., 0.5, pos[2]], [0.25, 0.25, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'c'

def sp_38(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a Amm2 system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., pos[2]], [0.5, 0., pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['c', 'd', 'e'])
        bool_set = map(f, [[pos[0], 0., pos[2]], [0., pos[1], pos[2]], [0.5, pos[1], pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'f'

def sp_39(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a Aem2 system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b', 'c'])
        bool_set = map(f, [[0., 0., pos[2]], [0.5, 0., pos[2]], [pos[0], 0.25, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'd'

def sp_40(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a Aem2 system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., pos[2]], [0.25, pos[1], pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'c'

def sp_41(multiplicity, pos):
    if multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a Aea2 system!")
    elif multiplicity == 4:
        return 'a'
    else:
        return 'b'

def sp_42(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8 and multiplicity != 16:
        raise ValueError("It is not a Fmm2 system!")
    elif multiplicity == 4:
        return 'a'
    elif multiplicity == 8:
        symbol_set = np.array(['b', 'c', 'd'])
        bool_set = map(f, [[0.25, 0.25, pos[2]], [0., pos[1], pos[2]], [pos[0], 0., pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'e'

def sp_43(multiplicity, pos):
    if multiplicity != 8 and multiplicity != 16:
        raise ValueError("It is not a Fdd2 system!")
    elif multiplicity == 8:
        return 'a'
    else:
        return 'b'

def sp_44(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a Imm2 system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., pos[2]], [0., 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['c', 'd'])
        bool_set = map(f, [[pos[0], 0., pos[2]], [0., pos[1], pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'e'

def sp_45(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a Iba2 system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., pos[2]], [0., 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'c'

def sp_46(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a Ima2 system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., pos[2]], [0.25, pos[1], pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'c'

def sp_47(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 1 and multiplicity != 2 and multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a Pmmm system!")
    elif multiplicity == 1:
        symbol_set = np.array(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
        bool_set = map(f, [[0., 0., 0.], [0.5, 0., 0.], [0., 0., 0.5], [0.5, 0., 0.5], [0., 0.5, 0.], [0.5, 0.5, 0.], [0., 0.5, 0.5], [0.5, 0.5, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 2:
        symbol_set = np.array(['i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'])
        bool_set = map(f, [[pos[0], 0., 0.], [pos[0], 0., 0.5], [pos[0], 0.5, 0.], [pos[0], 0.5, 0.5], [0., pos[1], 0.], [0., pos[1], 0.5], \
        [0.5, pos[1], 0.], [0.5, pos[1], 0.5], [0., 0., pos[2]], [0., 0.5, pos[2]], [0.5, 0., pos[2]], [0.5, 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['u', 'v', 'w', 'x', 'y', 'z'])
        bool_set = map(f, [[0., pos[1], pos[2]], [0.5, pos[1], pos[2]], [pos[0], 0., pos[2]], [pos[0], 0.5, pos[2]], [pos[0], pos[1], 0.], [pos[0], pos[1], 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'A'

def sp_48(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a Pnnn system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0., 0., 0.], [0.5, 0., 0.], [0., 0., 0.5], [0., 0.5, 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'])
        bool_set = map(f, [[0.25, 0.25, 0.25], [0.75, 0.75, 0.75], [pos[0], 0., 0.], [pos[0], 0., 0.5], [0., pos[1], 0.], [0.5, pos[1], 0.], \
        [0., 0., pos[2]], [0., 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'm'

def sp_48_s(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a Pnnn system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0.25, 0.25, 0.25], [0.75, 0.25, 0.25], [0.25, 0.25, 0.75], [0.25, 0.75, 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'])
        bool_set = map(f, [[0.5, 0.5, 0.5], [0., 0., 0.], [pos[0], 0.25, 0.25], [pos[0], 0.25, 0.75], [0.25, pos[1], 0.25], [0.75, pos[1], 0.25], \
        [0.25, 0.25, pos[2]], [0.25, 0.75, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'm'

def sp_49(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a Pccm system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
        bool_set = map(f, [[0., 0., 0.], [0.5, 0.5, 0.], [0., 0.5, 0.], [0.5, 0., 0.], [0., 0., 0.25], [0.5, 0., 0.25], [0., 0.5, 0.25], [0.5, 0.5, 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q'])
        bool_set = map(f, [[pos[0], 0., 0.25], [pos[0], 0.5, 0.25], [0., pos[1], 0.25], [0.5, pos[1], 0.25], [0., 0., pos[2]], [0.5, 0.5, pos[2]], \
        [0., 0.5, pos[2]], [0.5, 0., pos[2]], [pos[0], pos[1], 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'r'

def sp_50(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a Pban system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0., 0., 0.], [0.5, 0., 0.], [0.5, 0., 0.5], [0., 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'])
        bool_set = map(f, [[0.25, 0.25, 0.], [0.25, 0.25, 0.5], [pos[0], 0., 0.], [pos[0], 0., 0.5], [0., pos[1], 0.], [0., pos[1], 0.5], \
        [0., 0., pos[2]], [0., 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'm'

def sp_50_s(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a Pban system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0.25, 0.25, 0.], [0.75, 0.25, 0.], [0.75, 0.25, 0.5], [0.25, 0.25, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5], [pos[0], 0.25, 0.], [pos[0], 0.25, 0.5], [0.25, pos[1], 0.], [0.25, pos[1], 0.5], \
        [0.25, 0.25, pos[2]], [0.25, 0.75, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'm'

def sp_51(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a Pmma system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c', 'd', 'e', 'f'])
        bool_set = map(f, [[0., 0., 0.], [0., 0.5, 0.], [0., 0., 0.5], [0., 0.5, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['g', 'h', 'i', 'j', 'k'])
        bool_set = map(f, [[0., pos[1], 0.], [0., pos[1], 0.5], [pos[0], 0., pos[2]], [pos[0], 0.5, pos[2]], [0.25, pos[1], pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'l'

def sp_52(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a Pnna system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5], [0.25, 0., pos[2]], [pos[0], 0.25, 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'e'

def sp_53(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a Pmna system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0., 0., 0.], [0.5, 0., 0.], [0.5, 0.5, 0.], [0., 0.5, 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['e', 'f', 'g', 'h'])
        bool_set = map(f, [[pos[0], 0., 0.], [pos[0], 0.5, 0.], [0.25, pos[1], 0.25], [0., pos[1], pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'i'

def sp_54(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a Pcca system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b', 'c', 'd', 'e'])
        bool_set = map(f, [[0., 0., 0.], [0., 0.5, 0.], [0., pos[1], 0.25], [0.25, 0., pos[2]], [0.25, 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'f'

def sp_55(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a Pbam system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5], [0., 0.5, 0.], [0., 0.5, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['e', 'f', 'g', 'h'])
        bool_set = map(f, [[0., 0., pos[2]], [0., 0.5, pos[2]], [pos[0], pos[1], 0.], [pos[0], pos[1], 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'i'

def sp_56(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a Pccn system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5], [0.25, 0.25, pos[2]], [0.25, 0.75, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'e'

def sp_57(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a Pbcm system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0., 0., 0.], [0.5, 0., 0.], [pos[0], 0.25, 0.], [pos[0], pos[1], 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'e'

def sp_58(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a Pnnm system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5], [0., 0.5, 0.], [0., 0.5, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['e', 'f', 'g'])
        bool_set = map(f, [[0., 0., pos[2]], [0., 0.5, pos[2]], [pos[0], pos[1], 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'h'

def sp_59(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a Pmmn system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., pos[2]], [0., 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['c', 'd', 'e', 'f'])
        bool_set = map(f, [[0.25, 0.25, 0.], [0.25, 0.25, 0.5], [0., pos[1], pos[2]], [pos[0], 0., pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'g'

def sp_59_s(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a Pmmn system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0.25, 0.25, pos[2]], [0.25, 0.75, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['c', 'd', 'e', 'f'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5], [0.25, pos[1], pos[2]], [pos[0], 0.25, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'g'

def sp_60(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a Pbcn system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b', 'c'])
        bool_set = map(f, [[0., 0., 0.], [0., 0.5, 0.], [0., pos[1], 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'd'

def sp_61(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a Pbca system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'c'

def sp_62(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a Pnma system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b', 'c'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5], [pos[0], 0.25, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'd'

def sp_63(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8 and multiplicity != 16:
        raise ValueError("It is not a Cmcm system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b', 'c'])
        bool_set = map(f, [[0., 0., 0.], [0., 0.5, 0.], [0., pos[1], 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['d', 'e', 'f', 'g'])
        bool_set = map(f, [[0.25, 0.25, 0.], [pos[0], 0., 0.], [0., pos[1], pos[2]], [pos[0], pos[1], 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'h'

def sp_64(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8 and multiplicity != 16:
        raise ValueError("It is not a Cmce system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0.5, 0., 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['c', 'd', 'e', 'f'])
        bool_set = map(f, [[0.25, 0.25, 0.], [pos[0], 0., 0.], [0.25, pos[1], 0.25], [0., pos[1], pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'g'

def sp_65(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8 and multiplicity != 16:
        raise ValueError("It is not a Cmmm system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0., 0., 0.], [0.5, 0., 0.], [0.5, 0., 0.5], [0., 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'])
        bool_set = map(f, [[0.25, 0.25, 0.], [0.25, 0.25, 0.5], [pos[0], 0., 0.], [pos[0], 0., 0.5], [0., pos[1], 0.], [0., pos[1], 0.5], \
        [0., 0., pos[2]], [0., 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['m', 'n', 'o', 'p', 'q'])
        bool_set = map(f, [[0.25, 0.25, pos[2]], [0., pos[1], pos[2]], [pos[0], 0., pos[2]], [pos[0], pos[1], 0.], [pos[0], pos[1], 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'r'

def sp_66(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8 and multiplicity != 16:
        raise ValueError("It is not a Cccm system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b', 'c', 'd', 'e', 'f'])
        bool_set = map(f, [[0., 0., 0.25], [0., 0.5, 0.25], [0., 0., 0.], [0., 0.5, 0.], [0.25, 0.25, 0.], [0.25, 0.75, 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['g', 'h', 'i', 'j', 'k', 'l'])
        bool_set = map(f, [[pos[0], 0., 0.25], [0., pos[1], 0.25], [0., 0., pos[2]], [0., 0.5, pos[2]], [0.25, 0.25, pos[2]], [pos[0], pos[1], 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'm'

def sp_67(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8 and multiplicity != 16:
        raise ValueError("It is not a Cccm system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
        bool_set = map(f, [[0.25, 0., 0.], [0.25, 0., 0.5], [0., 0., 0.], [0., 0., 0.5], [0.25, 0.25, 0.], [0.25, 0.25, 0.5], [0., 0.25, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['h', 'i', 'j', 'k', 'l', 'm', 'n'])
        bool_set = map(f, [[pos[0], 0., 0.], [pos[0], 0., 0.5], [0.25, pos[1], 0.], [0.25, pos[1], 0.5], [0.25, 0., pos[2]], \
        [0, pos[1], pos[2]], [pos[0], 0.25, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'o'

def sp_68(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8 and multiplicity != 16:
        raise ValueError("It is not a Ccce system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['c', 'd', 'e', 'f', 'g', 'h'])
        bool_set = map(f, [[0.25, 0., 0.25], [0., 0.25, 0.25], [pos[0], 0., 0.], [0., pos[1], 0.], [0., 0., pos[2]], [0.25, 0.25, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'i'

def sp_68_s(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8 and multiplicity != 16:
        return False
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0.25, 0.25], [0., 0.25, 0.75]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['c', 'd', 'e', 'f', 'g', 'h'])
        bool_set = map(f, [[0.25, 0.75, 0.], [0., 0., 0.], [pos[0], 0.25, 0.25], [0., pos[1], 0.25], [0., 0.25, pos[2]], [0.25, 0., pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'i'

def sp_69(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8 and multiplicity != 16 and multiplicity != 32:
        raise ValueError("It is not a Cmmm system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['c', 'd', 'e', 'f', 'g', 'h', 'i'])
        bool_set = map(f, [[0., 0.25, 0.25], [0.25, 0., 0.25], [0.25, 0.25, 0.], [0.25, 0.25, 0.25], [pos[0], 0., 0.], [0., pos[1], 0.], [0., 0., pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 16:
        symbol_set = np.array(['j', 'k', 'l', 'm', 'n', 'o'])
        bool_set = map(f, [[0.25, 0.25, pos[2]], [0.25, pos[1], 0.25], [pos[0], 0.25, 0.25], [0., pos[1], pos[2]], [pos[0], 0., pos[2]], [pos[0], pos[1], 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'p'

def sp_70(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 8 and multiplicity != 16 and multiplicity != 32:
        raise ValueError("It is not a Fddd system!")
    elif multiplicity == 8:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 16:
        symbol_set = np.array(['c', 'd', 'e', 'f', 'g'])
        bool_set = map(f, [[0.125, 0.125, 0.125], [0.625, 0.625, 0.625], [pos[0], 0., 0.], [0., pos[1], 0.], [0., 0., pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'h'

def sp_70_s(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 8 and multiplicity != 16 and multiplicity != 32:
        raise ValueError("It is not a Fddd system!")
    elif multiplicity == 8:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0.125, 0.125, 0.125], [0.125, 0.125, 0.625]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 16:
        symbol_set = np.array(['c', 'd', 'e', 'f', 'g'])
        bool_set = map(f, [[0., 0., 0.], [0.5, 0.5, 0.5], [pos[0], 0.125, 0.125], [0.125, pos[1], 0.125], [0.125, 0.125, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'h'

def sp_71(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8 and multiplicity != 16:
        raise ValueError("It is not a Immm system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0., 0., 0.], [0., 0.5, 0.5], [0.5, 0.5, 0.], [0.5, 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['e', 'f', 'g', 'h', 'i', 'j'])
        bool_set = map(f, [[pos[0], 0., 0.], [pos[0], 0.5, 0.], [0., pos[1], 0.], [0., pos[1], 0.5], [0., 0., pos[2]], [0.5, 0., pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['k', 'l', 'm', 'n'])
        bool_set = map(f, [[0.25, 0.25, 0.25], [0., pos[1], pos[2]], [pos[0], 0., pos[2]], [pos[0], pos[1], 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'o'

def sp_72(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8 and multiplicity != 16:
        raise ValueError("It is not a Ibam system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0., 0., 0.25], [0.5, 0., 0.25], [0., 0., 0.], [0.5, 0., 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['e', 'f', 'g', 'h', 'i', 'j'])
        bool_set = map(f, [[0.25, 0.25, 0.25], [pos[0], 0., 0.25], [0., pos[1], 0.25], [0., 0., pos[2]], [0., 0.5, pos[2]], [pos[0], pos[1], 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'k'

def sp_73(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 8 and multiplicity != 16:
        raise ValueError("It is not a Ibca system!")
    elif multiplicity == 8:
        symbol_set = np.array(['a', 'b', 'c', 'd', 'e'])
        bool_set = map(f, [[0., 0., 0.], [0.25, 0.25, 0.25], [pos[0], 0., 0.25], [0.25, pos[1], 0.], [0., 0.25, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'f'

def sp_74(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8 and multiplicity != 16:
        raise ValueError("It is not a Imma system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b', 'c', 'd', 'e'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5], [0.25, 0.25, 0.25], [0.25, 0.25, 0.75], [0., 0.25, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['f', 'g', 'h', 'i'])
        bool_set = map(f, [[pos[0], 0., 0.], [0.25, pos[1], 0.25], [0., pos[1], pos[2]], [pos[0], 0.25, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'j'

def sp_75(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 1 and multiplicity != 2 and multiplicity != 4:
        raise ValueError("It is not a P4 system!")
    elif multiplicity == 1:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., pos[2]], [0.5, 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 2:
        return 'c'
    else:
        return 'd'

def sp_76(multiplicity, pos):
    if multiplicity != 4:
        raise ValueError("It is not a P4_1 system!")
    else:
        return 'a'

def sp_77(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4:
        raise ValueError("It is not a P4_2 system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c'])
        bool_set = map(f, [[0., 0., pos[2]], [0.5, 0.5, pos[2]], [0., 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'd'

def sp_78(multiplicity, pos):
    if multiplicity != 4:
        raise ValueError("It is not a P4_3 system!")
    else:
        return 'a'

def sp_79(multiplicity, pos):
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a I4 system!")
    elif multiplicity == 2:
        return 'a'
    elif multiplicity == 4:
        return 'b'
    else:
        return 'c'

def sp_80(multiplicity, pos):
    if multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a I4_1 system!")
    elif multiplicity == 4:
        return 'a'
    else:
        return 'b'

def sp_81(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 1 and multiplicity != 2 and multiplicity != 4:
        raise ValueError("It is not a P-4 system!")
    elif multiplicity == 1:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5], [0.5, 0.5, 0.], [0.5, 0.5, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 2:
        symbol_set = np.array(['e', 'f', 'g'])
        bool_set = map(f, [[0., 0., pos[2]], [0.5, 0.5, pos[2]], [0., 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'h'

def sp_82(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a I-4 system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5], [0., 0.5, 0.25], [0., 0.5, 0.75]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['e', 'f'])
        bool_set = map(f, [[0., 0., pos[2]], [0., 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'g'

def sp_83(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 1 and multiplicity != 2 and multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a P4/m system!")
    elif multiplicity == 1:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5], [0.5, 0.5, 0.], [0.5, 0.5, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 2:
        symbol_set = np.array(['e', 'f', 'g', 'h'])
        bool_set = map(f, [[0., 0.5, 0.], [0., 0.5, 0.5], [0., 0., pos[2]], [0.5, 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['i', 'j', 'k'])
        bool_set = map(f, [[0., 0.5, pos[2]], [pos[0], pos[1], 0.], [pos[0], pos[1], 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'l'

def sp_84(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a P4_2/m system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c', 'd', 'e', 'f'])
        bool_set = map(f, [[0., 0., 0.], [0.5, 0.5, 0.], [0., 0.5, 0.], [0., 0.5, 0.5], [0., 0., 0.25], [0.5, 0.5, 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['g', 'h', 'i', 'j'])
        bool_set = map(f, [[0., 0., pos[2]], [0.5, 0.5, pos[2]], [0., 0.5, pos[2]], [pos[0], pos[1], 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'k'

def sp_85(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a P4/n system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5], [0., 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['d', 'e', 'f'])
        bool_set = map(f, [[0.25, 0.25, 0.], [0.25, 0.25, 0.5], [0., 0., pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'g'

def sp_85_s(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a P4/n system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c'])
        bool_set = map(f, [[0.25, 0.75, 0.], [0.25, 0.75, 0.5], [0.25, 0.25, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['d', 'e', 'f'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5], [0.25, 0.75, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'g'

def sp_86(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a P4_2/n system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['c', 'd', 'e', 'f'])
        bool_set = map(f, [[0.25, 0.25, 0.25], [0.25, 0.25, 0.75], [0., 0.5, pos[2]], [0., 0., pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'g'

def sp_86_s(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a P4_2/n system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0.25, 0.25, 0.25], [0.25, 0.25, 0.75]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['c', 'd', 'e', 'f'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5], [0.75, 0.25, pos[2]], [0.25, 0.25, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'g'

def sp_87(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8 and multiplicity != 16:
        raise ValueError("It is not a I4/m system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['c', 'd', 'e'])
        bool_set = map(f, [[0., 0.5, 0.], [0., 0.5, 0.25], [0., 0., pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['f', 'g', 'h'])
        bool_set = map(f, [[0.25, 0.25, 0.25], [0., 0.5, pos[2]], [pos[0], pos[1], 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'i'

def sp_88(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8 and multiplicity != 16:
        raise ValueError("It is not a I4_1/a system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['c', 'd', 'e'])
        bool_set = map(f, [[0., 0.25, 0.125], [0., 0.25, 0.625], [0., 0., pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'f'

def sp_88_s(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8 and multiplicity != 16:
        raise ValueError("It is not a I4_1/a system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0.25, 0.125], [0., 0.25, 0.625]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['c', 'd', 'e'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5], [0., 0.25, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'f'

def sp_89(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 1 and multiplicity != 2 and multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a P422 system!")
    elif multiplicity == 1:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5], [0.5, 0.5, 0.], [0.5, 0.5, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 2:
        symbol_set = np.array(['e', 'f', 'g', 'h'])
        bool_set = map(f, [[0.5, 0., 0.], [0.5, 0., 0.5], [0., 0., pos[2]], [0.5, 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['i', 'j', 'k', 'l', 'm', 'n', 'o'])
        bool_set = map(f, [[0., 0.5, pos[2]], [pos[0], pos[0], 0.], [pos[0], pos[0], 0.5], [pos[0], 0., 0.], [pos[0], 0.5, 0.5], \
        [pos[0], 0., 0.5], [pos[0], 0.5, 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'p'

def sp_90(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a P42_12 system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5], [0., 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['d', 'e', 'f'])
        bool_set = map(f, [[0., 0., pos[2]], [pos[0], pos[0], 0.], [pos[0], pos[0], 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'g'

def sp_91(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a P4_122 system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b', 'c'])
        bool_set = map(f, [[0., pos[1], 0.], [0.5, pos[1], 0.], [pos[0], pos[0], 0.375]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'd'

def sp_92(multiplicity, pos):
    if multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a P4_12_12 system!")
    elif multiplicity == 4:
        return 'a'
    else:
        return 'b'

def sp_93(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a P4_222 system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c', 'd', 'e', 'f'])
        bool_set = map(f, [[0., 0., 0.], [0.5, 0.5, 0.], [0., 0.5, 0.], [0., 0.5, 0.5], [0., 0., 0.25], [0.5, 0.5, 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'])
        bool_set = map(f, [[0., 0., pos[2]], [0.5, 0.5, pos[2]], [0., 0.5, pos[2]], [pos[0], 0., 0.], [pos[0], 0.5, 0.5], [pos[0], 0., 0.5], \
        [pos[0], 0.5, 0.], [pos[0], pos[0], 0.25], [pos[0], pos[0], 0.75]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'p'

def sp_94(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a P4_22_12 system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['c', 'd', 'e', 'f'])
        bool_set = map(f, [[0., 0., pos[2]], [0., 0.5, pos[2]], [pos[0], pos[0], 0.], [pos[0], pos[0], 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'g'

def sp_95(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a P4_322 system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b', 'c'])
        bool_set = map(f, [[0., pos[1], 0.], [0.5, pos[1], 0.], [pos[0], pos[0], 0.625]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'd'

def sp_96(multiplicity, pos):
    if multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a P4_32_12 system!")
    elif multiplicity == 4:
        return 'a'
    else:
        return 'b'

def sp_97(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8 and multiplicity != 16:
        raise ValueError("It is not a I422 system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['c', 'd', 'e'])
        bool_set = map(f, [[0., 0.5, 0.], [0., 0.5, 0.25], [0., 0., pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['f', 'g', 'h', 'i', 'j'])
        bool_set = map(f, [[0., 0.5, pos[2]], [pos[0], pos[0], 0.], [pos[0], 0., 0.], [pos[0], 0., 0.5], [pos[0], pos[0]+0.5, 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'k'

def sp_98(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8 and multiplicity != 16:
        raise ValueError("It is not a I4_122 system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['c', 'd', 'e', 'f'])
        bool_set = map(f, [[0., 0., pos[2]], [pos[0], pos[0], 0.], [-pos[0], pos[0], 0.], [pos[0], 0.25, 0.125]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'g'

def sp_99(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 1 and multiplicity != 2 and multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a P4mm system!")
    elif multiplicity == 1:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., pos[2]], [0.5, 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 2:
        return 'c'
    elif multiplicity == 4:
        symbol_set = np.array(['d', 'e', 'f'])
        bool_set = map(f, [[pos[0], pos[0], pos[2]], [pos[0], 0., pos[2]], [pos[0], 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'g'

def sp_100(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a P4bm system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., pos[2]], [0.5, 0., pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        return 'c'
    else:
        return 'd'

def sp_101(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a P4_2cm system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., pos[2]], [0.5, 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['c', 'd'])
        bool_set = map(f, [[0., 0.5, pos[2]], [pos[0], pos[0], pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'e'

def sp_102(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a P4_2nm system!")
    elif multiplicity == 2:
        return 'a'
    elif multiplicity == 4:
        symbol_set = np.array(['b', 'c'])
        bool_set = map(f, [[0., 0.5, pos[2]], [pos[0], pos[0], pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'd'

def sp_103(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a P4cc system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., pos[2]], [0.5, 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        return 'c'
    else:
        return 'd'

def sp_104(multiplicity, pos):
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a P4nc system!")
    elif multiplicity == 2:
        return 'a'
    elif multiplicity == 4:
        return 'b'
    else:
        return 'c'

def sp_105(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a P4_2mc system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c'])
        bool_set = map(f, [[0., 0., pos[2]], [0.5, 0.5, pos[2]], [0., 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['d', 'e'])
        bool_set = map(f, [[pos[0], 0., pos[2]], [pos[0], 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'f'

def sp_106(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a P4_2bc system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., pos[2]], [0., 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'c'

def sp_107(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8 and multiplicity != 16:
        raise ValueError("It is not a I4mm system!")
    elif multiplicity == 2:
        return 'a'
    elif multiplicity == 4:
        return 'b'
    elif multiplicity == 8:
        symbol_set = np.array(['c', 'd'])
        bool_set = map(f, [[pos[0], pos[0], pos[2]], [pos[0], 0., pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'e'

def sp_108(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8 and multiplicity != 16:
        raise ValueError("It is not a I4cm system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., pos[2]], [0.5, 0., pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        return 'c'
    else:
        return 'd'

def sp_109(multiplicity, pos):
    if multiplicity != 4 and multiplicity != 8 and multiplicity != 16:
        raise ValueError("It is not a I4_1md system!")
    elif multiplicity == 4:
        return 'a'
    elif multiplicity == 8:
        return 'b'
    else:
        return 'c'

def sp_110(multiplicity, pos):
    if multiplicity != 8 and multiplicity != 16:
        raise ValueError("It is not a I4_1cd system!")
    elif multiplicity == 8:
        return 'a'
    else:
        return 'b'

def sp_111(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 1 and multiplicity != 2 and multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a P-42m system!")
    elif multiplicity == 1:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0., 0., 0.], [0.5, 0.5, 0.5], [0., 0., 0.5], [0.5, 0.5, 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 2:
        symbol_set = np.array(['e', 'f', 'g', 'h'])
        bool_set = map(f, [[0.5, 0., 0.], [0.5, 0., 0.5], [0., 0., pos[2]], [0.5, 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['i', 'j', 'k', 'l', 'm', 'n'])
        bool_set = map(f, [[pos[0], 0., 0.], [pos[0], 0.5, 0.5], [pos[0], 0., 0.5], [pos[0], 0.5, 0.], [0., 0.5, pos[2]], [pos[0], pos[0], pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'o'

def sp_112(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a P-42c system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c', 'd', 'e', 'f'])
        bool_set = map(f, [[0., 0., 0.25], [0.5, 0., 0.25], [0.5, 0.5, 0.25], [0., 0.5, 0.25], [0., 0., 0.], [0.5, 0.5, 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['g', 'h', 'i', 'j', 'k', 'l', 'm'])
        bool_set = map(f, [[pos[0], 0., 0.25], [0.5, pos[1], 0.25], [pos[0], 0.5, 0.25], [0., pos[1], 0.25], [0., 0., pos[2]], \
        [0.5, 0.5, pos[2]], [0., 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'n'

def sp_113(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a P-42_1m system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5], [0., 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['d', 'e'])
        bool_set = map(f, [[0., 0., pos[2]], [pos[0], pos[0]+0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'f'

def sp_114(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a P-42_1c system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['c', 'd'])
        bool_set = map(f, [[0., 0., pos[2]], [0., 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'e'

def sp_115(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 1 and multiplicity != 2 and multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a P-4m2 system!")
    elif multiplicity == 1:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0., 0., 0.], [0.5, 0.5, 0.], [0.5, 0.5, 0.5], [0., 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 2:
        symbol_set = np.array(['e', 'f', 'g'])
        bool_set = map(f, [[0., 0., pos[2]], [0.5, 0.5, pos[2]], [0., 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['h', 'i', 'j', 'k'])
        bool_set = map(f, [[pos[0], pos[0], 0.], [pos[0], pos[0], 0.5], [pos[0], 0., pos[2]], [pos[0], 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'l'

def sp_116(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a P-4c2 system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0., 0., 0.25], [0.5, 0.5, 0.25], [0., 0., 0.], [0.5, 0.5, 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['e', 'f', 'g', 'h', 'i'])
        bool_set = map(f, [[pos[0], pos[0], 0.25], [pos[0], pos[0], 0.75], [0., 0., pos[2]], [0.5, 0.5, pos[2]], [0., 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'j'

def sp_117(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a P-4b2 system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5], [0., 0.5, 0.], [0., 0.5, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['e', 'f', 'g', 'h'])
        bool_set = map(f, [[0., 0., pos[2]], [0., 0.5, pos[2]], [pos[0], pos[0]+0.5, 0.], [pos[0], pos[0]+0.5, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'i'

def sp_118(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8:
        raise ValueError("It is not a P-4n2 system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5], [0., 0.5, 0.25], [0., 0.5, 0.75]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['e', 'f', 'g', 'h'])
        bool_set = map(f, [[0., 0., pos[2]], [pos[0], -pos[0]+0.5, 0.25], [pos[0], pos[0]+0.5, 0.25], [0., 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'i'

def sp_119(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8 and multiplicity != 16:
        raise ValueError("It is not a I-4m2 system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5], [0., 0.5, 0.25], [0., 0.5, 0.75]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['e', 'f'])
        bool_set = map(f, [[0., 0., pos[2]], [0., 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['g', 'h', 'i'])
        bool_set = map(f, [[pos[0], pos[0], 0.], [pos[0], pos[0]+0.5, 0.25], [pos[0], 0., pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'j'

def sp_120(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8 and multiplicity != 16:
        raise ValueError("It is not a I-4c2 system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0., 0., 0.25], [0., 0., 0.], [0., 0.5, 0.25], [0., 0.5, 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['e', 'f', 'g', 'h'])
        bool_set = map(f, [[pos[0], pos[0], 0.25], [0., 0., pos[2]], [0., 0.5, pos[2]], [pos[0], pos[0]+0.5, 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'i'

def sp_121(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8 and multiplicity != 16:
        raise ValueError("It is not a I-42m system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['c', 'd', 'e'])
        bool_set = map(f, [[0., 0.5, 0.], [0., 0.5, 0.25], [0., 0., pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['f', 'g', 'h', 'i'])
        bool_set = map(f, [[pos[0], 0., 0.], [pos[0], 0., 0.5], [0., 0.5, pos[2]], [pos[0], pos[0], pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'j'

def sp_122(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8 and multiplicity != 16:
        raise ValueError("It is not a I-42d system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['c', 'd'])
        bool_set = map(f, [[0., 0., pos[2]], [pos[0], 0.25, 0.125]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'e'

def sp_123(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 1 and multiplicity != 2 and multiplicity != 4 and multiplicity != 8 and multiplicity != 16:
        raise ValueError("It is not a P4/mmm system!")
    elif multiplicity == 1:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5], [0.5, 0.5, 0.], [0.5, 0.5, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 2:
        symbol_set = np.array(['e', 'f', 'g', 'h'])
        bool_set = map(f, [[0., 0.5, 0.5], [0., 0.5, 0.], [0., 0., pos[2]], [0.5, 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['i', 'j', 'k', 'l', 'm', 'n', 'o'])
        bool_set = map(f, [[0., 0.5, pos[2]], [pos[0], pos[0], 0.], [pos[0], pos[0], 0.5], [pos[0], 0., 0.], [pos[0], 0., 0.5], [pos[0], 0.5, 0.], \
        [pos[0], 0.5, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['p', 'q', 'r', 's', 't'])
        bool_set = map(f, [[pos[0], pos[1], 0.], [pos[0], pos[1], 0.5], [pos[0], pos[0], pos[2]], [pos[0], 0., pos[2]], [pos[0], 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'u'

def sp_124(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8 and multiplicity != 16:
        raise ValueError("It is not a P4/mcc system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0., 0., 0.25], [0., 0., 0.], [0.5, 0.5, 0.25], [0.5, 0.5, 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['e', 'f', 'g', 'h'])
        bool_set = map(f, [[0., 0.5, 0.], [0., 0.5, 0.25], [0., 0., pos[2]], [0.5, 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['i', 'j', 'k', 'l', 'm'])
        bool_set = map(f, [[0., 0.5, pos[2]], [pos[0], pos[0], 0.25], [pos[0], 0., 0.25], [pos[0], 0.5, 0.25], [pos[0], pos[1], 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'n'

def sp_125(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8 and multiplicity != 16:
        raise ValueError("It is not a P4/nbm system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5], [0., 0.5, 0.], [0., 0.5, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['e', 'f', 'g', 'h'])
        bool_set = map(f, [[0.25, 0.25, 0.], [0.25, 0.25, 0.5], [0., 0., pos[2]], [0., 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['i', 'j', 'k', 'l', 'm'])
        bool_set = map(f, [[pos[0], pos[0], 0.], [pos[0], pos[0], 0.5], [pos[0], 0., 0.], [pos[0], 0., 0.5], [pos[0], pos[0]+0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'n'

def sp_125_s(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8 and multiplicity != 16:
        raise ValueError("It is not a P4/nbm system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0.25, 0.25, 0.], [0.25, 0.25, 0.5], [0.75, 0.25, 0.], [0.75, 0.25, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['e', 'f', 'g', 'h'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5], [0.25, 0.25, pos[2]], [0.75, 0.25, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['i', 'j', 'k', 'l', 'm'])
        bool_set = map(f, [[pos[0], pos[0], 0.], [pos[0], pos[0], 0.5], [pos[0], 0.25, 0.], [pos[0], 0.25, 0.5], [pos[0], -pos[0], pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'n'

def sp_126(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8 and multiplicity != 16:
        raise ValueError("It is not a P4/nnc system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['c', 'd', 'e'])
        bool_set = map(f, [[0.5, 0., 0.], [0.5, 0., 0.25], [0., 0., pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['f', 'g', 'h', 'i', 'j'])
        bool_set = map(f, [[0.25, 0.25, 0.25], [0.5, 0., pos[2]], [pos[0], pos[0], 0.], [pos[0], 0., 0.], [pos[0], 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'k'

def sp_126_s(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8 and multiplicity != 16:
        raise ValueError("It is not a P4/nnc system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0.25, 0.25, 0.25], [0.25, 0.25, 0.75]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['c', 'd', 'e'])
        bool_set = map(f, [[0.25, 0.75, 0.75], [0.25, 0.75, 0.], [0.25, 0.25, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['f', 'g', 'h', 'i', 'j'])
        bool_set = map(f, [[0., 0., 0.], [0.25, 0.75, pos[2]], [pos[0], pos[0], 0.25], [pos[0], 0.25, 0.25], [pos[0], 0.75, 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'k'

def sp_127(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8 and multiplicity != 16:
        raise ValueError("It is not a P4/mbm system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5], [0., 0.5, 0.5], [0., 0.5, 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['e', 'f', 'g', 'h'])
        bool_set = map(f, [[0., 0., pos[2]], [0., 0.5, pos[2]], [pos[0], pos[0]+0.5, 0.], [pos[0], pos[0]+0.5, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['i', 'j', 'k'])
        bool_set = map(f, [[pos[0], pos[1], 0.], [pos[0], pos[1], 0.5], [pos[0], pos[0]+0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'l'

def sp_128(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8 and multiplicity != 16:
        raise ValueError("It is not a P4/mnc system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['c', 'd', 'e'])
        bool_set = map(f, [[0., 0.5, 0.], [0., 0.5, 0.25], [0., 0., pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['f', 'g', 'h'])
        bool_set = map(f, [[0., 0.5, pos[2]], [pos[0], pos[0]+0.5, 0.25], [pos[0], pos[1], 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'i'

def sp_129(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8 and multiplicity != 16:
        raise ValueError("It is not a P4/nmm system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5], [0., 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['d', 'e', 'f'])
        bool_set = map(f, [[0.25, 0.25, 0.], [0.25, 0.25, 0.5], [0., 0., pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['g', 'h', 'i', 'j'])
        bool_set = map(f, [[pos[0], pos[0], 0.], [pos[0], pos[0], 0.5], [0., pos[1], pos[2]], [pos[0], pos[0]+0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'k'

def sp_129_s(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8 and multiplicity != 16:
        raise ValueError("It is not a P4/nmm system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c'])
        bool_set = map(f, [[0.75, 0.25, 0.], [0.75, 0.25, 0.5], [0.25, 0.25, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['d', 'e', 'f'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5], [0.75, 0.25, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['g', 'h', 'i', 'j'])
        bool_set = map(f, [[pos[0], -pos[0], 0.], [pos[0], -pos[0], 0.5], [0.25, pos[1], pos[2]], [pos[0], pos[0], pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'k'

def sp_130(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8 and multiplicity != 16:
        raise ValueError("It is not a P4/ncc system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b', 'c'])
        bool_set = map(f, [[0., 0., 0.25], [0., 0., 0.], [0., 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['d', 'e', 'f'])
        bool_set = map(f, [[0.25, 0.25, 0.], [0., 0., pos[2]], [pos[0], pos[0], 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'g'

def sp_130_s(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8 and multiplicity != 16:
        raise ValueError("It is not a P4/ncc system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b', 'c'])
        bool_set = map(f, [[0.75, 0.25, 0.25], [0.75, 0.25, 0.], [0.25, 0.25, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['d', 'e', 'f'])
        bool_set = map(f, [[0., 0., 0.], [0.75, 0.25, pos[2]], [pos[0], -pos[0], 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'g'

def sp_131(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8 and multiplicity != 16:
        raise ValueError("It is not a P4_2/mmc system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c', 'd', 'e', 'f'])
        bool_set = map(f, [[0., 0., 0.], [0.5, 0.5, 0.], [0., 0.5, 0.], [0., 0.5, 0.5], [0., 0., 0.25], [0.5, 0.5, 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['g', 'h', 'i', 'j', 'k', 'l', 'm'])
        bool_set = map(f, [[0., 0., pos[2]], [0.5, 0.5, pos[2]], [0., 0.5, pos[2]], [pos[0], 0., 0.], [pos[0], 0.5, 0.5], [pos[0], 0., 0.5], \
        [pos[0], 0.5, 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['n', 'o', 'p', 'q'])
        bool_set = map(f, [[pos[0], pos[0], 0.25], [0., pos[1], pos[2]], [0.5, pos[1], pos[2]], [pos[0], pos[1], 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'r'

def sp_132(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8 and multiplicity != 16:
        raise ValueError("It is not a P4/mcm system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.25], [0.5, 0.5, 0.], [0.5, 0.5, 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['e', 'f', 'g', 'h', 'i', 'j'])
        bool_set = map(f, [[0., 0.5, 0.25], [0., 0.5, 0.], [0., 0., pos[2]], [0.5, 0.5, pos[2]], [pos[0], pos[0], 0.], [pos[0], pos[0], 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['k', 'l', 'm', 'n', 'o'])
        bool_set = map(f, [[0., 0.5, pos[2]], [pos[0], 0., 0.25], [pos[0], 0.5, 0.25], [pos[0], pos[1], 0.], [pos[0], pos[0], pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'p'

def sp_133(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8 and multiplicity != 16:
        raise ValueError("It is not a P4_2/nbc system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0., 0.5, 0.25], [0., 0., 0.25], [0., 0.5, 0.], [0., 0., 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['e', 'f', 'g', 'h', 'i', 'j'])
        bool_set = map(f, [[0.25, 0.25, 0.25], [0., 0.5, pos[2]], [0., 0., pos[2]], [pos[0], 0., 0.25], [pos[0], 0., 0.75], [pos[0], pos[0]+0.5, 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'k'

def sp_133_s(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8 and multiplicity != 16:
        raise ValueError("It is not a P4_2/nbc system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0.25, 0.25, 0.], [0.75, 0.25, 0.], [0.25, 0.25, 0.25], [0.75, 0.25, 0.75]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['e', 'f', 'g', 'h', 'i', 'j'])
        bool_set = map(f, [[0., 0., 0.], [0.25, 0.25, pos[2]], [0.75, 0.25, pos[2]], [pos[0], 0.25, 0.], [pos[0], 0.25, 0.5], [pos[0], pos[0], 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'k'

def sp_134(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8 and multiplicity != 16:
        raise ValueError("It is not a P4_2/nnm system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['c', 'd', 'e', 'f', 'g'])
        bool_set = map(f, [[0., 0.5, 0.], [0., 0.5, 0.25], [0.25, 0.25, 0.25], [0.75, 0.75, 0.75], [0., 0., pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['h', 'i', 'j', 'k', 'l', 'm'])
        bool_set = map(f, [[0., 0.5, pos[2]], [pos[0], 0., 0.], [pos[0], 0., 0.5], [pos[0], pos[0]+0.5, 0.25], [pos[0], pos[0]+0.5, 0.75], \
        [pos[0], pos[0], pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'n'

def sp_134_s(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8 and multiplicity != 16:
        raise ValueError("It is not a P4_2/nnm system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0.25, 0.75, 0.25], [0.75, 0.25, 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['c', 'd', 'e', 'f', 'g'])
        bool_set = map(f, [[0.25, 0.25, 0.25], [0.25, 0.25, 0.], [0., 0., 0.5], [0., 0., 0.], [0.75, 0.25, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['h', 'i', 'j', 'k', 'l', 'm'])
        bool_set = map(f, [[0.25, 0.25, pos[2]], [pos[0], 0.25, 0.75], [pos[0], 0.25, 0.25], [pos[0], pos[0], 0.], [pos[0], pos[0], 0.5], \
        [pos[0], -pos[0], pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'n'

def sp_135(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8 and multiplicity != 16:
        raise ValueError("It is not a P4_2/mbc system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.25], [0., 0.5, 0.], [0., 0.5, 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['e', 'f', 'g', 'h'])
        bool_set = map(f, [[0., 0., pos[2]], [0., 0.5, pos[2]], [pos[0], pos[0]+0.5, 0.25], [pos[0], pos[1], 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'i'

def sp_136(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8 and multiplicity != 16:
        raise ValueError("It is not a P4_2/mnm system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['c', 'd', 'e', 'f', 'g'])
        bool_set = map(f, [[0., 0.5, 0.], [0., 0.5, 0.25], [0., 0., pos[2]], [pos[0], pos[0], 0.], [pos[0], -pos[0], 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['h', 'i', 'j'])
        bool_set = map(f, [[0., 0.5, pos[2]], [pos[0], pos[1], 0.], [pos[0], pos[0], pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'k'

def sp_137(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8 and multiplicity != 16:
        raise ValueError("It is not a P4_2/nmc system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['c', 'd'])
        bool_set = map(f, [[0., 0., pos[2]], [0., 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['e', 'f', 'g'])
        bool_set = map(f, [[0.25, 0.25, 0.25], [pos[0], pos[0], 0.], [0., pos[1], pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'h'

def sp_137_s(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8 and multiplicity != 16:
        raise ValueError("It is not a P4_2/nmc system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0.75, 0.25, 0.75], [0.75, 0.25, 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['c', 'd'])
        bool_set = map(f, [[0.75, 0.25, pos[2]], [0.25, 0.25, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['e', 'f', 'g'])
        bool_set = map(f, [[0., 0., 0.], [pos[0], -pos[0], 0.25], [0.25, pos[1], pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'h'

def sp_138(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8 and multiplicity != 16:
        raise ValueError("It is not a P4_2/ncm system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b', 'c', 'd', 'e'])
        bool_set = map(f, [[0., 0., 0.25], [0., 0., 0.], [0.25, 0.25, 0.25], [0.25, 0.25, 0.75], [0., 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['f', 'g', 'h', 'i'])
        bool_set = map(f, [[0., 0., pos[2]], [pos[0], pos[0], 0.25], [pos[0], pos[0], 0.75], [pos[0], pos[0]+0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'j'

def sp_138_s(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8 and multiplicity != 16:
        raise ValueError("It is not a P4_2/ncm system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b', 'c', 'd', 'e'])
        bool_set = map(f, [[0.75, 0.25, 0.], [0.75, 0.25, 0.75], [0., 0., 0.5], [0., 0., 0.], [0.25, 0.25, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['f', 'g', 'h', 'i'])
        bool_set = map(f, [[0.75, 0.25, pos[2]], [pos[0], -pos[0], 0.5], [pos[0], -pos[0], 0.], [pos[0], pos[0], pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'j'

def sp_139(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 8 and multiplicity != 16 and multiplicity != 32:
        raise ValueError("It is not a I4/mmm system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['c', 'd', 'e'])
        bool_set = map(f, [[0., 0.5, 0.], [0., 0.5, 0.25], [0., 0., pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['f', 'g', 'h', 'i', 'j'])
        bool_set = map(f, [[0.25, 0.25, 0.25], [0., 0.5, pos[2]], [pos[0], pos[0], 0.], [pos[0], 0., 0.], [pos[0], 0.5, 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 16:
        symbol_set = np.array(['k', 'l', 'm', 'n'])
        bool_set = map(f, [[pos[0], pos[0]+0.5, 0.25], [pos[0], pos[1], 0.], [pos[0], pos[0], pos[2]], [0., pos[1], pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'o'

def sp_140(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8 and multiplicity != 16 and multiplicity != 32:
        raise ValueError("It is not a I4/mcm system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0., 0., 0.25], [0., 0.5, 0.25], [0., 0., 0.], [0., 0.5, 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['e', 'f', 'g', 'h'])
        bool_set = map(f, [[0.25, 0.25, 0.25], [0., 0., pos[2]], [0., 0.5, pos[2]], [pos[0], pos[0]+0.5, 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 16:
        symbol_set = np.array(['i', 'j', 'k', 'l'])
        bool_set = map(f, [[pos[0], pos[0], 0.25], [pos[0], 0., 0.25], [pos[0], pos[1], 0.], [pos[0], pos[0]+0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'm'

def sp_141(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8 and multiplicity != 16 and multiplicity != 32:
        raise ValueError("It is not a I4_1/amd system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['c', 'd', 'e'])
        bool_set = map(f, [[0., 0.25, 0.125], [0., 0.25, 0.625], [0., 0., pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 16:
        symbol_set = np.array(['f', 'g', 'h'])
        bool_set = map(f, [[pos[0], 0.25, 0.125], [pos[0], pos[0], 0.], [0., pos[1], pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'i'

def sp_141_s(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8 and multiplicity != 16 and multiplicity != 32:
        raise ValueError("It is not a I4_1/amd system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0.75, 0.125], [0., 0.25, 0.375]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['c', 'd', 'e'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5], [0., 0.25, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 16:
        symbol_set = np.array(['f', 'g', 'h'])
        bool_set = map(f, [[pos[0], 0., 0.], [pos[0], pos[0]+0.25, 0.875], [0., pos[1], pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'i'

def sp_142(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 8 and multiplicity != 16 and multiplicity != 32:
        raise ValueError("It is not a I4_1/acd system!")
    elif multiplicity == 8:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 16:
        symbol_set = np.array(['c', 'd', 'e', 'f'])
        bool_set = map(f, [[0., 0.25, 0.125], [0., 0., pos[2]], [0.25, pos[1], 0.125], [pos[0], pos[0], 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'g'

def sp_142_s(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 8 and multiplicity != 16 and multiplicity != 32:
        raise ValueError("It is not a I4_1/acd system!")
    elif multiplicity == 8:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0.25, 0.375], [0., 0.25, 0.125]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 16:
        symbol_set = np.array(['c', 'd', 'e', 'f'])
        bool_set = map(f, [[0., 0., 0.], [0., 0.25, pos[2]], [pos[0], 0., 0.25], [pos[0], pos[0]+0.25, 0.125]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'g'

def sp_143(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 1 and multiplicity != 3:
        raise ValueError("It is not a P3 system!")
    elif multiplicity == 1:
        symbol_set = np.array(['a', 'b', 'c'])
        bool_set = map(f, [[0., 0., pos[2]], [1./3, 2./3, pos[2]], [2./3, 1./3, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'd'

def sp_144(multiplicity, pos):
    if multiplicity != 3:
        raise ValueError("It is not a P3_1 system!")
    else:
        return 'a'

def sp_145(multiplicity, pos):
    if multiplicity != 3:
        raise ValueError("It is not a P3_2 system!")
    else:
        return 'a'

def sp_146_R(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 1 and multiplicity != 3:
        return False
    elif multiplicity == 1:
        symbol_set = np.array(['a'])
        bool_set = map(f, [[pos[0], pos[0], pos[0]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'b'

def sp_146_H(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 3 and multiplicity != 9:
        return False
    elif multiplicity == 3:
        symbol_set = np.array(['a'])
        bool_set = map(f, [[0., 0., pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'b'

def sp_147(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 1 and multiplicity != 2 and multiplicity != 3 and multiplicity != 6:
        raise ValueError("It is not a P-3 system!")
    elif multiplicity == 1:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 2:
        symbol_set = np.array(['c', 'd'])
        bool_set = map(f, [[0., 0., pos[2]], [1./3, 2./3, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 3:
        symbol_set = np.array(['e', 'f'])
        bool_set = map(f, [[0.5, 0., 0.], [0.5, 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'g'

def sp_148_R(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 1 and multiplicity != 2 and multiplicity != 3 and multiplicity != 6:
        return False
    elif multiplicity == 1:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0.5, 0.5, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 2:
        symbol_set = np.array(['c'])
        bool_set = map(f, [[pos[0], pos[0], pos[0]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 3:
        symbol_set = np.array(['d', 'e'])
        bool_set = map(f, [[0.5, 0., 0.], [0., 0.5, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'f'

def sp_148_H(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 3 and multiplicity != 6 and multiplicity != 9 and multiplicity != 18:
        return False
    elif multiplicity == 3:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 6:
        symbol_set = np.array(['c'])
        bool_set = map(f, [[0., 0., pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 9:
        symbol_set = np.array(['d', 'e'])
        bool_set = map(f, [[0.5, 0., 0.5], [0.5, 0., 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'f'

def sp_149(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 1 and multiplicity != 2 and multiplicity != 3 and multiplicity != 6:
        raise ValueError("It is not a P312 system!")
    elif multiplicity == 1:
        symbol_set = np.array(['a', 'b', 'c', 'd', 'e', 'f'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5], [1./3, 2./3, 0.], [1./3, 2./3, 0.5], [2./3, 1./3, 0.], [2./3, 1./3, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 2:
        symbol_set = np.array(['g', 'h', 'i'])
        bool_set = map(f, [[0., 0., pos[2]], [1./3, 2./3, pos[2]], [2./3, 1./3, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 3:
        symbol_set = np.array(['j', 'k'])
        bool_set = map(f, [[pos[0], -pos[0], 0.], [pos[0], -pos[0], 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'l'

def sp_150(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 1 and multiplicity != 2 and multiplicity != 3 and multiplicity != 6:
        raise ValueError("It is not a P321 system!")
    elif multiplicity == 1:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 2:
        symbol_set = np.array(['c', 'd'])
        bool_set = map(f, [[0., 0., pos[2]], [1./3, 2./3, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 3:
        symbol_set = np.array(['e', 'f'])
        bool_set = map(f, [[pos[0], 0., 0.], [pos[0], 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'g'

def sp_151(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 3 and multiplicity != 6:
        raise ValueError("It is not a P3_112 system!")
    elif multiplicity == 3:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[pos[0], -pos[0], 1./3], [pos[0], -pos[0], 5./6]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'c'

def sp_152(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 3 and multiplicity != 6:
        raise ValueError("It is not a P3_121 system!")
    elif multiplicity == 3:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[pos[0], 0., 1./3], [pos[0], 0., 5./6]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'c'

def sp_153(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 3 and multiplicity != 6:
        raise ValueError("It is not a P3_212 system!")
    elif multiplicity == 3:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[pos[0], -pos[0], 2./3], [pos[0], -pos[0], 1./6]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'c'

def sp_154(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 3 and multiplicity != 6:
        raise ValueError("It is not a P3_221 system!")
    elif multiplicity == 3:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[pos[0], 0., 2./3], [pos[0], 0., 1./6]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'c'

def sp_155_R(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 1 and multiplicity != 2 and multiplicity != 3 and multiplicity != 6:
        return False
    elif multiplicity == 1:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0.5, 0.5, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 2:
        symbol_set = np.array(['c'])
        bool_set = map(f, [[pos[0], pos[0], pos[0]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 3:
        symbol_set = np.array(['d', 'e'])
        bool_set = map(f, [[0., pos[1], -pos[1]], [0.5, pos[1], -pos[1]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'f'

def sp_155_H(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 3 and multiplicity != 6 and multiplicity != 9 and multiplicity != 18:
        return False
    elif multiplicity == 3:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 6:
        symbol_set = np.array(['c'])
        bool_set = map(f, [[0., 0., pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 9:
        symbol_set = np.array(['d', 'e'])
        bool_set = map(f, [[pos[0], 0., 0.], [pos[0], 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'f'

def sp_156(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 1 and multiplicity != 3 and multiplicity != 6:
        raise ValueError("It is not a P3m1 system!")
    elif multiplicity == 1:
        symbol_set = np.array(['a', 'b', 'c'])
        bool_set = map(f, [[0., 0., pos[2]], [1./3, 2./3, pos[2]], [2./3, 1./3, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 3:
        return 'd'
    else:
        return 'e'

def sp_157(multiplicity, pos):
    if multiplicity != 1 and multiplicity != 2 and multiplicity != 3 and multiplicity != 6:
        raise ValueError("It is not a P31m system!")
    elif multiplicity == 1:
        return 'a'
    elif multiplicity == 2:
        return 'b'
    elif multiplicity == 3:
        return 'c'
    else:
        return 'd'

def sp_158(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 6:
        raise ValueError("It is not a P3c1 system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c'])
        bool_set = map(f, [[0., 0., pos[2]], [1./3, 2./3, pos[2]], [2./3, 1./3, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'd'

def sp_159(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 6:
        raise ValueError("It is not a P31c system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., pos[2]], [1./3, 2./3, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'c'

def sp_160_R(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 1 and multiplicity != 3 and multiplicity != 6:
        raise False
    elif multiplicity == 1:
        symbol_set = np.array(['a'])
        bool_set = map(f, [[pos[0], pos[0], pos[0]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 3:
        symbol_set = np.array(['b'])
        bool_set = map(f, [[pos[0], pos[0], pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'c'

def sp_160_H(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 3 and multiplicity != 9 and multiplicity != 18:
        raise False
    elif multiplicity == 3:
        symbol_set = np.array(['a'])
        bool_set = map(f, [[0., 0., pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 9:
        symbol_set = np.array(['b'])
        bool_set = map(f, [[pos[0], -pos[0], pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'c'

def sp_161_R(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 6:
        raise False
    elif multiplicity == 2:
        symbol_set = np.array(['a'])
        bool_set = map(f, [[pos[0], pos[0], pos[0]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'b'

def sp_161_H(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 6 and multiplicity != 18:
        raise False
    elif multiplicity == 6:
        symbol_set = np.array(['a'])
        bool_set = map(f, [[0., 0., pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'b'

def sp_162(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 1 and multiplicity != 2 and multiplicity != 3 and multiplicity != 4 and multiplicity != 6 and multiplicity != 12:
        raise ValueError("It is not a P-31m system!")
    elif multiplicity == 1:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 2:
        symbol_set = np.array(['c', 'd', 'e'])
        bool_set = map(f, [[1./3, 2./3, 0.], [1./3, 2./3, 0.5], [0., 0., pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 3:
        symbol_set = np.array(['f', 'g'])
        bool_set = map(f, [[0.5, 0., 0.], [0.5, 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        return 'h'
    elif multiplicity == 6:
        symbol_set = np.array(['i', 'j', 'k'])
        bool_set = map(f, [[pos[0], -pos[0], 0.], [pos[0], -pos[0], 0.5], [pos[0], 0., pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'l'

def sp_163(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 6 and multiplicity != 12:
        raise ValueError("It is not a P-31c system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0., 0., 0.25], [0., 0., 0.], [1./3, 2./3, 0.25], [2./3, 1./3, 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['e', 'f'])
        bool_set = map(f, [[0., 0., pos[2]], [1./3, 2./3, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 6:
        symbol_set = np.array(['g', 'h'])
        bool_set = map(f, [[0.5, 0., 0.], [pos[0], -pos[0], 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'i'

def sp_164(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 1 and multiplicity != 2 and multiplicity != 3 and multiplicity != 6 and multiplicity != 12:
        raise ValueError("It is not a P-3m1 system!")
    elif multiplicity == 1:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 2:
        symbol_set = np.array(['c', 'd'])
        bool_set = map(f, [[0., 0., pos[2]], [1./3, 2./3, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 3:
        symbol_set = np.array(['e', 'f'])
        bool_set = map(f, [[0.5, 0., 0.], [0.5, 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 6:
        symbol_set = np.array(['g', 'h', 'i'])
        bool_set = map(f, [[pos[0], 0., 0.], [pos[0], 0., 0.5], [pos[0], -pos[0], pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'j'

def sp_165(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 6 and multiplicity != 12:
        raise ValueError("It is not a P-3c1 system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.25], [0., 0., 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['c', 'd'])
        bool_set = map(f, [[0., 0., pos[2]], [1./3, 2./3, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 6:
        symbol_set = np.array(['e', 'f'])
        bool_set = map(f, [[0.5, 0., 0.], [pos[0], 0., 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'g'

def sp_166_R(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 1 and multiplicity != 2 and multiplicity != 3 and multiplicity != 6 and multiplicity != 12:
        return False
    elif multiplicity == 1:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0.5, 0.5, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 2:
        symbol_set = np.array(['c'])
        bool_set = map(f, [[pos[0], pos[0], pos[0]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 3:
        symbol_set = np.array(['d', 'e'])
        bool_set = map(f, [[0.5, 0., 0.], [0., 0.5, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 6:
        symbol_set = np.array(['f', 'g', 'h'])
        bool_set = map(f, [[pos[0], -pos[0], 0.], [pos[0], -pos[0], 0.5], [pos[0], pos[0], pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'i'

def sp_166_H(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 3 and multiplicity != 6 and multiplicity != 9 and multiplicity != 18 and multiplicity != 36:
        return False
    elif multiplicity == 3:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 6:
        symbol_set = np.array(['c'])
        bool_set = map(f, [[0., 0., pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 9:
        symbol_set = np.array(['d', 'e'])
        bool_set = map(f, [[0.5, 0., 0.5], [0.5, 0., 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 18:
        symbol_set = np.array(['f', 'g', 'h'])
        bool_set = map(f, [[pos[0], 0., 0.], [pos[0], 0., 0.5], [pos[0], -pos[0], pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'i'

def sp_167_R(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 6 and multiplicity != 12:
        return False
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0.25, 0.25, 0.25], [0., 0., 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['c'])
        bool_set = map(f, [pos[0], pos[0], pos[0]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 6:
        symbol_set = np.array(['d', 'e'])
        bool_set = map(f, [[0.5, 0., 0.], [pos[0], -pos[0]+0.5, 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'f'

def sp_167_H(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 6 and multiplicity != 12 and multiplicity != 18 and multiplicity != 36:
        return False
    elif multiplicity == 6:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.25], [0., 0., 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 12:
        symbol_set = np.array(['c'])
        bool_set = map(f, [[0., 0., pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 18:
        symbol_set = np.array(['d', 'e'])
        bool_set = map(f, [[0.5, 0., 0.], [pos[0], 0., 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'f'

def sp_168(multiplicity, pos):
    if multiplicity != 1 and multiplicity != 2 and multiplicity != 3 and multiplicity != 6:
        raise ValueError("It is not a P6 system!")
    elif multiplicity == 1:
        return 'a'
    elif multiplicity == 2:
        return 'b'
    elif multiplicity == 3:
        return 'c'
    else:
        return 'd'

def sp_169(multiplicity, pos):
    if multiplicity != 6:
        raise ValueError("It is not a P6_1 system!")
    else:
        return 'a'

def sp_170(multiplicity, pos):
    if multiplicity != 6:
        raise ValueError("It is not a P6_5 system!")
    else:
        return 'a'

def sp_171(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 3 and multiplicity != 6:
        raise ValueError("It is not a P6_2 system!")
    elif multiplicity == 3:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., pos[2]], [0.5, 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'c'

def sp_172(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 3 and multiplicity != 6:
        raise ValueError("It is not a P6_4 system!")
    elif multiplicity == 3:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., pos[2]], [0.5, 0.5, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'c'

def sp_173(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 6:
        raise ValueError("It is not a P6_3 system!")
    elif multiplicity == 3:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., pos[2]], [1./3, 2./3, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'c'

def sp_174(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 1 and multiplicity != 2 and multiplicity != 3 and multiplicity != 6:
        raise ValueError("It is not a P-6 system!")
    elif multiplicity == 1:
        symbol_set = np.array(['a', 'b', 'c', 'd', 'e', 'f'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5], [1./3, 2./3, 0.], [1./3, 2./3, 0.5], [2./3, 1./3, 0.], [2./3, 1./3, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 2:
        symbol_set = np.array(['g', 'h', 'i'])
        bool_set = map(f, [[0., 0., pos[2]], [1./3, 2./3, pos[2]], [2./3, 1./3, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 3:
        symbol_set = np.array(['j', 'k'])
        bool_set = map(f, [[pos[0], pos[1], 0.], [pos[0], pos[1], 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'l'

def sp_175(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 1 and multiplicity != 2 and multiplicity != 3 and multiplicity != 4 and multiplicity != 6 and multiplicity != 12:
        raise ValueError("It is not a P6/m system!")
    elif multiplicity == 1:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 2:
        symbol_set = np.array(['c', 'd', 'e'])
        bool_set = map(f, [[1./3, 2./3, 0.], [1./3, 2./3, 0.5], [0., 0., pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 3:
        symbol_set = np.array(['f', 'g'])
        bool_set = map(f, [[0.5, 0., 0.], [0.5, 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        return 'h'
    elif multiplicity == 6:
        symbol_set = np.array(['i', 'j', 'k'])
        bool_set = map(f, [[0.5, 0., pos[2]], [pos[0], pos[1], 0.], [pos[0], pos[1], 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'l'

def sp_176(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 6 and multiplicity != 12:
        raise ValueError("It is not a P6_3/m system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0., 0., 0.25], [0., 0., 0.], [1./3, 2./3, 0.25], [2./3, 1./3, 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['e', 'f'])
        bool_set = map(f, [[0., 0., pos[2]], [1./3, 2./3, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 6:
        symbol_set = np.array(['g', 'h'])
        bool_set = map(f, [[0.5, 0., 0.], [pos[0], pos[1], 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'i'

def sp_177(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 1 and multiplicity != 2 and multiplicity != 3 and multiplicity != 4 and multiplicity != 6 and multiplicity != 12:
        raise ValueError("It is not a P622 system!")
    elif multiplicity == 1:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 2:
        symbol_set = np.array(['c', 'd', 'e'])
        bool_set = map(f, [[1./3, 2./3, 0.], [1./3, 2./3, 0.5], [0., 0., pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 3:
        symbol_set = np.array(['f', 'g'])
        bool_set = map(f, [[0.5, 0., 0.], [0.5, 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        return 'h'
    elif multiplicity == 6:
        symbol_set = np.array(['i', 'j', 'k', 'l', 'm'])
        bool_set = map(f, [[0.5, 0., pos[2]], [pos[0], 0., 0.], [pos[0], 0., 0.5], [pos[0], -pos[0], 0.], [pos[0], -pos[0], 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'n'

def sp_178(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 6 and multiplicity != 12:
        raise ValueError("It is not a P6_122 system!")
    elif multiplicity == 6:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[pos[0], 0., 0.], [pos[0], 2 * pos[0], 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'c'

def sp_179(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 6 and multiplicity != 12:
        raise ValueError("It is not a P6_522 system!")
    elif multiplicity == 6:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[pos[0], 0., 0.], [pos[0], 2 * pos[0], 0.75]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'c'

def sp_180(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 3 and multiplicity != 6 and multiplicity != 12:
        raise ValueError("It is not a P6_222 system!")
    elif multiplicity == 3:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5], [0.5, 0., 0.], [0.5, 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 6:
        symbol_set = np.array(['e', 'f', 'g', 'h', 'i', 'j'])
        bool_set = map(f, [[0., 0., pos[2]], [0.5, 0., pos[2]], [pos[0], 0., 0.], [pos[0], 0., 0.5], [pos[0], 2 * pos[0], 0.], [pos[0], 2 * pos[0], 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'k'

def sp_181(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 3 and multiplicity != 6 and multiplicity != 12:
        raise ValueError("It is not a P6_422 system!")
    elif multiplicity == 3:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5], [0.5, 0., 0.], [0.5, 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 6:
        symbol_set = np.array(['e', 'f', 'g', 'h', 'i', 'j'])
        bool_set = map(f, [[0., 0., pos[2]], [0.5, 0., pos[2]], [pos[0], 0., 0.], [pos[0], 0., 0.5], [pos[0], 2 * pos[0], 0.], [pos[0], 2 * pos[0], 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'k'

def sp_182(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 6 and multiplicity != 12:
        raise ValueError("It is not a P6_322 system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.25], [1./3, 2./3, 0.25], [1./3, 2./3, 0.75]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['e', 'f'])
        bool_set = map(f, [[0., 0., pos[2]], [1./3, 2./3, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 6:
        symbol_set = np.array(['g', 'h'])
        bool_set = map(f, [[pos[0], 0., 0.], [pos[0], 2 * pos[0], 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'i'

def sp_183(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 1 and multiplicity != 2 and multiplicity != 3 and multiplicity != 6 and multiplicity != 12:
        raise ValueError("It is not a P6mm system!")
    elif multiplicity == 1:
        return 'a'
    elif multiplicity == 2:
        return 'b'
    elif multiplicity == 3:
        return 'c'
    elif multiplicity == 6:
        symbol_set = np.array(['d', 'e'])
        bool_set = map(f, [[pos[0], 0., pos[2]], [pos[0], -pos[0], pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'f'

def sp_184(multiplicity, pos):
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 6 and multiplicity != 12:
        raise ValueError("It is not a P6cc system!")
    elif multiplicity == 2:
        return 'a'
    elif multiplicity == 4:
        return 'b'
    elif multiplicity == 6:
        return 'c'
    else:
        return 'd'

def sp_185(multiplicity, pos):
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 6 and multiplicity != 12:
        raise ValueError("It is not a P6_3cm system!")
    elif multiplicity == 2:
        return 'a'
    elif multiplicity == 4:
        return 'b'
    elif multiplicity == 6:
        return 'c'
    else:
        return 'd'

def sp_186(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 6 and multiplicity != 12:
        raise ValueError("It is not a P6_3mc system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., pos[2]], [1./3, 2./3, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 6:
        return 'c'
    else:
        return 'd'

def sp_187(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 1 and multiplicity != 2 and multiplicity != 3 and multiplicity != 6 and multiplicity != 12:
        raise ValueError("It is not a P-6m2 system!")
    elif multiplicity == 1:
        symbol_set = np.array(['a', 'b', 'c', 'd', 'e', 'f'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5], [1./3, 2./3, 0.], [1./3, 2./3, 0.5], [2./3, 1./3, 0.], [2./3, 1./3, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 2:
        symbol_set = np.array(['g', 'h', 'i'])
        bool_set = map(f, [[0., 0., pos[2]], [1./3, 2./3, pos[2]], [2./3, 1./3, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 3:
        symbol_set = np.array(['j', 'k'])
        bool_set = map(f, [[pos[0], -pos[0], 0.], [pos[0], -pos[0], 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 6:
        symbol_set = np.array(['l', 'm', 'n'])
        bool_set = map(f, [[pos[0], pos[1], 0.], [pos[0], pos[1], 0.5], [pos[0], -pos[0], pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'o'

def sp_188(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 6 and multiplicity != 12:
        raise ValueError("It is not a P-6c2 system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c', 'd', 'e', 'f'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.25], [1./3, 2./3, 0.], [1./3, 2./3, 0.25], [2./3, 1./3, 0.], [2./3, 1./3, 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['g', 'h', 'i'])
        bool_set = map(f, [[0., 0., pos[2]], [1./3, 2./3, pos[2]], [2./3, 1./3, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 6:
        symbol_set = np.array(['j', 'k'])
        bool_set = map(f, [[pos[0], -pos[0], 0.], [pos[0], pos[1], 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'l'

def sp_189(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 1 and multiplicity != 2 and multiplicity != 3 and multiplicity != 4 and multiplicity != 6 and multiplicity != 12:
        raise ValueError("It is not a P-62m system!")
    elif multiplicity == 1:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 2:
        symbol_set = np.array(['c', 'd', 'e'])
        bool_set = map(f, [[1./3, 2./3, 0.], [1./3, 2./3, 0.5], [0., 0., pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 3:
        symbol_set = np.array(['f', 'g'])
        bool_set = map(f, [[pos[0], 0., 0.], [pos[0], 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        return 'h'
    elif multiplicity == 6:
        symbol_set = np.array(['i', 'j', 'k'])
        bool_set = map(f, [[pos[0], 0., pos[2]], [pos[0], pos[1], 0.], [pos[0], pos[1], 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'l'

def sp_190(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 6 and multiplicity != 12:
        raise ValueError("It is not a P-62c system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.25], [1./3, 2./3, 0.25], [2./3, 1./3, 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['e', 'f'])
        bool_set = map(f, [[0., 0., pos[2]], [1./3, 2./3, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 6:
        symbol_set = np.array(['g', 'h'])
        bool_set = map(f, [[pos[0], 0., 0.], [pos[0], pos[1], 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'i'

def sp_191(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 1 and multiplicity != 2 and multiplicity != 3 and multiplicity != 4 and multiplicity != 6 and multiplicity != 12 and multiplicity != 24:
        raise ValueError("It is not a P6/mmm system!")
    elif multiplicity == 1:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 2:
        symbol_set = np.array(['c', 'd', 'e'])
        bool_set = map(f, [[1./3, 2./3, 0.], [1./3, 2./3, 0.5], [0., 0., pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 3:
        symbol_set = np.array(['f', 'g'])
        bool_set = map(f, [[0.5, 0., 0.], [0.5, 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        return 'h'
    elif multiplicity == 6:
        symbol_set = np.array(['i', 'j', 'k', 'l', 'm'])
        bool_set = map(f, [[0.5, 0., pos[2]], [pos[0], 0., 0.], [pos[0], 0., 0.5], [pos[0], 2 * pos[0], 0.], [pos[0], 2 * pos[0], 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 12:
        symbol_set = np.array(['n', 'o', 'p', 'q'])
        bool_set = map(f, [[pos[0], 0., pos[2]], [pos[0], 2 * pos[0], pos[2]], [pos[0], pos[1], 0.], [pos[0], pos[1], 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'r'

def sp_192(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 6 and multiplicity != 8 and multiplicity != 12 and multiplicity != 24:
        raise ValueError("It is not a P6/mcc system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.25], [0., 0., 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['c', 'd', 'e'])
        bool_set = map(f, [[1./3, 2./3, 0.25], [1./3, 2./3, 0.], [0., 0., pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 6:
        symbol_set = np.array(['f', 'g'])
        bool_set = map(f, [[0.5, 0., 0.25], [0.5, 0., 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        return 'h'
    elif multiplicity == 12:
        symbol_set = np.array(['i', 'j', 'k', 'l'])
        bool_set = map(f, [[0.5, 0., pos[2]], [pos[0], 0., 0.25], [pos[0], 2 * pos[0], 0.25], [pos[0], pos[1], 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'm'

def sp_193(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 6 and multiplicity != 8 and multiplicity != 12 and multiplicity != 24:
        raise ValueError("It is not a P6_3/mcm system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.25], [0., 0., 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['c', 'd', 'e'])
        bool_set = map(f, [[1./3, 2./3, 0.25], [1./3, 2./3, 0.], [0., 0., pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 6:
        symbol_set = np.array(['f', 'g'])
        bool_set = map(f, [[0.5, 0., 0.], [pos[0], 0., 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        return 'h'
    elif multiplicity == 12:
        symbol_set = np.array(['i', 'j', 'k'])
        bool_set = map(f, [[pos[0], 2 * pos[0], 0.], [pos[0], pos[1], 0.25], [pos[0], 0., pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'l'

def sp_194(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 6 and multiplicity != 12 and multiplicity != 24:
        raise ValueError("It is not a P6_3/mmc system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0., 0., 0.], [0., 0., 0.25], [1./3, 2./3, 0.25], [1./3, 2./3, 0.75]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['e', 'f'])
        bool_set = map(f, [[0., 0., pos[2]], [1./3, 2./3, pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 6:
        symbol_set = np.array(['g', 'h'])
        bool_set = map(f, [[0.5, 0., 0.], [pos[0], 2 * pos[0], 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 12:
        symbol_set = np.array(['i', 'j', 'k'])
        bool_set = map(f, [[pos[0], 0., 0.], [pos[0], pos[1], 0.25], [pos[0], 2 * pos[0], pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'l'

def sp_195(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 1 and multiplicity != 3 and multiplicity != 4 and multiplicity != 6 and multiplicity != 12:
        raise ValueError("It is not a P23 system!")
    elif multiplicity == 1:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0.5, 0.5, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 3:
        symbol_set = np.array(['c', 'd'])
        bool_set = map(f, [[0., 0.5, 0.5], [0.5, 0., 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        return 'e'
    elif multiplicity == 6:
        symbol_set = np.array(['f', 'g', 'h', 'i'])
        bool_set = map(f, [[pos[0], 0., 0.], [pos[0], 0., 0.5], [pos[0], 0.5, 0.], [pos[0], 0.5, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'j'

def sp_196(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 16 and multiplicity != 24 and multiplicity != 48:
        raise ValueError("It is not a F23 system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0., 0., 0.], [0.5, 0.5, 0.5], [0.25, 0.25, 0.25], [0.75, 0.75, 0.75]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 16:
        return 'e'
    elif multiplicity == 24:
        symbol_set = np.array(['f', 'g'])
        bool_set = map(f, [[pos[0], 0., 0.], [pos[0], 0.25, 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'h'

def sp_197(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 6 and multiplicity != 8 and multiplicity != 12 and multiplicity != 24:
        raise ValueError("It is not a I23 system!")
    elif multiplicity == 2:
        return 'a'
    elif multiplicity == 6:
        return 'b'
    elif multiplicity == 8:
        return 'c'
    elif multiplicity == 12:
        symbol_set = np.array(['d', 'e'])
        bool_set = map(f, [[pos[0], 0., 0.], [pos[0], 0.5, 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'f'

def sp_198(multiplicity, pos):
    if multiplicity != 4 and multiplicity != 12:
        raise ValueError("It is not a P2_13 system!")
    elif multiplicity == 4:
        return 'a'
    else:
        return 'b'

def sp_199(multiplicity, pos):
    if multiplicity != 8 and multiplicity != 12 and multiplicity != 24:
        raise ValueError("It is not a I2_13 system!")
    elif multiplicity == 8:
        return 'a'
    elif multiplicity == 12:
        return 'b'
    else:
        return 'c'

def sp_200(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 1 and multiplicity != 3 and multiplicity != 6 and multiplicity != 8 and multiplicity != 12 and multiplicity != 24:
        raise ValueError("It is not a Pm-3 system!")
    elif multiplicity == 1:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0.5, 0.5, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 3:
        symbol_set = np.array(['c', 'd'])
        bool_set = map(f, [[0., 0.5, 0.5], [0.5, 0., 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 6:
        symbol_set = np.array(['e', 'f', 'g', 'h'])
        bool_set = map(f, [[pos[0], 0., 0.], [pos[0], 0., 0.5], [pos[0], 0.5, 0.], [pos[0], 0.5, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        return 'i'
    elif multiplicity == 12:
        symbol_set = np.array(['j', 'k'])
        bool_set = map(f, [[0., pos[1], pos[2]], [0.5, pos[1], pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'l'

def sp_201(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 6 and multiplicity != 8 and multiplicity != 12 and multiplicity != 24:
        raise ValueError("It is not a Pn-3 system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a'])
        bool_set = map(f, [[0., 0., 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['b', 'c'])
        bool_set = map(f, [[0.25, 0.25, 0.25], [0.75, 0.75, 0.75]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 6:
        symbol_set = np.array(['d'])
        bool_set = map(f, [[0., 0.5, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['e'])
        bool_set = map(f, [[pos[0], pos[0], pos[0]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 12:
        symbol_set = np.array(['f', 'g'])
        bool_set = map(f, [[pos[0], 0., 0.], [pos[0], 0.5, 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'h'

def sp_201_s(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 6 and multiplicity != 8 and multiplicity != 12 and multiplicity != 24:
        raise ValueError("It is not a Pn-3 system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a'])
        bool_set = map(f, [[0.25, 0.25, 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['b', 'c'])
        bool_set = map(f, [[0., 0., 0.], [0.5, 0.5, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 6:
        symbol_set = np.array(['d'])
        bool_set = map(f, [[0.25, 0.75, 0.75]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['e'])
        bool_set = map(f, [[pos[0], pos[0], pos[0]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 12:
        symbol_set = np.array(['f', 'g'])
        bool_set = map(f, [[pos[0], 0.25, 0.25], [pos[0], 0.75, 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'h'

def sp_202(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8 and multiplicity != 24 and multiplicity != 32 and multiplicity != 48 and multiplicity != 96:
        raise ValueError("It is not a Fm-3 system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0.5, 0.5, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        return 'c'
    elif multiplicity == 24:
        symbol_set = np.array(['d', 'e'])
        bool_set = map(f, [[0., 0.25, 0.25], [pos[0], 0., 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 32:
        return 'f'
    elif multiplicity == 48:
        symbol_set = np.array(['g', 'h'])
        bool_set = map(f, [[pos[0], 0.25, 0.25], [0., pos[1], pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'i'

def sp_203(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 8 and multiplicity != 16 and multiplicity != 32 and multiplicity != 48 and multiplicity != 96:
        raise ValueError("It is not a Fd-3 system!")
    elif multiplicity == 8:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0.5, 0.5, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 16:
        symbol_set = np.array(['c', 'd'])
        bool_set = map(f, [[0.125, 0.125, 0.125], [0.625, 0.625, 0.625]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 32:
        symbol_set = np.array(['e'])
        bool_set = map(f, [[pos[0], pos[0], pos[0]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 48:
        symbol_set = np.array(['f'])
        bool_set = map(f, [[pos[0], 0., 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'g'

def sp_203_s(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 8 and multiplicity != 16 and multiplicity != 32 and multiplicity != 48 and multiplicity != 96:
        raise ValueError("It is not a Fd-3 system!")
    elif multiplicity == 8:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0.125, 0.125, 0.125], [0.625, 0.625, 0.625]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 16:
        symbol_set = np.array(['c', 'd'])
        bool_set = map(f, [[0., 0., 0.], [0.5, 0.5, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 32:
        symbol_set = np.array(['e'])
        bool_set = map(f, [[pos[0], pos[0], pos[0]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 48:
        symbol_set = np.array(['f'])
        bool_set = map(f, [[pos[0], 0.125, 0.125]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'g'

def sp_204(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 6 and multiplicity != 8 and multiplicity != 12 and multiplicity != 16 and multiplicity != 24 and multiplicity != 48:
        raise ValueError("It is not a Im-3 system!")
    elif multiplicity == 2:
        return 'a'
    elif multiplicity == 6:
        return 'b'
    elif multiplicity == 8:
        return 'c'
    elif multiplicity == 12:
        symbol_set = np.array(['d', 'e'])
        bool_set = map(f, [[pos[0], 0., 0.], [pos[0], 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 16:
        return 'f'
    elif multiplicity == 24:
        return 'g'
    else:
        return 'h'

def sp_205(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8 and multiplicity != 24:
        raise ValueError("It is not a Pa-3 system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0.5, 0.5, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        return 'c'
    else:
        return 'd'

def sp_206(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 8 and multiplicity != 16 and multiplicity != 24 and multiplicity != 48:
        raise ValueError("It is not a Ia-3 system!")
    elif multiplicity == 8:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0.25, 0.25, 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 16:
        return 'c'
    elif multiplicity == 24:
        return 'd'
    else:
        return 'e'

def sp_207(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 1 and multiplicity != 3 and multiplicity != 6 and multiplicity != 8 and multiplicity != 12 and multiplicity != 24:
        raise ValueError("It is not a P432 system!")
    elif multiplicity == 1:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0.5, 0.5, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 3:
        symbol_set = np.array(['c', 'd'])
        bool_set = map(f, [[0., 0.5, 0.5], [0.5, 0., 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 6:
        symbol_set = np.array(['e', 'f'])
        bool_set = map(f, [[pos[0], 0., 0.], [pos[0], 0.5, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        return 'g'
    elif multiplicity == 12:
        symbol_set = np.array(['h', 'i', 'j'])
        bool_set = map(f, [[pos[0], 0.5, 0.], [0., pos[1], pos[1]], [0.5, pos[1], pos[1]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'k'

def sp_208(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 6 and multiplicity != 8 and multiplicity != 12 and multiplicity != 24:
        raise ValueError("It is not a P4_232 system!")
    elif multiplicity == 2:
        return 'a'
    elif multiplicity == 4:
        symbol_set = np.array(['b', 'c'])
        bool_set = map(f, [[0.25, 0.25, 0.25], [0.75, 0.75, 0.75]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 6:
        symbol_set = np.array(['d', 'e', 'f'])
        bool_set = map(f, [[0., 0.5, 0.5], [0.25, 0., 0.5], [0.25, 0.5, 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        return 'g'
    elif multiplicity == 12:
        symbol_set = np.array(['h', 'i', 'j', 'k', 'l'])
        bool_set = map(f, [[pos[0], 0., 0.], [pos[0], 0., 0.5], [pos[0], 0.5, 0.], [0.25, pos[1], -pos[1]+0.5], [0.25, pos[1], pos[1]+0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'm'

def sp_209(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8 and multiplicity != 24 and multiplicity != 32 and multiplicity != 48 and multiplicity != 96:
        raise ValueError("It is not a F432 system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0.5, 0.5, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        return 'c'
    elif multiplicity == 24:
        symbol_set = np.array(['d', 'e'])
        bool_set = map(f, [[0., 0.25, 0.25], [pos[0], 0., 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 32:
        return 'f'
    elif multiplicity == 48:
        symbol_set = np.array(['g', 'h', 'i'])
        bool_set = map(f, [[0., pos[1], pos[1]], [0.5, pos[1], pos[1]], [pos[0], 0.25, 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'j'

def sp_210(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 8 and multiplicity != 16 and multiplicity != 32 and multiplicity != 48 and multiplicity != 96:
        raise ValueError("It is not a F4_132 system!")
    elif multiplicity == 8:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0.5, 0.5, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 16:
        symbol_set = np.array(['c', 'd'])
        bool_set = map(f, [[0.125, 0.125, 0.125], [0.625, 0.625, 0.625]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 32:
        return 'e'
    elif multiplicity == 48:
        symbol_set = np.array(['f', 'g'])
        bool_set = map(f, [[pos[0], 0., 0.], [0.125, pos[1], -pos[1]+0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'h'

def sp_211(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 6 and multiplicity != 8 and multiplicity != 12 and multiplicity != 16 and multiplicity != 24 and multiplicity != 48:
        raise ValueError("It is not a I432 system!")
    elif multiplicity == 2:
        return 'a'
    elif multiplicity == 6:
        return 'b'
    elif multiplicity == 8:
        return 'c'
    elif multiplicity == 12:
        symbol_set = np.array(['d', 'e'])
        bool_set = map(f, [[0.25, 0.5, 0.], [pos[0], 0., 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 16:
        return 'f'
    elif multiplicity == 24:
        symbol_set = np.array(['g', 'h', 'i'])
        bool_set = map(f, [[pos[0], 0.5, 0.], [0., pos[1], pos[1]], [0.25, pos[1], -pos[1]+0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'j'

def sp_212(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8 and multiplicity != 12 and multiplicity != 24:
        raise ValueError("It is not a P4_332 system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0.125, 0.125, 0.125], [0.625, 0.625, 0.625]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        return 'c'
    elif multiplicity == 12:
        return 'd'
    else:
        return 'e'

def sp_213(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8 and multiplicity != 12 and multiplicity != 24:
        raise ValueError("It is not a P4_132 system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0.375, 0.375, 0.375], [0.875, 0.875, 0.875]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        return 'c'
    elif multiplicity == 12:
        return 'd'
    else:
        return 'e'

def sp_214(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 8 and multiplicity != 12 and multiplicity != 16 and multiplicity != 24 and multiplicity != 48:
        raise ValueError("It is not a I4_132 system!")
    elif multiplicity == 8:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0.125, 0.125, 0.125], [0.875, 0.875, 0.875]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 12:
        symbol_set = np.array(['c', 'd'])
        bool_set = map(f, [[0.125, 0., 0.25], [0.625, 0., 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 16:
        return 'e'
    elif multiplicity == 24:
        symbol_set = np.array(['f', 'g', 'h'])
        bool_set = map(f, [[pos[0], 0., 0.25], [0.125, pos[1], pos[1]+0.25], [0.125, pos[1], -pos[1]+0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'i'

def sp_215(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 1 and multiplicity != 3 and multiplicity != 4 and multiplicity != 6 and multiplicity != 12 and multiplicity != 24:
        raise ValueError("It is not a P-43m system!")
    elif multiplicity == 1:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0.5, 0.5, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 3:
        symbol_set = np.array(['c', 'd'])
        bool_set = map(f, [[0., 0.5, 0.5], [0.5, 0., 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        return 'e'
    elif multiplicity == 6:
        symbol_set = np.array(['f', 'g'])
        bool_set = map(f, [[pos[0], 0., 0.], [pos[0], 0.5, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 12:
        symbol_set = np.array(['h', 'i'])
        bool_set = map(f, [[pos[0], 0.5, 0.], [pos[0], pos[0], pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'j'

def sp_216(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 16 and multiplicity != 24 and multiplicity != 48 and multiplicity != 96:
        raise ValueError("It is not a F-43m system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b', 'c', 'd'])
        bool_set = map(f, [[0., 0., 0.], [0.5, 0.5, 0.5], [0.25, 0.25, 0.25], [0.75, 0.75, 0.75]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 16:
        return 'e'
    elif multiplicity == 24:
        symbol_set = np.array(['f', 'g'])
        bool_set = map(f, [[pos[0], 0., 0.], [pos[0], 0.25, 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 48:
        return 'h'
    else:
        return 'i'

def sp_217(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 6 and multiplicity != 8 and multiplicity != 12 and multiplicity != 24 and multiplicity != 48:
        raise ValueError("It is not a I-43m system!")
    elif multiplicity == 2:
        return 'a'
    elif multiplicity == 6:
        return 'b'
    elif multiplicity == 8:
        return 'c'
    elif multiplicity == 12:
        symbol_set = np.array(['d', 'e'])
        bool_set = map(f, [[0.25, 0.5, 0.], [pos[0], 0., 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 24:
        symbol_set = np.array(['f', 'g'])
        bool_set = map(f, [[pos[0], 0.5, 0.], [pos[0], pos[0], pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'h'

def sp_218(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 6 and multiplicity != 8 and multiplicity != 12 and multiplicity != 24:
        raise ValueError("It is not a P-43n system!")
    elif multiplicity == 2:
        return 'a'
    elif multiplicity == 6:
        symbol_set = np.array(['b', 'c', 'd'])
        bool_set = map(f, [[0., 0.5, 0.5], [0.25, 0.5, 0.], [0.25, 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        return 'e'
    elif multiplicity == 12:
        symbol_set = np.array(['f', 'g', 'h'])
        bool_set = map(f, [[pos[0], 0., 0.], [pos[0], 0.5, 0.], [pos[0], 0., 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'i'

def sp_219(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 8 and multiplicity != 24 and multiplicity != 32 and multiplicity != 48 and multiplicity != 96:
        raise ValueError("It is not a F-43c system!")
    elif multiplicity == 8:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0.25, 0.25, 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 24:
        symbol_set = np.array(['c', 'd'])
        bool_set = map(f, [[0., 0.25, 0.25], [0.25, 0., 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 32:
        return 'e'
    elif multiplicity == 48:
        symbol_set = np.array(['f', 'g'])
        bool_set = map(f, [[pos[0], 0., 0.], [pos[0], 0.25, 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'h'

def sp_220(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 12 and multiplicity != 16 and multiplicity != 24 and multiplicity != 48:
        raise ValueError("It is not a I-43d system!")
    elif multiplicity == 12:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0.375, 0., 0.25], [0.875, 0., 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 16:
        return 'c'
    elif multiplicity == 24:
        return 'd'
    else:
        return 'e'

def sp_221(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 1 and multiplicity != 3 and multiplicity != 6 and multiplicity != 8 and multiplicity != 12 and multiplicity != 24 and multiplicity != 48:
        raise ValueError("It is not a Pm-3m system!")
    elif multiplicity == 1:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0.5, 0.5, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 3:
        symbol_set = np.array(['c', 'd'])
        bool_set = map(f, [[0., 0.5, 0.5], [0.5, 0., 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 6:
        symbol_set = np.array(['e', 'f'])
        bool_set = map(f, [[pos[0], 0., 0.], [pos[0], 0.5, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        return 'g'
    elif multiplicity == 12:
        symbol_set = np.array(['h', 'i', 'j'])
        bool_set = map(f, [[pos[0], 0.5, 0.], [0., pos[1], pos[1]], [0.5, pos[1], pos[1]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 24:
        symbol_set = np.array(['k', 'l', 'm'])
        bool_set = map(f, [[0., pos[1], pos[2]], [0.5, pos[1], pos[2]], [pos[0], pos[0], pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'n'

def sp_222(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 6 and multiplicity != 8 and multiplicity != 12 and multiplicity != 16 and multiplicity != 24 and multiplicity != 48:
        raise ValueError("It is not a Pn-3n system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a'])
        bool_set = map(f, [[0., 0., 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 6:
        symbol_set = np.array(['b'])
        bool_set = map(f, [[0., 0.5, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['c'])
        bool_set = map(f, [[0.25, 0.25, 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 12:
        symbol_set = np.array(['d', 'e'])
        bool_set = map(f, [[0.25, 0., 0.5], [pos[0], 0., 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 16:
        symbol_set = np.array(['f'])
        bool_set = map(f, [[pos[0], pos[0], pos[0]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 24:
        symbol_set = np.array(['g', 'h'])
        bool_set = map(f, [[pos[0], 0., 0.5], [0., pos[1], pos[1]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'i'

def sp_222_s(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 6 and multiplicity != 8 and multiplicity != 12 and multiplicity != 16 and multiplicity != 24 and multiplicity != 48:
        raise ValueError("It is not a Pn-3n system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a'])
        bool_set = map(f, [[0.25, 0.25, 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 6:
        symbol_set = np.array(['b'])
        bool_set = map(f, [[0.75, 0.25, 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['c'])
        bool_set = map(f, [[0., 0., 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 12:
        symbol_set = np.array(['d', 'e'])
        bool_set = map(f, [[0., 0.75, 0.25], [pos[0], 0.25, 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 16:
        symbol_set = np.array(['f'])
        bool_set = map(f, [[pos[0], pos[0], pos[0]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 24:
        symbol_set = np.array(['g', 'h'])
        bool_set = map(f, [[pos[0], 0.75, 0.25], [0.25, pos[1], pos[1]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'i'

def sp_223(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 6 and multiplicity != 8 and multiplicity != 12 and multiplicity != 16 and multiplicity != 24 and multiplicity != 48:
        raise ValueError("It is not a Pm-3n system!")
    elif multiplicity == 2:
        return 'a'
    elif multiplicity == 6:
        symbol_set = np.array(['b', 'c', 'd'])
        bool_set = map(f, [[0., 0.5, 0.5], [0.25, 0., 0.5], [0.25, 0.5, 0]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        return 'e'
    elif multiplicity == 12:
        symbol_set = np.array(['f', 'g', 'h'])
        bool_set = map(f, [[pos[0], 0., 0.], [pos[0], 0., 0.5], [pos[0], 0.5, 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 16:
        return 'i'
    elif multiplicity == 24:
        symbol_set = np.array(['j', 'k'])
        bool_set = map(f, [[0.25, pos[1], pos[1]+0.5], [0., pos[1], pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'l'

def sp_224(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 6 and multiplicity != 8 and multiplicity != 12 and multiplicity != 24 and multiplicity != 48:
        raise ValueError("It is not a Pn-3m system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a'])
        bool_set = map(f, [[0., 0., 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['b', 'c'])
        bool_set = map(f, [[0.25, 0.25, 0.25], [0.75, 0.75, 0.75]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 6:
        symbol_set = np.array(['d'])
        bool_set = map(f, [[0., 0.5, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['e'])
        bool_set = map(f, [[pos[0], pos[0], pos[0]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 12:
        symbol_set = np.array(['f', 'g'])
        bool_set = map(f, [[0.25, 0., 0.5], [pos[0], 0., 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 24:
        symbol_set = np.array(['h', 'i', 'j', 'k'])
        bool_set = map(f, [[pos[0], 0., 0.5], [0.25, pos[1], -pos[1]+0.5], [0.25, pos[1], pos[1]+0.5], [pos[0], pos[0], pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'l'

def sp_224_s(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 4 and multiplicity != 6 and multiplicity != 8 and multiplicity != 12 and multiplicity != 24 and multiplicity != 48:
        raise ValueError("It is not a Pn-3m system!")
    elif multiplicity == 2:
        symbol_set = np.array(['a'])
        bool_set = map(f, [[0.25, 0.25, 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 4:
        symbol_set = np.array(['b', 'c'])
        bool_set = map(f, [[0., 0., 0.], [0.5, 0.5, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 6:
        symbol_set = np.array(['d'])
        bool_set = map(f, [[0.25, 0.75, 0.75]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        symbol_set = np.array(['e'])
        bool_set = map(f, [[pos[0], pos[0], pos[0]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 12:
        symbol_set = np.array(['f', 'g'])
        bool_set = map(f, [[0.5, 0.25, 0.75], [pos[0], 0.25, 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 24:
        symbol_set = np.array(['h', 'i', 'j', 'k'])
        bool_set = map(f, [[pos[0], 0.25, 0.75], [0.5, pos[1], pos[1]+0.5], [0.5, pos[1], -pos[1]], [pos[0], pos[0], pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'l'

def sp_225(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 4 and multiplicity != 8 and multiplicity != 24 and multiplicity != 32 and multiplicity != 48 and multiplicity != 96 and multiplicity != 192:
        raise ValueError("It is not a Fm-3m system!")
    elif multiplicity == 4:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0.5, 0.5, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 8:
        return 'c'
    elif multiplicity == 24:
        symbol_set = np.array(['d', 'e'])
        bool_set = map(f, [[0., 0.25, 0.25], [pos[0], 0., 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 32:
        return 'f'
    elif multiplicity == 48:
        symbol_set = np.array(['g', 'h', 'i'])
        bool_set = map(f, [[pos[0], 0.25, 0.25], [0., pos[1], pos[1]], [0.5, pos[1], pos[1]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 96:
        symbol_set = np.array(['j', 'k'])
        bool_set = map(f, [[0., pos[1], pos[2]], [pos[0], pos[0], pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'l'

def sp_226(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 8 and multiplicity != 24 and multiplicity != 48 and multiplicity != 64 and multiplicity != 96 and multiplicity != 192:
        raise ValueError("It is not a Fm-3c system!")
    elif multiplicity == 8:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0.25, 0.25, 0.25], [0., 0., 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 24:
        symbol_set = np.array(['c', 'd'])
        bool_set = map(f, [[0.25, 0., 0.], [0., 0.25, 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 48:
        symbol_set = np.array(['e', 'f'])
        bool_set = map(f, [[pos[0], 0., 0.], [pos[0], 0.25, 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 64:
        return 'g'
    elif multiplicity == 96:
        symbol_set = np.array(['h', 'i'])
        bool_set = map(f, [[0.25, pos[1], pos[1]], [0., pos[1], pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'j'

def sp_227(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 8 and multiplicity != 16 and multiplicity != 32 and multiplicity != 48 and multiplicity != 96 and multiplicity != 192:
        raise ValueError("It is not a Fd-3m system!")
    elif multiplicity == 8:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0.5, 0.5, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 16:
        symbol_set = np.array(['c', 'd'])
        bool_set = map(f, [[0.125, 0.125, 0.125], [0.625, 0.625, 0.625]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 32:
        symbol_set = np.array(['e'])
        bool_set = map(f, [[pos[0], pos[0], pos[0]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 48:
        symbol_set = np.array(['f'])
        bool_set = map(f, [[pos[0], 0., 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 96:
        symbol_set = np.array(['g', 'h'])
        bool_set = map(f, [[pos[0], pos[0], pos[2]], [0.125, pos[1], -pos[1]+0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'i'

def sp_227_s(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 8 and multiplicity != 16 and multiplicity != 32 and multiplicity != 48 and multiplicity != 96 and multiplicity != 192:
        raise ValueError("It is not a Fd-3m system!")
    elif multiplicity == 8:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0.125, 0.125, 0.125], [0.375, 0.375, 0.375]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 16:
        symbol_set = np.array(['c', 'd'])
        bool_set = map(f, [[0., 0., 0.], [0.5, 0.5, 0.5]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 32:
        symbol_set = np.array(['e'])
        bool_set = map(f, [[pos[0], pos[0], pos[0]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 48:
        symbol_set = np.array(['f'])
        bool_set = map(f, [[pos[0], 0.125, 0.125]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 96:
        symbol_set = np.array(['g', 'h'])
        bool_set = map(f, [[pos[0], pos[0], pos[2]], [0., pos[1], -pos[1]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'i'

def sp_228(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 16 and multiplicity != 32 and multiplicity != 48 and multiplicity != 64 and multiplicity != 96 and multiplicity != 192:
        raise ValueError("It is not a Fd-3c system!")
    elif multiplicity == 16:
        symbol_set = np.array(['a'])
        bool_set = map(f, [[0., 0., 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 32:
        symbol_set = np.array(['b', 'c'])
        bool_set = map(f, [[0.125, 0.125, 0.125], [0.375, 0.375, 0.375]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 48:
        symbol_set = np.array(['d'])
        bool_set = map(f, [[0.25, 0., 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 64:
        symbol_set = np.array(['e'])
        bool_set = map(f, [[pos[0], pos[0], pos[0]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 96:
        symbol_set = np.array(['f', 'g'])
        bool_set = map(f, [[pos[0], 0., 0.], [0.125, pos[1], -pos[1]+0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'h'

def sp_228_s(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 16 and multiplicity != 32 and multiplicity != 48 and multiplicity != 64 and multiplicity != 96 and multiplicity != 192:
        raise ValueError("It is not a Fd-3c system!")
    elif multiplicity == 16:
        symbol_set = np.array(['a'])
        bool_set = map(f, [[0.125, 0.125, 0.125]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 32:
        symbol_set = np.array(['b', 'c'])
        bool_set = map(f, [[0.25, 0.25, 0.25], [0., 0., 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 48:
        symbol_set = np.array(['d'])
        bool_set = map(f, [[0.875, 0.125, 0.125]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 64:
        symbol_set = np.array(['e'])
        bool_set = map(f, [[pos[0], pos[0], pos[0]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 96:
        symbol_set = np.array(['f', 'g'])
        bool_set = map(f, [[pos[0], 0.125, 0.125], [0.25, pos[1], -pos[1]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'h'

def sp_229(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 2 and multiplicity != 6 and multiplicity != 8 and multiplicity != 12 and multiplicity != 16 and multiplicity != 24 and multiplicity != 48 and multiplicity != 96:
        raise ValueError("It is not a Im-3m system!")
    elif multiplicity == 2:
        return 'a'
    elif multiplicity == 6:
        return 'b'
    elif multiplicity == 8:
        return 'c'
    elif multiplicity == 12:
        symbol_set = np.array(['d', 'e'])
        bool_set = map(f, [[0.25, 0., 0.5], [pos[0], 0., 0.]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 16:
        return 'f'
    elif multiplicity == 24:
        symbol_set = np.array(['g', 'h'])
        bool_set = map(f, [[pos[0], 0., 0.5], [0., pos[1], pos[1]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 48:
        symbol_set = np.array(['i', 'j', 'k'])
        bool_set = map(f, [[0.25, pos[1], -pos[1]+0.5], [0., pos[1], pos[2]], [pos[0], pos[0], pos[2]]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'l'

def sp_230(multiplicity, pos):
    f = lambda x: True if np.all(abs(x - pos) < 1e-2) else False
    if multiplicity != 16 and multiplicity != 24 and multiplicity != 32 and multiplicity != 48 and multiplicity != 96:
        raise ValueError("It is not a Ia-3d system!")
    elif multiplicity == 16:
        symbol_set = np.array(['a', 'b'])
        bool_set = map(f, [[0., 0., 0.], [0.125, 0.125, 0.125]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 24:
        symbol_set = np.array(['c', 'd'])
        bool_set = map(f, [[0.125, 0., 0.25], [0.375, 0., 0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    elif multiplicity == 32:
        return 'e'
    elif multiplicity == 48:
        symbol_set = np.array(['f', 'g'])
        bool_set = map(f, [[pos[0], 0., 0.25], [0.125, pos[1], -pos[1]+0.25]])
        bool_set = np.array(bool_set)
        if np.any(bool_set):
            return symbol_set[bool_set][0]
        else:
            return False
    else:
        return 'h'