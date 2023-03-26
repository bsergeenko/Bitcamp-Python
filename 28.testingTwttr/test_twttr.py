from twttr import shorten

def test_shorten():
    # test lowercase
    assert shorten("twitter") == "twttr"
    # test uppercase
    assert shorten("HELLO") == "HLL"
    # test mixcase
    assert shorten("teSTINg") == "tSTNg"
    # test text
    assert shorten("Hello, World") == "Hll, Wrld"
    # test numbers
    assert shorten("1235") == "1235"