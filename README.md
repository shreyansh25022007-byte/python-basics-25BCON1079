# Python Basics & Practice Scripts

A collection of beginner-friendly Python scripts demonstrating fundamental programming concepts, Object-Oriented Programming (OOP) basics, and standard algorithmic logic.

---

## 📋 Contents

1. [Factorial Calculation](#1-factorial-calculation)
2. [Student Class (OOP Basics)](#2-student-class-oop-basics)
3. [Fibonacci Series Generator](#3-fibonacci-series-generator)

---

## 📜 Script Breakdown

### 1. Factorial Calculation

Calculates the factorial of a given integer `n` using an iterative `for` loop.

```python
n = 5  # Ensure 'n' is defined before running

fact = 1

for i in range(1, n + 1):
    fact = fact * i

print(f"factorial of {n} = {fact}")
```

**Key Concepts:**

* `for` loops
* `range()` function
* Variable accumulation
* f-strings

**Output:**

```text
factorial of 5 = 120
```

---

### 2. Student Class (OOP Basics)

Demonstrates basic Object-Oriented Programming principles by defining a `Student` class with attributes for name, roll number, and marks/performance.

```python
class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks


# Create a student object
s1 = Student("Rahul", 101, "excellent")


# Print the student's details
print(f"name: {s1.name}")
print(f"roll: {s1.roll}")
print(f"marks: {s1.marks}")
```

**Key Concepts:**

* Object-Oriented Programming (OOP)
* Classes
* `__init__` constructor
* Instance variables
* Object instantiation

**Output:**

```text
name: Rahul
roll: 101
marks: excellent
```

---

### 3. Fibonacci Series Generator

Generates the first `n` numbers in the Fibonacci sequence and prints them separated by spaces.

```python
n = 10

a, b = 0, 1
result = []

for _ in range(n):
    result.append(a)

    next_num = a + b
    a = b
    b = next_num

print(' '.join(map(str, result)))
```

**Output:**

```text
0 1 1 2 3 5 8 13 21 34
```

**Key Concepts:**

* Simultaneous assignment
* List manipulation
* `map()` function
* String `.join()` method
* Fibonacci sequence logic

---


## 📚 Learning Goals

These scripts are designed to practice:

* Basic Python syntax
* Variables and data types
* Loops
* Lists
* String manipulation
* Built-in functions
* Object-Oriented Programming
* Basic algorithmic thinking

---

## 👨‍💻 Author

**Shreyansh**

A collection of Python practice programs created while learning programming fundamentals and problem-solving.
