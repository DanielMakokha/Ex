# Write a program that prints out the sine and cosine of the angles ranging from 0 to 345◦ in
# 15◦ increments. Each result should be rounded to 4 decimal places.

import math
# loop through the angles

for angle in range(0,350,15):
    
    # Convert the angle to radians
    radians=math.radians(angle)
    
    # convert to sine and cosine
    
    sine=round(math.sin(radians),4)
    cosine=round(math.cos(radians),4);
    
    # print the result
    
    print("The sine of the ",angle,"is",sine)
    print("The cosine of",angle,"is",cosine)