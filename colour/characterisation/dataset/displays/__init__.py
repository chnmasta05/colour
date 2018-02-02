#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from .crt import CRT_DISPLAYS_RGB_PRIMARIES
from .lcd import LCD_DISPLAYS_RGB_PRIMARIES
from colour.utilities import CaseInsensitiveMapping

DISPLAYS_RGB_PRIMARIES = CaseInsensitiveMapping(CRT_DISPLAYS_RGB_PRIMARIES)
DISPLAYS_RGB_PRIMARIES.update(LCD_DISPLAYS_RGB_PRIMARIES)
DISPLAYS_RGB_PRIMARIES.__doc__ = """
Displays *RGB* primaries multi-spectral power distributions.

DISPLAYS_RGB_PRIMARIES : CaseInsensitiveMapping
    **{Apple Studio Display, Typical CRT Brainard 1997}**
"""

__all__ = ['DISPLAYS_RGB_PRIMARIES']
