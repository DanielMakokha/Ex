# Write a program that asks the user to enter a length in centimeters. If the user enters a negative
# length, the program should tell the user that the entry is invalid. Otherwise, the program
# should convert the length to inches and print out the result. There are 2.54 centimeters in an
# inch.

# progrms pseudocode
    # prompts user for input in cm.
    # condition(invalid for negative input)
    
    
lenght_cm=float(input("Enter your length in cm: "));
# Condition
if lenght_cm<0:
    print("Invalid input")
else:
# Convert to inches
    lenght_inches=lenght_cm*2.54
    print("Your length in inches is: ",lenght_inches);