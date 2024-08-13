
'''

@Author: Jayesh Patil
@Date: 2024-08-13
@Last Modified by: Jayesh Patil
@Title: Loan Payment Calculator


'''


class Util:

    @staticmethod
    def monthlyPayment(principal, years, annual_rate):

        """
        
        
        Description:
            Calculates the monthly payment for a loan using the given formula.

        Parameters:
            principal (float): The principal loan amount.
            years (int): The number of years to pay off the loan.
            annual_rate (float): The annual interest rate (as a percentage).

        Return:
            float: The monthly payment amount.
        
        
        """
        
        n = 12 * years
        r = annual_rate / (12 * 100)
        if r == 0:
            return principal / n
        payment = (principal * r) / (1 - (1 + r) ** (-n))

        return payment


def main():
    try:
        principal = float(input("Enter The Principal Amount : "))
        years = int(input("Enter The Years : "))
        annual_rate = float(input("Enter The Annual Rate of Interest : "))
        
        if principal <= 0 or years <= 0 or annual_rate < 0:
            print("Principal, years, and annual rate must be positive numbers.")
        
        payment = Util.monthlyPayment(principal, years, annual_rate)
        print(f"Monthly payment for a loan of {principal} over {years} years at an annual rate of {annual_rate}% is: {payment:.2f} Rs")
        
    except ValueError:
        print("Invalid input. Please enter numeric values for principal, years, and annual rate.")

if __name__ == '__main__' :
    main()