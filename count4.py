# Write a program to compute the sum 1 − 2 + 3 − 4 + · · · + 1999 − 2000.

# Initialize a variable to hold the value of sum

sum=0;
for i in range(1,2001):
#    if number is even subtract from sum
    if i%2==0:
        sum-=i
        # if the current number is odd add it to the sum
    else:
        sum+=i
print("Result: ",sum)