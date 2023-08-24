# In-class examples for Day 2

#%% Dictionary methods
adict = dict(a=1, b=2.5, c='abc')

print(f"{adict['c'] = }")

# print(f"{adict['d'] = }")  # KeyError if the key is not found in the dictionary

# Using the get() method to return the default value if the key is not found
print(f"{adict.get('d', 'Not found') = }")

# The setdefault() method will insert the key and default value if the key is not found
print(f"{adict.setdefault('d', 0) = }")
print(f"{adict = }")

#%% Join 2 dictionaries

d1 = {'a':1, 'b':2, 'c':3}
d2 = dict(x=4, y=5, z=6)

# Method 1
d3 = d1.copy()
d3.update(d2)
print(f"{d3 = }")

# Method 2
d4 = d1 | d2
print(f"{d4 = }")

#%% Set operations
alist = [1, 2, 1, 3, 1, 4, 5, 1, 2, 0, 2.5, 0, 'a', 'abc', 2.5, 'a']
blist = list(set(alist))

print(f"{alist = }\n{blist = }")

#%% Set methods
name1 = ['Ali', 'Baba', 'Chen', 'Dave', 'Edward']
name2 = ['John', 'Cena', 'Ali', 'Donald', 'Edward']

common_names = list(set(name1) & set(name2))
print(f"{common_names = }")

uncommon_names = list(set(name1).symmetric_difference(set(name2)))
print(f"{uncommon_names = }")

all_names = list(set(name1) | set(name2))
print(f"{all_names = }")

#%% Conditional statement
mark = 45
if mark >= 50:
    print("Passed the test")
    print("Still passed the test")
    print("Passed the test again")
else:
    print("Failed the test")
    print("Still failed the test")
    print("Failed the test again")
print("Outside of if-else")

#%% Ternary operator
num = int(input("Enter an integer: "))
print(f"This is an {'even' if num % 2 == 0 else 'odd'} number.")

# Use if-else statement to perform the same operation
if num % 2 == 0:
    ans = 'even'
else:
    ans = 'odd'
print(f"This is an {ans} number.")

#%% False value testing
alist = []

# Method 1 - Use len() to check whether a list is empty
if len(alist) > 0:
    print("The list is not empty")
else:
    print("The list is empty")    

# Method 2 - Check the list itself (empty list is evaluated as false)
if alist:
    print("The list is not empty")
else:
    print("The list is empty")
    
#%% For loop
# Use zip() to iterate multiple lists (limited by the shortest list)
names = ['ali', 'baba', 'cloud', 'data']
ages = [13, 37, 23, 32, 45, 56]
blood_types = ['a', 'o', 'b', 'o', 'ab']

for i, j, k in zip(names, ages, blood_types):
    print(f"{i.capitalize()} is {j} years old with blood type {k.upper()}.")

# Automatically add an index to each iteration using enumerate()
for h, (i, j, k) in enumerate(zip(names, ages, blood_types), start=1):
    print(f"{h}. {i.capitalize()} is {j} years old with blood type {k.upper()}.")

#%% Using pass (ellipsis), break and continue to control loop

while True:
    name = input("Enter your name: ") or "Noname"
    print(f"Hello {name}")
    ...
    ans = input("Do you want to repeat? ([y]/n) ").lower() or 'y'
    if ans in ('y', 'yes'):
        continue
    elif ans in ('n', 'no'):
        print("Good bye!")
    else:
        print("Invalid choice!")
    break

#%% List comprehension example 1
# Select the words that start with vowels
words = ('ant', 'boy', 'eggs', 'cat', 'donkey', 'whale', 'orange')

# Method 1 - Use for loop
vowel_words1 = []
for w in words:
    if w[0] in 'aeiou':
        vowel_words1.append(w)
print(f"{vowel_words1 = }")

# Method 2 - Use list comprehension
vowel_words2 = [w for w in words if w[0] in 'aeiou']
print(f"{vowel_words2 = }")

#%% List comprehension example 2
# Calculate the number of odd numbers in a list
from random import randint
numbers = [randint(1, 100) for _ in range(100)]

# Method 1 - Use for loop
count = 0
for n in numbers:
    if n % 2 == 1:
        count += 1
print(f"There are {count} odd numbers in the list.")

# Method 2 - Use list comprehension
count2 = sum([n%2 for n in numbers])
print(f"There are {count2} odd numbers in the list.")

#%% Dictionary comprehension
# Create a new dictionary for discounted price (10%)
prices = dict(apple=1.5, orange=2.5, durian=20, mango=10)

# Method 1 - Use for loop
new_prices1 = {}
for k in prices:
    new_prices1[k] = prices[k] * 0.9
print(f"{new_prices1 = }")

# Method 2 - Use dictionary comprehension
new_prices2 = {k: prices[k] * 0.9 for k in prices}
print(f"{new_prices2 = }")

#%% Use any() and all() function
# Check whether any word in the tuple starts with a vowel
words = ('bees', 'cat', 'eggs')

# Method 1 - Use for loop
ans = False
for w in words:
    if w[0] in 'aeiou':
        ans = True
if ans:
    print("There is at least a word starting with a vowel")
else:
    print("There is no word starting with a vowel")
    
# Method 2 - Use any() and list comprehension
if any(True if w[0] in 'aeiou' else False for w in words):
    print("There is at least a word starting with a vowel")
else:
    print("There is no word starting with a vowel")

# Use all() and list comprehension to check all values
if all(True if w[0] in 'aeiou' else False for w in words):
    print("All words start with a vowel")
else:
    print("Not all words start with a vowel")

# Checking empty lists
list1 = [1, 2]
list2 = [3, 4]
list3 = [5, 6, 7]

if all((list1, list2, list3)):
    print("All lists are not empty")
else:
    print("Some of the lists are empty")    














