# Generate a random number between 1 and 10. Ask the user to guess the number and print a
# message based on whether they get it right or not.

import random


random_number=random.randint(1,10)
user_number=int(input("Guess a number between 1 and 10: "))
if user_number==random_number:
    print("right answer")
else:
    print("Wrong Answer:")
    print("Right Answer is: ",random_number)