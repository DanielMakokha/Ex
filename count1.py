# Write a program that counts how many of the squares of the numbers from 1 to 100 end in a
# 1.
count=0
for i in range(1,100):
    print(i**2,',',sep='',end='')
    if i**2%2==1:
        count=count+1;
print()
print(count);