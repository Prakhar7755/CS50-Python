try:                                                   # try this
    x = int(input("What's x ? "))

except ValueError:                                     # what to do in case of exception
    print("x is not an Integer")

else:  # if try succeed then there is not exception to hand which is why this code will initialize
    print(f"x is {x} |!|")  # can be written in try block also
