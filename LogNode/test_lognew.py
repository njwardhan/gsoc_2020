# -*- coding: utf-8 -*-
"""
Defines unit tests for :mod:`colour.models.rgb.transfer_functions.log`
module.
"""

from __future__ import division, unicode_literals

import numpy as np
import unittest

from lognew import (logarithm_basic, logarithm_lin_to_log, logarithm_log_to_lin, logarithm_camera_lin_to_log, logarithm_camera_log_to_lin)
from colour.utilities import domain_range_scale, ignore_numpy_errors

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013-2020 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = ['TestLogarithm_basic', 'TestLogarithm_linToLog', 'TestLogarithm_logToLin', 'TestLogarithm_cameraLinToLog', 'TestLogarithm_cameraLogToLin']

class TestLogarithm_basic(unittest.TestCase):
    """
    Defines :func:`colour.models.rgb.transfer_functions.log.logarithm_basic`
    definition unit tests methods.
    """

    def test_logarithm_basic(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.log.\
logarithm_basic` definition.
        """

        self.assertAlmostEqual(
            logarithm_basic(0.18), -2.47393118833, places=7)

        self.assertAlmostEqual(
            logarithm_basic(0.18, 10, 'log10'), -0.744727494897, places=7)

        self.assertAlmostEqual(
            logarithm_basic(-0.744727494897, 10, 'antiLog10'),
            0.17999999999987315,
            places=7)
        
        self.assertAlmostEqual(
            logarithm_basic(-2.47393118833, 2, 'antiLog2'),
            0.18000000000030097,
            places=7)


class TestLogarithm_linToLog(unittest.TestCase):
    """
    Defines :func:`colour.models.rgb.transfer_functions.log.logarithm_lin_to_log`
    definition unit tests methods.
    """

    def test_logarithm_lin_to_log(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.log.\
logarithm_lin_to_log` definition.
        """

        self.assertAlmostEqual(
            logarithm_lin_to_log(0.18), -2.47393118833, places=7)

        self.assertAlmostEqual(
            logarithm_lin_to_log(0.18, 2.2), -2.17487782383, places=7)

        self.assertAlmostEqual(
            logarithm_lin_to_log(0.18, 2.2, 0.001),
            -0.00217487782383,
            places=7)
        
        self.assertAlmostEqual(
            logarithm_lin_to_log(
            0.18, 2.2, 0.001, 0.12),
            -0.0048640068025,
            places=7)

        self.assertAlmostEqual(
            logarithm_lin_to_log(
            0.18, 2.2, 0.001, 0.12, 0.001),
            -0.0038640068025,
            places=7)
        
        self.assertAlmostEqual(
            logarithm_lin_to_log(
            0.18, 2.2, 0.001, 0.12, 0.001, 0.12),
            -0.00147920711504,
            places=7)


class TestLogarithm_logToLin(unittest.TestCase):
    """
    Defines :func:`colour.models.rgb.transfer_functions.log.logarithm_log_to_lin`
    definition unit tests methods.
    """

    def test_logarithm_log_to_lin(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.log.\
logarithm_log_to_lin` definition.
        """

        self.assertAlmostEqual(
            logarithm_log_to_lin(-2.47393118833), 0.18, places=7)

        self.assertAlmostEqual(
            logarithm_log_to_lin(-2.17487782383, 2.2), 0.18, places=7)

        self.assertAlmostEqual(
            logarithm_log_to_lin(
            -0.00217487782383, 2.2, 0.001),
            0.18,
            places=7)
        
        self.assertAlmostEqual(
            logarithm_log_to_lin(
            -0.0048640068025, 2.2, 0.001, 0.12),
            0.18,
            places=7)

        self.assertAlmostEqual(
            logarithm_log_to_lin(
            -0.0038640068025, 2.2, 0.001, 0.12, 0.001),
            0.18,
            places=7)

        self.assertAlmostEqual(
            logarithm_log_to_lin(
            -0.00147920711504, 2.2, 0.001, 0.12, 0.001, 0.12),
            0.18,
            places=7)


class TestLogarithm_cameraLinToLog(unittest.TestCase):
    """
    Defines :func:`colour.models.rgb.transfer_functions.log.logarithm_camera_lin_to_log`
    definition unit tests methods.
    """

    def test_logarithm_camera_lin_to_log(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.log.\
logarithm_camera_lin_to_log` definition.
        """

        self.assertAlmostEqual(
            logarithm_camera_lin_to_log(0.18, 2.2), -0.187152831975, places=7)

        self.assertAlmostEqual(
            logarithm_camera_lin_to_log(0.18, 2.2, 2.2), 
            -0.164529452496,
            places=7)

        self.assertAlmostEqual(
            logarithm_camera_lin_to_log(
            0.18, 2.2, 2.2, 0.001),
            -0.000164529452496,
            places=7)
        
        self.assertAlmostEqual(
            logarithm_camera_lin_to_log(
            0.18, 2.2, 2.2, 0.001, 0.001),
            -0.0089256313538,
            places=7)

        self.assertAlmostEqual(
            logarithm_camera_lin_to_log(
            0.18, 2.2, 2.2, 0.001, 0.001, 0.12),
            0.111074368646,
            places=7)
        
        self.assertAlmostEqual(
            logarithm_camera_lin_to_log(
            0.18, 2.2, 2.2, 0.001, 0.001, 0.12, 0.12),
            0.11731294726,
            places=7)


class TestLogarithm_cameraLogToLin(unittest.TestCase):
    """
    Defines :func:`colour.models.rgb.transfer_functions.log.logarithm_camera_log_to_lin`
    definition unit tests methods.
    """

    def test_logarithm_camera_log_to_lin(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.log.\
logarithm_camera_log_to_lin` definition.
        """

        self.assertAlmostEqual(
            logarithm_camera_log_to_lin(-0.187152831975, 2.2), 0.180000000001, places=7)

        self.assertAlmostEqual(
            logarithm_camera_log_to_lin(-0.164529452496, 2.2, 2.2), 0.180000000001, places=7)

        self.assertAlmostEqual(
            logarithm_camera_log_to_lin(
            -0.000164529452496, 2.2, 2.2, 0.001),
            0.180000000001,
            places=7)
        
        self.assertAlmostEqual(
            logarithm_camera_log_to_lin(
            -0.0089256313538, 2.2, 2.2, 0.001, 0.001),
            0.179999999996,
            places=7)

        self.assertAlmostEqual(
            logarithm_camera_log_to_lin(
            0.111074368646, 2.2, 2.2, 0.001, 0.001, 0.12),
            0.179999999649,
            places=7)

        self.assertAlmostEqual(
            logarithm_camera_log_to_lin(
            0.11731294726, 2.2, 2.2, 0.001, 0.001, 0.12, 0.12),
            0.17999999231,
            places=7)


if __name__ == '__main__':
    unittest.main()
