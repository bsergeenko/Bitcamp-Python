import bank

def test_value_hello():
    assert bank.value("Hello") == 0
    assert bank.value("HELLO") == 0
    assert bank.value("hello,") == 0

def test_value_h():
    assert bank.value("Hi") == 20
    assert bank.value("Hey") == 20
    assert bank.value("How are you") == 20

def test_value_other():
    assert bank.value("Gamarjoba") == 100
    assert bank.value("Guten Tag") == 100
    assert bank.value("Good morning") == 100
