'''

@Author: Jayesh Patil
@Date: 2024-08-13
@Last Modified by: Jayesh Patil
@Title: Square Root Calculator Using Newton's Method


'''

class Util:

    @staticmethod
    def sqrt(c):

        """
        
        
        Description:
            Computes the square root of a nonnegative number using Newton's method.

        Parameters:
            c (float): The nonnegative number for which to compute the square root.

        Return:
            float: The approximate square root of the given number.
        
        
        """
        
        
        if c < 0:
            raise ValueError("Cannot compute the square root of a negative number.")
        
        epsilon = 1e-15
        t = c
        
        while abs(t - c / t) > epsilon * t:
            t = (t + c / t) / 2
        
        return t
    


def main():
    try:
        c = float(input("Enter a nonnegative number: "))
        if c < 0:
            print("Error: The number must be nonnegative.")
        else:
            result = Util.sqrt(c)
            print(f"The square root of {c} is approximately {result:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

        

if __name__ == "__main__":
    main()