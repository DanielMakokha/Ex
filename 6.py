# Write a program that asks the user to enter two numbers, x and y , and computes x- y/x+y .

x=int(input("Enter value x: "))
y=int(input("Enter value y: "))

sum=x+y
diff=x-y

Answer=diff//sum

print("The Answer is: ",Answer)