# Weight loss workout plans:


def print_inputs(name, height, weight, gender, dl_weight, bmi, goal, days):
    """
    Print user inputs.
    """
    print(f'Well done {name.title()}, all inputs successfully submitted!\n')
    print(f'Your height: {height}cm')
    print(f'Your weight: {weight}kg')
    print(f'Your gender: {gender}')
    print(f'Your ideal weight: {round(dl_weight, 1)}kg')
    print(f'Your BMI: {round(bmi, 1)}')
    print(f'Your goal: {goal}')
    print(f'Workout days per week: {days}\n')

    print('This is the personalized workout plan for your needs:')


def print_weight_loss_male_2days_workout():
    """
    Print the weight loss, male, 2 days per week workout plan.
    """
    print(
    """
-> Monday:
Cardio - Run 20 minutes
Legs - Bodyweight squats 20 reps 5 times
Legs - Bodyweight split squats 30 reps 4 times
Shoulders - Dumbbell press 15 reps 3 times
Shoulders - Lateral raise 15 reps 3 times
Abs - Abdominal crunch 20 reps 3 times
Cardio - Spinning 20 minutes at high intensity

-> Thursday:
Cardio - Elliptical 20 minutes
Chest - Push ups 20 reps 5 times
Back - Pull ups machine 20 reps 5 times
Biceps - Barbell curl 15 reps 3 times
Triceps - Cable push-down 15 reps 3 times
Low-back - Superman 20 reps 3 times
Cardio - Rowing machine 20 minutes at high intensity
    """
    )


def print_weight_loss_female_2days_workout():
    """
    Print the weight loss, female, 2 days per week workout plan.
    """
    print(
    """
-> Monday:
Cardio - Run 20 minutes
Legs - Bodyweight squats 20 reps 5 times
Legs - Bodyweight split squats 30 reps 4 times
Glute - Glute bridge 15 reps 4 times
Shoulders - Dumbbell press 15 reps 3 times
Abs - Abdominal crunch 20 reps 3 times
Cardio - Spinning 20 minutes at high intensity

-> Thursday:
Cardio - Elliptical 20 minutes
Chest - Push ups (knees on the floor) 20 reps 4 times
Back - Pull ups machine 20 reps 4 times
Legs - Leg press machine 15 reps 4 times
Legs - Romanian Deadlift 15 reps 4 times
Cardio - Stair climber 15 minutes
Cardio - Rowing machine 15 minutes at high intensity
    """
    )


def print_weight_loss_male_4days_workout():
    """
    Print the weight loss, male, 4 days per week workout plan.
    """
    print(
    """
-> Monday:
Cardio - Run 20 minutes
Legs - Bodyweight squats 20 reps 5 times
Legs - Bodyweight split squats 30 reps 4 times
Shoulders - Dumbbell press 15 reps 3 times
Shoulders - Lateral raise 15 reps 3 times
Abs - Abdominal crunch 20 reps 3 times
Cardio - Spinning 20 minutes at high intensity

-> Wednesday:
Cardio - Run 30 minutes low intesity
Cardio - Spinning 20 minutes at high intensity

-> Friday:
Cardio - Elliptical 20 minutes
Chest - Push ups 20 reps 5 times
Back - Pull ups machine 20 reps 5 times
Biceps - Barbell curl 15 reps 3 times
Triceps - Cable push-down 15 reps 3 times
Low-back - Superman 20 reps 3 times
Cardio - Rowing machine  20 minutes at high intensity

-> Sunday:
Cardio - Elliptical 20 minutes
Cardio - Jumping rope 15 minutes
Cardio - Rowing machine 10 minutes at high intensity
    """
    )


def print_weight_loss_female_4days_workout():
    """
    Print the weight loss, female, 4 days per week workout plan.
    """
    print(
    """
-> Monday:
Cardio - Run 20 minutes
Legs - Bodyweight squats 20 reps 5 times
Legs - Bodyweight split squats 30 reps 4 times
Glute - Glute bridge 15 reps 4 times
Shoulders - Dumbbell press 15 reps 3 times
Abs - Abdominal crunch 20 reps 3 times
Cardio - Spinning 20 minutes at high intensity

-> Wednesday:
Cardio - Run 30 minutes low intesity
Cardio - Spinning 20 minutes at high intensity

-> Friday:
Cardio - Elliptical 20 minutes
Chest - Push ups (knees on the floor) 20 reps 4 times
Back - Pull ups machine 20 reps 4 times
Legs - Leg press machine 15 reps 4 times
Legs - Romanian Deadlift 15 reps 4 times
Cardio - Stair climber 15 minutes
Cardio - Rowing machine 15 minutes at high intensity

-> Sunday:
Cardio - Elliptical 20 minutes
Cardio - Jumping rope 15 minutes
Cardio - Rowing machine 10 minutes at high intensity
    """
    )


def print_weight_loss_male_6days_workout():
    """
    Print the weight loss, male, 6 days per week workout plan.
    """
    print(
    """
-> Monday:
Cardio - Run 20 minutes
Legs - Bodyweight squats 20 reps 5 times
Legs - Bodyweight split squats 30 reps 4 times
Shoulders - Dumbbell press 15 reps 3 times
Shoulders - Lateral raise 15 reps 3 times
Abs - Abdominal crunch 20 reps 3 times
Cardio - Spinning 10 minutes at high intensity

-> Tuesday:
Cardio - Run 30 minutes low intesity
Cardio - Spinning 20 minutes at high intensity

-> Wednesday:
Cardio - Elliptical 20 minutes
Chest - Push ups 20 reps 5 times
Back - Pull ups machine 20 reps 5 times
Biceps - Barbell curl 15 reps 3 times
Triceps - Cable push-down 15 reps 3 times
Low-back - Superman 20 reps 3 times
Cardio - Rowing machine 10 minutes at high intensity

-> Thursday:
Cardio - Elliptical 20 minutes
Cardio - Jumping rope 15 minutes
Cardio - Rowing machine 10 minutes at high intensity

-> Friday:
Cardio - Run 20 minutes
Chest - Barbell bench press 20 reps 5 times
Back - Seated cable row 20 reps 5 times
Shoulders - Dumbbell press 15 reps 3 times
Biceps - Barbell curl 15 reps 3 times
Triceps - Cable push-down 15 reps 3 times
Legs - Bodyweight squats 20 reps 5 times

-> Saturday:
Cardio - Run 40 minutes medium intensity
    """
    )


def print_weight_loss_female_6days_workout():
    """
    Print the weight loss, female, 6 days per week workout plan.
    """
    print(
    """
-> Monday:
Cardio - Run 20 minutes
Legs - Bodyweight squats 20 reps 5 times
Legs - Bodyweight split squats 30 reps 4 times
Glute - Glute bridge 15 reps 4 times
Shoulders - Dumbbell press 15 reps 3 times
Abs - Abdominal crunch 20 reps 3 times
Cardio - Spinning 20 minutes at high intensity

-> Tuesday:
Cardio - Run 30 minutes low intesity
Cardio - Spinning 20 minutes at high intensity

-> Wednesday:
Cardio - Elliptical 20 minutes
Chest - Push ups (knees on the floor) 20 reps 4 times
Back - Pull ups machine 20 reps 4 times
Legs - Leg press machine 15 reps 4 times
Legs - Romanian Deadlift 15 reps 4 times
Cardio - Stair climber 15 minutes
Cardio - Rowing machine 15 minutes at high intensity

-> Thursday:
Cardio - Elliptical 20 minutes
Cardio - Jumping rope 15 minutes
Cardio - Rowing machine 10 minutes at high intensity

-> Friday:
Cardio - Run 20 minutes;')
Chest - Barbell bench press 15 reps 4 times
Back - Seated cable row 15 reps 4 times
Biceps - Barbell curl 15 reps 3 times
Triceps - Cable push-down 15 reps 3 times
Legs - Bodyweight squats 20 reps 5 times
Cardio - Rowing machine 10 minutes at high intensity

-> Saturday:
Cardio - Run 40 minutes medium intensity
    """
    )


# Gain muscle workout plans:

def print_gain_muscle_male_2days_workout():
    """
    Print the gain muscle, male, 2 days per week workout plan.
    """
    print(
    """
-> Monday:
Cardio - Run 10 minutes
Legs - Squats superset Leg extention 12 reps 4 times
Legs - Split squats superset leg curl 12 reps 4 times
Shoulders - Dumbbell press superset Lateral raise 12 reps 3 times
Abs - Abdominal crunch 20 reps 4 times
    

-> Thursday:
Cardio - Elliptical 10 minutes
Chest - Barbell bench press superset push ups 12 reps 5 times
Back - Pull ups machine superset cable row 12 reps 5 times
Biceps & Triceps - Barbell curl + cable push-down 12 reps 3 times
Low-back - Superman 20 reps 3 times
    """
    )


def print_gain_muscle_female_2days_workout():
    """
    Print the gain muscle, female, 2 days per week workout plan.
    """
    print(
"""
-> Monday:
Cardio - Run 10 minutes
Legs - Squats superset Leg extention 12 reps 4 times
Legs - Split squats superset leg curl 12 reps 4 times
Shoulders - Dumbbell press superset Lateral raise 12 reps 3 times
Abs - Abdominal crunch 20 reps 4 times

-> Thursday
Cardio - Elliptical 10 minutes
Chest - Barbell bench press superset push ups 12 reps 4 times
Back - Pull ups machine superset cable row 12 reps 4 times
Glute - Weighted hip thrust superset Side lunge 12 reps 4 times
Low-back - Superman 20 reps 3 times
"""
)


def print_gain_muscle_male_4days_workout():
    """
    Print the gain muscle, male, 4 days per week workout plan.
    """
    print(
    """
-> Monday:
Cardio - Run 10 minutes
Legs - Squats superset Leg extention 12 reps 4 times
Legs - Split squats superset leg curl 12 reps 4 times
Shoulders - Dumbbell press superset Lateral raise 12 reps 3 times
Abs - Abdominal crunch 20 reps 4 times

-> Wednesday:
Cardio - Elliptical 10 minutes
Chest - Barbell bench press superset push ups 12 reps 4 times
Back - Pull ups machine superset cable row 12 reps 4 times
Biceps & Triceps - Barbell curl superset cable push-down 12 reps 3 times
Low-back - Superman 20 reps 3 times

-> Friday:
Cardio - Stairs machine 10 minutes
Legs - Leg press superset Leg extention 12 reps 4 times
Legs - Romanian deadlift superset leg curl 12 reps 4 times
Shoulders - Barbell over head press superset Frontal raise 12 reps 3 times
Abs - Russian twist 20 reps 4 times

-> Sunday:
Cardio - Rowing machine 10 minutes
Chest - Dumbbell bench press superset Cable crossover 12 reps 4 times
Back - Pull ups machine superset cable row 12 reps 4 times
Biceps & Triceps - Dumbbell curl superset Skullcrusher 12 reps 3 times
Low-back - Back extension 20 reps 3 times
    """
    )


def print_gain_muscle_female_4days_workout():
    """
    Print the gain muscle, female, 4 days per week workout plan.
    """
    print(
    """
-> Monday:
Cardio - Run 10 minutes
Legs - Squats superset Leg extention 12 reps 4 times
Legs - Split squats superset leg curl 12 reps 4 times
Glute & Shoulders - Glute bridge superset Dumbbell press 15 reps 4 times
Abs - Abdominal crunch 20 reps 4 times

-> Wednesday:
Cardio - Elliptical 10 minutes
Chest - Barbell bench press superset push ups 12 reps 4 times
Back - Pull ups machine superset cable row 12 reps 4 times
Biceps & Triceps - Barbell curl superset cable push-down 12 reps 3 times
Low-back - Superman 20 reps 3 times

-> Friday:
Cardio - Stairs machine 10 minutes
Legs - Leg press Leg extention 12 reps 4 times
Legs - Romanian deadlift superset leg curl 12 reps 4 times
Glute & Shoulders - Sumo deadlift superset Lateral raise 12 reps 3 times
Abs - Russian twist 20 reps 4 times

-> Sunday:
Cardio - Rowing machine 10 minutes
Chest - Dumbbell bench press superset Cable crossover 12 reps 4 times
Back - Pull ups machine superset cable row 12 reps 4 times
Low-back - Back extension 20 reps 3 times
Cardio - Stairs machin 20 minutes high intensity
    """
    )


def print_gain_muscle_male_6days_workout():
    """
    Print the gain muscle, male, 6 days per week workout plan.
    """
    print(
    """
-> Monday:
Cardio - Run 10 minutes
Legs - Squats superset Leg extention 12 reps 4 times
Legs - Split squats superset leg curl 12 reps 4 times
Shoulders - Dumbbell press superset Lateral raise 12 reps 3 times
Abs - Abdominal crunch 20 reps 4 times

-> Tuesday:
Cardio - Elliptical 10 minutes
Chest - Barbell bench press superset push ups 12 reps 4 times
Back - Pull ups machine superset cable row 12 reps 4 times
Biceps & Triceps - Barbell curl superset cable push-down 12 reps 3 times
Low-back - Superman 20 reps 3 times

-> Wednesday:
Cardio - Stairs machine 10 minutes
Legs - Leg press superdet Leg extention 12 reps 4 times
Legs - Romanian deadlift superset leg curl 12 reps 4 times
Shoulders - Barbell over head press superset Frontal raise 12 reps 3 times
Abs - Russian twist 20 reps 4 times

-> Thursday:
Cardio - Rowing machine 10 minutes
Chest - Dumbbell bench press superset Cable crossover 12 reps 4 times
Back - Pull ups machine superset cable row 12 reps 4 times
Biceps & Triceps - Dumbbell curl superset Skullcrusher 12 reps 3 times
Low-back - Back extensions 20 reps 3 times

-> Friday:
Cardio - Run 10 minutes
Legs - Squats superset Leg extention 12 reps 4 times
Legs - Split squats superset leg curl 12 reps 4 times
Shoulders - Dumbbell press superset Lateral raise 12 reps 3 times
Abs - Abdominal crunch 20 reps 4 times

-> Saturday:
Cardio - Elliptical 10 minutes
Chest - Barbell bench press superset chest flye 12 reps 4 times
Back - Pull ups machine superset kroc row 12 reps 4 times
Biceps & Triceps - Barbell curl superset cable push-down 12 reps 3 times
Low-back - Back extensions 20 reps 3 times
    """
    )


def print_gain_muscle_female_6days_workout():
    """
    Print the gain muscle, female, 6 days per week workout plan.
    """
    print(
    """
-> Monday:
Cardio - Run 10 minutes
Legs - Squats superset Leg extention 12 reps 4 times
Legs - Split squats superset leg curl 12 reps 4 times
Glute & Shoulders - Glute bridge superset Dumbbell press 15 reps 4 times
Abs - Abdominal crunch 20 reps 4 times

-> Tuesday:
Cardio - Elliptical 10 minutes
Chest - Barbell bench press superset push ups 12 reps 4 times
Back - Pull ups machine superset cable row 12 reps 4 times
Biceps & Triceps - Barbell curl superset cable push-down 12 reps 3 times
Low-back - Superman 20 reps 3 times

-> Wednesday:
Cardio - Stairs machine 10 minutes
Legs - Leg press superdet Leg extention 12 reps 4 times
Legs - Romanian deadlift superset leg curl 12 reps 4 times
Glute & Shoulders - Sumo deadlift superset lateral raise 12 reps 3 times
Abs - Russian twist 20 reps 4 times

-> Thursday:
Cardio - Rowing machine 10 minutes
Chest - Dumbbell bench press superset Cable crossover 12 reps 4 times
Back - Pull ups machine superset cable row 12 reps 4 times
Low-back - Back extensions 20 reps 3 times
Cardio - Stairs machin 20 minutes high intensity 

-> Friday:
Cardio - Run 10 minutes
Legs - Squats superset Leg extention 12 reps 4 times
Legs - Split squats superset leg curl 12 reps 4 times
Glute - Glute bridge superset sumo deadlift 15 reps 3 times
Abs - Abdominal crunch 20 reps 3 times

-> Saturday:
Cardio - Elliptical 20 minutes
Chest - Barbell bench press superset chest flye 12 reps 3 times
Back - Pull ups machine superset kroc row 12 reps 3 times
Biceps & Triceps - Barbell curl superset cable push-down 12 reps 3 times
Low-back - Back extensions 20 reps 3 times
    """
    )