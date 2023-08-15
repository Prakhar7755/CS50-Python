'''
print("\nhello, terminal \n")

x = int(input("ENTER ANY NUMBER "))

if x % 2 == 0:
    print("even")
else:
    print('odd')
'''

"""

def main():
    x = int(input("whats x ? "))
    if is_even(x):
        print("even")

    else:
        print("odd")


def is_even(n):
    if n%2==0:
        return True
    else:
        return False
    
main()

"""


def main():
    x = int(input("whats x ? "))
    if is_even(x):
        print("even")

    else:
        print("odd")


# def is_even(n):
#     return True if n % 2 == 0 else False         # ANOTHER WAY TO WRITE IT

def is_even(n):        # another way
    return n % 2 == 0


main()
