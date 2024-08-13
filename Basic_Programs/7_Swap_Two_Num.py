'''
@Author: Jayesh Patil

@Date: 2024-12-08 01:05 PM


@Last Modified by: Jayesh Patil


@Last Modified time: 2024-12-08 01:05 PM

@Title : Swap Two Numbers
'''
"""
Description:

    The `Swap_number` function takes two numbers and swaps their values. 

Parameters:

    num1 (int):
        - The first number that you want to swap.
    
    num2 (int):
        - The second number that you want to swap.
Returns:

    None:
        - This function doesn't return any values.
        - Instead, it prints the numbers before and after the swap to the screen.
"""


def Swap_number(num1 , num2):
    print(f"Numbers are Before Swap {num1},{num2}")
    temp = num1
    num1 = num2
    num2 = temp
    print(f"Swap Numbers are {num1},{num2}")   
num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))

Swap_number(num1,num2)
