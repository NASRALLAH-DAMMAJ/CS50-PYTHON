import pytest
from fuel import convert, gauge

# ======= Convert tests =======
def test_convert_valid():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("99/100") == 99
    assert convert("1/100") == 1

def test_convert_value_error_not_int():
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("1.5/3")
    with pytest.raises(ValueError):
        convert("3/-1")

def test_convert_value_error_bad_fraction():
    with pytest.raises(ValueError):
        convert("5/4")

def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")

# ======= Gauge tests =======
def test_gauge_empty_and_full():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_gauge_normal_percent():
    assert gauge(50) == "50%"
    assert gauge(25) == "25%"
