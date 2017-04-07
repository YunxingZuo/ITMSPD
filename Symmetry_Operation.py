# coding: utf-8
# Copyright © 2016 YunXing Zuo, WeiJi Hsiao

import numpy as np
from math import cos
from math import sin
from math import pi

__author__ = 'YunXing Zuo, WeiJi Hsiao'
__email__ = 'weiji.hsiao@gmail.com'
__date__ = 'Oct. 25, 2016'

class SymmOp(object):
    # affine transformation combine the rotations and translations into a 4x4 array
    def __init__(self, affine_transformation_matrix, symprec=1e-5):
        affine_transformation_matrix = np.array(affine_transformation_matrix)
        if affine_transformation_matrix.shape != (4, 4):
            raise valueError("Affine Matrix must be a 4x4 numpy array")
        self.affine_matrix = affine_transformation_matrix
        self.symprec = symprec

    # this method is really used to construct the class
    @staticmethod
    def rotations_combine_translations(rotations_matrix, translation_vec, symprec=1e-5):
        rotations_matrix = np.array(rotations_matrix)
        translation_vec = np.array(translation_vec)
        if rotations_matrix.shape != (3, 3):
            raise valueError("Rotation Matrix must be a 3x3 array")
        if translation_vec.shape != (3,):
            raise valueError("Translation vector must be 1x3 array")
        affine_matrix = np.eye(4)
        affine_matrix[0:3][:, 0:3] = rotations_matrix
        affine_matrix[0:3][:, 3] = translation_vec
        return SymmOp(affine_matrix, symprec)

    @property
    def rotation_matrix(self):
        return self.affine_matrix[0:3][:, 0:3]

    @property
    def translation_vector(self):
        return self.affine_matrix[0:3][:, 3]

    # apply the operations to the points
    def operate(self, point):
        affine_point = np.array([point[0], point[1], point[2], 1])
        return np.dot(self.affine_matrix, affine_point)[0:3]

    # apply the operations to multiple points
    def operate_multiple_points(self, points):
        points = np.array(points)
        affine_points = np.concatenate([points, np.ones(points.shape[:-1] + (1,))], axis = -1)
        return np.inner(affine_points, self.affine_matrix)[:, :-1]

    # something tricky in the application of the rotation_matrix on the tensor
    def transform_tensor(self, tensor):
        dim = tensor.shape
        rank = len(dim)
        assert all([i == 3 for i in dim])
        # Build einstein sum string
        lc = string.ascii_lowercase
        indices = lc[:rank], lc[rank:2 * rank]
        einsum_string = ','.join([a + i for a, i in zip(*indices)])
        einsum_string += ',{}->{}'.format(*indices[::-1])
        einsum_args = [self.rotation_matrix] * rank + [tensor]

        return np.einsum(einsum_string, *einsum_args)

    # check if two points are identical
    def whether_symmetrical(self, point_a, point_b, lattice_constant, symprec = 1e-3):
        diff = self.operate(point_a) - point_b

        # exclude the error of integer times of directions of lattice, like [0.99999, 0., 0.] 
        diff -= np.rint(diff)
        dist = np.linalg.norm(np.dot(diff, lattice_constant))
        if dist < symprec:
            return True
        else:
            return False

    @staticmethod
    def axis_angle_and_translation(axis, angle, angle_in_radius=False, translation_vec=(0, 0, 0)):

        if isinstance(axis, (tuple, list)):
            axis = np.array(axis)

        if isinstance(translation_vec, (tuple, list)):
            vec = np.array(translation_vec)

        theta = angle if angle_in_radius else angle * pi / 180

        # Rodrigues' rotation formula
        cos_theta = cos(theta)
        sin_theta = sin(theta)
        normal = axis / np.linalg.norm(axis)
        u, v, w = normal
        R = np.zeros((3, 3))
        R[0, 0] = cos_theta + u ** 2 * (1 - cos_theta)
        R[0, 1] = u * v * (1 - cos_theta) - w * sin_theta
        R[0, 2] = u * w * (1 - cos_theta) + v * sin_theta
        R[1, 0] = u * v * (1 - cos_theta) + w * sin_theta
        R[1, 1] = cos_theta + v ** 2 * (1 - cos_theta)
        R[1, 2] = v * w * (1 - cos_theta) - u * sin_theta
        R[2, 0] = u * w * (1 - cos_theta) - v * sin_theta
        R[2, 1] = v * w * (1 - cos_theta) + u * sin_theta
        R[2, 2] = cos_theta + w ** 2 * (1 - cos_theta)

        return SymmOp.rotations_combine_translations(R, vec)

    @staticmethod
    def origin_axis_and_angle(origin, axis, angle, angle_in_radius=False):

        # substitue the rotated vector (v) with vector (v-origin) given the axis and angle
        theta = angle if angle_in_radius else angle * pi / 180

        normal = np.array(axis, dtype=float) / np.linalg.norm(axis)
        u, v, w = normal
        a, b, c = origin
        cos_theta = cos(theta)
        sin_theta = sin(theta)

        transform_mat = np.zeros((4, 4))
        transform_mat[0, 0] = cos_theta + u ** 2 * (1 - cos_theta)
        transform_mat[0, 1] = u * v * (1 - cos_theta) - w * sin_theta
        transform_mat[0, 2] = u * w * (1 - cos_theta) + v * sin_theta
        transform_mat[0, 3] = -a * transform_mat[0, 0] - b * transform_mat[0, 1] - c * transform_mat[0, 2]
        transform_mat[1, 0] = u * v * (1 - cos_theta) + w * sin_theta
        transform_mat[1, 1] = cos_theta + v ** 2 * (1 - cos_theta)
        transform_mat[1, 2] = v * w * (1 - cos_theta) - u * sin_theta
        transform_mat[1, 3] = -a * transform_mat[1, 0] - b * transform_mat[1, 1] - c * transform_mat[1, 2]
        transform_mat[2, 0] = u * w * (1 - cos_theta) - v * sin_theta
        transform_mat[2, 1] = v * w * (1 - cos_theta) + u * sin_theta
        transform_mat[2, 2] = cos_theta + w ** 2 * (1 - cos_theta)
        transform_mat[2, 3] = -a * transform_mat[2, 0] - b * transform_mat[2, 1] - c * transform_mat[2, 2]
        transform_mat[3, 3] = 1

        return SymmOp(transform_mat)

    @staticmethod
    def reflection(normal, origin=(0, 0, 0)):
        # return a matrix represent mirror_reflection given normal to the mirror plane and the origin the mirror plane passes through
        n = np.array(normal, dtype=float) / np.linalg.norm(normal)

        u, v, w = n

        # P2 = 2{[(P0 - P1)· n]n} + P1
        xx = 1 - 2 * u ** 2
        xy = yx = -2 * v * u
        xz = zx = -2 * w * u
        yy = 1 - 2 * v ** 2
        yz = zy = -2 * w * v
        zz = 1 - 2 * w ** 2
        x0 = origin[0]
        y0 = origin[1]
        z0 = origin[2]
        tran0 = 2 * u ** 2 * x0 + 2 * v * u * y0 + 2 * w * u * z0
        tran1 = 2 * u * v * x0 + 2 * v ** 2 * y0 + 2 * w * v * z0
        tran2 = 2 * u * w * x0 + 2 * v * w * y0 + 2 * w ** 2 * z0
        mirror_mat = np.array([[xx, xy, xz, tran0], [yx, yy, yz, tran1], [zx, zy, zz, tran2], [0, 0, 0, 1]])

        return SymmOp(mirror_mat)

    @staticmethod
    def inversion(origin=(0, 0, 0)):
        # return inversion symmetry operations given the origin
        inversion_mat = -np.eye(4)
        inversion_mat[3][3] = 1
        inversion_mat[0:3][3] = 2 * np.array(origin)

        return SymmOp(inversion_mat)

    # rotation first, reflection later
    @staticmethod
    def rotation_to_reflection(axis, angle, origin=(0, 0, 0)):

        rot = SymmOp.origin_axis_and_angle(origin, axis, angle)
        ref = SymmOp.reflection(axis, origin)
        rot_to_ref_mat = np.dot(rot.affine_matrix, ref.affine_matrix)
        return SymmOp(rot_to_ref_mat)

    # return a string indicate the rotation and translation
    def xyz_string(self):
        xyz = ['x', 'y', 'z']
        strings = []

        if not np.allclose(self.rotation_matrix, np.rint(self.rotation_matrix)):
            raise ValueError('Rotation matrix must be integer')

        for r, t in zip(self.rotation_matrix, self.translation_vector):
            symbols = []
            for val, axis in zip(r, xyz):
                val = int(round(val))
                if val == 1:
                    if symbols:
                        symbols.append('+')
                    symbols.append(axis)
                elif val == -1:
                    symbols.append('-' + axis)
                elif val > 1:
                    if symbols:
                        symbols.append('+')
                    symbols.append(str(val) + axis)
                elif val < -1:
                    symbols.append(str(val) + axis)
            import fractions
            f = fractions.Fraction(float(t)).limit_denominator()
            if abs(f) > 1e-6:
                if f > 0:
                    symbols.append('+')
                symbols.append(str(f))
            strings.append("".join(symbols))
        return ",".join(strings)
