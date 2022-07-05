def get_user_data():
    """
    Get the name, height, weight, and gender input date from the user.
    Run a while loop to collect all the valid input from the user. 
    The loop stops when the input data is valid. 
    """
    while True:
        print('Please provide us with the following requested data so we can provide you with your ideal weight and your customized workout plan.')
        print('Please enter your name.')
        user_name = input('Enter your name:\n')

        print('Please enter your height in cm.')
        user_height = input('Enter your height in cm:\n')

        print('Please enter your weight in kg.')
        user_weight = input('Enter your weight in kg:\n')

        print('Please tell us your gender.')
        user_weight = input('Enter your gender:\n')

        if validate_data(value):
            print(f'Welcome {user_name.title()}!The data you provided is valid.')

