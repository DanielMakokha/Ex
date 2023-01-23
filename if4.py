# Write a program that asks the user how many credits they have taken. If they have taken 23
# or less, print that the student is a freshman. If they have taken between 24 and 53, print that
# they are a sophomore. The range for juniors is 54 to 83, and for seniors it is 84 and over.

number_of_credits=int(input("Enter the credits taken: "))

if number_of_credits<=23:
    print("Freshman");
elif number_of_credits<=53:
    print("sophomore");
elif number_of_credits<=83:
    print("juniours");
else:
    print("Seniours");