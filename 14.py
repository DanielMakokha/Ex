# Write a program that asks the user to enter an angle in degrees and prints out the sine of that
# angle

import math
# Take input from the user.
angle=float(input("Enter an angle in degrees: "))

# Convert angle to radians
radians=math.radians(angle)

# convert angle to sine
sine=math.sin(radians)

print("The sine of",angle,"is",sine)
