height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

height_float=float(height)
weight_float=float(weight)

BMI=weight_float/height_float**2

#     formatting a float to 2 decimal places :
BMI_format="{:.2f}".format(BMI)
print(BMI_format)