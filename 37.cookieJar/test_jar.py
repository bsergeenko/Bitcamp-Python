from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar = Jar(100)
    assert jar.capacity == 100
    with pytest.raises(ValueError):
        Jar(-1)

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    jar = Jar(15)
    jar.deposit(15)
    assert jar.size == 15
    with pytest.raises(ValueError):
        jar = Jar()
        jar.deposit(20)


def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(5)
    assert jar.size == 7
    with pytest.raises(ValueError):
        jar = Jar()
        jar.size == 10
        jar.withdraw(15)