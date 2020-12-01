import colour
import numpy as np
from scipy.spatial import cKDTree

def invert_LUT3D(LUT, size=None, extrapolate=True, query_size=4):
    LUT = LUT.copy()
    source_size = LUT.size
    SIZE = source_size
    target_size = (
        colour.utilities.as_int(2 ** (np.sqrt(source_size) + 1) + 1)
        if size is None else size)
    if target_size > 129:
        colour.utilities.usage_warning(
            'LUT3D inverse computation time could be excessive!')
    if extrapolate:
        LUT.table = np.pad(
            LUT.table, [(1, 1), (1, 1), (1, 1), (0, 0)], 'reflect',
            reflect_type='odd')
        LUT.domain[0] -= 1 / (SIZE - 1)
        LUT.domain[1] += 1 / (SIZE - 1)
    LUT_intermediate = colour.LUT3D(size=target_size, domain=LUT.domain)
    indexes = LUT_intermediate.table
    LUT_intermediate.table = LUT.apply(LUT_intermediate.table)
    tree = cKDTree(LUT_intermediate.table.reshape(-1, 3))
    LUT_inverse = colour.LUT3D(size=target_size, domain=LUT.domain)
    query = tree.query(indexes, query_size, n_jobs=-1)[-1]
    if query_size == 1:
        LUT_inverse.table = indexes.reshape(-1, 3)[query].reshape(
            [target_size, target_size, target_size, 3])
    else:
        LUT_inverse.table = np.mean(indexes.reshape(-1, 3)[query],
                                    axis=-2).reshape(
            [target_size, target_size, target_size, 3])
    LUT_target = colour.LUT3D(size=target_size, domain=LUT.domain)
    LUT_target.table = LUT_inverse.apply(LUT_target.table)
    return LUT_target

RGB = [0.18, 0.18, 0.18]
LUT = colour.LUT3D()
LUT.table = colour.cctf_encoding(LUT.table)
RGB_a = LUT.apply(RGB)
LUT_inverse = invert_LUT3D(LUT)
RGB_i = LUT_inverse.apply(RGB_a)

print(RGB)
print(RGB_a)
print(RGB_i)


