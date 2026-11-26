# Q1. Check whether a number is positive, negative, or zero

def numDetector(num):
    if num < 0:
        return "negative"
    elif num > 0:
        return "positive"
    else:
        return "zero"


print(numDetector(1))
print(numDetector(1282.99292))
print(numDetector(-0))
print(numDetector(-22))


# Q2. Find the largest of three numbers without using max()

def largest(a, b, c):
    if a == b and b == c:
        return "All numbers are equal"
    elif a >= b and a >= c:
        return f"{a} is the largest"
    elif b >= a and b >= c:
        return f"{b} is the largest"
    else:
        return f"{c} is the largest"


print(largest(1, 1, 1))
print(largest(1, 3, 4))
print(largest(92, 8, 0))
print(largest(-1, -19, 0))
print(largest(193, 92, 0))
print(largest(5, 5, 3))


# Q3. Check whether a year is a leap year

def isLeap(year):
    if year % 400 == 0:
        return "Leap Year"
    elif year % 100 == 0:
        return "Not a Leap Year"
    elif year % 4 == 0:
        return "Leap Year"
    else:
        return "Not a Leap Year"


print(isLeap(2027))
print(isLeap(2004))
print(isLeap(0))
print(isLeap(1900))
print(isLeap(2000))