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
print(f"marks: {s1.marks:}")
