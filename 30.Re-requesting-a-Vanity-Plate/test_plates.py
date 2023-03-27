from plates import is_valid

def test_invalid_legth():
    assert is_valid("A") == False
    assert is_valid("ABCDRGHJK") == False
    assert is_valid("Afdhd125") == False

def test_valid_start_with_letter():
    assert is_valid("AA44") == True
    assert is_valid("00KLK") == False
    assert is_valid("5Q32") == False

def test_invalid_middle_nums():
    assert is_valid("AA12AA") == False
    assert is_valid("MK125A") == False
    assert is_valid("AA125") == True

def test_invalid_zero():
    assert is_valid("AA0123") == False
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True

def test_invalid_punctuation():
    assert is_valid("AA,12") == False
    assert is_valid("AA./15") == False
    assert is_valid("kl??") == False