# USING AN INFINTE LOOP

while True:
    try:                                          # try this
        x = int(input("What's x ? "))

    except ValueError:                             # what to do in case of exception
        print("x is not an Integer")
    else:
        break  # can also be placed in try block without else


print(f"x is {x}")
