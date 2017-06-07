# -*- coding: utf-8 -*-
'''A result pattern for python'''

from pyresult.result import (  # noqa
    ok,
    error,
    result,
    is_ok,
    is_error,
    value
)
from pyresult.operators import (  # noqa
    errmap,
    fold,
    rmap,
    and_then,
    and_else,
    resolve,
    do,
)

__author__ = """Jindrich Kralevic Smitka"""
__email__ = 'smitka.j@gmail.com'
__version__ = '0.5.0'
