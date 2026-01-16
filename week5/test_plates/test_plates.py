from plates import is_valid


def test_is_valid_few():
    assert is_valid("a") == False

def test_is_valid_many():
    assert is_valid("aaaaaaa") == False

def test_is_valid_nums():
    assert is_valid("111111") == False

def test_is_valid_start_nums():
    assert is_valid("11aaaa") == False

def test_is_valid_num_used():
    assert is_valid("aa11aa") == False

def test_is_valid_0():
    assert is_valid("aaa0123") == False