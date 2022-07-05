from email.policy import strict


def get_user_data():
    """
    Get the name, height, weight, and gender input date from the user.
    Run a while loop to collect all the valid input from the user. 
    The loop stops when the input data is valid. 
    """
    while True:
        print('Please provide us with the following requested data so we can provide you with your ideal weight and your customized workout plan.')
        
        print('Please enter your name.')
        user_name = input('Enter your name:\n\n')

        if validate_name(user_name):
            print(f'Welcome {user_name.title()}!The data you provided is valid.\n')
        else: continue

        print('Please enter your height in cm.')
        user_height = input('Enter your height in cm:\n')

        print('Please enter your weight in kg.')
        user_weight = input('Enter your weight in kg:\n')

        print('Please tell us your gender.')
        user_weight = input('Enter your gender:\n')

        

def validate_name(value):
    """
    Validates the name input provided by the user.
    Returns a message if the input is not valid and repeats the loop.
    Returns a message if the input is valid and proceeds with the rest of the loop.
    """
    try:
        if len(value) > 15: 
            raise ValueError
            print('try again')
    except ValueError as e:
        print(f'Invalid data: {e}, please try again.\n')
        return False

    return True
        
get_user_data()