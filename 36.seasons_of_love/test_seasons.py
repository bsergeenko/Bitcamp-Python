from seasons import minutes, minutes_to_words

def test_calculate_birthday():
    assert minutes("1995-01-01") == 14889600
    assert minutes("2023-04-15") == 12960
    assert minutes("2023-04-23") == 1440

def test_minutes_to_word():
    assert minutes_to_words(1) == "one"
    assert minutes_to_words(158123456) == "one hundred fifty-eight million, one hundred twenty-three thousand, four hundred fifty-six"