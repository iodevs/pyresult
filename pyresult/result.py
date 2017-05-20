# -*- coding: utf-8 -*-
# pylint: disable=too-few-public-methods
'''Result pattern implementation'''

import six



class ResultError(Exception):
    '''Result error'''
    pass


class Result(object):
    '''Base result class'''
    pass


@six.python_2_unicode_compatible
class Ok(Result):
    '''Represents the correct result'''
    def __init__(self, val):
        self.__val = val

    def __str__(self):
        return unicode('Ok: {0}'.format(self.val), 'utf-8')

    @property
    def val(self):
        '''Value can be only readed'''
        return self.__val


@six.python_2_unicode_compatible
class Error(Result):
    '''Represents the wrong result'''
    def __init__(self, msg):
        self.__message = msg

    def __str__(self):
        return u'Error: {0}'.format(
            self.message
            if isinstance(self.message, six.text_type)
            else unicode(self.message, 'utf-8')
        )

    @property
    def message(self):
        '''Messeage can be only readed'''
        return self.__message


def ok(val):  # pylint: disable=invalid-name
    '''Create Ok result'''
    return Ok(val)


def error(msg):
    '''Create error result'''
    return Error(msg)


def result(res):
    '''Check value is result'''
    if not isinstance(res, Result):
        raise ResultError(u'Error: Value \'{0}\' isn\'t result instance.'.format(res))
    return res


def is_ok(res):
    '''Check result is Ok'''
    return isinstance(result(res), Ok)


def is_error(res):
    '''Check result is Error'''
    return isinstance(result(res), Error)


def value(res):
    '''Return stored value in Result'''
    if is_error(res):
        raise ResultError(res.message)
    return res.val


