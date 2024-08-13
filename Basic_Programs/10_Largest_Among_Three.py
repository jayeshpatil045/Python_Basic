'''
@Author: Jayesh Patil


@Date: 2024-12-08 01:25 PM


@Last Modified by: Jayesh Patil


@Last Modified time: 2024-12-08 01:25


@Title :  Program to Find the Largest Among Three Numbers

'''
"""
Description:

    The `check_largest` function determines which of three given numbers is the largest. 

Parameters:

    num1 (int):
        - The first number to compare.
    
    num2 (int):
        - The second number to compare.
    
    num3 (int):
        - The third number to compare.

Returns:

    str:
        - The function returns a string indicating which of the three numbers is the largest.
"""

def check_largest(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return f"{num1} is the largest number."
    elif num2 > num1 and num2 > num3:
        return f"{num2} is the largest number."
    else:
        return f"{num3} is the largest number."

# Input: First, second, and third numbers
num1 = int(input("Enter the first number: "))       
num2 = int(input("Enter the second number: "))  
num3 = int(input("Enter the third number: "))   

# Call the function and print the result
print(check_largest(num1, num2, num3))


