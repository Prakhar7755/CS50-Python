print("Hello, Terminal")

'''
for i in range(3):
    print("#")
'''

'''
def main():
    print_row(4)

def print_row(width):
    print("?\t"*width,end="")     

main()
'''


def main():
    print_square(3)  # 3 X 3 bricks


def print_square(size):

    # for each row in square
    for i in range(size):

        # for each brick in a row
        for j in range(size):

            # print the brick
            print("#\t", end="")
        
        print()


main()
