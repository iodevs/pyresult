#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from pyresult.result import ResultError, ok, error, result, is_ok, is_error, value
from pyresult.operators import errmap, rmap, and_then, and_else, resolve


def test_errmap_is_ok():

    val = ('Error', 'msg')
    def f(q):
        return q + " hello"

    assert errmap(f, val) == ('Error', 'msg hello')


def test_errmap_original_res():

    val = ('Ok', 'val')
    def f(val):
        return val

    assert errmap(f, val) == val


def test_rmap_is_ok():

    val = ('Ok', 'val')
    def f(val):
        return val

    assert rmap(f, val) == val


def test_rmap_original_res():

    val = ('Error', 'msg')
    def f(val):
        return val

    assert rmap(f, val) == val


def test_and_then_is_ok():

    val = 1

    def f(a):
        return ('Ok', a + 1)

    assert and_then(f, ok(val)) == ('Ok', val + 1)


def test_and_then_original_res():

    val = ('Error', 'msg')
    def f(a):
        return a + 1

    assert and_then(f, val) == val


def test_and_else_is_ok():

    val = 1

    def f(a):
        return ('Error', a + 1)

    assert and_else(f, error(val)) == ('Error', val + 1)


def test_and_else_original_res():

    val = ('Ok', 'val')
    def f(val):
        return val

    assert and_else(f, val) == val


def test_resolve_original_res():

    val = ('Error', ('Error', 'msg'))

    assert resolve(val) == val


def test_resolve_isnt_ok():

    val = ('Ok', ('Ok', 'val'))

    assert resolve(val) == ('Ok', 'val')
