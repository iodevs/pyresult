# -*- coding: utf-8 -*-
'''Result pattern implementation'''

import collections

OK = 'Ok'
ERROR = 'Error'

Result = collections.namedtuple('Result', ('status', 'value'))


class ResultError(Exception):
    '''Result error'''
    pass


def ok(val):  # pylint: disable=invalid-name
    '''Create Ok result'''
    return Result(OK, val)


def error(msg):
    '''Create error result'''
    return Result(ERROR, msg)


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
