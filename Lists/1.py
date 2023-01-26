# Write a program that asks the user to enter a list of integers. Do the following:
# (a) Print the total number of items in the list.

# Prompt the user for the input
    
L=eval(input("Enter a list: "))
print(f"The total number of items is {len(L)}")
    
# (b) Print the last item in the list.
print(f"The last item is {L[3]}")

# (c) Print the list in reverse order.
r=L.reverse()
print(r)
# (d) Print Yes if the list contains a 5 and No otherwise.
if 5 in L:
    print("yes")
else:
    print("No")
# (e) Print the number of fives in the list.
count=0
if 5 in L:
    count+=1
    print(count)
# (f) Remove the first and last items from the list, sort the remaining items, and print the
# result.
print(L[0]) and print(L[-1])
print(L.sort())

# (g) Print how many integers in the list are less than 5.

