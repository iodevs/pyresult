# -*- coding: utf-8 -*-
'''Result operators'''

from toolz import curry

from pyresult.result import error, is_error, ok, is_ok, result, value


@curry
def errmap(func, res):
    '''Transform error with `func`.

    errmap: (x -> y) -> Result a x -> Result a y
    '''
    return error(func(res.message)) if is_error(res) else res


@curry
def rmap(func, res):
    '''Map `func` to result `res`

    rmap: (a -> value) -> Result a -> Result value
    '''
    return ok(func(res.val)) if is_ok(res) else res


@curry
def rmapn(func, results):
    '''Map `func` to `results`

    rmapn: (*args -> value) -> List Result a -> Result value
    '''
    args = []
    errors = []
    for res in results:
        if is_ok(res):
            args.append(value(res))
        else:
            errors.append(res.message)

    if errors:
        return error(u'\n'.join(errors))

    return ok(func(*args))


@curry
def and_then(func, res):
    '''Chain together a sequence of computations that may fail.

    and_then: (a -> Result b x) -> Result a x -> Result b x
    '''
    return func(res.val) if is_ok(res) else res


@curry
def and_else(func, res):
    '''When `res` is error, then call `func` with it

    and_else: (x -> Result b x) -> Result a x -> Result a x
    '''
    return func(res.message) if is_error(res) else res


def resolve(res):
    '''Flatten nested results

    resolve: Result (Result a x) x -> Result a x
    '''
    return res if is_error(res) else result(res.val)
