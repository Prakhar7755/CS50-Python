name = input("what's your name? ")

match name:
    case "harry" | "ron" | "hermoine":
        print("griffindor")
    case "snape" | "draco malfoy":
        print("slytherine")
    case _:
        print(name,"who?")
