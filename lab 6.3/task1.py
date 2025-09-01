class Student:
    def __init__(self):
        self.name = input("Enter student name: ")
        self.roll_no = input("Enter roll number: ")
        self.marks = float(input("Enter marks: "))

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.marks}")

    def calculate_grade(self):
        if self.marks >= 90:
            grade = 'A'
        elif self.marks >= 75:
            grade = 'B'
        elif self.marks >= 60:
            grade = 'C'
        else:
            grade = 'Fail'
        print(f"Grade: {grade}")

# Example usage
if __name__ == "__main__":
    student = Student()
    print("\nStudent Details:")
    student.display_details()
    student.calculate_grade()