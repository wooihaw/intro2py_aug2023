# Write a Python script to ask for an integer number, 
# and print the corresponding binary and hexadecimal numbers.
# E.g.
# Enter an integer: 1234
# Binary: 10011010010, Hexadecimal: 4d2

num = input("Enter an integer: ")

if num.isdigit():
    print(f"Binary: {int(num):b}, Hexadecimal: {int(num):x}")
else:
    print("Invalid input!")