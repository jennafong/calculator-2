"""CLI application for a prefix-notation calculator."""



from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod)

con = True

while con:
    input_string = input("> ")
    tokens = input_string.split(' ')

    if tokens[0] == "q":
        con = False
    else:
        if tokens[0] == "+":
            print(add(int(tokens[1]),int(tokens[2])))
        elif tokens[0] =="-":
            print(subtract(int(tokens[1]),int(tokens[2])))
        elif tokens[0] =="*":
            print(multiply(int(tokens[1]),int(tokens[2])))
        elif tokens[0] =="/":
            print(divide(int(tokens[1]),int(tokens[2])))
        elif tokens[0] =="square":
            print(square(int(tokens[1])))
        elif tokens[0] =="cube":
            print(cube(int(tokens[1])))
        elif tokens[0] =="pow":
            print(power(int(tokens[1]),int(tokens[2])))
        else:
            tokens[0] =="mod"
            print(mod(int(tokens[1]),int(tokens[2])))