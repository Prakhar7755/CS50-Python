from hello import hello


def test_hello():
    assert hello("David") == "Hello, David"
    assert hello("Indra") == "Hello, Indra"


def test_default():
    assert hello() == "Hello, World"

def test_list():
    for name in ["Ashura","Harsha","Amoghvarsha"]:
        assert hello(name) == f"Hello, {name}"
