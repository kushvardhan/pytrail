# Python Fundamentals 01
## Variables, Objects, Data Types & Type Conversion

## 1. Variables

A variable is a name that refers to an object in memory. Python does not require explicit type declarations.

```python
name = "Kush"
age = 23
height = 5.11
is_learning = True
```

### Naming Rules

- Must start with a letter or underscore.
- Cannot start with a number.
- Can contain letters, numbers and underscores.
- Case-sensitive: `name` and `Name` are different.
- Cannot use reserved keywords.
- Use `snake_case` for variable names.

```python
user_name = "Kush"
total_amount = 500
_private_value = 10
```

Check reserved keywords:

```python
import keyword

print(keyword.kwlist)
print(keyword.iskeyword("class"))  # True
```

### Multiple Assignment

```python
a, b, c = 10, 20, 30

x = y = z = 100

a, b = b, a
```

Python supports unpacking:

```python
first, *middle, last = [1, 2, 3, 4, 5]

print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5
```

Wrong number of unpacked values raises `ValueError`.

```python
a, b = [10, 20, 30]  # ValueError
```

---

## 2. Variables vs Objects

Python is dynamically typed and strongly typed.

- Dynamic typing: variable names do not have fixed declared types.
- Strong typing: Python does not freely combine incompatible types.

```python
value = 100
value = "Python"
value = True
```

The same name can reference objects of different types.

### Important: Names and References

```python
a = 10
b = a

a = 20

print(a)  # 20
print(b)  # 10
```

`b` still references the original integer object.

### Mutable Object Behaviour

```python
a = [1, 2, 3]
b = a

a.append(4)

print(a)  # [1, 2, 3, 4]
print(b)  # [1, 2, 3, 4]
```

Both names reference the same list.

### Object Identity

```python
a = [1, 2]
b = [1, 2]
c = a

print(a == b)  # True
print(a is b)  # False
print(a is c)  # True

print(id(a))
print(id(b))
```

- `==` compares values.
- `is` compares object identity.
- `id()` returns an object's identity during its lifetime.

Do not use `is` to compare ordinary values.

---

## 3. Python Data Types

Python objects have types. Use `type()` to inspect them.

```python
print(type(10))       # int
print(type(10.5))     # float
print(type("Hello"))  # str
print(type(True))     # bool
print(type(None))     # NoneType
```

### Numeric Types

| Type | Examples |
|---|---|
| int | `10`, `-5`, `0` |
| float | `10.5`, `-2.5` |
| complex | `2+3j` |
| bool | `True`, `False` |

### Sequence Types

| Type | Example | Mutable |
|---|---|---|
| str | `"Python"` | No |
| list | `[1, 2, 3]` | Yes |
| tuple | `(1, 2, 3)` | No |
| range | `range(5)` | No |

### Other Built-in Types

| Type | Example | Mutable |
|---|---|---|
| set | `{1, 2, 3}` | Yes |
| frozenset | `frozenset({1, 2})` | No |
| dict | `{"name": "Kush"}` | Yes |
| bytes | `b"hello"` | No |
| bytearray | `bytearray(b"hello")` | Yes |
| NoneType | `None` | No |

### Checking Types

```python
value = True

print(type(value))
print(isinstance(value, bool))  # True
print(isinstance(value, int))   # True
```

`isinstance()` also checks inheritance.

### Interesting Python Behaviour

```python
print(isinstance(True, int))  # True
print(True + True)            # 2
print(False * 10)             # 0
```

In Python, `bool` is a subclass of `int`.

---

## 4. Mutable vs Immutable Types

### Mutable

Objects can be changed after creation.

Examples:

- list
- dict
- set
- bytearray

```python
numbers = [1, 2, 3]
numbers.append(4)

print(numbers)  # [1, 2, 3, 4]
```

### Immutable

Objects cannot be changed after creation.

Examples:

- int
- float
- bool
- str
- tuple
- frozenset
- bytes

```python
name = "Python"
name = name + " Programming"

print(name)
```

A new string is created rather than modifying the original string.

### Tuple Gotcha

A tuple is immutable, but it can contain mutable objects.

```python
data = ([1, 2], 3)

data[0].append(4)

print(data)  # ([1, 2, 4], 3)
```

The tuple's structure cannot be changed, but its contained list can.

---

## 5. Integers and Floating-Point Numbers

Python integers have arbitrary precision, limited by available memory.

```python
number = 999999999999999999999999999999999999
print(number)
```

Unlike fixed-width integer types in Java or Go, ordinary Python integers do not overflow at a fixed 32-bit or 64-bit boundary.

### Integer Division

```python
print(10 / 3)   # 3.333...
print(10 // 3)  # 3
print(10 % 3)   # 1
```

Important: `//` performs floor division, not simply truncation toward zero.

```python
print(-7 // 2)  # -4
print(-7 % 2)   # 1
```

Python maintains the relationship:

`a == (a // b) * b + (a % b)`

For positive and negative divisors, the remainder follows the divisor's sign.

### Floating-Point Precision

```python
print(0.1 + 0.2)
# 0.30000000000000004
```

Many decimal fractions cannot be represented exactly in binary floating-point.

For approximate comparison:

```python
import math

print(math.isclose(0.1 + 0.2, 0.3))  # True
```

For exact decimal arithmetic:

```python
from decimal import Decimal

a = Decimal("0.1")
b = Decimal("0.2")

print(a + b)  # 0.3
```

Avoid constructing `Decimal` directly from floats when exact decimal input is intended.

### Special Floating-Point Values

```python
import math

print(float("inf"))
print(float("-inf"))
print(float("nan"))

print(math.isnan(float("nan")))  # True
```

`NaN` is unusual:

```python
nan = float("nan")

print(nan == nan)  # False
```

---

## 6. Strings

Strings represent Unicode text and are immutable sequences.

```python
language = "Python"

print(language[0])    # P
print(language[-1])   # n
print(language[0:3])  # Pyt
print(language[::-1]) # nohtyP
```

### Indexing

```python
text = "Python"

print(text[0])   # P
print(text[-1])  # n
print(text[6])   # IndexError
```

Negative indexes count from the end.

### Slicing

Syntax:

`sequence[start:stop:step]`

The stop index is excluded.

```python
text = "Python"

print(text[1:4])   # yth
print(text[:3])    # Pyt
print(text[3:])    # hon
print(text[::2])   # Pto
print(text[::-1])  # nohtyP
```

Out-of-range slicing does not raise an error.

```python
print(text[100:])  # ''
```

### String Immutability

```python
text = "Python"

text[0] = "J"  # TypeError
```

### String Formatting

F-strings are generally the cleanest option.

```python
name = "Kush"
age = 23

print(f"My name is {name} and I am {age}.")
```

Formatting options:

```python
price = 1234.5678

print(f"{price:.2f}")       # 1234.57
print(f"{price:,.2f}")      # 1,234.57
print(f"{0.25:.0%}")        # 25%
```

### Useful String Methods

```python
text = "  Hello Python  "

print(text.strip())
print(text.lstrip())
print(text.rstrip())
print(text.lower())
print(text.upper())
print(text.title())
print(text.capitalize())
print(text.replace("Python", "World"))
print(text.split())
print(text.find("Python"))
print(text.startswith("  Hello"))
print(text.endswith("  "))
```

### String Membership

```python
text = "Python Programming"

print("Python" in text)  # True
print("Java" not in text)  # True
```

### Escape Characters

```python
print("Hello\nWorld")
print("Hello\tWorld")
print("He said \"Hello\"")
print("C:\\Users\\Kush")
```

Raw strings are useful for paths and regular expressions.

```python
path = r"C:\Users\Kush\Documents"
print(path)
```

### Unicode

```python
text = "Python 🐍"

print(len(text))
print(text[7])
```

Python strings operate on Unicode code points, not grapheme clusters. Some visible characters consist of multiple code points.

---

## 7. Type Conversion

Converting an object from one type to another.

### Explicit Conversion

```python
age = int("23")
price = float("99.50")
name = str(100)
numbers = list((1, 2, 3))
```

### Common Conversions

| Function | Purpose |
|---|---|
| `int()` | Convert to integer |
| `float()` | Convert to float |
| `str()` | Convert to string |
| `bool()` | Convert to boolean |
| `list()` | Convert to list |
| `tuple()` | Convert to tuple |
| `set()` | Convert to set |
| `dict()` | Construct a dictionary |
| `bytes()` | Construct bytes |
| `complex()` | Construct complex number |

### Conversion Edge Cases

```python
int("25")       # 25
int("25.5")     # ValueError
int(25.9)       # 25
float("25.5")   # 25.5

int(True)       # 1
int(False)      # 0

bool(0)         # False
bool(1)         # True
bool("")        # False
bool("False")   # True
bool([])        # False
bool([0])       # True
```

`int()` truncates floating-point values toward zero.

### Base Conversion

```python
print(int("1010", 2))  # 10
print(int("17", 8))    # 15
print(int("FF", 16))   # 255

print(bin(10))  # 0b1010
print(oct(10))  # 0o12
print(hex(255)) # 0xff
```

### Conversion Errors

```python
int("hello")  # ValueError
int(None)     # TypeError
```

Never assume conversion will always succeed when working with user input or external data.

---

## 8. Truthy and Falsy Values

Python uses truth-value testing in conditions.

### Falsy Values

- `False`
- `None`
- `0`
- `0.0`
- `0j`
- `""`
- `[]`
- `()`
- `{}`
- `set()`
- `range(0)`

Most other objects are truthy.

```python
print(bool(""))       # False
print(bool("0"))      # True
print(bool("False"))  # True
print(bool([]))       # False
print(bool([0]))      # True
```

### Custom Truthiness

A custom class can define its truth value using `__bool__()` or `__len__()`.

```python
class Box:
    def __len__(self):
        return 0

print(bool(Box()))  # False
```

---

## 9. User Input

`input()` always returns a string.

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Hello {name}, age {age}")
```

### Multiple Inputs

```python
a, b = input("Enter two values: ").split()

print(a, b)
```

Both values are strings.

For integers:

```python
a, b = map(int, input("Enter numbers: ").split())

print(a + b)
```

### Safe Input Handling

```python
try:
    age = int(input("Enter age: "))
    print(age)
except ValueError:
    print("Please enter a valid integer.")
```

Input validation is important because users can enter empty strings, invalid numbers or unexpected data.

---

## 10. None and Identity

`None` represents the absence of a value.

```python
result = None

if result is None:
    print("No result")
```

Use:

- `is None`
- `is not None`

Avoid comparing `None` using equality when checking for the singleton itself.

### Equality vs Identity

```python
a = [1, 2]
b = [1, 2]

print(a == b)  # True
print(a is b)  # False
```

Do not depend on object interning or implementation-specific identity behaviour for integers and strings.

---

## 11. Python vs Other Languages

| Feature | Python | Java | Go |
|---|---|---|---|
| Variable declaration | Dynamic | Static | Static |
| Type annotation required | No | Yes | Yes |
| Integer precision | Arbitrary | Fixed-width | Fixed-width |
| String mutability | Immutable | Immutable | Immutable |
| Boolean | `True`, `False` | `true`, `false` | `true`, `false` |
| Null-like value | `None` | `null` | `nil` |
| Multiple assignment | Yes | Limited | Yes |
| Semicolons | Usually unnecessary | Usually required | Usually required |

Important differences:

- Python uses indentation to define code blocks.
- Python is dynamically typed but strongly typed.
- Python's `bool` is a subclass of `int`.
- Python integers support arbitrary precision.
- Python's `input()` returns a string.
- Python uses `None` rather than `null` or `nil`.
- Python supports multiple assignment and unpacking.
- Python has no separate character type; a single character is a string.

---

## 12. Common Errors

| Error | Common cause |
|---|---|
| `NameError` | Using an undefined name |
| `TypeError` | Incompatible operation or wrong argument type |
| `ValueError` | Correct type but invalid value |
| `IndexError` | Invalid sequence index |
| `KeyError` | Missing dictionary key |
| `ZeroDivisionError` | Dividing by zero |
| `AttributeError` | Accessing a missing attribute |
| `OverflowError` | Numeric operation exceeds a supported range |

Examples:

```python
print(unknown_variable)  # NameError
```

```python
print("10" + 10)  # TypeError
```

```python
int("hello")  # ValueError
```

```python
[1, 2][5]  # IndexError
```

---

## 13. Practice Exercises

### Variables and References

1. Create variables for your name, age, height and learning status.
2. Swap two variables without using a third variable.
3. Demonstrate multiple assignment.
4. Show the difference between reassignment and mutation.
5. Create two variables referencing the same list and demonstrate the effect of modifying it.

### Data Types

6. Identify the types of at least 10 different values.
7. Demonstrate why `isinstance(True, int)` returns `True`.
8. Create examples of mutable and immutable objects.
9. Demonstrate a tuple containing a mutable list.
10. Check the truthiness of different values.

### Strings and Numbers

11. Reverse a string without using a loop.
12. Extract a substring using slicing.
13. Format a price to two decimal places.
14. Demonstrate floating-point precision issues.
15. Compare `//`, `/` and `%` with positive and negative values.

### Type Conversion and Input

16. Take a user's age as input and convert it into an integer.
17. Convert a binary string into a decimal integer.
18. Demonstrate why `bool("False")` returns `True`.
19. Handle invalid numeric input.
20. Take multiple numbers in a single input statement and calculate their sum.

---

## 14. Key Takeaways

- Variables are names referencing objects.
- Python is dynamically and strongly typed.
- Every value is an object.
- Objects can be mutable or immutable.
- `==` compares values; `is` compares identity.
- Strings are immutable Unicode sequences.
- Python integers have arbitrary precision.
- Floating-point arithmetic has precision limitations.
- `input()` always returns a string.
- `bool` is a subclass of `int`.
- `None` represents the absence of a value.
- Type conversion can raise exceptions.
- Truthiness is used extensively in Python conditions.
