"""
RIMM, ROMM and ERIMM Encodings
==============================

Defines the *RIMM, ROMM and ERIMM* encodings opto-electrical transfer functions
(OETF) and electro-optical transfer functions (EOTF):

-   :func:`colour.models.cctf_encoding_ROMMRGB`
-   :func:`colour.models.cctf_decoding_ROMMRGB`
-   :func:`colour.models.cctf_encoding_ProPhotoRGB`
-   :func:`colour.models.cctf_decoding_ProPhotoRGB`
-   :func:`colour.models.cctf_encoding_RIMMRGB`
-   :func:`colour.models.cctf_decoding_RIMMRGB`
-   :func:`colour.models.log_encoding_ERIMMRGB`
-   :func:`colour.models.log_decoding_ERIMMRGB`

References
----------
-   :cite:`ANSI2003a` : ANSI. (2003). Specification of ROMM RGB (pp. 1-2).
    http://www.color.org/ROMMRGB.pdf
-   :cite:`Spaulding2000b` : Spaulding, K. E., Woolfe, G. J., & Giorgianni, E.
    J. (2000). Reference Input/Output Medium Metric RGB Color Encodings
    (RIMM/ROMM RGB) (pp. 1-8). http://www.photo-lovers.org/pdf/color/romm.pdf
"""

from __future__ import annotations

import numpy as np

from colour.algebra import spow
from colour.hints import ArrayLike, NDArrayFloat, NDArrayReal, Union
from colour.utilities import (
    as_float,
    as_float_scalar,
    as_int,
    copy_definition,
    domain_range_scale,
    from_range_1,
    to_domain_1,
)

__author__ = "Colour Developers"
__copyright__ = "Copyright 2013 Colour Developers"
__license__ = "New BSD License - https://opensource.org/licenses/BSD-3-Clause"
__maintainer__ = "Colour Developers"
__email__ = "colour-developers@colour-science.org"
__status__ = "Production"

__all__ = [
    "cctf_encoding_ROMMRGB",
    "cctf_decoding_ROMMRGB",
    "cctf_encoding_ProPhotoRGB",
    "cctf_decoding_ProPhotoRGB",
    "cctf_encoding_RIMMRGB",
    "cctf_decoding_RIMMRGB",
    "log_encoding_ERIMMRGB",
    "log_decoding_ERIMMRGB",
]


def cctf_encoding_ROMMRGB(
    X: ArrayLike, bit_depth: int = 8, out_int: bool = False
) -> NDArrayReal:
    """
    Define the *ROMM RGB* encoding colour component transfer function
    (Encoding CCTF).

    Parameters
    ----------
    X
        Linear data :math:`X_{ROMM}`.
    bit_depth
        Bit depth used for conversion.
    out_int
        Whether to return value as int code value or float equivalent of a
        code value at a given bit depth.

    Returns
    -------
    :class:`numpy.ndarray`
        Non-linear data :math:`X'_{ROMM}`.

    Notes
    -----
    +----------------+-----------------------+---------------+
    | **Domain \\***  | **Scale - Reference** | **Scale - 1** |
    +================+=======================+===============+
    | ``X``          | [0, 1]                | [0, 1]        |
    +----------------+-----------------------+---------------+

    +----------------+-----------------------+---------------+
    | **Range \\***   | **Scale - Reference** | **Scale - 1** |
    +================+=======================+===============+
    | ``X_p``        | [0, 1]                | [0, 1]        |
    +----------------+-----------------------+---------------+

    \\* This definition has an output int switch, thus the domain-range
    scale information is only given for the floating point mode.

    References
    ----------
    :cite:`ANSI2003a`, :cite:`Spaulding2000b`

    Examples
    --------
    >>> cctf_encoding_ROMMRGB(0.18)  # doctest: +ELLIPSIS
    0.3857114...
    >>> cctf_encoding_ROMMRGB(0.18, out_int=True)
    98
    """

    X = to_domain_1(X)

    I_max = 2**bit_depth - 1

    E_t = 16 ** (1.8 / (1 - 1.8))

    X_p = np.where(X < E_t, X * 16 * I_max, spow(X, 1 / 1.8) * I_max)

    if out_int:
        return as_int(np.round(X_p))
    else:
        return as_float(from_range_1(X_p / I_max))


def cctf_decoding_ROMMRGB(
    X_p: Union[ArrayLike, ArrayLike],
    bit_depth: int = 8,
    in_int: bool = False,
) -> NDArrayFloat:
    """
    Define the *ROMM RGB* decoding colour component transfer function
    (Encoding CCTF).

    Parameters
    ----------
    X_p
        Non-linear data :math:`X'_{ROMM}`.
    bit_depth
        Bit depth used for conversion.
    in_int
        Whether to treat the input value as int code value or float
        equivalent of a code value at a given bit depth.

    Returns
    -------
    :class:`numpy.ndarray`
        Linear data :math:`X_{ROMM}`.

    Notes
    -----
    +----------------+-----------------------+---------------+
    | **Domain \\***  | **Scale - Reference** | **Scale - 1** |
    +================+=======================+===============+
    | ``X_p``        | [0, 1]                | [0, 1]        |
    +----------------+-----------------------+---------------+

    +----------------+-----------------------+---------------+
    | **Range \\***   | **Scale - Reference** | **Scale - 1** |
    +================+=======================+===============+
    | ``X``          | [0, 1]                | [0, 1]        |
    +----------------+-----------------------+---------------+

    \\* This definition has an input int switch, thus the domain-range
    scale information is only given for the floating point mode.

    References
    ----------
    :cite:`ANSI2003a`, :cite:`Spaulding2000b`

    Examples
    --------
    >>> cctf_decoding_ROMMRGB(0.385711424751138)  # doctest: +ELLIPSIS
    0.1...
    >>> cctf_decoding_ROMMRGB(98, in_int=True)  # doctest: +ELLIPSIS
    0.1...
    """

    X_p = to_domain_1(X_p)

    I_max = 2**bit_depth - 1

    if not in_int:
        X_p = X_p * I_max

    E_t = 16 ** (1.8 / (1 - 1.8))

    X = np.where(
        X_p < 16 * E_t * I_max,
        X_p / (16 * I_max),
        spow(X_p / I_max, 1.8),
    )

    return as_float(from_range_1(X))


cctf_encoding_ProPhotoRGB = copy_definition(
    cctf_encoding_ROMMRGB, "cctf_encoding_ProPhotoRGB"
)
# If-clause required for optimised python launch.
if cctf_encoding_ProPhotoRGB.__doc__ is not None:
    cctf_encoding_ProPhotoRGB.__doc__ = (
        cctf_encoding_ProPhotoRGB.__doc__.replace(
            "*ROMM RGB*", "*ProPhoto RGB*"
        )
    )
cctf_decoding_ProPhotoRGB = copy_definition(
    cctf_decoding_ROMMRGB, "cctf_decoding_ProPhotoRGB"
)
# If-clause required for optimised python launch.
if cctf_decoding_ProPhotoRGB.__doc__ is not None:
    cctf_decoding_ProPhotoRGB.__doc__ = (
        cctf_decoding_ProPhotoRGB.__doc__.replace(
            "*ROMM RGB*", "*ProPhoto RGB*"
        )
    )


def cctf_encoding_RIMMRGB(
    X: ArrayLike,
    bit_depth: int = 8,
    out_int: bool = False,
    E_clip: float = 2.0,
) -> NDArrayReal:
    """
    Define the *RIMM RGB* encoding colour component transfer function
    (Encoding CCTF).

    *RIMM RGB* encoding non-linearity is based on that specified by
    *Recommendation ITU-R BT.709-6*.

    Parameters
    ----------
    X
        Linear data :math:`X_{RIMM}`.
    bit_depth
        Bit depth used for conversion.
    out_int
        Whether to return value as int code value or float equivalent of a
        code value at a given bit depth.
    E_clip
        Maximum exposure level.

    Returns
    -------
    :class:`numpy.ndarray`
        Non-linear data :math:`X'_{RIMM}`.

    Notes
    -----
    +----------------+-----------------------+---------------+
    | **Domain \\***  | **Scale - Reference** | **Scale - 1** |
    +================+=======================+===============+
    | ``X``          | [0, 1]                | [0, 1]        |
    +----------------+-----------------------+---------------+

    +----------------+-----------------------+---------------+
    | **Range \\***   | **Scale - Reference** | **Scale - 1** |
    +================+=======================+===============+
    | ``X_p``        | [0, 1]                | [0, 1]        |
    +----------------+-----------------------+---------------+

    \\* This definition has an output int switch, thus the domain-range
    scale information is only given for the floating point mode.

    References
    ----------
    :cite:`Spaulding2000b`

    Examples
    --------
    >>> cctf_encoding_RIMMRGB(0.18)  # doctest: +ELLIPSIS
    0.2916737...
    >>> cctf_encoding_RIMMRGB(0.18, out_int=True)
    74
    """

    X = to_domain_1(X)

    I_max = 2**bit_depth - 1

    V_clip = 1.099 * spow(E_clip, 0.45) - 0.099
    q = I_max / V_clip

    X_p = q * np.select(
        [X < 0.0, X < 0.018, X >= 0.018, X > E_clip],
        [0, 4.5 * X, 1.099 * spow(X, 0.45) - 0.099, I_max],
    )

    if out_int:
        return as_int(np.round(X_p))
    else:
        return as_float(from_range_1(X_p / I_max))


def cctf_decoding_RIMMRGB(
    X_p: Union[ArrayLike, ArrayLike],
    bit_depth: int = 8,
    in_int: bool = False,
    E_clip: float = 2.0,
) -> NDArrayFloat:
    """
    Define the *RIMM RGB* decoding colour component transfer function
    (Encoding CCTF).

    Parameters
    ----------
    X_p
        Non-linear data :math:`X'_{RIMM}`.
    bit_depth
        Bit depth used for conversion.
    in_int
        Whether to treat the input value as int code value or float
        equivalent of a code value at a given bit depth.
    E_clip
        Maximum exposure level.

    Returns
    -------
    :class:`numpy.ndarray`
        Linear data :math:`X_{RIMM}`.

    Notes
    -----
    +----------------+-----------------------+---------------+
    | **Domain \\***  | **Scale - Reference** | **Scale - 1** |
    +================+=======================+===============+
    | ``X_p``        | [0, 1]                | [0, 1]        |
    +----------------+-----------------------+---------------+

    +----------------+-----------------------+---------------+
    | **Range \\***   | **Scale - Reference** | **Scale - 1** |
    +================+=======================+===============+
    | ``X``          | [0, 1]                | [0, 1]        |
    +----------------+-----------------------+---------------+

    \\* This definition has an input int switch, thus the domain-range
    scale information is only given for the floating point mode.

    References
    ----------
    :cite:`Spaulding2000b`

    Examples
    --------
    >>> cctf_decoding_RIMMRGB(0.291673732475746)  # doctest: +ELLIPSIS
    0.1...
    >>> cctf_decoding_RIMMRGB(74, in_int=True)  # doctest: +ELLIPSIS
    0.1...
    """

    X_p = to_domain_1(X_p)

    I_max = as_float_scalar(2**bit_depth - 1)

    if not in_int:
        X_p = X_p * I_max

    V_clip = 1.099 * spow(E_clip, 0.45) - 0.099

    m = V_clip * X_p / I_max

    with domain_range_scale("ignore"):
        X = np.where(
            X_p / I_max
            < cctf_encoding_RIMMRGB(0.018, bit_depth, E_clip=E_clip),
            m / 4.5,
            spow((m + 0.099) / 1.099, 1 / 0.45),
        )

    return as_float(from_range_1(X))


def log_encoding_ERIMMRGB(
    X: ArrayLike,
    bit_depth: int = 8,
    out_int: bool = False,
    E_min: float = 0.001,
    E_clip: float = 316.2,
) -> NDArrayReal:
    """
    Define the *ERIMM RGB* log encoding curve / opto-electronic transfer
    function (OETF).

    Parameters
    ----------
    X
        Linear data :math:`X_{ERIMM}`.
    bit_depth
        Bit depth used for conversion.
    out_int
        Whether to return value as int code value or float equivalent of a
        code value at a given bit depth.
    E_min
        Minimum exposure limit.
    E_clip
        Maximum exposure limit.

    Returns
    -------
    :class:`numpy.ndarray`
        Non-linear data :math:`X'_{ERIMM}`.

    Notes
    -----
    +----------------+-----------------------+---------------+
    | **Domain \\***  | **Scale - Reference** | **Scale - 1** |
    +================+=======================+===============+
    | ``X``          | [0, 1]                | [0, 1]        |
    +----------------+-----------------------+---------------+

    +----------------+-----------------------+---------------+
    | **Range \\***   | **Scale - Reference** | **Scale - 1** |
    +================+=======================+===============+
    | ``X_p``        | [0, 1]                | [0, 1]        |
    +----------------+-----------------------+---------------+

    \\* This definition has an output int switch, thus the domain-range
    scale information is only given for the floating point mode.

    References
    ----------
    :cite:`Spaulding2000b`

    Examples
    --------
    >>> log_encoding_ERIMMRGB(0.18)  # doctest: +ELLIPSIS
    0.4100523...
    >>> log_encoding_ERIMMRGB(0.18, out_int=True)
    105
    """

    X = to_domain_1(X)

    I_max = 2**bit_depth - 1

    E_t = np.exp(1) * E_min

    l_E_t = np.log(E_t)
    l_E_min = np.log(E_min)
    l_E_clip = np.log(E_clip)
    X_p = np.select(
        [
            X < 0.0,
            X <= E_t,
            X > E_t,
            X > E_clip,
        ],
        [
            0,
            I_max * ((l_E_t - l_E_min) / (l_E_clip - l_E_min)) * X / E_t,
            I_max * ((np.log(X) - l_E_min) / (l_E_clip - l_E_min)),
            I_max,
        ],
    )

    if out_int:
        return as_int(np.round(X_p))
    else:
        return as_float(from_range_1(X_p / I_max))


def log_decoding_ERIMMRGB(
    X_p: Union[ArrayLike, ArrayLike],
    bit_depth: int = 8,
    in_int: bool = False,
    E_min: float = 0.001,
    E_clip: float = 316.2,
) -> NDArrayFloat:
    """
    Define the *ERIMM RGB* log decoding curve / electro-optical transfer
    function (EOTF).

    Parameters
    ----------
    X_p
        Non-linear data :math:`X'_{ERIMM}`.
    bit_depth
        Bit depth used for conversion.
    in_int
        Whether to treat the input value as int code value or float
        equivalent of a code value at a given bit depth.
    E_min
        Minimum exposure limit.
    E_clip
        Maximum exposure limit.

    Returns
    -------
    :class:`numpy.ndarray`
        Linear data :math:`X_{ERIMM}`.

    Notes
    -----
    +----------------+-----------------------+---------------+
    | **Domain \\***  | **Scale - Reference** | **Scale - 1** |
    +================+=======================+===============+
    | ``X_p``        | [0, 1]                | [0, 1]        |
    +----------------+-----------------------+---------------+

    +----------------+-----------------------+---------------+
    | **Range \\***   | **Scale - Reference** | **Scale - 1** |
    +================+=======================+===============+
    | ``X``          | [0, 1]                | [0, 1]        |
    +----------------+-----------------------+---------------+

    \\* This definition has an input int switch, thus the domain-range
    scale information is only given for the floating point mode.

    References
    ----------
    :cite:`Spaulding2000b`

    Examples
    --------
    >>> log_decoding_ERIMMRGB(0.410052389492129)  # doctest: +ELLIPSIS
    0.1...
    >>> log_decoding_ERIMMRGB(105, in_int=True)  # doctest: +ELLIPSIS
    0.1...
    """

    X_p = to_domain_1(X_p)

    I_max = 2**bit_depth - 1

    if not in_int:
        X_p = X_p * I_max

    E_t = np.exp(1) * E_min

    l_E_t = np.log(E_t)
    l_E_min = np.log(E_min)
    l_E_clip = np.log(E_clip)
    X = np.where(
        X_p <= I_max * ((l_E_t - l_E_min) / (l_E_clip - l_E_min)),
        ((l_E_clip - l_E_min) / (l_E_t - l_E_min)) * ((X_p * E_t) / I_max),
        np.exp((X_p / I_max) * (l_E_clip - l_E_min) + l_E_min),
    )

    return as_float(from_range_1(X))
