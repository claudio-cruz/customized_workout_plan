from email.policy import strict


def get_user_data():
    """
    Get the name, height, weight, and gender input date from the user.
    Run a while loop to collect all the valid input from the user. 
    The loop stops when the input data is valid. 
    """
    while True:
        print('\nPlease provide us with the following requested data so we can provide you with your ideal weight and your customized workout plan.\n')
        
        user_name = input('Please enter your name:\n')

        if validate_name(user_name):
            print(f'Welcome {user_name.title()}! Your name has been submitted.\n')
        else: continue

        print('Please enter your height in cm.')
        user_height = input('Enter your height in cm: ')

        print('Please enter your weight in kg.')
        user_weight = input('Enter your weight in kg: ')

        print('Please tell us your gender.')
        user_weight = input('Enter your gender: ')

        

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
        
get_user_data()