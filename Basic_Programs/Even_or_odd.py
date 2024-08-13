
'''
@Author: Jayesh Patil


@Date: 2024-12-08 01:25 PM


@Last Modified by: Jayesh Patil


@Last Modified time: 2024-12-08 01:25


@Title :  Program to Check Whether a Number is Even or Odd
'''
"""
Description:

    The `Even_or_odd` function checks whether a given number is even or odd. 
Parameters:
        num (int):
        - The number that you want to check.

Returns:
        - This function doesn't return any values.
        - Instead, it prints whether the given number is even or odd to the screen.
"""

def Even_or_odd(num):
    if num %2 == 0:
        print(f"{num} this Number is Even ")
    else:
        print(f"{num} this Number is odd")
num = int(input("Enter the Number"))
Even_or_odd(num)        
           