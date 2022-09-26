print("Welcome to the Body Mass Index Calculator 2.0")
#
height = float(input("Please enter your height in metre: \n"))
weight = float(input("Please enter your weight in kilograms: \n"))
#

#
bmi = weight / (height ** 2)
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight")
elif 18.5 < bmi < 25:
    print(f"your BMI is {bmi} you have a normal weight")
elif 25 < bmi < 30:
    print(f"Your BMI is {bmi}, you are overweight")
elif 30 < bmi < 35:
    print(f"Your BMI is {bmi}, you are obese")
else:
    print(f"Your BMI is {bmi}, you are clinically obese")

#
