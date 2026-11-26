# Topic 1: Python Operators

# Q1. Predict the output

a = 10
b = 3

print(a // b)
print(a % b)
print(a ** b)
print(a / b)

# Output:
# 3
# 1
# 1000
# 3.3333333333333335


# Q2. What will be the output?

x = 5
x += 3
x *= 2
x -= 4

print(x)

# Output:
# 12


# Q3. Sum of digits of a four-digit integer without converting into a string

num = int(input("Enter a 4-digit number: "))
total = 0

for i in range(4):
    rem = num % 10
    total += rem
    num //= 10

print("Sum of digits:", total)


# Q4. Predict the output

a = 10
b = 20
c = 30

result = a < b and b > c or a == 10

print(result)

# Output:
# True


# Q5. Swap two variables without using a third variable

def swap(a, b):
    a = a + b
    b = a - b
    a = a - b

    return a, b


print(swap(1, 2))

# Output:
# (2, 1)


# Topic 2: Python Data Types

# Q1. Predict the output

x = 10
y = 10.0
z = "10"

print(type(x))
print(type(y))
print(type(z))
print(x == y)
print(x == z)

# Output:
# <class 'int'>
# <class 'float'>
# <class 'str'>
# True
# False


# Q2. What will happen here?

a = True
b = 5

print(a + b)
print(a * b)
print(type(a + b))

# Output:
# 6
# 5
# <class 'int'>


# Q3. Identify the data type of each variable

a = [1, 2, 3]
b = (1, 2, 3)
c = {1, 2, 3}
d = {"name": "John"}
e = None
f = 3 + 4j

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

# Output:
# <class 'list'>
# <class 'tuple'>
# <class 'set'>
# <class 'dict'>
# <class 'NoneType'>
# <class 'complex'>


# Q4. Write a program that determines whether a value is an integer, float, or something else

def isInt(num):
    if type(num) == int:
        print("int")
    elif type(num) == float:
        print("float")
    else:
        print("something else")


isInt(1)
isInt(2.33)
isInt("jsjs")
isInt(True)

# Output:
# int
# float
# something else
# something else


# Q5. Predict the output

a = [1, 2, 3]
b = a
c = a.copy()

b.append(4)
c.append(5)

print(a)
print(b)
print(c)

# Output:
# [1, 2, 3, 4]
# [1, 2, 3, 4]
# [1, 2, 3, 5]