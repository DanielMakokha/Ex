# Write a multiplication game program for kids. The program should give the player ten ran-
# domly generated multiplication questions to do. After each, the program should tell them
# whether they got it right or wrong and what the correct answer is.

import random
from random import randint

for i in range(10):
    a=randint(1,10)
    b=randint(1,10)
    result=a*b
    print(a,"*",b,"=")
    answer=int(input("Answer:"))
    if answer==result:
        print("Right")
    else:
        print("Wrong")
        print("The right answer is ",result)
        
  
"""This is the programming language
of our choice and we love it so"""
