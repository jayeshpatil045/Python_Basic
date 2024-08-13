'''

@Author: Jayesh Patil
@Date: 2024-11-08 
@Last Modified by: Jayesh Patil
@Title : Harmonic Number Calculator


'''

def calculate_harmonic_number(n):

    """
    
    Description:
        Computes the Nth harmonic number, which is the sum of the series:
        1/1 + 1/2 + 1/3 + ... + 1/N.

    Parameter:
        n (int): The harmonic value N. Must be a positive integer.

    Return:
        float: The Nth harmonic number.
    
    
    """
    
    if n <= 0:
        return ("\nPlease enter a positive integer greater than 0.")

    harmonic_sum = 0.0

    for i in range(1, n + 1):
        harmonic_sum += 1 / i

    return harmonic_sum

def main():
    try:
        n = int(input("\nEnter the harmonic value N (N > 0): "))
        result = calculate_harmonic_number(n)
        print(f"\nThe {n}th harmonic number is: {result:.4f}")
    except Exception:
        print("\nInvalid input. Please enter an integer value.")

if __name__ == '__main__':
    main()

    