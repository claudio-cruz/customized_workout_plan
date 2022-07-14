# **Customized Workout Plan**

Customized Workout Plan is a Python terminal app that runs on Heroku.

The Customized Workout Plan app has three main goals: getting the BMI (body mass index), ideal weight, and most importantly, getting a customized workout plan for the user's needs.

The users answer 6 questions. The app runs the code and generates the user's BMI, the user's ideal weight, and the customized workout plan.

#link
#layout image

## How the app works
Users answer the first four questions: “user name”, “user height”, “user weight”, and “user gender”.
The app runs the code using the user's first four answers and prints the BMI and ideal weight for the user.
Then users answer the final two questions, user workout goal (weight loss or gain muscle), and user workout days per week (2, 4 or 6 days).
The app runs the code again with all user input answers and prints the personalized workout plan for the user's specific needs.

## Features

- __First four inputs__

  - Name, used to identify the user.
  - Height, used to calculate the ideal weight and BMI.
  - Weight, used to calculate the ideal weight and BMI.
  - Gender, used to calculate the BMI and the workout plan.

#inputs image

- __Ideal weight and BMI__

  - Calculate the user's ideal weight using the formula:
    - 50 + (0.91 * (height - 152.4) for male.
    - 45.5 + (0.91 * (height - 152.4) for female.
  - Calculate the user's BMI using the formula:
    - weight / (height / 100)**2 for male and female.

#ideal weight and BMI image

- __BMI chard__

  - Prints the BMI chart for male and female.

#BMI chard image

- __Workout goal input__
  - Provide two workout goal options:
    - "weight loss" for lose weight.
    - "gain muscle" for muscle gain.

#Workout goal input image

- __Workout days per week input__

  - Provide three workout options to users:
    - "2" for 2 workout days per week.
    - "4" for 4 workout days per week.
    - "6" for 6 workout days per week.

#Workout days per week input image

- __Input submission message__

  - If all inputs are correct, print the following:
    - Print all the user inputs.
    - Print user ideal weight.
    - Print user BMI.

#Input submission message image

- __Personalized workout plan__

  - Print to the console the personalized workout plan for each user.

#Personalized workout plan image