'''
@Author: Jayesh Patil


@Date: 2024-13-08 


@Last Modified by: Jayesh Patil


@Last Modified time: 2024-13-08 01:42 PM


@Title :  
'''
class Util:
    @staticmethod
    def temperature_conversion(value, unit):
        if unit == 'C':
            # Convert Celsius to Fahrenheit
            converted_value = (value * 9/5) + 32
            target_unit = 'F'
        elif unit == 'F':
            # Convert Fahrenheit to Celsius
            converted_value = (value - 32) * 5/9
            target_unit = 'C'
        else:
            raise ValueError("Invalid unit. Use 'C' for Celsius or 'F' for Fahrenheit.")
        
        return converted_value, target_unit

def main():
    try:
        value = float(input("Enter the temperature value: "))
        unit = input("Enter the temperature unit (C/F): ").upper()
        converted_value, target_unit = Util.temperature_conversion(value, unit)
        print(f"{value} {unit} is equal to {converted_value:.2f} {target_unit}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
