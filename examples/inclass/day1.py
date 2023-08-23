# In-class examples for Day 1

#%% Numeric data types
a = 1239840912830467729834098297231979021380823089407892302398
b = a ** 10
print(a, b)
print(a.__sizeof__())
print(b.__sizeof__())

c = 1_234_567_890
print(c)

#%% Binary and hexadecimal numbers
a = 0b10110101
b = 0x12cafe
print(a, b)
print(bin(a), hex(b))

#%% Variables
# class = 1  # Using keyword as a variable name will cause a syntax error

a = 'abc'
print(type(a))

# type = 1  # Built-in function will be shadowed by variable of the same name
# print(type(a))

#%% Convert between data types
a, b, c = 1, 2.5, '789'
print(type(a), type(b), type(c), sep=',')

d = float(a)
e = int(b)
f = int(c)

print(d, e, f, sep=',')

g = '123abc'  # A string representing a hex number
h = int(g, base=16)
print(h, hex(h))

#%% Arithmetic operators
a = 3 ** 2
b = -3 ** 2
c = (-3) ** 2 
print(a, b, c, sep=',')

#%% Comparison operators
a = 10
b = 25
print(a < b)
print(a > b)
print(a == b)
print(a != b)

print(0 <= a < 20)
print(50 <= b < 100)

#%% String indexing and slicing
s = "Introduction to Python"
print("First character: ", s[0])
print("Last character: ", s[-1])
print("First 12 characters: ", s[:12])
print("Last 6 characters: ", s[-6:])

print("Reverse string: ", s[::-1])

#%% String methods
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.replace('n', 'm'))
print(s)

#%% String methods 2
s1 = 'Abc'
s2 = '123'
s3 = s1 + s2

print(s1.isalpha())
print(s2.isdigit())
print(s3.isalpha())
print(s3.isalnum())

s4 = s3.lower().replace('A', 'z')  # String methods can be chained
print(s4)

#%% f-string formatting
a = 12.345
b = 6789

print(f"{a = }, {a = :.1f}, {a = :.2f}, {a = :.5f}")

print(f"{b = }, {b = :08x}, {b = :016b}")

print("Python is a \N{snake}")

#%% Getting input
ans = input("Enter a number: ")

print(f"{ans = }, {type(ans) = }")

print(f"10 times of the number is {10 * ans}")

if ans.isdigit():
    print(f"10 times of the number is {10 * int(ans)}")
else:
    print("Invalid input!")



















