# -*- coding: utf-8 -*-
'''Result pattern implementation'''


OK = 'Ok'
ERROR = 'Error'

STATUS_IDX = 0
VALUE_IDX = 1


class ResultError(Exception):
    '''Result error'''
    pass


def ok(val):  # pylint: disable=invalid-name
    '''Create Ok result'''
    return (OK, val)


def error(msg):
    '''Create error result'''
    return (ERROR, msg)


def result(res):
    '''Check value is result'''
    if not isinstance(res, tuple) or len(res) != 2:
        raise ResultError(u'Error: Value \'{0}\' isn\'t 2-tuple.'.format(res))
    if res[STATUS_IDX] != OK and res[STATUS_IDX] != ERROR:
        raise ResultError(
            u'Error: Value \'{0}\' isn\'t \'Ok\' or \'Error\'.'.format(res)
        )
    return res


def is_ok(res):
    '''Check result is Ok'''
    return result(res)[STATUS_IDX] == OK


def is_error(res):
    '''Check result is Error'''
    return result(res)[STATUS_IDX] == ERROR


def value(res):
    '''Return stored value in Result'''
    if is_error(res):
        raise ResultError(res[VALUE_IDX])
    return res[VALUE_IDX]
