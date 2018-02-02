# -*- coding: utf-8 -*-
'''A result pattern for python'''

from pyresult.result import (  # noqa
    ok,
    error,
    result,
    is_ok,
    is_error,
    value,
    get,
    from_try_except,
    from_maybe,
)
from pyresult.operators import (  # noqa
    errmap,
    fold,
    rmap,
    and_then,
    and_else,
    resolve,
    do,
    with_default,
)

__author__ = """Jindrich Kralevic Smitka"""
__email__ = 'smitka.j@gmail.com'
__version__ = '1.1.0'
