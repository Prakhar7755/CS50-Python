'''                                     
def main():
    x = get_Int()
    print(f"x is {x}")


def get_Int():

    while True:
        try:                                          # try this
            
            x = int(input("What's x ? "))
            return x

        except ValueError:                             # what to do in case of exception
        
            # print("x is not an Integer")

        # else:
        #     return x


main()
'''


def main():
    x = get_Int()
    print(f"x is {x}")


def get_Int():
    while True:
        try:
            return int(input("What's x ? "))

        except ValueError:
            pass


main()
