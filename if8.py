# Write a program that asks the user to enter a number and prints out all the divisors of that
# number.

num=eval(input("Enter a number: "))

for i in range(1,100):
    if i%num==0:
        print(i,',',sep='',end='')