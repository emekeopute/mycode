#!/usr/bin/env python3

"""Amazon || Author: Emeke Opute"""

def calc():
    user_operation = input("Please enter: + for add, - for subtract, / for divide, * for multiply: ")
    add_inputs = []
    _sum = []

    def add():
        user_input = input("Please type a number and press enter: ")
        while user_input:
            try:
                float(user_input)
                add_inputs.append(float(user_input))
                print(add_inputs)
                x = input("Would you like to add another number? Y/N :")
                if x.lower() == "y":
                    add()
                elif x.lower() == "n":
                    break
                else:
                    print("You entered an invalid input")
                    add()
            except :
                input(" Please enter a valid number")
                add()
        _sum.append(sum(add_inputs))

    if user_operation == "+":
        add()
        print(f"Answer: {sum(_sum)}")

calc()
