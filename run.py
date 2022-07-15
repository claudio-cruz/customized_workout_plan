from email.policy import strict
from unittest import expectedFailure

from tomlkit import integer

import workout_plans

workout_goal_options = ['weight loss', 'gain muscle']
gender_options = ['male', 'female']


def get_user_data():
    """
    Get the name, height, weight, and gender input date from the user.
    Run a while loop to collect all the valid input from the user.
    Print a message when the input is valid.
    The loop stops when all the input data is valid.
    """

    global user_name
    global user_height
    global user_weight
    global user_gender

    while True:
        user_name = input('Please enter your name: (1 to 15 characters max)\n')
        if validate_name(user_name):
            print(f'Hi {user_name.title()}, your name has been submitted.\n')
        else:
            continue
        break

    while True:
        print('The height must be a number between 40 and 250 cm.')
        user_height = input('Please enter your height in cm:\n')
        if validate_height_weight(user_height):
            print(f'Your height is {user_height}cm, it has been submitted.\n')
        else:
            continue
        break

    while True:
        print('The weight must be a number between 40 and 250 kg.')
        user_weight = input('Please enter your weight in kg:\n')
        if validate_height_weight(user_weight):
            print(f'Your weight is {user_weight}kg, it has been submitted.\n')
        else:
            continue
        break

    while True:
        user_gender = input('Enter your gender: ("male" or "female")\n')
        if validate_input(user_gender, gender_options):
            print(f'You are a {user_gender}, it has been submitted.\n')
        else:
            continue
        break


def validate_name(value):
    """
    Validate the name input provided by the user.
    Return a message if the input is not valid and repeat the loop.
    """

    if len(value) not in range(1, 15):
        print('\nInvalid name. Name input must be 1 to 15 characters max\n')
        return False

    return True


def validate_height_weight(value):
    """
    Validate the height and the weight input provided by the user.
    If the input is not a valid number print a message and repeat the loop.
    """
    try:
        value = float(value)
        if value not in range(40, 250):
            raise ValueError

    except ValueError as e:
        print('Invalid input, it must be a number between 40 and 250!\n')
        return False

    return True


def calculate_ideal_weight(height, gender):
    """
    Calculate the ideal weight and add it to the variable ideal_weight.
    """
    global ideal_weight
    height = float(height)

    if gender == 'male':
        ideal_weight = 50 + (0.91 * (height - 152.4))
        print(f'-> Your ideal weight is {round(ideal_weight, 1)}kg')

    elif gender == 'female':
        ideal_weight = 45.5 + (0.91 * (height - 152.4))
        print(f'-> Your ideal weight is {round(ideal_weight, 1)}kg.')


def calculate_bmi(weight, height):
    """
    Calculate the BMI (body mass index).
    Print a message saying underweight, healthy weight, over weith, or obese.
    Print a message with the BMI chart for men and women.
    """
    global user_bmi
    weight = float(weight)
    height = float(height)
    user_bmi = weight / (height / 100)**2
    bmi_message = f'-> {user_name.title()}, your BMI is {round(user_bmi, 1)} '

    if user_bmi < 18.5:
        print(f'{bmi_message}'+'which means that you are underweight.\n')

    elif user_bmi <= 24.9:
        print(f'{bmi_message}'+'which means that you have a healthy weight.\n')

    elif user_bmi <= 29.9:
        print(f'{bmi_message}'+'which means that you are overweight.\n')

    elif user_bmi >= 30.0:
        print(f'{bmi_message}'+'which means that you are obese.\n')

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
    Print a message with the option chosen and submit it if it is valid.
    """
    global user_workout_goal

    while True:
        print(f"\n{name.title()}, tell us wha's your workout goal.")
        print('Write one of the following 2 goal options:')
        user_workout_goal = input('"weight loss" or "gain muscle"\n')

        if validate_input(user_workout_goal, workout_goal_options):
            print(f'You submited {user_workout_goal} successfully!\n')
            break


def validate_input(value, option):
    """
    Validate the gender input provided by the user.
    Validate the workout goal input provided by the user.
    Print a message if the input is not valid and repeat the loop.
    """

    if value.lower() not in option:
        print('Invalid input!\n')
        return False

    return True


def get_week_workout_days():
    """
    Get how many days per week the user want to train.
    Give 3 input options to the user: 2, 4, or 6 days.
    """
    global user_workout_days

    while True:
        print('\nTell us how many days per week you want to train?')
        user_workout_days = input('Write only ("2", "4", or "6") days:\n')

        if validate_week_workout_days(user_workout_days):
            print(f'You submited {user_workout_days} days successfully!\n')
            break


def validate_week_workout_days(value):
    """
    Validate the workout level input provided by the user.
    Return an error message if the input is not valid and repeat the loop.
    Return a validation message if the input is valid.
    """

    workout_days_options = ["2", "4", "6"]
    if value not in workout_days_options:
        print('Invalid input, write ("2", "4", or "6")!')
        return False

    return True


def personalized_workout_plan():
    """
    Print personalized workout plan.
    """

    # Weight loss male workout plans.
    if user_workout_goal == 'weight loss' and user_gender == 'male':
        if user_workout_days == '2':
            workout_plans.print_weight_loss_male_2days_workout()
        elif user_workout_days == '4':
            workout_plans.print_weight_loss_male_4days_workout()
        elif user_workout_days == '6':
            workout_plans.print_weight_loss_male_6days_workout()

    # Weight loss female worout plans.
    elif user_workout_goal == 'weight loss' and user_gender == 'female':
        if user_workout_days == '2':
            workout_plans.print_weight_loss_female_2days_workout()
        elif user_workout_days == '4':
            workout_plans.print_weight_loss_female_4days_workout()
        elif user_workout_days == '6':
            workout_plans.print_weight_loss_female_6days_workout()

    # Gain muscle male workout plans.
    elif user_workout_goal == 'gain muscle' and user_gender == 'male':
        if user_workout_days == '2':
            workout_plans.print_gain_muscle_male_2days_workout()
        elif user_workout_days == '4':
            workout_plans.print_gain_muscle_male_4days_workout()
        elif user_workout_days == '6':
            workout_plans.print_gain_muscle_male_6days_workout()

    # Gain muscle female workout plans.
    elif user_workout_goal == 'gain muscle' and user_gender == 'female':
        if user_workout_days == '2':
            workout_plans.print_gain_muscle_female_2days_workout()
        elif user_workout_days == '4':
            workout_plans.print_gain_muscle_female_4days_workout()
        elif user_workout_days == '6':
            workout_plans.print_gain_muscle_female_6days_workout()


def main():
    """
    Run all program functions.
    """
    print('\n-------------------------------------------------\n'
          'Welcome to your customized workout plan app.\n'
          'Please provide us with the following requested data\n'
          'so we can generate your ideal weight, BMI, and your\n'
          'customized workout plan.\n'
          '---------------------------------------------------\n')
    get_user_data()
    calculate_ideal_weight(user_height, user_gender)
    calculate_bmi(user_weight, user_height)
    get_workout_goal(user_name)
    get_week_workout_days()
    workout_plans.print_inputs(user_name, user_height, user_weight,
                               user_gender, ideal_weight, user_bmi,
                               user_workout_goal, user_workout_days)
    personalized_workout_plan()


if __name__ == '__main__':
    main()
