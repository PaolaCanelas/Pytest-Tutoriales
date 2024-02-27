import pytest
from src.main import sum, is_greater_than, login

def test_sum():
    assert sum(2, 5) == 7


def test_is_greater_than():
    assert is_greater_than(10, 2)


def test_login_pass():
    login_passed=login("captiva2024", "123456")
    assert login_passed


def test_login_fail():
    login_failed=login("captiva202", "123456800")
    assert not login_failed