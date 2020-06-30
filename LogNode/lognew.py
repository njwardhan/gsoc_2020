import numpy as np, math
from colour.utilities import as_float, as_float_array, suppress_warnings

def logarithm_basic(x, base=2, style='log2'):
    """
    Defines the basic logarithmic function.

    Parameters
    ----------
    x : numeric
        The data to undergo basic logarithmic conversion.
    base : numeric, optional
        The base value used for the conversion.
    style : unicode, optional
        **{'log10', 'antiLog10', 'log2', 'antiLog2'}**,
        Defines the behaviour for the logarithmic function to operate:

        -   *log10*: Applies a base 10 logarithm to the passed value.
        -   *antiLog10*: Applies a base 10 anti-logarithm to the passed value.
        -   *log2*: Applies a base 2 logarithm to the passed value.
        -   *antiLog2*: Applies a base 2 anti-logarithm to the passed value.
        
    Returns
    -------
    numeric or ndarray
        Logarithmically converted data.

    Raises
    ------
    ValueError
        If the *style* is not defined.

    Examples
    --------
    The basic logarithmic function *styles* operate as follows:

    >>> logarithm_basic(0.18)  # doctest: +ELLIPSIS
    -2.4739311883324122
    >>> logarithm_basic(0.18, 10, 'log10')  # doctest: +ELLIPSIS
    -0.74472749489669388
    >>> logarithm_basic(-2.473931188332412, 2, 'antiLog2')  # doctest: +ELLIPSIS
    0.18000000000000002
    >>> logarithm_basic(-0.7447274948966939, 10, 'antiLog10')  # doctest: +ELLIPSIS
    0.18000000000000002
    """ 

    FLT_MIN = 1.175494e-38 

    def log_base(x, base=2):
        """
        Returns the (base) logarithm of the passed value. 
        """
        y = math.log(x, base)
        return y
    
    def antilog_base(x, base=2):
        """
        Returns the (base) anti-logarithm of the passed value.
        """

        return base ** x

    style = style.lower()
    if style == 'log10':
        return as_float(np.where(x>FLT_MIN, log_base(x, 10), log_base(FLT_MIN, 10)))
    elif style == 'antilog10':
        return antilog_base(x, 10)
    elif style == 'log2':
        return as_float(np.where(x>FLT_MIN, log_base(x), log_base(FLT_MIN)))
    elif style == 'antilog2':
        return antilog_base(x)
    else:
        raise ValueError(
            'Undefined style used: "{0}", must be one of the following: '
            '"{1}".'.format(
                style, ', '.join([
                    'log10', 'antiLog10', 'log2', 'antiLog2'
                ])))

def logarithm_lin_to_log(x, base=2, logSideSlope=1, linSideSlope=1, logSideOffset=0, linSideOffset=0):
    """
    Defines the linear to logarithm encoding transfer function.

    Parameters
    ----------
    x : numeric
        Linear data to undergo encoding.
    base : numeric, optional
        The base value used for the transfer.
    logSideSlope : numeric, optional
        It is the slope (or gain) applied to the log side of the logarithmic segment.
        Its default value is 1. 
    linSideSlope : numeric, optional
        It is the slope of the linear side of the logarithmic segment.
        Its default value is 1.
    logSideOffset : numeric, optional
        It is the offset applied to the log side of the logarithmic segment.
        Its default value is 0.
    linSideOffset : numeric, optional
        It is the offset applied to the linaer side of the logarithmic segment.
        Its default value is 0.

    Returns
    -------
    numeric or ndarray
        Logarithmic encoded data.

    Examples
    --------
    >>> logarithm_lin_to_log(0.18)  # doctest: +ELLIPSIS
    -2.4739311883324122
    """

    FLT_MIN = 1.175494e-38  
    return as_float((logSideSlope * math.log(max(linSideSlope * x + linSideOffset, FLT_MIN), base) + logSideOffset))

def logarithm_log_to_lin(x, base=2, logSideSlope=1, linSideSlope=1, logSideOffset=0, linSideOffset=0):
    """
    Defines the logarithmic to linear decoding transfer function.

    Parameters
    ----------
    x : numeric
        Logarithmic data to undergo decoding.
    base : numeric, optional
        The base value used for the transfer.
    logSideSlope : numeric, optional
        It is the slope (or gain) applied to the log side of the logarithmic segment.
        Its default value is 1. 
    linSideSlope : numeric, optional
        It is the slope of the linear side of the logarithmic segment.
        Its default value is 1.
    logSideOffset : numeric, optional
        It is the offset applied to the log side of the logarithmic segment.
        Its default value is 0.
    linSideOffset : numeric, optional
        It is the offset applied to the linaer side of the logarithmic segment.
        Its default value is 0.

    Returns
    -------
    numeric or ndarray
        Linear decoded data.

    Example
    --------
    >>> logarithm_log_to_lin(-2.47393118833)  # doctest: +ELLIPSIS
    0.18000000000030097
    """

    return as_float(((base ** ((x-logSideOffset) / logSideSlope) - linSideOffset) / linSideSlope)) 

def logarithm_camera_lin_to_log(x, linSideBreak, base=2, logSideSlope=1, linSideSlope=1, logSideOffset=0, linSideOffset=0):
    """
    Defines the parametrized camera log encoding function, which does the linear to logarithmic conversion.  

    Parameters
    ----------
    x : numeric
        Linear data to undergo encdoing.
    linSideBreak : numeric
        It is the the break-point, defined in linear space, at which the piece-wise function transitions 
        between the logarithmic and linear segments.
    base : numeric, optional
        The base value used for the transfer.
    logSideSlope : numeric, optional
        It is the slope (or gain) applied to the log side of the logarithmic segment.
        Its default value is 1. 
    linSideSlope : numeric, optional
        It is the slope of the linear side of the logarithmic segment.
        Its default value is 1.
    logSideOffset : numeric, optional
        It is the offset applied to the log side of the logarithmic segment.
        Its default value is 0.
    linSideOffset : numeric, optional
        It is the offset applied to the linaer side of the logarithmic segment.
        Its default value is 0.

    Returns
    -------
    numeric or ndarray
        Logarithmic encoded data.

    Example
    --------
    >>> logarithm_camera_lin_to_log(0.18, 2.2)  # doctest: +ELLIPSIS
    -0.18715283197538601
    """

    logSideBreak = logSideSlope * math.log((linSideSlope * linSideBreak + linSideOffset), base) + logSideOffset
    linearSlope = logSideSlope * (linSideSlope / ((linSideSlope * linSideBreak + linSideOffset) * np.log(base)))
    linearOffset = logSideBreak - linearSlope * linSideBreak

    return as_float(np.where(x <= linSideBreak, linearSlope * x + linearOffset, logarithm_lin_to_log(x)))

def logarithm_camera_log_to_lin(x, linSideBreak, base=2, logSideSlope=1, linSideSlope=1, logSideOffset=0, linSideOffset=0):
    """
    Defines the parametrized camera log decoding function, which does the logarithmic to linear conversion. 

    Parameters
    ----------
    x : numeric
        Logarithmic data to undergo decoding.
    linSideBreak : numeric
        It is the the break-point, defined in linear space, at which the piece-wise function transitions 
        between the logarithmic and linear segments.
    base : numeric, optional
        The base value used for the transfer.
    logSideSlope : numeric, optional
        It is the slope (or gain) applied to the log side of the logarithmic segment.
        Its default value is 1. 
    linSideSlope : numeric, optional
        It is the slope of the linear side of the logarithmic segment.
        Its default value is 1.
    logSideOffset : numeric, optional
        It is the offset applied to the log side of the logarithmic segment.
        Its default value is 0.
    linSideOffset : numeric, optional
        It is the offset applied to the linaer side of the logarithmic segment.
        Its default value is 0.

    Returns
    -------
    numeric or ndarray
        Linear decoded data.

    Example
    --------
    >>> logarithm_camera_log_to_lin(-0.187152831975, 2.2)  # doctest: +ELLIPSIS
    0.18000000000058866
    """

    logSideBreak = logSideSlope * math.log((linSideSlope * linSideBreak + linSideOffset), base) + logSideOffset
    linearSlope = logSideSlope * (linSideSlope / ((linSideSlope * linSideBreak + linSideOffset) * np.log(base)))
    linearOffset = logSideBreak - linearSlope * linSideBreak

    return as_float(np.where(x <= logSideBreak, (x-linearOffset)/linearSlope, logarithm_log_to_lin(x)))