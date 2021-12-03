# final assignment for week 8
# program is to take a users input, append a list/array, and then produce a result
# assignment is a BMI calculator
# list for user's height and weight
user = []
bmi = 0
# Take names
while (len(user) != 6):
    user.append(input("Please submit the first user's name "))
    user.append(input("Please submit the second user's name "))
    user.append(input("Please submit the third user's name "))
    user.append(input("Please submit the forth user's name "))
    user.append(input("Please submit the fifth user's name "))
    user.append(input("Please submit the sixth user's name "))
#take user's weight and height, then print results
for val in str(user[0]):
    x = int(input("Please submit the first user's height in inches: "))
    y = int(input("Please submit the first user's weight in pounds: "))
    bmi == str(print(user[0],"'s BMI is: ", (y * 703 / (x ** 2))))
    bmi = (y * 703 / (x **2))
    if bmi <= 18.5:
        print(user[0],'is underweight.')
    elif bmi > 18.5 and bmi <= 24.9:
        print(user[0],'is at a normal weight.')
    elif bmi > 24.9 and bmi <=30:
        print(user[0],'is overweight.')
    else:
        bmi < 30
        print(user[0],'is obese.')
for val in str(user[1]):
    x = eval(input("Please submit the second user's height in inches: "))
    y = eval(input("Please submit the second user's weight in pounds: "))
    bmi = str(print(user[1],"'s BMI is: ", (y * 703 / (x ** 2))))
    bmi = (y * 703 / (x **2))
    if bmi <= 18.5:
        print(user[1],'is underweight.')
    elif bmi > 18.5 and bmi <= 24.9:
        print(user[1],'is at a normal weight.')
    elif bmi > 24.9 and bmi <=30:
        print(user[1],'is overweight.')
    else:
        bmi < 30
        print(user[1],'is obese.')
for val in str(user[2]):
    x = eval(input("Please submit the third user's height in inches: "))
    y = eval(input("Please submit the third user's weight in pounds: "))
    bmi = str(print(user[2],"'s BMI is: ", (y * 703 / (x ** 2))))
    bmi = (y * 703 / (x **2))
    if bmi <= 18.5:
        print(user[2],'is underweight.')
    elif bmi > 18.5 and bmi <= 24.9:
        print(user[2],'is at a normal weight.')
    elif bmi > 24.9 and bmi <=30:
        print(user[2],'is overweight.')
    else:
        bmi < 30
        print(user[2],'is obese.')
for val in str(user[3]):
    x = eval(input("Please submit the forth user's height in inches: "))
    y = eval(input("Please submit the forth user's weight in pounds: "))
    bmi = str(print(user[3],"'s BMI is: ", (y * 703 / (x ** 2))))
    bmi = (y * 703 / (x **2))
    if bmi <= 18.5:
        print(user[3],'is underweight.')
    elif bmi > 18.5 and bmi <= 24.9:
        print(user[3],'is at a normal weight.')
    elif bmi > 24.9 and bmi <=30:
        print(user[3],'is overweight.')
    else:
        bmi < 30
        print(user[3],'is obese.')
for val in str(user[4]):
    x = eval(input("Please submit the fifth user's height in inches: "))
    y = eval(input("Please submit the fifth user's weight in pounds: "))
    bmi = str(print(user[4],"'s BMI is: ", (y * 703 / (x ** 2))))
    bmi = (y * 703 / (x **2))
    if bmi <= 18.5:
        print(user[4],'is underweight.')
    elif bmi > 18.5 and bmi <= 24.9:
        print(user[4],'is at a normal weight.')
    elif bmi > 24.9 and bmi <=30:
        print(user[4],'is overweight.')
    else:
        bmi < 30
        print(user[4],'is obese.')
for val in str(user[5]):
    x = eval(input("Please submit the sixth user's height in inches: "))
    y = eval(input("Please submit the sixth user's weight in pounds: "))
    bmi = str(print(user[5],"'s BMI is: ", (y * 703 / (x ** 2))))
    bmi = (y * 703 / (x **2))
    if bmi <= 18.5:
        print(user[5],'is underweight.')
    elif bmi > 18.5 and bmi <= 24.9:
        print(user[5],'is at a normal weight.')
    elif bmi > 24.9 and bmi <=30:
        print(user[5],'is overweight.')
    else:
        bmi < 30
        print(user[5],'is obese.')
for val in str(user):
    if len(user) == 6:
          break
input('')
          
