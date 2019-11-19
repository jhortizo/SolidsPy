# -*- coding: utf-8 -*-
"""
Numeric integration routines
----------------------------
Weights and coordinates for Gauss-Legendre quadrature [WGAUSS]_. The
values for triangles is presented in section 5.5 of Bathe book [BATHE]_.

References
----------
.. [WGAUSS] Wikipedia contributors. "Gaussian quadrature." Wikipedia,
   The Free Encyclopedia, 2 Nov.  2015. Web. 25 Dec. 2015.
   url: https://en.wikipedia.org/wiki/Gaussian_quadrature
.. [BATHE] Bathe, Klaus-Jürgen. Finite element procedures. Prentice Hall,
   Pearson Education, 2006.
"""
from __future__ import absolute_import, division, print_function
from itertools import product
import numpy as np


#%% General
def gauss_1d(npts):
    """Return Gauss points and weights for Gauss quadrature in 1D

    Parameters
    ----------
    npts : int
      Number of quadrature points.

    Returns
    -------
    wts : ndarray
      Weights for the Gauss-Legendre quadrature.
    pts : ndarray
      Points for the Gauss-Legendre quadrature.
    """
    if npts == 2:
        pts = [-0.577350269189625764, 0.577350269189625764]
        wts = [1.00000000000000000, 1.00000000000000000]
    elif npts == 3:
        pts = [-0.774596669241483377, 0, 0.774596669241483377]
        wts = [0.555555555555555556, 0.888888888888888889,
               0.555555555555555556]
    elif npts == 4:
        pts = [-0.861136311594052575, -0.339981043584856265,
               0.339981043584856265, 0.861136311594052575]
        wts = [0.347854845137453857, 0.652145154862546143,
               0.652145154862546143, 0.347854845137453857]
    elif npts == 5:
        pts = [-0.906179845938663993, -0.538469310105683091, 0,
               0.538469310105683091, 0.906179845938663993]
        wts = [0.236926885056189088, 0.478628670499366468,
               0.568888888888888889, 0.478628670499366468,
               0.236926885056189088]
    elif npts == 6:
        pts = [-0.932469514203152028, -0.661209386466264514,
               -0.238619186083196909, 0.238619186083196909,
               0.661209386466264514, 0.932469514203152028]
        wts = [0.171324492379170345, 0.360761573048138608,
               0.467913934572691047, 0.467913934572691047,
               0.360761573048138608, 0.171324492379170345]
    elif npts == 7:
        pts = [-0.949107912342758525, -0.741531185599394440,
               -0.405845151377397167, 0, 0.405845151377397167,
               0.741531185599394440, 0.949107912342758525]
        wts = [0.129484966168869693, 0.279705391489276668,
               0.381830050505118945, 0.417959183673469388,
               0.381830050505118945, 0.279705391489276668,
               0.129484966168869693]
    elif npts == 8:
        pts = [-0.960289856497536232, -0.796666477413626740,
               -0.525532409916328986, -0.183434642495649805,
               0.183434642495649805, 0.525532409916328986,
               0.796666477413626740, 0.960289856497536232]
        wts = [0.101228536290376259, 0.222381034453374471,
               0.313706645877887287, 0.362683783378361983,
               0.362683783378361983, 0.313706645877887287,
               0.222381034453374471, 0.101228536290376259]
    elif npts == 9:
        pts = [-0.968160239507626090, -0.836031107326635794,
               -0.613371432700590397, -0.324253423403808929, 0,
               0.324253423403808929, 0.613371432700590397,
               0.836031107326635794, 0.968160239507626090]
        wts = [0.0812743883615744120, 0.180648160694857404,
               0.260610696402935462, 0.312347077040002840,
               0.330239355001259763, 0.312347077040002840,
               0.260610696402935462, 0.180648160694857404,
               0.0812743883615744120]
    elif npts == 10:
        pts = [-0.973906528517171720, -0.865063366688984511,
               -0.679409568299024406, -0.433395394129247191,
               -0.148874338981631211, 0.148874338981631211,
               0.433395394129247191, 0.679409568299024406,
               0.865063366688984511, 0.973906528517171720]
        wts = [0.0666713443086881376, 0.149451349150580593,
               0.219086362515982044, 0.269266719309996355,
               0.295524224714752870, 0.295524224714752870,
               0.269266719309996355, 0.219086362515982044,
               0.149451349150580593, 0.0666713443086881376]
    else:
        msg = "The number of points should be in [2, 10]"
        raise ValueError(msg)

    return pts, wts


def gauss_nd(npts, ndim=2):
    """
    Return Gauss points and weights for Gauss quadrature in
    an ND hypercube.

    Parameters
    ----------
    npts : int
      Number of quadrature points.

    Returns
    -------
    nd_wts : ndarray
      Weights for the Gauss-Legendre quadrature.
    nd_pts : ndarray
      Points for the Gauss-Legendre quadrature.
    """
    pts, wts = gauss_1d(npts)
    nd_pts = np.array(list(product(pts, repeat=ndim)))
    nd_wts = product(wts, repeat=ndim)
    nd_wts = [np.prod(nd_wt) for nd_wt in nd_wts]
    return nd_pts, nd_wts


def gauss_tri(order=2):
    """
    Gauss points and weights for a triangle up to order 7

    Returns
    -------
    pts : ndarray
      Points for the Gauss-Legendre quadrature.
    wts : ndarray
      Weights for the Gauss-Legendre quadrature.

    References
    ----------
    .. [BATHE] Bathe, Klaus-Jürgen. Finite element procedures. Prentice Hall,
       Pearson Education, 2006.

    """
    if order == 1:
        pts = np.array([[0.3333333333333, 0.3333333333333]])
        wts = np.array([1.0])
    elif order == 2:
        pts = np.array([
            [0.1666666666667, 0.1666666666667],
            [0.6666666666667, 0.1666666666667],
            [0.1666666666667, 0.6666666666667]])
        wts = np.full([3], 0.333333333333)
    elif order in [3, 4, 5]:
        pts = np.array([
            [0.1012865073235, 0.1012865073235],
            [0.7974269853531, 0.1012865073235],
            [0.1012865073235, 0.7974269853531],
            [0.4701420641051, 0.0597158717898],
            [0.4701420641051, 0.4701420641051],
            [0.0597158717898, 0.4701420641051],
            [0.3333333333333, 0.3333333333333]])
        wts = np.array([
            0.1259391805448, 0.1259391805448, 0.1259391805448,
            0.1323941527885, 0.1323941527885, 0.1323941527885,
            0.225])
    elif order in [6, 7]:
        pts = np.array([
            [0.0651301029022, 0.0651301029022],
            [0.8697397941956, 0.0651301029022],
            [0.0651301029022, 0.8697397941956],
            [0.3128654960049, 0.0486903154253],
            [0.6384441885698, 0.3128654960049],
            [0.0486903154253, 0.6384441885698],
            [0.6384441885698, 0.0486903154253],
            [0.3128654960049, 0.6384441885698],
            [0.0486903154253, 0.3128654960049],
            [0.2603459660790, 0.2603459660790],
            [0.4793080678413, 0.2603459660790],
            [0.2603459660790, 0.4793080678413],
            [0.3333333333333, 0.3333333333333]])
        wts = np.array([
            0.0533472356088, 0.0533472356088, 0.0533472356088,
            0.0771137608903, 0.0771137608903, 0.0771137608903,
            0.0771137608903, 0.0771137608903, 0.0771137608903,
            0.1756152574332, 0.1756152574332, 0.1756152574332,
            -0.1495700444677])
    else:
        msg = "The order should be in [1, 7]"
        raise ValueError(msg)
    return pts, wts


#%% Fixed grids (old)
def gpoints2x2():
    """Gauss points for a 2 by 2 grid

    Returns
    -------
    wts : ndarray
      Weights for the Gauss-Legendre quadrature.
    pts : ndarray
      Points for the Gauss-Legendre quadrature.

    """
    wts = np.ones([4])
    pts = np.zeros([4, 2])
    pts[0, 0] = -0.577350269189626
    pts[1, 0] = 0.577350269189626
    pts[2, 0] = -0.577350269189626
    pts[3, 0] = 0.577350269189626

    pts[0, 1] = 0.577350269189626
    pts[1, 1] = 0.577350269189626
    pts[2, 1] = -0.577350269189626
    pts[3, 1] = -0.577350269189626

    return wts, pts


def gpoints7():
    """Gauss points for a triangle (7 points)

    Returns
    -------
    wts : ndarray
      Weights for the Gauss-Legendre quadrature.
    pts : ndarray
      Points for the Gauss-Legendre quadrature.

    """
    wts = np.zeros([7])
    pts = np.zeros([7, 2])
    wts[0] = 0.1259391805448
    wts[1] = 0.1259391805448
    wts[2] = 0.1259391805448
    wts[3] = 0.1323941527885
    wts[4] = 0.1323941527885
    wts[5] = 0.1323941527885
    wts[6] = 0.225

    pts[0, 0] = 0.1012865073235
    pts[1, 0] = 0.7974269853531
    pts[2, 0] = 0.1012865073235
    pts[3, 0] = 0.4701420641051
    pts[4, 0] = 0.4701420641051
    pts[5, 0] = 0.0597158717898
    pts[6, 0] = 0.3333333333333

    pts[0, 1] = 0.1012865073235
    pts[1, 1] = 0.1012865073235
    pts[2, 1] = 0.7974269853531
    pts[3, 1] = 0.0597158717898
    pts[4, 1] = 0.4701420641051
    pts[5, 1] = 0.4701420641051
    pts[6, 1] = 0.3333333333333

    return wts, pts


def gpoints3():
    """Gauss points for a triangle element (3 points)

    Returns
    -------
    wts : ndarray
      Weights for the Gauss-Legendre quadrature.
    pts : ndarray
      Points for the Gauss-Legendre quadrature.

    """
    wts = np.full([3], 0.333333333333)
    pts = np.zeros([3, 2])

    pts[0, 0] = 0.1666666666667
    pts[1, 0] = 0.6666666666667
    pts[2, 0] = 0.1666666666667

    pts[0, 1] = 0.1666666666667
    pts[1, 1] = 0.1666666666667
    pts[2, 1] = 0.6666666666667

    return wts, pts
