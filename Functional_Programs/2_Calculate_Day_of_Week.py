'''

@Author: Jayesh Patil
@Date: 2024-08-13
@Last Modified by: Jayesh Patil
@Title: Calculate Day of the Week for a Given Date


'''

def day_of_week(month, date, year):

    """
    
    
    Description:
        Calculates the day of the week for a given date using the Gregorian calendar formula.

    Parameters:
        month (int): Month (1 for January, 2 for February, etc.)
        date (int): Day of the month
        year (int): Year

    Return:
        int: Returns the day of the week (0 for Sunday, 1 for Monday, ..., 6 for Saturday)
    
    
    """
    
    y0 = year - (14 - month) // 12
    x = y0 + y0 // 4 - y0 // 100 + y0 // 400
    m0 = month + 12 * ((14 - month) // 12) - 2
    d0 = (date + x + (31 * m0) // 12) % 7

    return d0

try:
    month = int(input("Enter month (1-12): "))
    date = int(input("Enter day (1-31): "))
    year = int(input("Enter year: "))
    
    if month < 1 or month > 12 or date < 1 or date > 31:
        print("Invalid date. Please enter valid values for month and day.")
    else:
        day_index = day_of_week(month, date, year)
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        print(f"The day of the week for {month}/{date}/{year} is: {days[day_index]} ({day_index})")
except ValueError:
    print("Invalid input !!! \nPlease enter valid integers for month, day, and year....")