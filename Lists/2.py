# Write a program that generates a list of 20 random numbers between 1 and 100.
# (a) Print the list.
# (b) Print the average of the elements in the list.
# (c) Print the largest and smallest values in the list.
# (d) Print the second largest and second smallest entries in the list
# (e) Print how many even numbers are in the list.
from random import randint;
L=[]
for i in range(20):
   L.append(randint(1,100))
print(L,',',sep='',end='')

average=sum(L)/len(L)
print()
print(average)
L.sort()
print(L[0])
# print()
print(L[-1])
print(L[1]," ",L[-2])

count=0;
for c in L:
    if c%2==0:
        count+=1;
        print(c,",",sep="",end="")
print(count)