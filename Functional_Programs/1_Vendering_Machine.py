'''


@Author: Jayesh Patil
@Date: 2024-08-13
@Last Modified by: Jayesh Patil
@Title : Fewest Notes to be Returned by Vending Machine


'''

def calculate_change(change, notes=None):


    """


    Description:
        Calculates the minimum number of notes needed to return the change.

    Parameters:
        change (int): The amount of change to be returned by the vending machine.
        notes (list): A list of available note denominations.

    Return:
        tuple: A tuple containing the total number of notes used and a list of notes returned.
    
    
    """
    
    
    if notes is None:
        notes = [1000, 500, 100, 50, 10, 5, 2, 1]  

    change_notes = []
    for note in notes:
        if change >= note:
            num_notes = change // note
            change_notes.append((note, num_notes))
            change -= num_notes * note

    total_notes = sum(count for _, count in change_notes)
    return total_notes, change_notes

try:
    change = int(input("Enter the change to be returned by the vending machine: "))
    
    if change <= 0:
        print("Please enter a positive amount of change.")
    else:
        total_notes, change_notes = calculate_change(change)
        print(f"Minimum number of notes needed: {total_notes}")
        print("Notes returned:")
        for note, count in change_notes:
            print(f"Rs {note} : {count} notes")
except ValueError:
    print("Invalid input !!!. \nPlease enter a valid integer amount...")