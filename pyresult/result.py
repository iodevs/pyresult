# -*- coding: utf-8 -*-
# pylint: disable=too-few-public-methods
'''Result pattern implementation'''

import six



class ResultError(Exception):
    '''Result error'''
    pass


def ok(val):  # pylint: disable=invalid-name
    '''Create Ok result'''
    return ('Ok', val)


def error(msg):
    '''Create error result'''
    return ('Error', msg)



def result(res):
    '''Check value is result'''
    if not isinstance(res, tuple) or len(res) != 2:
        raise ResultError(u'Error: Value \'{0}\' isn\'t 2-tuple.'.format(res))
    if res[0] != 'Ok' and res[0] != 'Error':
        raise ResultError(
            u'Error: Value \'{0}\' isn\'t \'Ok\' or \'Error\'.'.format(res)
        )
    return res


def is_ok(res):
    '''Check result is Ok'''
    return True if result(res)[0] == 'Ok' else False


def is_error(res):
    '''Check result is Error'''
    return True if result(res)[0] == 'Error' else False


def value(res):
    '''Return stored value in Result'''
    if is_error(res):
        raise ResultError(res[1])
    return res[1]


