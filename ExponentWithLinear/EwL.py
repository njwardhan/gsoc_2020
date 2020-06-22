import colour, math, numpy as np
from colour.utilities import as_float_array

def basic_exponent(x , exponent, style='basicFwd'):
    x = as_float_array(x)
    exponent = as_float_array(exponent)

    def xFwd(x):
        y = x ** exponent
        return (y)

    def xRev(y):
        return y ** (1/exponent)
    
    style = style.lower()

    if style == 'basicfwd':
        return np.where(x>0, xFwd(x), 0)
    elif style == 'basicrev':
        return np.where(x>0, xRev(x), 0)
    elif style == 'basicmirrorfwd':
        return np.where(x>=0, xFwd(x), -xFwd(-x))
    elif style == 'basicmirrorrev':
        return np.where(x>=0, xRev(x), -xRev(-x))
    elif style == 'basicpassthrufwd':
        return np.where(x>0, xFwd(x), x)
    elif style == 'basicpassthrurev':
        return np.where(x>0, xRev(x), x)
    else:
        raise ValueError('Undefined style used')


def monCurve_exponent(x, exponent, offset, style='monCurveFwd'):
    x = as_float_array(x)
    exponent = as_float_array(exponent)
    offset = as_float_array(offset)
    s = ((exponent-1)/offset)*((exponent*offset)/((exponent-1)*(offset+1)))**exponent

    def monCurveFwd(x):
        xBreak = offset/(exponent-1)
        y = ((x+offset)/(1+offset))**exponent
        return np.where(x>=xBreak, y, x*s)

    def monCurveRev(y):
        yBreak = ((exponent*offset)/((exponent-1)*(offset+1)))**exponent
        return np.where(y>=yBreak, ((1+offset)*(y**(1/exponent)))-offset, y/s)

    style = style.lower()

    if style == 'moncurvefwd':
        return monCurveFwd(x)
    elif style == 'moncurverev':
        return monCurveRev(x)
    elif style == 'moncurvemirrorfwd':
        return np.where(x>=0, monCurveFwd(x), -monCurveFwd(-x))
    elif style == 'moncurvemirrorrev':
        return np.where(x>=0, monCurveRev(x), -monCurveRev(-x))
    else:
        raise ValueError('Undefined style used')
