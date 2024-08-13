'''


@Author: Jayesh Patil
@Date: 2024-08-13
@Last Modified by: Jayesh Patil
@Title: Temperature Conversion Utility



'''

class Util:

    @staticmethod
    def temperatureConversion(value, scale):
    
        """
    
    
        Description:
            Converts temperature between Celsius and Fahrenheit.

        Parameters:
            value (float): Temperature value to be converted.
            scale (str): The scale of the input temperature ('C' for Celsius, 'F' for Fahrenheit).

        Return:
            float: The converted temperature value in the opposite scale.
        
        
        """
        
        if scale == 'C':
            return (value * 9/5) + 32
        elif scale == 'F':
            return (value - 32) * 5/9
        else:
            raise ValueError("Invalid scale. Use 'C' for Celsius or 'F' for Fahrenheit.")
        


try:
    value = float(input("Enter the temperature value: "))
    scale = input("Enter the temperature scale (C for Celsius, F for Fahrenheit): ").upper()
    
    if scale not in ['C', 'F']:
        print("Invalid scale. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    else:
        converted_temp = Util.temperatureConversion(value, scale)
        if scale == 'C':
            print(f"{value}°C is equal to {converted_temp:.2f}°F")
        else:
            print(f"{value}°F is equal to {converted_temp:.2f}°C")
except ValueError as e:
    print(f"Error: {e}")