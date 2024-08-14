'''

@Author: Jayesh Patil
@Date: 2024-08-12
@Last Modified by: Jayesh Patil
@Title: Decimal to Binary Converter


'''

class Util:

    @staticmethod
    def toBinary(number):
        
        """
        
        
        Description:
            Converts a decimal number to its binary representation with padding to ensure a 4-byte (32-bit) string.

        Parameters:
            n (int): The decimal number to be converted (non-negative integer).

        Return:
            str: The binary representation of the decimal number with 32-bit padding.
        
        
        """
        
        if number < 0:
            raise ValueError("Input must be a non-negative integer.")

        binary_str = bin(number)[2:]

        padded_binary_str = binary_str.zfill(32)

        return padded_binary_str

def main():
    try:
        number = int(input("Enter a non-negative decimal number: "))
        if number < 0:
            print("Error: The number must be non-negative.")
        else:
            result = Util.toBinary(number)
            print(f"The 32-bit binary representation of {number} is: {result}")
    except ValueError:
        print("Invalid input. Please enter a non-negative integer.")

if __name__ == "__main__":
    main()