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
    rmap,
    and_then,
    and_else,
    resolve,
)

__author__ = """Jindrich Kralevic Smitka"""
__email__ = 'smitka.j@gmail.com'
__version__ = '0.2.0'
