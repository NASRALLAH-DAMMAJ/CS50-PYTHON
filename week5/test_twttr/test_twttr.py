from twttr import shorten

def test_shorten():
    assert shorten("twetter") == "twttr"
    assert shorten("ali") == "l"
    assert shorten("Ali Mohemid") == "l Mhmd"
    assert shorten("Kemi") == "Km"
    assert shorten("Star Wars") == "Str Wrs"
    assert shorten("CS50") == "CS50"
    assert shorten("No, however!") == "N, hwvr!"
