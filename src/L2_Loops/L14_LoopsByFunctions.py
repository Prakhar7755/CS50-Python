def main():
    number = get_number()  # define this function now
    meow(number)


def meow(n):
    for _ in range(n):
        print("meow")


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n                         # can use break then use return also


main()
