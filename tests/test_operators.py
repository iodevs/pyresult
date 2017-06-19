#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring, invalid-name

from pyresult.result import OK, ERROR, ok, error
from pyresult.operators import (
    errmap,
    rmap,
    and_then,
    and_else,
    fold,
    resolve,
    do,
    with_default
)


def test_errmap_is_ok():
    val = (ERROR, 'msg')

    def f(q):
        return q + " hello"

    assert errmap(f, val) == (ERROR, 'msg hello')


def test_errmap_original_res():
    val = (OK, 'val')

    def f(val):
        return val

    assert errmap(f, val) == val


def test_rmap_is_ok():
    val = (OK, 'val')

    def f(val):
        return val

    assert rmap(f, val) == val


def test_rmap_original_res():
    val = (ERROR, 'msg')

    def f(val):
        return val

    assert rmap(f, val) == val


def test_and_then_is_ok():

    val = 1

    def f(a):
        return (OK, a + 1)

    assert and_then(f, ok(val)) == (OK, val + 1)


def test_and_then_original_res():
    val = (ERROR, 'msg')

    def f(a):
        return a + 1

    assert and_then(f, val) == val


def test_and_else_is_ok():

    val = 1

    def f(a):
        return (ERROR, a + 1)

    assert and_else(f, error(val)) == (ERROR, val + 1)


def test_and_else_original_res():
    val = (OK, 'val')

    def f(val):
        return val

    assert and_else(f, val) == val


def test_fold_all_is_ok():

    res = [('Ok', 'val1'), ('Ok', 'val2'), ('Ok', 'val3')]

    assert fold(res) == ('Ok', ['val1', 'val2', 'val3'])


def test_fold_not_all_is_ok():

    res = [('Ok', 'val1'), ('Error', 'msg1'), ('Ok', 'val3')]

    assert fold(res) == ('Error', [None, 'msg1', None])


def test_resolve_original_res():

    val = (ERROR, (ERROR, 'msg'))

    assert resolve(val) == val


def test_resolve_isnt_ok():

    val = (OK, (OK, 'val'))

    assert resolve(val) == (OK, 'val')


def test_do_return_original_error():
    err = error('ERROR')

    assert do(ok, err) == err


def test_do_return_original_result():
    result = ok('FOO BAR')

    assert do(lambda _: ok('BAZ FOO'), result) == result


def test_do_return_error_from_function():
    err = error('BAZ FOO')

    assert do(lambda _: err, ok('FOO BAR')) == err


def test_with_default_return_original_value():
    res = ok('FOO BAR')

    assert with_default('BAZ', res) == 'FOO BAR'


def test_with_default_return_default_value_when_result_is_error():
    res = error('FOO BAR')

    assert with_default('BAZ', res) == 'BAZ'
