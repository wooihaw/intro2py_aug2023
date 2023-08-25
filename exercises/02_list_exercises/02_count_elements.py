# Write a Python script that takes a list, and prints each element and the number of times the element occurs in the list.
alist = [99, 3, -1.2, 2.5, -1.2, -1.2, 5.75, 'xyz', 'a', 99, 'P', 'a', 2.5, 'xyz', 99, 'xyz', 99, 'xyz', 1, -1.2]
print(f'{alist=}')

# Use for loop to iterate through a set of unique items and use count() method
# to check the number of occurance for each item
for i in set(alist):
    print(f"{i}: {alist.count(i)}")
    