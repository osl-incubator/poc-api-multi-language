"""Tests for `poc-multi-api` package."""

from pocapi import simple


def test_avg_list():
    assert simple.avg_list([1, 2, 3, 4, 5]) == 3.0
