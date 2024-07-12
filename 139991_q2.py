
"""This is  a Student object with a name and an empty dictionary for grades."""
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def get_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)

class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_all_students(self):
        if not self.students:
            print("No students in the class.")
        for student in self.students:
            print(f"Student Name: {student.name}, Grades: {student.grades}")

    def get_student_average(self, student_name):
        for student in self.students:
            if student.name == student_name:
                return student.get_average_grade()
        return None
    def get_class_average_for_subject(self, subject):
        total, count = 0, 0
        for student in self.students:
            if subject in student.grades:
                total += student.grades[subject]
                count += 1
        return total / count if count else 0

""" demonstration of functionalities"""
if __name__ == "__main__":
    classroom = Classroom()

    """sadding students"""
    student1 = Student("Alice")
    student1.add_grade("Math", 90)
    student1.add_grade("Science", 85)
    student2 = Student("Bob")
    student2.add_grade("Math", 80)
    student2.add_grade("Science", 78)
    classroom.add_student(student1)
    classroom.add_student(student2)

    """ displaying all students"""
    classroom.display_all_students()

    """ getting the average grade of a student"""
    print(f"Alice's average grade: {classroom.get_student_average('Alice')}")

    """ getting ze class average for a subject"""
    print(f"Class average for Math: {classroom.get_class_average_for_subject('Math')}")
