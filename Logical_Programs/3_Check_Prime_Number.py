'''
@Author: Jayesh Patil


@Date: 2024-13-08 


@Last Modified by: Jayesh Patil


@Last Modified time: 2024-13-08  11:03 AM


@Title : Prime_Number
'''
"""
Description:

    The `check_prime` function determines whether a given number is a prime number.
    A prime number is a positive integer greater than 1 that has no positive divisors other than 1 and itself.
    The function checks for this by testing divisibility by numbers up to the square root of the input number,
    which is an efficient way to determine primality.

Parameters:

    n (int):
        - The number you want to check for primality.
        - This number is passed into the function to determine whether it is a prime number.

Usage:
    
    The function first handles edge cases, such as numbers less than or equal to 1 (which are not prime),
    and the number 2, which is the smallest and only even prime number.
    
    For numbers greater than 2, the function checks if the number is even (and therefore not prime).
    Then, it iterates over odd numbers starting from 3 up to the square root of `n`, checking if any of these
    numbers divide `n` evenly. If any divisor is found, the function returns `False`, indicating the number is not prime.
    If no divisors are found, it returns `True`, confirming that the number is prime.

Returns:

    bool:
        - The function returns `True` if the given number is a prime number.
        - If the number is not prime, the function returns `False`.
"""

def check_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False  
    
    if n == 2:
        return True  
    
    if n % 2 == 0:
        return False  
    
   
    for i in range(3, n):
        if n % i == 0:
            return False  
    
    return True 

def main():
    num = int(input("Enter a number to check if it's prime: "))
    if check_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

if __name__ == "__main__":
    main()
