import colour
import numpy as np
from scipy.spatial import cKDTree

def invert(self):
    """
    Returns the inverted format of the current *LUT*.
    Returns
    -------
    LUT3D
        Inverted *LUT* class instance.
    Warning
    -------
    The *invert* function is in experimental state and some inversions may
    be inaccurate and time-taking.
    Examples
    --------
    >>> LUT = LUT3D()
    >>> print(LUT)
    LUT3D - Unity 33
    ----------------
    <BLANKLINE>
    Dimensions : 3
    Domain     : [[ 0.  0.  0.]
                    [ 1.  1.  1.]]
    Size       : (33, 33, 33, 3)
    >>> print(LUT.invert())
    LUT3D - Inverted Format
    -----------------------
    <BLANKLINE>
    Dimensions : 3
    Domain     : [[ 0.  0.  0.]
                    [ 1.  1.  1.]]
    Size       : (33, 33, 33, 3)
    """
    size = self.size
    LUT_inverse = colour.LUT3D(size=size, name='Inverted Format')
    indexes = LUT_inverse.table

    tree = cKDTree(self.table.reshape(-1, 3))
    query = tree.query(indexes)[-1]

    LUT_inverse.table = indexes.reshape(-1, 3)[query].reshape(
        [size, size, size, 3])

    return LUT_inverse

RGB = [0.18, 0.18, 0.18]
LUT = colour.LUT3D()
LUT.table = colour.cctf_encoding(LUT.table)
RGB_a = LUT.apply(RGB)
LUT_inverse = invert(LUT)
RGB_i = LUT_inverse.apply(RGB_a)

print(RGB)
print(RGB_a)
print(RGB_i)
