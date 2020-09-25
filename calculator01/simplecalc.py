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
                    _sum.append(sum(add_inputs))
                else:
                    user_input = x
            except :
                input(" Please enter a valid number")
                add()

    if user_operation == "+":
        add()
        print("Answer: " + sum(add_inputs))

calc()

# else:
#                     x = input("please enter q to exit calculator")
#                     if x == "q":
#                         exit()
