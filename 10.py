# One way to find out the last digit of a number is to mod the number by 10. Write a
# program that asks the user to enter a power. Then find the last digit of 2 raised to that
# power

# Ex1
# power=int(input("Enter power: "))
# result=2**power
# last_digit=result%10
# print("The last digit is: ",last_digit)

# Ex2
# One way to find out the last two digits of a number is to mod the number by 100. Write
# a program that asks the user to enter a power. Then find the last two digits of 2 raised to
# that power.

# power=int(input("Enter power: "))
# result=2**power
# last_digit=result%100
# print("The last digit is: ",last_digit)

# Ex3
# Write a program that asks the user to enter a power and how many digits they want.
# Find the last that many digits of 2 raised to the power the user entered.
power = int(input("Enter a power: "))
num_of_digits = int(input("Enter how many digits you want: "))
result = str(2 ** power)
last_digits = result[-num_of_digits:]
print("The last", num_of_digits, "digits of 2 raised to the power of", power, "is:", last_digits)

