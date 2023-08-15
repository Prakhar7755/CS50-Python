def main():
    x = input("What's x ? ")
    print("x squared is", square(x))


def square(n):
    return n*n  # change it to n+n for checking error from n*n


if __name__ == "__main__":  # using this main is not always called
    main()
