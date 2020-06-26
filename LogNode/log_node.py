from __future__ import division, unicode_literals
import numpy as np, math

import numpy as np
from colour.utilities import from_range_1, to_domain_1, as_float_array


def basic_logarithm(x, base=2, style='log2'):
    FLT_MIN = 1.175494e-38 

    def log_base(x, base=2):
        y = math.log(x, base)
        return y
    
    def antilog_base(y, base=2):
        return base ** y

    style = style.lower()
    if style == 'log10':
        return np.where(x>FLT_MIN, log_base(x, 10), log_base(FLT_MIN, 10))
    elif style == 'antilog10':
        return antilog_base(x, 10)
    elif style == 'log2':
        return np.where(x>FLT_MIN, log_base(x), log_base(FLT_MIN))
    elif style == 'antilog2':
        return antilog_base(x)

def encoding_decoding_logarithm(x, style='linToLog', linSideBreak=1, base=2, logSideSlope=1, linSideSlope=1, logSideOffset=0, linSideOffset=0):
    FLT_MIN = 1.175494e-38

    def linToLog(x, base=2, logSideSlope=1, linSideSlope=1, logSideOffset=0, linSideOffset=0):
        y = logSideSlope * math.log(max(linSideSlope * x + linSideOffset, FLT_MIN), base) + logSideOffset
        return y

    def logToLin(y, base=2, logSideSlope=1, linSideSlope=1, logSideOffset=0, linSideOffset=0):
        return ((base ** ((y-logSideOffset) / logSideSlope) - linSideOffset) / linSideSlope)

    logSideBreak = logSideSlope * math.log((linSideSlope * linSideBreak + linSideOffset), base) + logSideOffset
    linearSlope = logSideSlope * (linSideSlope / ((linSideSlope * linSideBreak + linSideOffset) * np.log(base)))
    linearOffset = logSideBreak - linearSlope * linSideBreak

    style = style.lower()
    if style == 'lintolog':
        return linToLog(x)
    elif style == 'logtolin':
        return logToLin(x)
    elif style == 'cameralintolog':
        return np.where(x <= linSideBreak, linearSlope * x + linearOffset, linToLog(x))
    elif style == 'cameralogtolin':
        return np.where(x <= logSideBreak, (x-linearOffset)/linearSlope, logToLin(x))
    