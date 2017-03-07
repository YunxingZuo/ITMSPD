# coding: utf-8

import numpy as np
from itertools import permutations
from Symmetry_Operation import *

Pnma = np.array([[[1,  0,  0,  0],
                  [0,  1,  0,  0],
                  [0,  0,  1,  0],
                  [0,  0,  0,  1]],

                 [[-1, 0,  0,  0],
                  [0, -1,  0,  0],
                  [0,  0, -1,  0],
                  [0,  0,  0,  1]],

                 [[-1, 0, 0, 0.5],
                  [ 0, 1, 0, 0.5],
                  [ 0, 0, 1, 0.5],
                  [ 0, 0, 0,   1]],

                 [[1,  0, 0, 0.5],
                  [0, -1, 0, 0.5],
                  [0, 0, -1, 0.5],
                  [0,  0, 0,   1]],

                 [[1,  0, 0, 0.5],
                  [0,  1, 0,   0],
                  [0, 0, -1, 0.5],
                  [0,  0, 0,   1]],

                 [[-1, 0, 0, 0.5],
                  [0, -1, 0,   0],
                  [0,  0, 1, 0.5],
                  [0,  0, 0,   1]],

                 [[1,  0, 0,   0],
                  [0, -1, 0, 0.5],
                  [0,  0, 1,   0],
                  [0,  0, 0,   1]],

                 [[-1, 0, 0,   0],
                  [0,  1, 0, 0.5],
                  [0,  0, -1,  0],
                  [0,  0, 0,   1]]])

Pnam = np.array([[[1,  0,  0,  0],
                  [0,  1,  0,  0],
                  [0,  0,  1,  0],
                  [0,  0,  0,  1]],

                 [[-1, 0,  0,  0],
                  [0, -1,  0,  0],
                  [0,  0, -1,  0],
                  [0,  0,  0,  1]],

                 [[-1, 0, 0, 0.5],
                  [ 0, 1, 0, 0.5],
                  [ 0, 0, 1, 0.5],
                  [ 0, 0, 0,   1]],

                 [[1,  0, 0, 0.5],
                  [0, -1, 0, 0.5],
                  [0, 0, -1, 0.5],
                  [0,  0, 0,   1]],

                 [[1,  0, 0, 0.5],
                  [0, -1, 0, 0.5],
                  [0,  0, 1,   0],
                  [0,  0, 0,   1]],

                 [[-1, 0, 0, 0.5],
                  [0,  1, 0, 0.5],
                  [0, 0, -1,   0],
                  [0,  0, 0,   1]],

                 [[1,  0, 0,   0],
                  [0,  1, 0,   0],
                  [0, 0, -1, 0.5],
                  [0,  0, 0,   1]],

                 [[-1, 0, 0,   0],
                  [0, -1, 0,   0],
                  [0,  0, 1, 0.5],
                  [0,  0, 0,   1]]])

Pmnb = np.array([[[1,  0,  0,  0],
                  [0,  1,  0,  0],
                  [0,  0,  1,  0],
                  [0,  0,  0,  1]],

                 [[-1, 0,  0,  0],
                  [0, -1,  0,  0],
                  [0,  0, -1,  0],
                  [0,  0,  0,  1]],

                 [[ 1, 0, 0, 0.5],
                  [0, -1, 0, 0.5],
                  [ 0, 0, 1, 0.5],
                  [ 0, 0, 0,   1]],

                 [[-1, 0, 0, 0.5],
                  [0,  1, 0, 0.5],
                  [0, 0, -1, 0.5],
                  [0,  0, 0,   1]],

                 [[1,  0, 0,   0],
                  [0,  1, 0, 0.5],
                  [0, 0, -1, 0.5],
                  [0,  0, 0,   1]],

                 [[-1, 0, 0,   0],
                  [0, -1, 0, 0.5],
                  [0,  0, 1, 0.5],
                  [0,  0, 0,   1]],

                 [[-1, 0, 0, 0.5],
                  [0,  1, 0,   0],
                  [0,  0, 1,   0],
                  [0,  0, 0,   1]],

                 [[1,  0, 0, 0.5],
                  [0, -1, 0,   0],
                  [0,  0, -1,  0],
                  [0,  0, 0,   1]]])

Pbnm = np.array([[[1,  0,  0,  0],
                  [0,  1,  0,  0],
                  [0,  0,  1,  0],
                  [0,  0,  0,  1]],

                 [[-1, 0,  0,  0],
                  [0, -1,  0,  0],
                  [0,  0, -1,  0],
                  [0,  0,  0,  1]],

                 [[ 1, 0, 0, 0.5],
                  [0, -1, 0, 0.5],
                  [ 0, 0, 1, 0.5],
                  [ 0, 0, 0,   1]],

                 [[-1, 0, 0, 0.5],
                  [0,  1, 0, 0.5],
                  [0, 0, -1, 0.5],
                  [0,  0, 0,   1]],

                 [[-1, 0, 0, 0.5],
                  [0,  1, 0, 0.5],
                  [0,  0, 1,   0],
                  [0,  0, 0,   1]],

                 [[1,  0, 0, 0.5],
                  [0, -1, 0, 0.5],
                  [0, 0, -1,   0],
                  [0,  0, 0,   1]],

                 [[1,  0, 0,   0],
                  [0,  1, 0,   0],
                  [0, 0, -1, 0.5],
                  [0,  0, 0,   1]],

                 [[-1, 0, 0,   0],
                  [0, -1, 0,   0],
                  [0,  0, 1, 0.5],
                  [0,  0, 0,   1]]])

Pmcn = np.array([[[1,  0,  0,  0],
                  [0,  1,  0,  0],
                  [0,  0,  1,  0],
                  [0,  0,  0,  1]],

                 [[-1, 0,  0,  0],
                  [0, -1,  0,  0],
                  [0,  0, -1,  0],
                  [0,  0,  0,  1]],

                 [[ 1, 0, 0, 0.5],
                  [ 0, 1, 0, 0.5],
                  [0, 0, -1, 0.5],
                  [ 0, 0, 0,   1]],

                 [[-1, 0, 0, 0.5],
                  [0, -1, 0, 0.5],
                  [0,  0, 1, 0.5],
                  [0,  0, 0,   1]],

                 [[1,  0, 0,   0],
                  [0, -1, 0, 0.5],
                  [0,  0, 1, 0.5],
                  [0,  0, 0,   1]],

                 [[-1, 0, 0,   0],
                  [0,  1, 0, 0.5],
                  [0, 0, -1, 0.5],
                  [0,  0, 0,   1]],

                 [[-1, 0, 0, 0.5],
                  [0,  1, 0,   0],
                  [0,  0, 1,   0],
                  [0,  0, 0,   1]],

                 [[1,  0, 0, 0.5],
                  [0, -1, 0,   0],
                  [0, 0, -1,   0],
                  [0,  0, 0,   1]]])

Pcmn = np.array([[[1,  0,  0,  0],
                  [0,  1,  0,  0],
                  [0,  0,  1,  0],
                  [0,  0,  0,  1]],

                 [[-1, 0,  0,  0],
                  [0, -1,  0,  0],
                  [0,  0, -1,  0],
                  [0,  0,  0,  1]],

                 [[ 1, 0, 0, 0.5],
                  [ 0, 1, 0, 0.5],
                  [0, 0, -1, 0.5],
                  [ 0, 0, 0,   1]],

                 [[-1, 0, 0, 0.5],
                  [0, -1, 0, 0.5],
                  [0,  0, 1, 0.5],
                  [0,  0, 0,   1]],

                 [[-1, 0, 0, 0.5],
                  [0,  1, 0,   0],
                  [0,  0, 1, 0.5],
                  [0,  0, 0,   1]],

                 [[1,  0, 0, 0.5],
                  [0, -1, 0,   0],
                  [0, 0, -1, 0.5],
                  [0,  0, 0,   1]],

                 [[1,  0, 0,   0],
                  [0, -1, 0, 0.5],
                  [0,  0, 1,   0],
                  [0,  0, 0,   1]],

                 [[-1, 0, 0,   0],
                  [0,  1, 0, 0.5],
                  [0, 0, -1,   0],
                  [0,  0, 0,   1]]])

P4_12_12__1 = np.array([[[1,  0,  0,  0],
                         [0,  1,  0,  0],
                         [0,  0,  1,  0],
                         [0,  0,  0,  1]],
                        [[-1, 0,  0,  0],
                         [0, -1,  0,  0],
                         [0,  0, 1, 0.5],
                         [0,  0,  0,  1]],
                        [[0, -1, 0, 0.5],
                         [1,  0, 0, 0.5],
                         [0, 0, 1, 0.25],
                         [0,  0,  0,  1]],
                        [[0,  1, 0, 0.5],
                         [-1, 0, 0, 0.5],
                         [0, 0, 1, 0.75],
                         [0,  0,  0,  1]],
                        [[1,  0, 0, 0.5],
                         [0, -1, 0, 0.5],
                         [0, 0, -1, 0.75],
                         [0,  0,  0,  1]],
                        [[-1, 0, 0, 0.5],
                         [0,  1, 0, 0.5],
                         [0, 0, -1, 0.25],
                         [0,  0,  0,  1]],
                        [[0, -1,  0,  0],
                         [-1, 0,  0,  0],
                         [0, 0, -1, 0.5],
                         [0,  0,  0,  1]],
                        [[0,  1,  0,  0],
                         [1,  0,  0,  0],
                         [0,  0, -1,  0],
                         [0,  0,  0,  1]]])

P4_12_12__2 = np.array([[[1,  0,  0,  0],
                         [0,  1,  0,  0],
                         [0,  0,  1,  0],
                         [0,  0,  0,  1]],
                        [[-1, 0,  0,  0],
                         [0, -1,  0,  0],
                         [0,  0, 1, 0.5],
                         [0,  0,  0,  1]],
                        [[0, -1,  0,  0],
                         [1,  0,  0,  0],
                         [0, 0, 1, 0.25],
                         [0,  0,  0,  1]],
                        [[0,  1,  0,  0],
                         [-1, 0,  0,  0],
                         [0, 0, 1, 0.75],
                         [0,  0,  0,  1]],
                        [[1,  0, 0, 0.5],
                         [0, -1, 0, 0.5],
                         [0, 0, -1, 0.75],
                         [0,  0,  0,  1]],
                        [[-1, 0, 0, 0.5],
                         [0,  1, 0, 0.5],
                         [0, 0, -1, 0.25],
                         [0,  0,  0,  1]],
                        [[0, -1, 0, 0.5],
                         [-1, 0, 0, 0.5],
                         [0, 0, -1, 0.5],
                         [0,  0,  0,  1]],
                        [[0,  1, 0, 0.5],
                         [1,  0, 0, 0.5],
                         [0,  0, -1,  0],
                         [0,  0,  0,  1]]])

P4_12_12__3 = np.array([[[1,  0,  0,  0],
                         [0,  1,  0,  0],
                         [0,  0,  1,  0],
                         [0,  0,  0,  1]],
                        [[-1, 0, 0, 0.5],
                         [0, -1,  0,  0],
                         [0,  0, 1, 0.5],
                         [0,  0,  0,  1]],
                        [[0, -1, 0, 0.25],
                         [1,  0, 0, 0.75],
                         [0, 0, 1, 0.25],
                         [0,  0,  0,  1]],
                        [[0,  1, 0, 0.25],
                         [-1, 0, 0, 0.25],
                         [0, 0, 1, 0.75],
                         [0,  0,  0,  1]],
                        [[1,  0, 0, 0.5],
                         [0, -1, 0, 0.5],
                         [0,  0, -1,  0],
                         [0,  0,  0,  1]],
                        [[-1, 0,  0,  0],
                         [0,  1, 0, 0.5],
                         [0, 0, -1, 0.5],
                         [0,  0,  0,  1]],
                        [[0, -1, 0, 0.75],
                         [-1, 0, 0, 0.75],
                         [0, 0, -1, 0.75],
                         [0,  0,  0,  1]],
                        [[0,  1, 0, 0.75],
                         [1,  0, 0, 0.25],
                         [0, 0, -1, 0.25],
                         [0,  0,  0,  1]]])

def get_orbit(symm_ops, p, tol=5e-4):
    orbit = []
    for op in symm_ops:
        o = SymmOp(op)
        pp = o.operate(p)
        pp = np.mod(np.round(pp, decimals=10), 1)
        pp[np.where(np.abs(1 - pp) < tol)] = 0
        if not in_array_list(orbit, pp, tol=tol):
            orbit.append(pp)
    return orbit

def in_array_list(array_list, a, tol=1e-5):
    """
    Extremely efficient nd-array comparison using numpy's broadcasting. This
    function checks if a particular array a, is present in a list of arrays.
    It works for arrays of any size, e.g., even matrix searches.

    Args:
        array_list ([array]): A list of arrays to compare to.
        a (array): The test array for comparison.
        tol (float): The tolerance. Defaults to 1e-5. If 0, an exact match is
            done.

    Returns:
        (bool)
    """
    if len(array_list) == 0:
        return False
    axes = tuple(range(1, a.ndim + 1))
    if not tol:
        return np.any(np.all(np.equal(array_list, a[None, :]), axes))
    else:
        return np.any(np.sum(np.abs(array_list - a[None, :]), axes) < tol)

def generate_pos(p):
    p = np.array(p)
    ps = []
    for i in permutations([0, 1, 2], 3):
        ps.append(p[np.array(i)])
    return ps