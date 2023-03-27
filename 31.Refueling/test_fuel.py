from fuel import convert, gauge
import pytest

def main():
    test_ZeroDivision()
    test_ValueError()

def test_convert():
    assert convert("1/2") == 50
    assert convert("5/5") == 100
    assert convert("1/4") == 25

def test_gauge():
    assert gauge(50) == "50%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"

def test_ZeroDivision():
    with pytest.raises(ZeroDivisionError, match=r"Error: Cannot divide by zero"):
        convert("1/0")

def test_ValueError():
    with pytest.raises(ValueError, match=r"Only integers are allowed"):
        convert("cat/dog")

def test_ValueError():
    with pytest.raises(ValueError, match=r"percentage more than 100"):
        convert("2/1")

if __name__ == "__main__":
    main()
