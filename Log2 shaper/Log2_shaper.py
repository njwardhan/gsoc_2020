"""
Log2 Shaper Implementation
==========================

A 48-nits OCIO shaper used with a basic algorithm responsible for the generic transform from linear to log base-2 encoding.

Reference
---------
aces-dev: ACESutil.Lin_to_Log2_param.ctl: https://github.com/ampas/aces-dev/blob/master/transforms/ctl/utilities/ACESutil.Lin_to_Log2_param.ctl 

"""

import numpy as np
import colour

def lin_to_log2_32f(lin, middleGrey, minExposure, maxExposure):
    if (lin <= 0.0):
        return 0.0
    lg2 = np.log2(lin / middleGrey)
    logNorm = (lg2 - minExposure)/(maxExposure - minExposure)
    
    if (logNorm < 0.0):
        logNorm = 0
    return logNorm

domain = [0.18 * 2 ** -6.5 , 0.18 * 2 ** 6.5]
shaper = colour.LUT1D(size = 4096, domain = domain)
shaper.table = 0.18 * 2**(np.linspace(-6.5, 6.5, 4096))

# The table values of shaper are currently linear and in the range of 0.002 to 16.297(approximately)
print(shaper.table)

b=[]
for i in shaper.table:
    b.append(lin_to_log2_32f(i, 0.18, 3, 6.5))
shaper.table = b
print('\n')

# The table values of shaper are now converted to values in the range of 0 to 1 which symbolizes logarithmic endoing 
print(shaper.table)
