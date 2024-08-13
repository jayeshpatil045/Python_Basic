'''

@Author: Jayesh Patil
@Date: 2024-11-08
@Last Modified by: Jayesh Patil
@Title : Prime Factorization Calculator


'''

def prime_factors(n):

    """
    
    Description:
        Computes the prime factorization of a given number N using brute force.
        The function traverses till i*i <= N for efficiency in factorization.

    Parameter:
        n (int): The number to find the prime factors of. Must be a positive integer.

    Return:
        list: A list of prime factors of the number N.
    
    
    """
    
    factors = []

    while n % 2 == 0:
        factors.append(2)
        n //= 2

    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i

    if n > 2:
        factors.append(n)

    return factors

def main():
    try:
        n = int(input("\nEnter a number to find its prime factors: "))
        if n > 0:
            result = prime_factors(n)
            print(f"\nThe prime factors of {n} are: {result}")
        else:
            print("\nPlease enter a positive integer greater than 0.")
    except Exception:
        print("\nInvalid input. Please enter an integer value.")
        

if __name__ == '__main__':
    main()