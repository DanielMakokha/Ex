# Write a program that asks the user to enter a value n, and then computes (1 + 1/2 + 1/3 + · · · + 1/n ) −
# ln(n). The ln function is log in the math module.
import math
# prompt the user to enter value n
n=int(input("Enter the value for n: "))

# initialize the variable to store sum
sum=0

# iterate the numbers from 1 to n
for i in range(1,n+1):
    # Add the curren term to the sum
    sum+=1/i;
    
# subtract ln(n) from the sum
result=sum-math.log(n)

# print the result
print("Result: ",result)

    