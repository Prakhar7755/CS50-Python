from hello import hello


def test_default():
    assert hello() == "hello, world"


def test_argument():
    assert hello("david") == "hello, david"


def test_arg():
    for name in ["Hermoine", "Harry", "Ron", "Draco"]:
        assert hello(name) == f"hello, {name}"
