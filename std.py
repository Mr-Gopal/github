class Student:
    def __init__(self, name, roll_no, year):
        self.name = name
        self.roll_no = roll_no
        self.year = year

    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll: {self.roll_no}")
        print(f"year: {self.roll_no}")

s = Student("Raju", 56, 2025)