print(f"Factorial of {n} = {fact}")

class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

# Create an instance (like s1 in C)
s1 = Student("Rahul", 161, 87.5)

# Print the fields
print(f"Name: {s1.name}")
print(f"Roll: {s1.roll}")
print(f"Marks: {s1.marks:.1f}")