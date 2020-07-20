import numpy as np, colour

from colour.constants import DEFAULT_INT_DTYPE
from colour.io.luts import LUT3D, LUTSequence
from colour.io.luts.common import path_to_title
from colour.utilities import as_int_array, as_float_array


def read_LUT_UnorderedSonySPI3D(path):
        title = path_to_title(path)
        domain_min, domain_max = np.array([0, 0, 0]), np.array([1, 1, 1])
        size = 2
        indexes = []
        table = []
        comments = []
        with open(path) as spi3d_file:
            lines = filter(None,
                           (line.strip() for line in spi3d_file.readlines()))
            for line in lines:
                if line.startswith('#'):
                    comments.append(line[1:].strip())
                    continue
                tokens = line.split()
                if len(tokens) == 3:
                    assert len(set(tokens)) == 1, (
                        'Non-uniform "LUT" shape is unsupported!')
                    size = DEFAULT_INT_DTYPE(tokens[0])
                if len(tokens) == 6:
                    indexes.append(as_int_array(tokens[:3]))
                    table.append(as_float_array(tokens[3:]))
        indexes = as_int_array(indexes)
        sorting_indexes = np.lexsort((indexes[:,2], indexes[:,1], indexes[:,0]))
        #print(sorting_indexes)
        assert np.array_equal(
            indexes[sorting_indexes],
            DEFAULT_INT_DTYPE(np.around(
                LUT3D.linear_table(size) * (size - 1))).reshape(
                (-1, 3))), 'Indexes do not match expected "LUT3D" indexes!'
        table = as_float_array(table)[sorting_indexes].reshape([size, size, size, 3])
        return LUT3D(
            table, title, np.vstack([domain_min, domain_max]),
            comments=comments)


NJW = read_LUT_UnorderedSonySPI3D('/home/njwardhan/Desktop/Unordered_test.cube')
#print(NJW)
