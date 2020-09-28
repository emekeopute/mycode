#!/usr/bin/env python3
import numpy as np

"""Amazon || Author: Emeke Opute"""
## declares empty list holder
var_list = []
## creates the addition method with user input check
def add():
    number_ = input("Please type a number and press enter: ")
    try:
        float(number_)
        while True:
            var_list.append(float(number_))
            print(var_list)
            x = input("Would you like to add another number? Y/N: ")
            if x.lower() == "y":
                add()
            else:
                if x.lower() == "n":
                    break
    except :
        print("You have entered an invalid input")
        input(" Please enter a valid number: ")
        add()
## creates the multiplication method with user input check
def multiply():
    number_ = input("Please type a number and press enter: ")
    try:
        float(number_)
        while True:
            var_list.append(float(number_))
            print(var_list)
            if len(var_list) < 2:
                x = input("Please enter another another to continue operation: ")
            try:
                float(x)
                if True:
                    del(number_)
                    var_list.append(float(x))
                    print(var_list)
            except:
                print("You have entered an invalid input")
                multiply()
            else:
                if len(var_list) >= 2:
                    x = input("Would you like to add more number to the multiplication list Y/N: ")
                    if x.lower() == "y":
                        multiply()
                    else:
                        if x.lower() == "n":
                            break
    except :
        print("You have entered an invalid input")
        input(" Please enter a valid number: ")
        add()
## creates the division method with user input check
def divide():
    number_ = input("Please type a number and press enter: ")
    if float(number_) and len(var_list) == 0:
        var_list.append(number_)
        divide()
    else :
        print("You have entered an invalid input")
        input(" Please enter a valid number: ")
        divide()
## creates the subtraction method with user input check
def subtract():
    number_ = input("Please type a number and press enter: ")
    if float(number_) and len(var_list) == 0:
        var_list.append(number_)
        subtract()
    else :
        print("You have entered an invalid input")
        input(" Please enter a valid number: ")
        divide()
## main method
def calc():
    ## user instruction set
    user_operation = input("Please enter: + for add, - for subtract, / for divide, * for multiply: ")
    if user_operation == "+":
        add()
        final_ans = sum(var_list)
        print(f"Answer: {final_ans}")
    elif user_operation == "*":
        multiply()
        final_ans = np.prod(var_list, start = 1)
        print(f"Answer: {final_ans}")
    elif user_operation == "/":
        divide()
        final_ans = var_list[0]/var_list[1]
        print(f"{var_list[0]}/{var_list[1]} = {final_ans}")
    elif user_operation == "-":
        subtract()
        final_ans = var_list[0]-var_list[1]
        print(f"{var_list[0]}-{var_list[1]} = {final_ans}")
    else:
        print("Please select a valid operation")
        calc()
calc()
