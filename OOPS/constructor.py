class Student:
    def __init__(self, fname, age):  # arguments
        self.name = fname
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


s1 = Student("GK", 22)  # object-creation
s1.display()  # object-calling-the-moethod-inside-the-class
