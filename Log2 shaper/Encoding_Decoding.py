import numpy as np
from colour.utilities import from_range_1, to_domain_1


def log_encoding_Log2(lin, middle_grey, min_exposure, max_exposure):
    lin = to_domain_1(lin)

    lg2 = np.log2(lin / middle_grey)
    log_norm = (lg2 - min_exposure) / (max_exposure - min_exposure)
    
    return from_range_1(log_norm)


def log_decoding_Log2(log_norm, middle_grey, min_exposure, max_exposure):
    log_norm = to_domain_1(log_norm)

    lg2 = log_norm*(max_exposure - min_exposure) + min_exposure
    lin = (2 ** lg2) * middle_grey

    return from_range_1(lin)


args = 0.18, 0.18 * 2 ** -6.5 , 0.18 * 2 ** 6.5

log_decoding_Log2(log_encoding_Log2(np.linspace(0, 1, 11), *args), *args)


