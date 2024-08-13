'''@Author: Jayesh Patil


@Date: 2024-11-08 12:05 PM


@Last Modified by: Jayesh Patil


@Last Modified time: 2024-11-08 12:05 PM


@Title : Power of 2
'''
def powers_of_2(N):
    if N < 0 or N >= 31:
        print("Please enter a value of N between 0 and 30.")
        return
    
    
    for i in range(N):
        print(f"2^{i} = {2 ** i}")
        N += 1
N = int(input("Enter the power value N (0 <= N < 31): "))

powers_of_2(N)


