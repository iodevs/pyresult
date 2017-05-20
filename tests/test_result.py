#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pyresult
----------------------------------

Tests for `pyresult` module.
"""

import pytest


from pyresult.result import ResultError, ok, error, result, is_ok, is_error, value


def test_ok_returns_tuple():

    text = 'Hello World'

    rv = ok(text)

    assert rv == ('Ok', text)


def test_error_returns_tuple():

    msg = 'Error msg here!'

    rv = error(msg)

    assert rv == ('Error', msg)


def test_result_ok_tuple():
    with pytest.raises(ResultError):
        result(['Ok', 'Hello World'])


def test_result_ok_2tuple():
    with pytest.raises(ResultError):
        result(('Ok'))


def test_result_error_tuple():
    with pytest.raises(ResultError):
        result(['Error', 'Hello World'])


def test_result_error_2tuple():
    with pytest.raises(ResultError):
        result(('Error'))


def test_result_isnt_ok_either_error():
    with pytest.raises(ResultError):
        result(('', 'Nothing.'))


def test_is_ok_true():

    rv = ('Ok', 'value')

    assert is_ok(rv) == True


def test_is_ok_false():

    rv = ('Error', 'value')

    assert is_ok(rv) == False


def test_is_error_true():

    rv = ('Error', 'msg')

    assert is_error(rv) == True


def test_is_error_false():

    rv = ('Ok', 'msg')

    assert is_error(rv) == False


def test_value_return_ok_val():

    rv = ('Ok', 'val')

    assert value(rv) == 'val'


def test_value_return_error_val():
    with pytest.raises(ResultError):
        value(('Error', 'msg'))

        