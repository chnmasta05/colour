#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Blackbody - Planckian Radiator
==============================

Defines objects to compute the spectral radiance of a planckian radiator and
its spectral power distribution.

See Also
--------
colour.colorimetry.spectrum.SpectralPowerDistribution
"""

from __future__ import unicode_literals

import math
import numpy as np
import warnings

from colour.colorimetry import SpectralPowerDistribution
from colour.utilities import memoize

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013 - 2014 - Colour Developers'
__license__ = 'New BSD License - http://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = ['C1',
           'C2',
           'N',
           'planck_law',
           'blackbody_spectral_radiance',
           'blackbody_spectral_power_distribution']

C1 = 3.741771e-16  # 2 * math.pi * PLANCK_CONSTANT * LIGHT_SPEED ** 2
C2 = 1.4388e-2  # PLANCK_CONSTANT * LIGHT_SPEED / BOLTZMANN_CONSTANT
N = 1.

_PLANCK_LAW_CACHE = {}


@memoize(_PLANCK_LAW_CACHE)
def planck_law(wavelength, temperature, c1=C1, c2=C2, n=N):
    """
    Returns the spectral radiance of a blackbody at thermodynamic temperature
    :math:`T[K]` in a medium having index of refraction :math:`n`.

    Notes
    -----
    The following form implementation is expressed in term of wavelength.
    The SI unit of radiance is *watts per steradian per square metre*.

    References
    ----------
    .. [1]  `CIE 015:2004 Colorimetry, 3rd edition: Appendix E.
            Information on the Use of Planck"s Equation for Standard Air.
            <https://law.resource.org/pub/us/cfr/ibr/003/cie.15.2004.pdf>`_

    Parameters
    ----------
    wavelength : float
        Wavelength in meters.
    temperature : float
        Temperature :math:`T[K]` in kelvin degrees.
    c1 : float, optional
        The official value of :math:`c1` is provided by the Committee on Data
        for Science and Technology (CODATA), and is
        :math:`c1=3,741771x10.16\ W/m_2` (Mohr and Taylor, 2000).
    c2 : float, optional
        Since :math:`T` is measured on the International Temperature Scale,
        the value of :math:`c2` used in colorimetry should follow that adopted
        in the current International Temperature Scale (ITS-90)
        (Preston-Thomas, 1990; Mielenz et aI., 1991), namely
        :math:`c2=1,4388x10.2\ m/K`.
    n : float, optional
        Medium index of refraction. For dry air at 15°C and 101 325 Pa,
        containing 0,03 percent by volume of carbon dioxide, it is
        approximately 1,00028 throughout the visible region although
        CIE 15:2004 recommends using :math:`n=1`.

    Returns
    -------
    float
        Radiance in *watts per steradian per square metre*.

    Examples
    --------
    >>> colour.planck_law(500 * 1e-9, 5500)
    20472701909806.58
    """

    t = temperature
    l = wavelength

    try:
        with warnings.catch_warnings():
            warnings.simplefilter('error')
            return (((c1 * n ** -2 * l ** -5) / math.pi) *
                    (math.exp(c2 / (n * l * t)) - 1) ** -1)
    except (OverflowError, RuntimeWarning) as error:
        return 0.0


blackbody_spectral_radiance = planck_law


def blackbody_spectral_power_distribution(temperature,
                                          start=None,
                                          end=None,
                                          steps=None,
                                          c1=C1,
                                          c2=C2,
                                          n=N):
    """
    Returns the spectral power distribution of the planckian radiator for given
    temperature :math:`T[K]`.

    Parameters
    ----------
    temperature : float
        Temperature :math:`T[K]` in kelvin degrees.
    start : float
        Wavelengths range start in nm.
    end : float
        Wavelengths range end in nm.
    steps : float
        Wavelengths range steps.
    c1 : float, optional
        The official value of :math:`c1` is provided by the Committee on Data
        for Science and Technology (CODATA), and is
        :math:`c1=3,741771x10.16\ W/m_2` (Mohr and Taylor, 2000).
    c2 : float, optional
        Since :math:`T` is measured on the International Temperature Scale,
        the value of :math:`c2` used in colorimetry should follow that adopted
        in the current International Temperature Scale (ITS-90)
        (Preston-Thomas, 1990; Mielenz et aI., 1991), namely
        :math:`c2=1,4388x10.2\ m/K`.
    n : float, optional
        Medium index of refraction. For dry air at 15°C and 101 325 Pa,
        containing 0,03 percent by volume of carbon dioxide, it is
        approximately 1,00028 throughout the visible region although
        CIE 15:2004 recommends using :math:`n=1`.

    Returns
    ----------
    SpectralPowerDistribution
        Blackbody spectral power distribution.

    Examples
    --------
    >>> cmfs = colour.STANDARD_OBSERVERS_CMFS.get('CIE 1931 2 Degree Standard Observer')
    >>> colour.blackbody_spectral_power_distribution(5000, *cmfs.shape)
    <colour.colorimetry.spectrum.SpectralPowerDistribution at 0x10616fe90>
    """

    return SpectralPowerDistribution(
        name='{0}K Blackbody'.format(temperature),
        data=dict((wavelength,
                   blackbody_spectral_radiance(
                       wavelength * 1e-9,
                       temperature,
                       c1, c2,
                       n))
                  for wavelength in np.arange(start, end + steps, steps)))