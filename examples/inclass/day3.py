# In-class examples for Day 3
#%% Functions and return value
def myfunc1(x, y):
    print(x, y)

def myfunc2(x: int, y: int) -> int:
    '''This is a function to add 2 arguments'''
    return x + y

a = myfunc1(11, 22)

b = myfunc2(33, 44)

print(f"{a = }, {b = }")

alist = [3, 1, 2, 5, 4]

blist = sorted(alist)
print(f"{alist = }, {blist = }")

clist = alist.sort()
print(f"{alist = }, {clist = }")

#%% Function that returns multiple values
def myfunc3(x: int, y: int, z: int) -> tuple[int]: #This is a function
    '''This is a function which returns 3 values'''
    return x**2, y**3, z**4

a = myfunc3(2, 3, 4)
print(f"{a = }, {type(a) = }")

b, c, d = myfunc3(5, 6, 7)
print(f"{b = }, {c = }, {d = }")

#%% Functions are objects
def func1(x):
    return x + 1

def func2(y):
    return y - 1

def func3(z):
    return z * 2

functions = (func1, func2, func3)
for f in functions:
    print(f(10))

d_func = {'function1': func1, 'function2': func2, 'function3': func3}
for k in d_func:
    print(f"{k} output: {d_func[k](10)}")

#%% Lambda function example 1
alist = [(1, 2, 3), (11, 4, 1), (7, 9, 2)]
blist = sorted(alist)
print(f"{blist = }")

# To sort according to 3rd element in ascending order
clist = sorted(alist, key=lambda x: x[2])
print(f"{clist = }")

#%% Lambda function example 2
# Sort the list based on the ID numbers
ID = ['ID21', 'ID7', 'ID55', 'ID101', 'ID3', 'ID82', 'ID12']

sorted_ID = sorted(ID)
print(f"{sorted_ID = }")

sorted_ID2 = sorted(ID, key=lambda x: int(x[2:]))
print(f"{sorted_ID2 = }")

print(min(ID, key=lambda x: int(x[2:])))
print(max(ID, key=lambda x: int(x[2:])))

d = {'a': 3, 'b':1, 'c': 2, 'd':1}
print(max(d, key=lambda x: d[x]))

#%% Lambda function example 3
GID =  ['G2ID25', 'G2ID2', 'G1ID14', 'G1ID2']

print(sorted(GID))

# Sort G in descending order and ID in ascending order
print(sorted(GID, key=lambda x: (-int(x[1]), int(x[4:]))))

#%% Using map() function
# Reverse each string in a list
words = ['apple', 'bell', 'cat', 'door', 'eggs']

# Method 1 - Use for loop
r1 = []
for w in words:
    r1.append(w[::-1])
print(f"{r1 = }")    

# Method 2 - Use list comprehension
r2 = [w[::-1] for w in words]
print(f"{r2 = }")

# Method 3 - Use map() function
r3 = list(map(lambda w: w[::-1], words))
print(f"{r3 = }")    

#%% Using filter() function
# Select only the palindrome from a list
words = ('ant', 'boy', 'civic', 'dad', 'madam', 'fish')

# Method 1 - Use for loop
p1 = []
for w in words:
    if w == w[::-1]:
        p1.append(w)
print(f"{p1 = }")    

# Method 2 - Use list comprehension
p2 = [w for w in words if w == w[::-1]]
print(f"{p2 = }")    

# Method 3 - Use filter() function
p3 = list(filter(lambda w: w == w[::-1], words))
print(f"{p3 = }")    

#%% Combining map() and filter()
# Find the square of even numbers from 1 to 20

# Method 1 - Use for loop
s1 = []
for n in range(1, 21):
    if n % 2 == 0:
        s1.append(n*n)
print(f"{s1 = }")

# Method 2 - Use list comprehension
s2 = [n*n for n in range(1, 21) if n % 2 == 0]
print(f"{s2 = }")

# Method 3 - Use map() and filter()
s3 = list(map(lambda n: n*n, filter(lambda n: n % 2 == 0, range(1, 21))))
print(f"{s3 = }")    

#%% Iterator

alist = list(range(10000000))
print(alist.__sizeof__())

myiter = iter(alist)
print(myiter.__sizeof__())

for i in myiter:
    if i == 1000:
        break
    print(i)

#%% OOP example
class Rectangle:
    desc = 'This is a rectangle'  # class attribute
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.__secret = "Top secret"  # private attribute
    def __str__(self):
        return f"Rectangle with length of {self.length} and width of {self.width}"
    def __repr__(self):
        return f"Rectangle({self.length}, {self.width})"
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2*self.length + 2*self.width
    def __eq__(self, other):
        return self.area() == other.area()
    def __gt__(self, other):
        return self.area() > other.area()
    def reveal_secret(self):
        return f"The secret is {self.__secret}"
    
rec1 = Rectangle(2, 3)
rec2 = Rectangle(3, 4)
print(rec1, rec2, sep="\n")

alist = [rec1, rec2]
print(alist)

print(f"{rec1.area() = }, {rec2.area() = }")
print(f"{rec1.perimeter() = }, {rec2.perimeter() = }")

print(rec1 == rec2)
print(rec1 > rec2)
print(rec1 < rec2)

rec3 = Rectangle(1, 2)
alist.append(rec3)
print(sorted(alist))

print(rec1.length)
print(rec1.reveal_secret())

#%% Child class
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
    def __str__(self):
        return f"Square with side of {self.length}"
    def __repr__(self):
        return f"Square({self.length})"

sqr1 = Square(1)
sqr2 = Square(2)
sqr3 = Square(3)

print(sqr1, sqr2, sqr3, sep=",")

blist = [sqr3, sqr1, sqr2]
print(f"{blist = }")
print(sorted(blist))

print(f"{sqr1.area() = }, {sqr1.perimeter() = }")







