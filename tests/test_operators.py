#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest


from pyresult.operators import errmap, rmap, and_then, and_else, resolve


def test_errmap_is_ok():

    val = ('Error', 'msg')
    def f(val):
        return val

    assert errmap(f, val) == val


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

    val = ('Ok', 'val')
    def f(val):
        return val

    assert and_then(f, val) == 'val'


def test_and_then_original_res():

    val = ('Error', 'msg')
    def f(val):
        return val

    assert and_then(f, val) == val


def test_and_else_is_ok():

    val = ('Error', 'msg')
    def f(val):
        return val

    assert and_else(f, val) == 'msg'


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

#   return res if is_error(res) else result(res[1])


