#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring

"""
test_pyresult
----------------------------------

Tests for `pyresult` module.
"""

import pytest

from toolz import identity

from pyresult.result import OK, ERROR, ResultError
from pyresult import (
    ok,
    error,
    result,
    is_ok,
    is_error,
    value,
    get,
    from_try_except
)


def test_ok_returns_tuple():
    text = 'Hello World'

    rv = ok(text)

    assert rv == (OK, text)


def test_error_returns_tuple():
    msg = 'Error msg here!'

    rv = error(msg)

    assert rv == (ERROR, msg)


def test_result_ok_tuple():
    with pytest.raises(ResultError):
        result([OK, 'Hello World'])


def test_result_ok_2tuple():
    with pytest.raises(ResultError):
        result((OK,))


def test_result_error_tuple():
    with pytest.raises(ResultError):
        result([ERROR, 'Hello World'])


def test_result_error_2tuple():
    with pytest.raises(ResultError):
        result((ERROR,))


def test_result_isnt_ok_either_error():
    with pytest.raises(ResultError):
        result(('', 'Nothing.'))


def test_is_ok_true():

    rv = (OK, 'value')

    assert is_ok(rv) is True


def test_is_ok_false():

    rv = (ERROR, 'value')

    assert is_ok(rv) is False


def test_is_error_true():

    rv = (ERROR, 'msg')

    assert is_error(rv) is True


def test_is_error_false():

    rv = (OK, 'msg')

    assert is_error(rv) is False


def test_create_result_from_value():
    res = from_try_except(lambda x: x, 1111)

    assert is_ok(res)
    assert res.value == 1111


def test_create_result_from_excpetion():
    def throw():
        raise Exception('ERROR')

    res = from_try_except(throw)

    assert is_error(res)
    assert str(res.value) == 'ERROR'


def test_value_return_ok_val():

    rv = (OK, 'val')

    assert value(rv) == 'val'


def test_value_return_error_val():
    with pytest.raises(ResultError):
        value((ERROR, 'msg'))


def test_get_return_ok_value():
    res = ok('OK')

    assert get(identity, identity, res) == 'OK'


def test_get_return_error_value():
    res = error('ERROR')

    assert get(identity, identity, res) == 'ERROR'
