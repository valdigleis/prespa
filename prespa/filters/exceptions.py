#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Exception classes used by filters."""

class ImageErrors(Exception):
    """The base class for filter errors."""

    pass


class NotSquareImage(ImageErrors):
    """The image not have NxN dimension"""

    pass

class DimensionNotIsPowerTwo(ImageErrors):
    """"The dimension n not is power two"""

    pass

class DepthType(ImageErrors):
    """The depth not is an int value"""

    pass

class DepthInconsistent(ImageErrors):
    """The filtering depth was greater than the image dimension base."""

    pass

class DepthNegative(ImageErrors):
    """The filtering depth was greater than the height of the automaton tree"""

    pass