h = int(input("Please input your height (cm) "))
w = int(input("Please input your weight (kg) "))
h = h/100
bmi = w/(h*h)

if bmi < 16:
    print ("You are severely underweight")
elif bmi < 18.5:
    print ("You are underweight")
elif bmi < 25:
    print ("You are normal")
elif bmi < 30:
    print ("You are overweight")
else:
    print ("You're obese")