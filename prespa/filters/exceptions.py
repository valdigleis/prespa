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

class ModeNotDefine(Exception):
    """The mode not is define."""

    pass