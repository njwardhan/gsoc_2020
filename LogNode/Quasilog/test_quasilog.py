from __future__ import division, unicode_literals

import numpy as np
import unittest

from quasilog import (
    logarithmic_function_basic, logarithmic_function_quasilog, 
    logarithmic_function_camera, log_encoding_Log2,
    log_decoding_Log2)
from colour.utilities import domain_range_scale, ignore_numpy_errors


class TestLogarithmFunction_Quasilog(unittest.TestCase):
    """
    Defines :func:`colour.models.rgb.transfer_functions.log.\
logarithmic_function_quasilog` definition unit tests methods.
    """

    def test_logarithmic_function_quasilog(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.log.\
logarithmic_function_quasilog` definition.
        """

        self.assertAlmostEqual(
            logarithmic_function_quasilog(0.18), -2.47393118833, places=7)

        self.assertAlmostEqual(
            logarithmic_function_quasilog(0.18, 2.2, 'linToLog'),
            -2.17487782383,
            places=7)

        self.assertAlmostEqual(
            logarithmic_function_quasilog(0.18, 2.2, 'linToLog', 0.001),
            -0.002174877823,
            places=7)

        self.assertAlmostEqual(
            logarithmic_function_quasilog(0.18, 2.2, 'linToLog', 0.001, 0.12),
            -0.0048640068025,
            places=7)

        self.assertAlmostEqual(
            logarithmic_function_quasilog(0.18, 2.2, 'linToLog', 0.001, 0.12,
                                        0.001),
            -0.003864006802,
            places=7)

        self.assertAlmostEqual(
            logarithmic_function_quasilog(0.18, 2.2, 'linToLog', 0.001, 0.12,
                                        0.001, 0.12),
            -0.001479207115,
            places=7)

        self.assertAlmostEqual(
            logarithmic_function_quasilog(-2.47393118833, 2, 'logToLin'),
            0.18,
            places=7)

        self.assertAlmostEqual(
            logarithmic_function_quasilog(-2.17487782383, 2.2, 'logToLin'),
            0.18,
            places=7)

        self.assertAlmostEqual(
            logarithmic_function_quasilog(-0.002174877823, 2.2, 'logToLin', 0.001),
            0.18,
            places=7)

        self.assertAlmostEqual(
            logarithmic_function_quasilog(-0.004864006802, 2.2, 'logToLin', 0.001, 0.12),
            0.18,
            places=7)

        self.assertAlmostEqual(
            logarithmic_function_quasilog(-0.003864006802, 2.2, 'logToLin',
                                        0.001, 0.12, 0.001),
            0.18,
            places=7)

        self.assertAlmostEqual(
            logarithmic_function_quasilog(-0.001479207115, 2.2, 'logToLin',
                                        0.001, 0.12, 0.001, 0.12),
            0.18,
            places=7)




class TestLogarithmFunction_Camera(unittest.TestCase):
    """
    Defines :func:`colour.models.rgb.transfer_functions.log.\
logarithmic_function_camera` definition unit tests methods.
    """

    def test_logarithmic_function_camera(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.log.\
logarithmic_function_camera` definition.
        """


        self.assertAlmostEqual(
            logarithmic_function_camera(0.18, 2, 'cameraLinToLog', 2.2),
            -0.187152831975,
            places=7)

        self.assertAlmostEqual(
            logarithmic_function_camera(0.18, 2.2, 'cameraLinToLog', 2.2),
            -0.164529452496,
            places=7)

        self.assertAlmostEqual(
            logarithmic_function_camera(0.18, 2.2, 'cameraLinToLog', 2.2,
                                        0.001),
            -0.000164529452,
            places=7)

        self.assertAlmostEqual(
            logarithmic_function_camera(0.18, 2.2, 'cameraLinToLog', 2.2,
                                        0.001, 0.001),
            -0.008925631353,
            places=7)

        self.assertAlmostEqual(
            logarithmic_function_camera(0.18, 2.2, 'cameraLinToLog', 2.2,
                                        0.001, 0.001, 0.12),
            0.111074368646,
            places=7)

        self.assertAlmostEqual(
            logarithmic_function_camera(0.18, 2.2, 'cameraLinToLog', 2.2,
                                        0.001, 0.001, 0.12, 0.12),
            0.11731294726,
            places=7)

        self.assertAlmostEqual(
            logarithmic_function_camera(-0.187152831975, 2,
                                        'cameraLogToLin', 2.2),
            0.180000000001,
            places=7)

        self.assertAlmostEqual(
            logarithmic_function_camera(-0.164529452496, 2.2, 'cameraLogToLin',
                                        2.2),
            0.180000000001,
            places=7)

        self.assertAlmostEqual(
            logarithmic_function_camera(-0.000164529452, 2.2, 'cameraLogToLin',
                                        2.2, 0.001),
            0.180000000001,
            places=7)

        self.assertAlmostEqual(
            logarithmic_function_camera(-0.008925631353, 2.2, 'cameraLogToLin',
                                        2.2, 0.001, 0.001),
            0.180000000001,
            places=7)

        self.assertAlmostEqual(
            logarithmic_function_camera(0.111074368646, 2.2, 'cameraLogToLin',
                                        2.2, 0.001, 0.001, 0.12),
            0.179999999649,
            places=7)

        self.assertAlmostEqual(
            logarithmic_function_camera(0.11731294726, 2.2, 'cameraLogToLin',
                                        2.2, 0.001, 0.001, 0.12, 0.12),
            0.17999999231,
            places=7)