import numpy as np, colour

from colour.constants import DEFAULT_INT_DTYPE
from colour.io.luts import LUT3D, LUTSequence
from colour.io.luts.common import path_to_title
from colour.utilities import as_int_array, as_float_array


def read_unordered_LUT_SonySPI3D(path):
    """
    Reads given unordered *Sony* *.spi3d* *LUT* file.

    Parameters
    ----------
    path : unicode
        *LUT* path.

    Returns
    -------
    LUT3D or LUT3x1D
        :class:`LUT3D` or :class:`LUT3x1D` class instance.
    """

    title = path_to_title(path)
    domain_min, domain_max = np.array([0, 0, 0]), np.array([1, 1, 1])
    indexes = []
    comments = []
    table_unordered = []
    table_ordered = []
    
    with open(path) as spi3d_file:
        lines = filter(None, (line.strip() for line in spi3d_file.readlines()))
        for line in lines:
            if line.startswith('#'):
                comments.append(line[1:].strip())
                continue

            tokens = line.split()
            if len(tokens) == 3:
                size = DEFAULT_INT_DTYPE(tokens[0])
                
            if len(tokens) == 6:
                indexes.append(as_int_array(tokens[:3]))
                table_unordered.append(as_float_array(tokens[3:]))

    test_indexes = np.around(LUT3D.linear_table(size) * (size - 1)).reshape((-1, 3))
    for i in range(64):
        for j in range(64):
            if (np.array_equal(test_indexes[i], indexes[j])):
                table_ordered.append(table_unordered[j])
    
    table_ordered = as_float_array(table_ordered).reshape([size, size, size, 3])
    
    return LUT3D(
            table_ordered, title, np.vstack([domain_min, domain_max]), comments=comments)
