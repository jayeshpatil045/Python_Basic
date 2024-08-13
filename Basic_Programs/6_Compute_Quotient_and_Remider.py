'''
@Author: Jayesh Patil


@Date: 2024-12-08 02:10 PM


@Last Modified by: Jayesh Patil


@Last Modified time: 2024-12-08 02:10 PM


@Title :  Program to Compute Quotient and Remainder

'''
# Function to find quotient and remainder
def find_quotient_remainder(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

# Example usage
a = 10
b = 3
quotient, remainder = find_quotient_remainder(a, b)
print("Quotient:", quotient)
print("Remainder:", remainder)
