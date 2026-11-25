# Python Fundamentals 02
## Operators, Expressions, Conditions & Loops

## 1. Operators

Operators perform operations on values and variables.

Python has several operator categories:

| Category | Operators |
|---|---|
| Arithmetic | `+`, `-`, `*`, `/`, `//`, `%`, `**`, `@` |
| Comparison | `==`, `!=`, `>`, `<`, `>=`, `<=` |
| Assignment | `=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=` |
| Logical | `and`, `or`, `not` |
| Bitwise | `&`, `|`, `^`, `~`, `<<`, `>>` |
| Membership | `in`, `not in` |
| Identity | `is`, `is not` |
| Conditional expression | `value_if_true if condition else value_if_false` |

---

## 2. Arithmetic Operators

Used for mathematical calculations.

```python
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000
```

### Floor Division

`//` rounds the result down towards negative infinity.

```python
print(7 // 2)    # 3
print(-7 // 2)   # -4
print(7 // -2)   # -4
```

This differs from languages where integer division truncates toward zero.

### Modulus

Returns the remainder.

```python
print(10 % 3)   # 1
print(-7 % 3)   # 2
print(7 % -3)   # -2
```

The remainder has the same sign as the divisor when it is non-zero.

### Exponentiation

```python
print(2 ** 3)   # 8
print(9 ** 0.5) # 3.0
```

Python also supports complex results in certain mathematical operations.

### Matrix Multiplication

`@` is the matrix multiplication operator.

```python
# Usually used with libraries such as NumPy.
# Its behaviour depends on the objects implementing it.
```

### Division by Zero

```python
print(10 / 0)  # ZeroDivisionError
```

---

## 3. Operator Precedence

Python follows a defined order when evaluating expressions.

General order, from higher to lower precedence:

1. Parentheses and grouping
2. Exponentiation
3. Unary operators (`+x`, `-x`, `~x`)
4. Multiplication, division, floor division, modulus, matrix multiplication
5. Addition and subtraction
6. Bitwise shifts
7. Bitwise AND
8. Bitwise XOR
9. Bitwise OR
10. Comparisons, membership and identity
11. `not`
12. `and`
13. `or`
14. Conditional expression
15. `lambda`
16. Assignment expression (`:=`)

Use parentheses whenever the intended order is not obvious.

```python
result = 10 + 5 * 2

print(result)  # 20
```

```python
result = (10 + 5) * 2

print(result)  # 30
```

### Interesting Behaviour: Exponentiation

Exponentiation is right-associative.

```python
print(2 ** 3 ** 2)  # 512

# Equivalent to:
print(2 ** (3 ** 2))
```

Unary minus and exponentiation:

```python
print(-2 ** 2)    # -4
print((-2) ** 2)  # 4
```

---

## 4. Comparison Operators

Used to compare two values. The result is generally a boolean.

```python
a = 10
b = 20

print(a == b)  # False
print(a != b)  # True
print(a > b)   # False
print(a < b)   # True
print(a >= b)  # False
print(a <= b)  # True
```

### Chained Comparisons

Python supports mathematical-style chained comparisons.

```python
age = 23

print(18 <= age <= 60)  # True
```

This is equivalent to:

```python
print(18 <= age and age <= 60)
```

The middle expression is evaluated only once.

### Comparing Different Types

```python
print(10 == 10.0)  # True
print(10 == "10")  # False
```

Equality can compare different types.

But ordering unrelated types generally raises an error:

```python
print(10 > "5")  # TypeError
```

### Boolean and Integer Comparisons

```python
print(True == 1)   # True
print(False == 0)  # True
```

Be careful when comparing values from different types.

---

## 5. Assignment Operators

Assignment operators update variables.

```python
x = 10

x += 5
print(x)  # 15

x -= 3
print(x)  # 12

x *= 2
print(x)  # 24

x /= 4
print(x)  # 6.0

x //= 2
print(x)  # 3.0

x %= 2
print(x)  # 1.0
```

Other operators:

```python
x **= 2
x &= 3
x |= 2
x ^= 1
x <<= 2
x >>= 1
```

### Important: Augmented Assignment

For mutable objects, augmented assignment can modify the existing object.

```python
a = [1, 2]
b = a

a += [3]

print(a)      # [1, 2, 3]
print(b)      # [1, 2, 3]
print(a is b) # True
```

Compare with ordinary reassignment:

```python
a = [1, 2]
b = a

a = a + [3]

print(a)      # [1, 2, 3]
print(b)      # [1, 2]
print(a is b) # False
```

This is an important Python-specific distinction.

---

## 6. Logical Operators

Python provides three logical operators.

### AND

Returns a truthy value only when both operands are truthy.

```python
print(True and True)    # True
print(True and False)   # False
```

### OR

Returns a truthy value when at least one operand is truthy.

```python
print(True or False)  # True
print(False or False) # False
```

### NOT

Reverses the truth value.

```python
print(not True)   # False
print(not False)  # True
```

### Important: Short-Circuit Evaluation

Python stops evaluating when the result is already determined.

```python
x = 0

result = x != 0 and 10 / x > 2

print(result)  # False
```

The division is never executed.

With `or`:

```python
result = True or 10 / 0

print(result)  # True
```

The second expression is not evaluated.

### Important: AND and OR Return Operands

Unlike many languages where logical operators always return booleans, Python's `and` and `or` return one of their operands.

```python
print(10 and 20)  # 20
print(0 and 20)   # 0

print(10 or 20)   # 10
print(0 or 20)    # 20
```

This is useful for understanding expressions such as:

```python
username = input("Username: ") or "Guest"
```

If the input is empty, the username becomes `"Guest"`.

However, use explicit conditions when the distinction between an empty value and a missing value matters.

---

## 7. Bitwise Operators

Bitwise operators work on individual bits of integer values.

Consider:

```python
a = 5  # 0101
b = 3  # 0011
```

### AND (`&`)

A bit is set only when both bits are set.

```python
print(a & b)  # 1
```

### OR (`|`)

A bit is set when either bit is set.

```python
print(a | b)  # 7
```

### XOR (`^`)

A bit is set when the two bits differ.

```python
print(a ^ b)  # 6
```

### NOT (`~`)

Inverts the bits.

```python
print(~5)  # -6
```

Python integers use arbitrary precision and have effectively unbounded sign extension for bitwise operations.

### Left Shift (`<<`)

Shifts bits to the left.

```python
print(5 << 1)  # 10
print(5 << 2)  # 20
```

### Right Shift (`>>`)

Shifts bits to the right.

```python
print(20 >> 1)  # 10
print(20 >> 2)  # 5
```

### Practical Use

Bitwise operators are useful for:

- Permissions and flags.
- Bit masks.
- Low-level data processing.
- Binary protocols.
- Performance-sensitive numerical operations.

Do not confuse `and` with `&`, or `or` with `|`.

---

## 8. Membership Operators

Used to check whether an element exists inside a collection or sequence.

```python
numbers = [10, 20, 30]

print(20 in numbers)      # True
print(50 not in numbers)  # True
```

### Strings

```python
text = "Python Programming"

print("Python" in text)  # True
print("python" in text)  # False
```

String membership is case-sensitive.

### Dictionaries

Membership checks dictionary keys, not values.

```python
user = {
    "name": "Kush",
    "age": 23
}

print("name" in user)  # True
print("Kush" in user)  # False
```

To check values:

```python
print("Kush" in user.values())  # True
```

### Sets

Membership checking in sets is generally average O(1).

---

## 9. Identity Operators

Identity checks whether two names refer to the same object.

```python
a = [1, 2]
b = [1, 2]
c = a

print(a is b)      # False
print(a is c)      # True
print(a is not b)  # True
```

Use identity checks for singleton objects:

```python
result = None

if result is None:
    print("No result")
```

Never rely on `is` for ordinary string or integer equality.

---

## 10. Conditional Statements

Conditions allow a program to make decisions.

### if

```python
age = 23

if age >= 18:
    print("Adult")
```

### if-else

```python
age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

### if-elif-else

```python
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
```

Python checks conditions from top to bottom and executes the first matching branch.

### Nested Conditions

```python
age = 23
has_id = True

if age >= 18:
    if has_id:
        print("Access granted")
    else:
        print("ID required")
else:
    print("Access denied")
```

### Python Uses Indentation

Unlike Java, JavaScript or Go, Python uses indentation to define blocks.

```python
if True:
    print("Inside block")
    print("Still inside")

print("Outside block")
```

Incorrect indentation causes `IndentationError` or `TabError`.

Use four spaces per indentation level.

### Pass Statement

`pass` is a placeholder that performs no operation.

```python
if age >= 18:
    pass
else:
    print("Minor")
```

Useful when designing a structure before implementing it.

### Conditional Expression (Ternary)

```python
age = 23

result = "Adult" if age >= 18 else "Minor"

print(result)
```

It is an expression, not a replacement for every `if-else` statement.

### Walrus Operator (`:=`)

Assignment expressions assign a value while evaluating an expression.

```python
if (length := len("Python")) > 5:
    print(length)
```

Use it sparingly. Ordinary assignment is often clearer.

---

## 11. Loops

Loops execute a block repeatedly.

Python has two main loop statements:

- `for`
- `while`

### For Loop

Used to iterate over an iterable.

```python
for number in [1, 2, 3, 4, 5]:
    print(number)
```

### Loop Through a String

```python
for character in "Python":
    print(character)
```

### Range

`range()` generates a sequence of integers.

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

Syntax:

`range(start, stop, step)`

```python
range(5)       # 0 to 4
range(1, 5)    # 1 to 4
range(0, 10, 2)  # 0, 2, 4, 6, 8
range(10, 0, -1) # 10 to 1
```

The stop value is excluded.

### Range Is Not a List

```python
numbers = range(5)

print(numbers)       # range(0, 5)
print(list(numbers)) # [0, 1, 2, 3, 4]
```

A range is an immutable, memory-efficient sequence object.

### While Loop

Runs while a condition remains true.

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Always ensure the condition eventually becomes false unless an infinite loop is intentional.

---

## 12. Loop Control Statements

### break

Immediately exits the nearest enclosing loop.

```python
for number in range(10):
    if number == 5:
        break

    print(number)
```

Output: `0 1 2 3 4`

### continue

Skips the rest of the current iteration.

```python
for number in range(5):
    if number == 2:
        continue

    print(number)
```

Output: `0 1 3 4`

### pass

Does nothing and continues normally.

```python
for number in range(5):
    if number == 2:
        pass

    print(number)
```

### else With Loops

Python supports `else` with both `for` and `while`.

The `else` block executes when the loop finishes normally, not when it exits using `break`.

```python
for number in range(5):
    print(number)
else:
    print("Loop completed")
```

With break:

```python
for number in range(5):
    if number == 2:
        break
else:
    print("This will not execute")
```

### Practical Use: Searching

```python
numbers = [10, 20, 30, 40]
target = 30

for number in numbers:
    if number == target:
        print("Found")
        break
else:
    print("Not found")
```

---

## 13. Nested Loops

A loop inside another loop.

```python
for i in range(3):
    for j in range(3):
        print(i, j)
```

The inner loop completes all its iterations for each outer iteration.

### Pattern Example

```python
for i in range(1, 5):
    for j in range(i):
        print("*", end="")

    print()
```

Output:

```text
*
**
***
****
```

### Performance

If both loops run `n` times, the total number of iterations is approximately `n²`.

This is O(n²) time complexity.

Avoid unnecessary nested loops when working with large datasets.

---

## 14. Iteration Gotchas

### Modifying a List While Iterating

Avoid removing items from a list while directly iterating over it.

Problematic:

```python
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number % 2 == 0:
        numbers.remove(number)

print(numbers)
```

This can skip elements because the list changes while the iterator advances.

Better:

```python
numbers = [1, 2, 3, 4, 5]

numbers = [
    number for number in numbers
    if number % 2 != 0
]
```

Or iterate over a copy:

```python
for number in numbers.copy():
    if number % 2 == 0:
        numbers.remove(number)
```

### Loop Variables Remain Available

```python
for number in range(3):
    pass

print(number)  # 2
```

Unlike JavaScript's block-scoped `let`, a Python `for` loop does not create a separate block scope.

### Empty Range

```python
for i in range(5, 5):
    print(i)
```

Nothing is printed.

### Infinite Loops

```python
while True:
    command = input("Enter exit to stop: ")

    if command == "exit":
        break
```

Intentional infinite loops are common in servers and interactive programs.

---

## 15. Useful Loop Functions

### enumerate()

Provides an index and value.

```python
languages = ["Python", "Go", "Java"]

for index, language in enumerate(languages):
    print(index, language)
```

Starting index:

```python
for index, language in enumerate(languages, start=1):
    print(index, language)
```

### zip()

Iterates over multiple iterables together.

```python
names = ["Kush", "Rahul"]
ages = [23, 24]

for name, age in zip(names, ages):
    print(name, age)
```

By default, `zip()` stops at the shortest iterable.

To detect unequal lengths:

```python
for name, age in zip(names, ages, strict=True):
    print(name, age)
```

`strict=True` requires Python 3.10 or later.

### reversed()

```python
for number in reversed([1, 2, 3]):
    print(number)
```

### sorted()

```python
numbers = [5, 2, 8, 1]

for number in sorted(numbers):
    print(number)
```

### sum(), min(), max()

```python
numbers = [10, 20, 30]

print(sum(numbers))
print(min(numbers))
print(max(numbers))
```

---

## 16. Loop vs Comprehension

Python provides comprehensions for creating collections concisely.

### Traditional Loop

```python
squares = []

for number in range(5):
    squares.append(number ** 2)
```

### List Comprehension

```python
squares = [number ** 2 for number in range(5)]
```

### With Conditions

```python
even_numbers = [
    number for number in range(10)
    if number % 2 == 0
]
```

### Dictionary Comprehension

```python
squares = {
    number: number ** 2
    for number in range(5)
}
```

### Set Comprehension

```python
unique_squares = {
    number ** 2 for number in range(5)
}
```

### Generator Expression

```python
squares = (number ** 2 for number in range(5))

for value in squares:
    print(value)
```

Generator expressions produce values lazily rather than building the entire collection immediately.

Important: A generator is generally exhausted after its values have been consumed.

Use comprehensions when they improve readability. Avoid excessively nested or complicated expressions.

---

## 17. Python vs Other Languages

| Feature | Python | JavaScript | Go |
|---|---|---|---|
| Blocks | Indentation | Braces | Braces |
| Main loop | `for`, `while` | `for`, `while` | `for` |
| Range iteration | `range()` | `for...of` | `range` |
| Logical AND | `and` | `&&` | `&&` |
| Logical OR | `or` | `||` | `||` |
| Logical NOT | `not` | `!` | `!` |
| Boolean values | `True`, `False` | `true`, `false` | `true`, `false` |
| Ternary | `a if c else b` | `c ? a : b` | No ternary |
| Membership | `in` | `includes()` | Usually explicit search |
| Loop else | Supported | Not supported | Not supported |
| Chained comparisons | Supported | Not equivalent | Not supported |

### Important Differences

1. Python uses `and`, `or`, `not` instead of `&&`, `||`, `!`.
2. Python supports chained comparisons such as `10 < x < 100`.
3. Python's `for` loop iterates over objects, not just numeric counters.
4. Python supports `else` with loops.
5. Python's `and` and `or` return operands, not necessarily booleans.
6. Python uses indentation instead of braces.
7. Python's `range()` excludes its ending value.
8. Python does not have a traditional C-style `for (initialization; condition; update)` loop.

---

## 18. Common Mistakes

| Mistake | Why it happens |
|---|---|
| Using `=` instead of `==` | Confusing assignment and comparison |
| Using `&` instead of `and` | Confusing bitwise and logical operators |
| Missing indentation | Python requires correctly indented blocks |
| Forgetting `range()` excludes stop | Incorrect loop boundaries |
| Forgetting to update a while condition | Infinite loop |
| Modifying a list while iterating | Unexpected skipped elements |
| Using `is` instead of `==` | Confusing identity and equality |
| Assuming `and` returns True/False | It returns one of its operands |
| Incorrect operator precedence | Misunderstanding evaluation order |
| Assuming `else` always executes after a loop | `break` skips loop-else |

---

## 19. Practice Exercises

### Arithmetic and Operators

1. Build a calculator supporting addition, subtraction, multiplication and division.
2. Find the quotient and remainder of two integers.
3. Check whether a number is even or odd.
4. Calculate the power of a number.
5. Demonstrate negative floor division.
6. Swap two variables using assignment.
7. Demonstrate bitwise AND, OR and XOR.

### Conditions

8. Check whether a number is positive, negative or zero.
9. Find the largest of three numbers.
10. Check whether a year is a leap year.
11. Create a grading system using marks.
12. Check whether a person is eligible for a driving licence.
13. Build a simple login check.
14. Use chained comparisons to validate an age range.
15. Build a calculator using conditional statements.

### Loops

16. Print numbers from 1 to 100.
17. Print all even numbers between 1 and 100.
18. Calculate the sum of the first N natural numbers.
19. Print a multiplication table.
20. Calculate the factorial of a number.
21. Reverse an integer.
22. Count the digits of a number.
23. Check whether a number is prime.
24. Print the Fibonacci sequence.
25. Create a number-guessing game.
26. Search for an element in a list using a loop.
27. Demonstrate `break`, `continue` and loop `else`.
28. Print a triangle pattern using nested loops.
29. Create a list of squares using comprehension.
30. Iterate over two lists together using `zip()`.

---

## 20. Key Takeaways

- Operators perform calculations and comparisons.
- Python follows a defined operator precedence.
- `//` performs floor division.
- `%` returns the remainder.
- `and` and `or` use short-circuit evaluation.
- Logical operators can return operands.
- Bitwise operators operate on integer bits.
- Membership checks whether an element exists.
- Identity checks whether two references point to the same object.
- Python uses `if`, `elif` and `else` for decisions.
- Indentation defines code blocks.
- `for` iterates over iterables.
- `range()` excludes its stop value.
- `while` repeats while a condition is true.
- `break` exits a loop.
- `continue` skips an iteration.
- Loop `else` executes when no `break` occurs.
- `enumerate()` provides indexes.
- `zip()` combines iterables.
- Comprehensions create collections concisely.
- Generators produce values lazily.