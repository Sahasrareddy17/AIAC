class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if 90 <= self.marks <= 100:
            return "A"
        elif 75 <= self.marks < 90:
            return "B"
        elif 60 <= self.marks < 75:
            return "B"
        elif 50 <= self.marks < 60:
            return "C"
        else:
            return "F (Fail)"

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {self.grade}")

# Example usage:
if __name__ == "__main__":
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    marks = float(input("Enter marks: "))
    student = Student(name, roll_no, marks)
    student.display_details()




