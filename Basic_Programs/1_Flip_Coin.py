'''
@Author: Jayesh Patil


@Date: 2024-12-08 11:43 Am


@Last Modified by: Jayesh Patil


@Last Modified time: 2024-12-08 11:43 AM


@Title :  Flip Coin and print percentage of Heads and Tails
'''
import random
"""
Description:

    The `flip_coin` function use to flipping a coin a certain number of times.
    The function uses Python `random` module to randomly decide each flip's outcome.

Parameters:

    num_flips (int):
        - The number of times the coin will be flipped.
        - It should be a positive number. 

Returns:
        - This function doesn't return any values.
        - Instead, it prints the total number of flips.
"""


def fipl_coin(num_filp):
    """This Function calculate Flip coin Percentage"""
    if num_filp < 0:
        print("Enter postive value ")
        return
    heads =0
    tails =0
    for i in range(num_filp):
        if random.random() < 0.5:
            tails +=1
        else:
            heads +=1
    headsper = (heads/num_filp)*100
    tailsper = (tails/num_filp)*100
    print(f"total filps : {num_filp}")
    print(f"Heads : {heads}({headsper :.2f}%)")  
    print(f"Tails : {tails}({tailsper :.2f}%)")  
num_filp = int(input("enter the filp "))

fipl_coin(num_filp)
#call the function 

