def main():
    x = get_Int("What's x ? ")
    print(f"x is {x}")


def get_Int(prompt):
    while True:
        try:
            return int(input(prompt))

        except ValueError:
            pass


main()
