import colour, numpy as np
from colour.algebra import (LinearInterpolator, table_interpolation_trilinear,
                            Extrapolator)
from colour.utilities.deprecation import handle_arguments_deprecation

def invert(self):
    """
    Computes and returns the inverse of the *LUT*.

    Returns
    -------
    LUT1D
        Inverse *LUT* class instance.

    Warning
    -------
    The *invert* definition is subject to precision issues, whenever
    possible, use the :meth:`colour.io.luts.lut.AbstractLUT.apply` method
    with the ``inverse`` argument.

    Examples
    --------
    >>> LUT = LUT1D(LUT1D.linear_table(1024) ** (1 / 2.2))
    >>> LUT_inverse = LUT.invert()
    >>> LUT_inverse.apply(LUT.apply(0.18))  # doctest: +ELLIPSIS
    0.1800000...
    """

    if self.is_domain_explicit():
        samples = self.domain
    else:
        domain_min, domain_max = self.domain
        samples = np.linspace(domain_min, domain_max, self.size)

    table_inverse = Extrapolator(LinearInterpolator(self.table,
                                                        samples))(samples)

    LUT_inverse = LUT1D(table_inverse, '{0} Inverse'.format(self.name), self.domain)

    return LUT_inverse

def apply(self,
            RGB,
            interpolator=LinearInterpolator,
            interpolator_kwargs=None,
            inverse=False,
            **kwargs):
    """
    Applies the *LUT* to given *RGB* colourspace array using given method.

    Parameters
    ----------
    RGB : array_like
        *RGB* colourspace array to apply the *LUT* onto.
    interpolator : object, optional
        Interpolator class type to use as interpolating function.
    interpolator_kwargs : dict_like, optional
        Arguments to use when instantiating the interpolating function.
    inverse : boolean, optional
        Checks if the LUT has to be applied in forward or backward
        direction.

    Other Parameters
    ----------------
    \\**kwargs : dict, optional
        Keywords arguments for deprecation management.

    Returns
    -------
    ndarray
        Interpolated *RGB* colourspace array.

    Examples
    --------
    >>> LUT = LUT1D(LUT1D.linear_table() ** (1 / 2.2))
    >>> RGB = np.array([0.18, 0.18, 0.18])

    *LUT* applied to the given *RGB* colourspace in forward direction:

    >>> LUT.apply(RGB)  # doctest: +ELLIPSIS
    array([ 0.4529220...,  0.4529220...,  0.4529220...])

    *LUT* applied to the modified *RGB* colourspace in reverse direction:

    >>> LUT.apply(LUT.apply(RGB), inverse=True)  # doctest: +ELLIPSIS
    array([ 0.18...,  0.18...,  0.18...])
    """

    interpolator_kwargs = handle_arguments_deprecation({
        'ArgumentRenamed': [['interpolator_args', 'interpolator_kwargs']],
    }, **kwargs).get('interpolator_kwargs', interpolator_kwargs)

    if interpolator_kwargs is None:
        interpolator_kwargs = {}

    if self.is_domain_explicit():
        samples = self.domain    
    else:
        domain_min, domain_max = self.domain

        samples = np.linspace(domain_min, domain_max, self.size)
    
    if inverse:
        self.table = Extrapolator(LinearInterpolator(self.table, samples))(samples)

    RGB_i = interpolator(samples, self.table,
                                    **interpolator_kwargs)(RGB)

    return RGB_i