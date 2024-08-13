'''
@Author: Jayesh Patil


@Date: 2024-12-08 


@Last Modified by: Jayesh Patil


@Last Modified time: 2024-12-08 10:23 PM


@Title : Fibonacci Series
'''
def fibonacci_series(n):
    """Generates a Fibonacci series up to the n-th term."""
    fib_sequence = []
    
    if n <= 0:
        return fib_sequence  # Return an empty list for non-positive n
    
    # Initialize the first two terms
    a, b = 0, 1
    
    for i in range(n):
        fib_sequence.append(a)
        a, b = b, a + b  # Update the values of a and b for the next term
    
    return fib_sequence

def main():
    # Input: Number of terms in the Fibonacci series
    num_terms = int(input("Enter the number of terms for the Fibonacci series: "))
    
    # Generate and print the Fibonacci series
    series = fibonacci_series(num_terms)
    print(f"Fibonacci series up to {num_terms} terms: {series}")

if __name__ == "__main__":
    main()


