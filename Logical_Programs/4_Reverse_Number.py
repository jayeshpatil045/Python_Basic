'''
@Author: Jayesh Patil


@Date: 2024-13-08 


@Last Modified by: Jayesh Patil


@Last Modified time: 2024-13-08  11:10 AM


@Title : Reverse_number
'''
"""
Description:

    The `reverse_number` function reverses the digits of a given positive integer. 
    This is achieved by repeatedly extracting the last digit of the number and appending it to a new reversed number. 
    The function continues this process until all digits have been reversed.

Parameters:

    n (int):
        - The positive integer you want to reverse.
        - This number is passed into the function and will be reversed digit by digit.

Usage:
    
    The function initializes a variable `reverse` to 0, which will hold the reversed number.
    It then enters a loop where it repeatedly extracts the last digit of the number `n` using the modulo operator `%`.
    This digit is then added to the `reverse` variable after shifting the existing digits left (by multiplying `reverse` by 10).
    The original number `n` is reduced by removing its last digit using integer division `//`.
    The process continues until the number `n` becomes 0, at which point the reversed number is returned.

Returns:

    int:
        - The function returns the integer that represents the digits of the original number in reverse order.
"""

def reverse_number(n):
    reverse = 0  
    
    while n > 0:
        remainder = n % 10  # Get the last digit of the number
        reverse = reverse * 10 + remainder  # Add the digit to the reversed number
        n = n // 10  # Remove the last digit from the number
    
    return reverse

def main():
    num = int(input("Enter a number to reverse: "))
    reversed_num = reverse_number(num)
    print(f"The reversed number is: {reversed_num}")

if __name__ == "__main__":
    main()
