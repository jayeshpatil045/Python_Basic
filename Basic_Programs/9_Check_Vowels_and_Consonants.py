'''
@Author: Jayesh Patil


@Date: 2024-12-08 01:25 PM


@Last Modified by: Jayesh Patil


@Last Modified time: 2024-12-08 01:25


@Title :  Program to Check Whether an Alphabet is Vowel or Consonant
'''
"""
Description:
        The `check_vowel_or_consonant` function checks whether a given alphabet character is a vowel or a consonant. 

Parameters:
    char (str):
        - The alphabet character you want to check.
        - This should be a single character input by the user.
Returns:
     str:
        - The function returns a string that indicates whether the input character is a vowel or a consonant.
"""

def check_vowel_or_consonant(char):
    if len(char) != 1 or not char.isalpha():
        return "Please enter a single alphabetic character."

    # Define vowels
    vowels = 'aeiouAEIOU'
    
    if char in vowels:
        return f"{char} is a Vowel."
    else:
        return f"{char} is a Consonant."

# Example usage
char = input("Enter an alphabet: ")
print(check_vowel_or_consonant(char))
