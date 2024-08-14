'''
@Author: Jayesh Patil


@Date: 2024-13-08 


@Last Modified by: Jayesh Patil


@Last Modified time: 2024-13-08  10:43 AM


@Title : Perfect_Number
'''
"""
Description:

    The `perfect_number` function checks whether a given number is a perfect number.
    A perfect number is defined as a positive integer that is equal to the sum of its positive divisors,
    excluding the number itself. The function determines this by iterating through all numbers less
    than the given number, finding its divisors, and summing them up. If the sum equals the original number,
    the function confirms that the number is perfect.

Parameters:

    n (int):
        - The number you want to check.
        - This number is passed into the function to determine whether it is a perfect number.

Usage:
    
    The function iterates from 1 to `n-1` to find all divisors of `n`. It sums these divisors and checks if the
    sum is equal to `n`. If they are equal, the function returns `True`, indicating that the number is perfect.
    Otherwise, it returns `False`.

Returns:

    bool:
        - The function returns `True` if the given number is a perfect number.
        - If the number is not perfect, the function returns `False`.
"""

def perfect_number(n):
    if n < 0:
        
        return False  
    
    sum_of_divisors = 0  
    
    
    for i in range(1, n):
        if n % i == 0:
            sum_of_divisors += i  
    
    return sum_of_divisors == n  

def main():
    num = int(input("Enter the number: "))
    if perfect_number(num):
        print(f"{num} is a perfect number.")
    else:
        print(f"{num} is not a perfect number.")

if __name__ == "__main__":
    main()
