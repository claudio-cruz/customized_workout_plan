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
        
        global user_name
        user_name = input('Please enter your name:\n')
        if validate_name(user_name):
            print(f'Welcome {user_name.title()}! Your name has been submitted.\n')
        else: continue

        global user_height
        user_height = float(input('Please enter your height in cm:\n'))
        if validate_height_weight(user_height):
            print('Your height has been submitted.\n')
        else: continue

        global user_weight
        user_weight = float(input('Please enter your weight in kg:\n'))
        if validate_height_weight(user_weight):
            print('Your weight has been submitted.\n')
        else: continue

        global user_gender
        user_gender = input('Enter your gender:\n')
        if validate_gender(user_gender):
            print('Your gender has been submitted.\n')
        else: continue
        break

    return user_name, user_height, user_weight, user_gender

        
def validate_name(value):
    """
    Validate the name input provided by the user.
    Return a message if the input is not valid and repeats the loop.
    Return a message if the input is valid and proceeds with the rest of the loop.
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
    Validate the height and the weight input provided by the user.
    If the input is not a valid number prints a message and repeats the loop.
    Retur a message if the input is valid and proceeds with the rest of the loop.
    """
    try:
        if value not in range(40, 250):
            raise ValueError

    except ValueError as e:
        print('\nInvalid input:')
        return False

    return True


def validate_gender(value):
    """
    Validate the gender input provided by the user.
    Return an error message if the input is not valid.
    Return a validation message if the input is valid.
    """
    try:
        gender_options = ['male', 'female']
        if value.lower() not in gender_options:
            raise ValueError

    except ValueError as e:
        print('Invalid input:')
        return False

    return True


def calculate_ideal_weight(height, gender):
    """
    Calculate the ideal weight and add it to the variable ideal_weight.
    """
    global ideal_weight
    if gender == 'male':
        
        ideal_weight = 50 + (0.91 * (height - 152.4))
        print(f'Your ideal weight is {round(ideal_weight, 1)}')
        return ideal_weight
    elif gender == 'female':
        ideal_weight = 45.5 + (0.91 * (height - 152.4))
        print(f'Your ideal weight is {round(ideal_weight, 1)}')
        return ideal_weight


def calculate_bmi(weight, height):
    """
    Calculate the BMI (body mass index).
    Return a message if the user is underweight, healthy weight, over weith, or obese.
    Print a message with the BMI chart for men and women.
    """
    global user_bmi
    user_bmi = weight / (height / 100)**2

    if user_bmi < 18.5:
        print(f'{user_name.title()}, your BMI is {round(user_bmi, 1)} which means that you are underweight.\n')
    
    elif user_bmi <= 24.9:
        print(f'{user_name.title()}, your BMI is {round(user_bmi, 1)} which means that you you have a healthy weight.\n')
    
    elif user_bmi <= 29.9:
        print(f'{user_name.title()}, your BMI is {round(user_bmi, 1)} which means that you are overweight.\n')
    
    elif user_bmi >= 30.0:
        print(f'{user_name.title()}, your BMI is {round(user_bmi, 1)} which means that you are obese.\n')
    
    bmi_chart_dic = {
        'Below 18.5': 'Underweight',
        '18.5-24.9': 'Healthy weight',
        '25.0-29.9': 'Overweight',
        '30.0 and above': 'Obesity'
    }
    print('BMI Chart for Men and Women:')
    for key in bmi_chart_dic:
         print(key, '->', bmi_chart_dic[key])


get_user_data()
calculate_ideal_weight(user_height, user_gender)
calculate_bmi(user_weight, user_height)