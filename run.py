from email.policy import strict
from unittest import expectedFailure

from tomlkit import integer


def get_user_data():
    """
    Get the name, height, weight, and gender input date from the user.
    Run a while loop to collect all the valid input from the user. 
    The loop stops when the input data is valid. 
    """
    while True:
        print('\nPlease provide us with the following requested data so we can provide you with your ideal weight and your customized workout plan.\n')
        
        """user_name = input('Please enter your name:\n')
        if validate_name(user_name):
            print(f'Welcome {user_name.title()}! Your name has been submitted.\n')
        else: continue"""

        input_height = input('Please enter your height in cm: \n')
        user_height = int(input_height)
        print(type(user_height))
        if validate_height_weight(user_height):
            print('Your height has been submitted.\n')
        else: continue

        input_weight = input('Please enter your weight in kg: \n')
        try:
            user_weight = int(input_weight)
        except:
            print('no')
        if validate_height_weight(user_weight):
            print('Your weight has been submitted.\n')
        else: continue

        print('Please tell us your gender.')
        user_weight = input('Enter your gender: ')
        break

        
def validate_name(value):
    """
    Validates the name input provided by the user.
    Returns a message if the input is not valid and repeats the loop.
    Returns a message if the input is valid and proceeds with the rest of the loop.
    """
    try:
        if len(value) > 15 or value == '':
            raise ValueError
            
    except ValueError as e:
        print(f'\nInvalid name: please submit your name with fifteen characters or less in total.')
        print('The name input can not be empty.\n')
        return False

    return True


def validate_height_weight(value):
    """
    Validates the height and the weight input provided by the user.
    If the input is not a valid number prints a message and repeats the loop.
    Returns a message if the input is valid and proceeds with the rest of the loop.
    """
    try:
        if type(value) != int or len(str(value)) != 3:
            raise ValueError

    except ValueError as e:
        print('\nInvalid input:')
        return False

    return True


get_user_data()