# Write a program that asks the user to enter a weight in kilograms. The program should
# convert it to pounds, printing the answer rounded to the nearest tenth of a pound.

weight_kg=int(input("Enter your weight in kilograms: "));
# conversion into pounds
weight_pds=weight_kg*2.202622623
print("Your weight in pounds is: ",round(weight_pds,2))

