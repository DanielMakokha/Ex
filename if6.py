# A store charges $12 per item if you buy less than 10 items. If you buy between 10 and 99
# items, the cost is $10 per item. If you buy 100 or more items, the cost is $7 per item. Write a
# program that asks the user how many items they are buying and prints the total cost.

no_items=int(input("The number of items to buy: "))

if no_items<10:
    cost=12*no_items;
    print("Total cost: ",cost)
elif no_items<99:
    cost=10*no_items;
    print("Total cost: ",cost)
else:
    cost=7*no_items;
    print("Total cost: ",cost)
    