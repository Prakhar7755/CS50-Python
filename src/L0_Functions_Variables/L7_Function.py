'''
def main():
    name = input("what's your name ")
    hello(name)


def hello(to):
    print("hello", to)


main()  # calling the function
'''

#                             FUNCTION USING RETURN VALUE


def main():
    x = int(input("what's x "))
    print("x squared is", square(x))


def square(N):
    #return N**2
    return pow(N,2)
    # return N*N


main()
