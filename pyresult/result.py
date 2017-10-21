# -*- coding: utf-8 -*-
'''Result pattern implementation'''

from collections import namedtuple
from toolz import curry


OK = 'Ok'
ERROR = 'Error'


class Result(namedtuple('Result', ('status', 'value'))):
    '''Result'''
    __slots__ = ()

    def __and__(self, other):
        '''Calculate the AND of two results.

        :param other: Result e a
        :returns: Result e a

        >>> from pyresult import ok, error

        >>> ok(1) & ok(2)
        Result(status='Ok', value=[1, 2])

        >>> ok(1) & error(2)
        Result(status='Error', value=[2])

        >>> error(1) & ok(2)
        Result(status='Error', value=[1])

        >>> error(1) & error(2)
        Result(status='Error', value=[1, 2])

        '''
        cond = (is_ok(self), is_ok(other))

        if cond == (True, True):
            return ok([self.value, other.value])
        elif cond == (True, False):
            return error([other.value])
        elif cond == (False, True):
            return error([self.value])
        elif cond == (False, False):  # pragma: no branch
            return error([self.value, other.value])

    def __or__(self, other):
        '''Calculate the OR of two results.

        :param other: Result e a
        :returns: Result e a

        >>> from pyresult import ok, error

        >>> ok(1) | ok(2)
        Result(status='Ok', value=[1, 2])

        >>> ok(1) | error(2)
        Result(status='Ok', value=[1])

        >>> error(1) | ok(2)
        Result(status='Ok', value=[2])

        >>> error(1) | error(2)
        Result(status='Error', value=[1, 2])
        '''
        cond = (is_ok(self), is_ok(other))

        if cond == (True, True):
            return ok([self.value, other.value])
        elif cond == (True, False):
            return ok([self.value])
        elif cond == (False, True):
            return ok([other.value])
        elif cond == (False, False):  # pragma: no branch
            return error([self.value, other.value])


class ResultError(Exception):
    '''Result error'''
    pass


def ok(val):  # pylint: disable=invalid-name
    '''Create Ok result'''
    return Result(OK, val)


def error(msg):
    '''Create error result'''
    return Result(ERROR, msg)


def from_try_except(fun, *args, **kwargs):
    '''Create result from exception.

    from_try_except :: (*args -> **kw -> val) -> List a -> Dict b -> Result e val
    '''
    try:
        return ok(fun(*args, **kwargs))
    except Exception as err:
        return error(err)


def result(res):
    '''Check value is result'''
    if not isinstance(res, tuple) or len(res) != 2:
        raise ResultError(u'Error: Value \'{0!r}\' isn\'t 2-tuple.'.format(res))
    res = Result(*res)
    if res.status != OK and res.status != ERROR:
        raise ResultError(
            u'Error: Value \'{0!r}\' isn\'t \'Ok\' or \'Error\'.'.format(res)
        )
    return res


def is_ok(res):
    '''Check result is Ok'''
    return result(res).status == OK


def is_error(res):
    '''Check result is Error'''
    return result(res).status == ERROR


def value(res):
    '''Return stored value in Result'''
    res = result(res)
    if is_error(res):
        raise ResultError(res.value)
    return res.value


@curry
def get(error_fn, ok_fn, res):
    '''Releasing the value. Apply `ok_fn` to result value and returns result
    or apply `error_fn` to error and returns result.

    get :: (e -> val) -> (a -> val) -> Result e a -> val
    '''
    return ok_fn(res.value) if is_ok(res) else error_fn(res.value)
