def massege_to_user(name, height, weight, gender, dl_weight, bmi, goal, level):
    print(f'Well done {name.title()}, you submitted all inputs successfully!\n')
    print(f'Your height: {height}cm;')
    print(f'Your weight: {weight}kg;')
    print(f'Your gender: {gender};')
    print(f'Your ideal weight: {round(dl_weight, 1)}kg;')
    print(f'Your BMI: {round(bmi, 1)};')
    print(f'Your goal: {goal};')
    print(f'Your level: {level};\n')

    print('This is the personalized workout plan for your needs:\n')


def fat_loss_male_low_level_workout():
    """
    Print the fat loss, male, low lever workout plan.
    """
    print('Day 1:')
    print('Cardio - Run 20 minutes;')
    print('Legs - Bodyweight squats 20 reps 5 times;')
    print('Legs - Bodyweight split squats 30 reps 4 times;')
    print('Shoulders - Dumbbell press 15 reps 3 times;')
    print('Shoulders - Lateral raise 15 reps 3 times;')
    print('Abs - Abdominal crunch 20 reps 3 times;')
    print('Cardio - Spinning 20 minutes at high intensity;\n')

    print('Day 2:')
    print('Cardio - Elliptical 20 minutes;')
    print('Chest - Push ups 20 reps 5 times;')
    print('Back - Pull ups machine 20 reps 5 times;')
    print('Biceps - Barbell curl 15 reps 3 times;')
    print('Triceps - Cable push-down 15 reps 3 times;')
    print('Low-back - Superman 20 reps 3 times;')
    print('Cardio - Rowing machine  20 minutes at high intensity;\n')