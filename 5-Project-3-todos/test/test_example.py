import pytest


def test_equal_or_not_equal():
    assert 3 == 3


def test_not_equal_or_not_equal():
    assert 3 != 2


def test_is_instance():
    assert isinstance("this is a string", str)
    assert not isinstance("10", int)


def test_boolean():
    validated = True
    assert validated is True
    assert ("hello" == "world") is False


def test_type():
    assert type("hello" is str)
    assert type("world" is not int)


def test_greater_and_less_than():
    assert 5 > 2
    assert 5 < 10


def test_list():
    num_list = [1, 2, 3, 4, 5]
    any_list = [False, False]
    assert 1 in num_list
    assert 6 not in num_list
    assert all(num_list)
    assert not any(any_list)
