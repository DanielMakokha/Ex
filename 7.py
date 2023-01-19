# Write a program that asks the user to enter an angle between −180◦ and 180◦ . Using an
# expression with the modulo operator, convert the angle to its equivalent between 0◦ and
# 360◦ .

Angle=int(input("Enter an angle between -180 and 180: "))

# Conversion to the equivalent angle using the modulus operator
equivalent_angle=Angle%360
print("The equivalent angle between -180 and 180: ",equivalent_angle)
