from email.policy import strict
from unittest import expectedFailure

from tomlkit import integer

import workout_plans


def get_user_data():
    """
    Get the name, height, weight, and gender input date from the user.
    Run a while loop to collect all the valid input from the user. 
    Print a message when the input is valid.
    The loop stops when all the input data is valid. 
    """
    while True:
        
        global user_name
        global user_height
        global user_weight
        global user_gender

        user_name = input('Please enter your name: (1 to 15 characters max)\n')
        if validate_name(user_name):
            print(f'Hi {user_name.title()}, your name has been submitted.\n')
        else: continue

        
        print('The height must be a number between 40 and 250 cm.')
        user_height = float(input('Please enter your height in cm:\n'))
        if validate_height_weight(user_height):
            print(f'Your height is {user_height}cm, it has been submitted.\n')
        else: continue

        print('The weight must be a number between 40 and 250 kg.')
        user_weight = float(input('Please enter your weight in kg:\n'))
        if validate_height_weight(user_weight):
            print(f'Your weight is {user_weight}kg, it has been submitted.\n')
        else: continue

        user_gender = input('Enter your gender: ("male" or "female")\n')
        if validate_gender(user_gender):
            print(f'You are a {user_gender}, it has been submitted.\n')
        else: continue
        break

        
def validate_name(value):
    """
    Validate the name input provided by the user.
    Return a message if the input is not valid and repeat the loop.
    """
    if len(value) not in range(1, 15):
        print('\nInvalid name. The name input must be 1 to 15 characters max\n')
        return False

    return True


def validate_height_weight(value):
    """
    Validate the height and the weight input provided by the user.
    If the input is not a valid number print a message and repeat the loop.
    """
    try:
        if value not in range(40, 250):
            raise ValueError

    except ValueError as e:
        print('\nInvalid input, it must be a number between 40 and 250!\n')
        return False

    return True


def validate_gender(value):
    """
    Validate the gender input provided by the user.
    Return an error message if the input is not valid and repeat the loop.
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
        print(f'-> Your ideal weight is {round(ideal_weight, 1)}kg')
        
    elif gender == 'female':
        ideal_weight = 45.5 + (0.91 * (height - 152.4))
        print(f'-> Your ideal weight is {round(ideal_weight, 1)}kg.')


def calculate_bmi(weight, height):
    """
    Calculate the BMI (body mass index).
    Return a message if the user is underweight, healthy weight, over weith, or obese.
    Print a message with the BMI chart for men and women.
    """
    global user_bmi
    user_bmi = weight / (height / 100)**2

    if user_bmi < 18.5:
        print(f'-> {user_name.title()}, your BMI is {round(user_bmi, 1)} '
        'which means that you are underweight.\n')
    
    elif user_bmi <= 24.9:
        print(f'-> {user_name.title()}, your BMI is {round(user_bmi, 1)} '
        'which means that you you have a healthy weight.\n')
    
    elif user_bmi <= 29.9:
        print(f'-> {user_name.title()}, your BMI is {round(user_bmi, 1)} '
        'which means that you are overweight.\n')
    
    elif user_bmi >= 30.0:
        print(f'-> {user_name.title()}, your BMI is {round(user_bmi, 1)} '
        'which means that you are obese.\n')

    bmi_chart_dic = {
        'Below 18.5': 'Underweight',
        '18.5-24.9': 'Healthy weight',
        '25.0-29.9': 'Overweight',
        '30.0 and above': 'Obesity'
    }
    print('BMI Chart for Men and Women:')
    for key in bmi_chart_dic:
         print(key, '->', bmi_chart_dic[key])


def get_workout_goal(name):
    """
    Get the workout goal input from the user.
    Print a message with the option chosen and submit it.
    """
    global user_workout_goal

    while True:
        print(f"\n{name.title()}, tell us wha's your workout goal.")
        print('Write one of the following 2 options:')
        user_workout_goal = input('"weight loss" or "gain muscle"\n')

        if validate_workout_goal(user_workout_goal):
            print(f'You submited {user_workout_goal} successfully!\n')
            break


def validate_workout_goal(value):
    """
    Validate the workout goal input provided by the user.
    Return an error message if the input is not valid and repeat the loop.
    Return a validation message if the input is valid.
    """
    try:
        workout_goal_options = ['weight loss', 'gain muscle']
        if value.lower() not in workout_goal_options:
            raise ValueError

    except ValueError as e:
        print('Invalid input:')
        return False

    return True


def get_workout_level(name):
    """
    Get the workout lever input from the user.
    Give 3 input options to the user: low level, medium level and hight level.
    """
    global user_workout_level

    while True:
        print(f'\n{name.title()}, write one of the following 3 options:')
        print('"low level", "medium level", or "hight level"')
        print('Low level    ->  workout 2 days a week.')
        print('Medium level ->  workout 4 days a week.')
        print('Hight level  ->  workout 6 days a week.')
        user_workout_level = input("Tell us wha's your workout level:\n")

        if validate_workout_level(user_workout_level):
            print(f'You submited {user_workout_level} successfully!\n')
            break


def validate_workout_level(value):
    """
    Validate the workout level input provided by the user.
    Return an error message if the input is not valid and repeat the loop.
    Return a validation message if the input is valid.
    """
    try:
        workout_plan_options = ["low level", "medium level", "hight level"]
        if value.lower() not in workout_plan_options:
            raise ValueError

    except ValueError as e:
        print('Invalid input:')
        return False

    return True

def personalized_workout_plan():
    """
    Return personalized workout plan.
    """

    # Weight loss male workout plans.
    if user_workout_goal == 'weight loss' and user_gender == 'male':
        if user_workout_level == 'low level':
            workout_plans.weight_loss_male_low_level_workout()
        elif user_workout_level == 'medium level':
            workout_plans.weight_loss_male_medium_level_workout()
        elif user_workout_level == 'hight level':
            workout_plans.weight_loss_male_hight_level_workout()
    
    # Weight loss female worout plans.
    elif user_workout_goal == 'weight loss' and user_gender == 'female':
        if user_workout_level == 'low level':
            workout_plans.weight_loss_female_low_level_workout()
        elif user_workout_level == 'medium level':
            workout_plans.weight_loss_female_medium_level_workout()
        elif user_workout_level == 'hight level':
             workout_plans.weight_loss_female_hight_level_workout()

    # Gain muscle male workout plans.
    elif user_workout_goal == 'gain muscle' and user_gender == 'male':
        if user_workout_level == 'low level':
            workout_plans.gain_muscle_male_low_level_workout()
        elif user_workout_level == 'medium level':
            workout_plans.gain_muscle_male_medium_level_workout()
        elif user_workout_level == 'hight level':
            workout_plans.gain_muscle_male_high_level_workout()

    # Gain muscle female workout plans.
    elif user_workout_goal == 'gain muscle' and user_gender == 'female':
        if user_workout_level == 'low level':
            workout_plans.gain_muscle_female_low_level_workout()
        elif user_workout_level == 'medium level':
            workout_plans.gain_muscle_female_medium_level_workout()
        elif user_workout_level == 'hight level':
            workout_plans.gain_muscle_female_high_level_workout()


def main():
    """
    Run all program functions.
    """
    get_user_data()
    calculate_ideal_weight(user_height, user_gender)
    calculate_bmi(user_weight, user_height)
    get_workout_goal(user_name)
    get_workout_level(user_name)
    workout_plans.massege_to_user(user_name, user_height, user_weight, 
            user_gender, ideal_weight, user_bmi, user_workout_goal, 
            user_workout_level)
    personalized_workout_plan()


print('\nWelcome to your customized workout plan app.')
print('Please provide us with the following requested data so we can generate'
 ' your ideal weight, BMI, and your customized workout plan.\n')

main()
