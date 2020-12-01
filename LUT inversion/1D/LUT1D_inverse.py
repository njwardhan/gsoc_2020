import numpy as np, colour
from colour.algebra import LinearInterpolator
from colour.constants import DEFAULT_INT_DTYPE
from colour.utilities.deprecation import handle_arguments_deprecation


def inverse(self):
    """
    Generates the inverse effect of a given 1D *LUT*. 

    Returns
    -------
    ndarray
        A table with the reverse effect as that of a given 1D *LUT*.
    """

    SIZE = len(self._table)
    table_i = colour.LUT1D.linear_table(size=SIZE)
    table_i = colour.Extrapolator(
        colour.LinearInterpolator(
        self._table, table_i))(table_i)
    return table_i


def apply(self,
          RGB,
          inverse=False,
          interpolator=LinearInterpolator,
          interpolator_kwargs=None,
          **kwargs):
    """
    Applies the *LUT* to given *RGB* colourspace array using given method.
    Parameters
    ----------
    RGB : array_like
        *RGB* colourspace array to apply the *LUT* onto.
    inverse : boolean, optional
        Checks if the LUT has to be applied in forward or backward
        direction.
    interpolator : object, optional
        Interpolator class type to use as interpolating function.
    interpolator_kwargs : dict_like, optional
        Arguments to use when instantiating the interpolating function.
    Other Parameters
    ----------------
    \\**kwargs : dict, optional
        Keywords arguments for deprecation management.
    Returns
    -------
    ndarray
        Interpolated *RGB* colourspace array.
    """

    interpolator_kwargs = handle_arguments_deprecation({
        'ArgumentRenamed': [['interpolator_args', 'interpolator_kwargs']],
    }, **kwargs).get('interpolator_kwargs', interpolator_kwargs)

    if interpolator_kwargs is None:
        interpolator_kwargs = {}

    if inverse:
        SIZE = len(self._table)
        LUT_inverse = colour.LUT1D(size=SIZE)
        LUT_inverse.table = colour.Extrapolator(
            colour.LinearInterpolator(self._table, LUT_inverse.table))(LUT_inverse.table)
        RGB_i = LUT_inverse.apply(RGB)
        
        return RGB_i

    else:    
        if self.is_domain_explicit():
            samples = self.domain
        else:
            domain_min, domain_max = self.domain

        samples = np.linspace(domain_min, domain_max, self._table.size)

        RGB_interpolator = interpolator(samples, self._table,
                                            **interpolator_kwargs)
        return RGB_interpolator(RGB)

