# Learning Log 01 — Python Basics

**Date:** 25 November 2026  
**Topic:** Variables, Data Types & Type Conversion  
**Status:** In Progress

---

## 1. Variables

Variables are names that reference objects in memory. Python does not require explicit type declarations.

```python
name = "Kush"
age = 23
height = 5.11
is_learning = True
```

### Rules
- Must start with a letter or underscore.
- Cannot start with a number.
- Can contain letters, numbers and underscores.
- Case-sensitive (`name` and `Name` are different).
- Cannot use Python keywords (`class`, `if`, `for`, etc.).
- Use `snake_case` for variable names.

### Multiple Assignments

```python
a, b, c = 10, 20, 30

x = y = z = 100

a, b = b, a
```

### Interesting Behaviour

```python
a = 10
b = a

a = 20

print(a)  # 20
print(b)  # 10
```

Reassigning `a` does not change `b`.

But mutable objects behave differently:

```python
a = [1, 2, 3]
b = a

a.append(4)

print(b)  # [1, 2, 3, 4]
```

Both names reference the same list.

---

## 2. Data Types

Python is dynamically typed. A variable can reference objects of different types during its lifetime.

### Basic Types

| Type | Example |
|---|---|
| int | `10`, `-5`, `0` |
| float | `10.5`, `-2.5` |
| str | `"Python"` |
| bool | `True`, `False` |
| NoneType | `None` |
| complex | `2 + 3j` |

### Collection Types

| Type | Example | Mutable? |
|---|---|---|
| list | `[1, 2, 3]` | Yes |
| tuple | `(1, 2, 3)` | No |
| set | `{1, 2, 3}` | Yes |
| dict | `{"name": "Kush"}` | Yes |

### Checking Types

```python
age = 23

print(type(age))          # <class 'int'>
print(isinstance(age, int))  # True
```

Prefer `isinstance()` when checking whether an object belongs to a type or its subclasses.

### Interesting Behaviour

```python
print(type(True))          # <class 'bool'>
print(isinstance(True, int))  # True

print(type(10 / 2))        # <class 'float'>
print(type(10 // 2))       # <class 'int'>
```

In Python, `bool` is a subclass of `int`.

---

## 3. Strings

Strings represent text and are immutable.

```python
name = "Python"

print(name[0])     # P
print(name[-1])    # n
print(name[0:3])   # Pyt
print(name[::-1])  # nohtyP
```

### String Formatting

```python
name = "Kush"
age = 23

print(f"My name is {name} and I am {age}.")
```

### Useful Methods

```python
text = "  Hello Python  "

print(text.strip())
print(text.lower())
print(text.upper())
print(text.replace("Python", "World"))
print(text.split())
```

### Edge Cases

```python
name = "Python"

name[0] = "J"  # TypeError: strings are immutable
```

```python
text = "Python"

print(text[100:])  # Empty string
print(text[100])   # IndexError
```

Slicing out-of-range indexes is allowed; direct indexing is not.

---

## 4. Type Conversion

Converting one data type into another.

### Explicit Conversion

```python
age = "23"

age = int(age)
price = float("99.50")
number = str(100)

print(age)
print(price)
print(number)
```

### Implicit Conversion

Python automatically converts certain compatible types.

```python
a = 10
b = 2.5

result = a + b

print(result)       # 12.5
print(type(result)) # float
```

### Conversion Edge Cases

```python
int("25")       # 25
int("25.5")     # ValueError
float("25.5")   # 25.5

int(True)       # 1
int(False)      # 0

bool(0)         # False
bool(1)         # True
bool("")        # False
bool("False")   # True
```

Important: `bool("False")` is `True` because every non-empty string is truthy.

---

## 5. User Input

Python's `input()` always returns a string.

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Hello {name}, you are {age}.")
```

### Common Mistake

```python
age = input("Enter age: ")

print(age + 5)  # TypeError
```

Correct:

```python
age = int(input("Enter age: "))

print(age + 5)
```

### Safer Input Handling

```python
try:
    age = int(input("Enter age: "))
    print(age)
except ValueError:
    print("Please enter a valid integer.")
```

---

## 6. Numbers & Precision

Python supports integers and floating-point numbers.

```python
print(10 / 3)     # 3.333333...
print(10 // 3)    # 3
print(10 % 3)     # 1
print(2 ** 3)     # 8
```

### Floating-Point Precision

```python
print(0.1 + 0.2)

# 0.30000000000000004
```

This happens because many decimal fractions cannot be represented exactly in binary floating-point.

For approximate comparisons:

```python
import math

print(math.isclose(0.1 + 0.2, 0.3))  # True
```

For exact decimal calculations, explore the `decimal` module.

### Division Edge Case

```python
print(10 / 0)  # ZeroDivisionError
```

---

## 7. Identity, Equality & None

These are not the same:

- `==` compares values.
- `is` compares object identity.

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # True
print(a is b)  # False
print(a is c)  # True
```

### None

`None` represents the absence of a value.

```python
result = None

if result is None:
    print("No result available")
```

Use `is None`, not `== None`.

---

## 8. Practice

Try solving these without looking at solutions.

1. Swap two variables without using a third variable.
2. Take a user's name, age and height as input.
3. Convert a string containing a number into an integer.
4. Check the type of different variables.
5. Reverse a string using slicing.
6. Explain why `bool("False")` returns `True`.
7. Find the difference between `==` and `is`.
8. Demonstrate how two variables can reference the same list.
9. Calculate the remainder and quotient of two numbers.
10. Handle invalid integer input using `try-except`.

---

## 9. Key Takeaways

- Python is dynamically typed.
- Variables reference objects.
- Python has mutable and immutable data types.
- `input()` always returns a string.
- Explicit conversion can raise `ValueError` or `TypeError`.
- `bool` is a subclass of `int`.
- `==` checks equality; `is` checks identity.
- Floating-point calculations can have precision errors.
- Empty collections, zero, `None` and empty strings are falsy.

---

## 10. Further Reading

- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- [Python Built-in Types](https://docs.python.org/3/library/stdtypes.html)
- [Python Built-in Functions](https://docs.python.org/3/library/functions.html)
- [Python Data Model](https://docs.python.org/3/reference/datamodel.html)

**Next Topic:** Operators, Expressions & Control Flow