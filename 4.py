# Write a program that generates a random decimal number between 1 and 10 with two decimal
# places of accuracy. Examples are 1.23, 3.45, 9.80, and 5.00

# Example1
# from random import randint
# print(randint(100,999)/100)

# Ex2

import random

num1=float(1)
num2=float(10)
decimal=int(2)
rounded_number=round(random.uniform(1,10),decimal)
print(rounded_number)
