# -*- coding: utf-8 -*-
'''Result operators'''

from toolz import curry

from pyresult.result import (
    ok,
    error,
    result,
    is_ok,
    is_error,
)


@curry
def errmap(func, res):
    '''Transform error with `func`.

    errmap: (x -> y) -> Result a x -> Result a y
    '''
    res = result(res)
    return error(func(res.value)) if is_error(res) else res


@curry
def rmap(func, res):
    '''Map `func` to result `res`

    rmap: (a -> value) -> Result a -> Result value
    '''
    res = result(res)
    return ok(func(res.value)) if is_ok(res) else res


@curry
def and_then(func, res):
    '''Chain together a sequence of computations that may fail.

    and_then: (a -> Result b x) -> Result a x -> Result b x
    '''
    res = result(res)
    return result(func(res.value)) if is_ok(res) else res


@curry
def and_else(func, res):
    '''When `res` is error, then call `func` with it

    and_else: (x -> Result b x) -> Result a x -> Result a x
    '''
    res = result(res)
    return result(func(res.value)) if is_error(res) else res


@curry
def fold(res):
    ''' List results is decomposited into list of results values
    and list of result errors.

    fold: (List Result a x) -> Result (List a) (List x)
    '''
    len_res = len(res)
    val = [None] * len_res
    err = [None] * len_res

    for i, item in enumerate(res):
        result_item = result(item)
        if is_ok(result_item):
            val[i] = result_item.value
        else:
            err[i] = result_item.value

    if None in val:
        return error(err)
    else:
        return ok(val)


def resolve(res):
    '''Flatten nested results

    resolve: Result (Result a x) x -> Result a x
    '''
    res = result(res)
    return res if is_error(res) else result(res.value)


@curry
def do(func, res):  # pylint: disable=invalid-name
    '''Run `func` when result `res` is ok
    and then return `res` if function return ok result,
    otherwise return its error result.

    do: (val -> Result x e) -> Result val e -> Result val e
    '''
    res = result(res)

    return and_then(lambda _: res, func(res.value)) if is_ok(res) else res


@curry
def with_default(default_value, res):
    '''Return `default_value` when result is error
    otherwise result value.

    with_default :: a -> Result a x -> a
    '''
    res = result(res)
    return res.value if is_ok(res) else default_value
