from calculator import square


def main():
    test_square()


def test_square(): # assert using try-except
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared is not 4")

    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared is not 9")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 squared is not 4")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 squared is not 9")
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 squared is not 0")


'''
def test_square(): # less code using assert keyword
    assert square(2) == 4
    assert square(3) == 9  # AssertionError will be shown
'''
'''
def test_square():

    if square(2) != 4:
        print("2 squared was not 4")
    if square(3) != 9:                    # when n+n this condition returns an test error condition
        print("3 squared was not 9")
'''

if __name__ == "__main__":
    main()
