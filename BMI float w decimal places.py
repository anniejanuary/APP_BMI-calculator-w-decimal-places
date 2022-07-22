height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

#     1 __ BMI as a rounded int :

BMI=round(weight/height**2)

if BMI < 18.5:
  print(f"Your BMI is: {BMI}, you are are underweight")
elif BMI < 25:
  print(f"Your BMI is: {BMI}, you have a normal weight")
elif BMI < 30:
  print(f"Your BMI is: {BMI}, you are slightly overweight")
elif BMI < 35:
  print(f"Your BMI is: {BMI}, you are obese")
else:
  print(f"Your BMI is: {BMI}, you are clinically obese")
  
  
#     2 A __ BMI as a float to X decimal places : 

BMI=weight/height**2
BMI_format="{:.2f}".format(BMI)

if float(BMI_format) < 18.5:
  print(f"Your BMI is: {BMI_format}, you are are underweight")
elif float(BMI_format) >= 18.5:
  print(f"Your BMI is: {BMI_format}, you have a normal weight")
elif float(BMI_format) >= 25:
  print(f"Your BMI is: {BMI_format}, you are slightly overweight")
elif float(BMI_format) >= 30:
  print(f"Your BMI is: {BMI_format}, you are obese")
else:
  print(f"Your BMI is: {BMI_format}, you are clinically obese")


  #     2 B __ BMI as a float to X decimal places not showing 0 if it's in the last place :
  
BMI=weight/height**2
BMI_format=round(BMI, 2)

if float(BMI_format) < 18.5:
  print(f"Your BMI is: {BMI_format}, you are are underweight")
elif float(BMI_format) >= 18.5:
  print(f"Your BMI is: {BMI_format}, you have a normal weight")
elif float(BMI_format) >= 25:
  print(f"Your BMI is: {BMI_format}, you are slightly overweight")
elif float(BMI_format) >= 30:
  print(f"Your BMI is: {BMI_format}, you are obese")
else:
  print(f"Your BMI is: {BMI_format}, you are clinically obese")
