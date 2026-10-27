"""
Student quiz marks and grades calculator
"""

from enum import Enum

# IN PROGRESS FOR REFACTORING


def main():
    """
    healthchecks
    """
    print("Assignment 3")

    students = int(input("Number of students:"))
    students_list = []

    for i in range(students):
        print(f"Student {i + 1}")
        student = Student()
        quiz_m = int(input("Enter quiz marks:"))
        student.quiz_marks(quiz_m)
        assignment_m = int(input("Enter assignment marks:"))
        student.assignment_marks(assignment_m)
        exam_m = int(input("Enter exam marks:"))
        student.exam_marks(exam_m)

        students_list.append(student)

    ## Calculate students sum score
    for i in students_list:
        print(i.student_grade())


class Student:
    """
    Initialize newstudent class
    """

    def __init__(self, quiz=0, assignment=0, exam=0):
        self.quiz = quiz
        self.assignment = assignment
        self.exam = (
            exam  # removed commas from all 3 because thats what making em all tuple
        )
        # decided to remove sum and grade because both are derived from 3

    def quiz_marks(self, x):
        """
        Add/Update new quiz marks for student
        """
        if not 0 <= x <= 40:
            raise ValueError("Marks is more than 40 or less than 0")
        self.quiz = x

    def assignment_marks(self, x):
        """
        Add/Update new assignment marks for student
        """
        if not 0 <= x <= 30:
            raise ValueError("Marks is more than 30 or less than 0")
        self.assignment = x

    def exam_marks(self, x):
        """
        Add/Update new exam marks for student
        """

        if not 0 <= x <= 30:  # negative value should not be possible
            raise ValueError("Marks is more than 30 or less than 0")
        self.exam = x

    def sum_marks(self):
        """
        calculate the total marks of student
        """
        # refactored becasue it should return total not add a total to the student class
        return self.quiz + self.assignment + self.exam

    def student_grade(self):
        """
        Identify student grade based on sum
        """
        if 90 <= self.sum_marks() <= 100:
            x = 1
        elif 80 <= self.sum_marks() <= 89:
            x = 2
        elif 70 <= self.sum_marks() <= 79:
            x = 3
        elif 60 <= self.sum_marks() <= 69:
            x = 4
        elif 50 <= self.sum_marks() <= 59:
            x = 5
        else:
            x = 6

        return self.Grade(x).name

    class Grade(Enum):
        """
        Grade enum
        """

        A = 1
        B = 2
        C = 3
        D = 4
        E = 5
        F = 6


if __name__ == "__main__":  # it is main genius
    main()
