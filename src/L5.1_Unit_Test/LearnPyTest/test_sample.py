def func(x):
    return x+1


def test_answer():
    assert func(3) == 4

# pytest -q test_sample.py
# pytest --quiet test_sample.py
