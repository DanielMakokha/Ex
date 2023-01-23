# Write a program that asks the user to enter a number and prints the sum of the divisors of
# that number. The sum of the divisors of a number is an important function in number theory.

num=int(input("Enter a number: "))
sum=0
for i in range(1,num+1):
    if num%i==0:
        sum+=1
print("Result",sum)