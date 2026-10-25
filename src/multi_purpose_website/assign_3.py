from enum import Enum

# IN PROGRESS FOR REFACTORING

def main():
    print("Assignment 3")

class Student:
    def __init__(self, quiz = 0, assignment = 0, exam = 0):
        self.quiz = quiz
        self.assignment = assignment
        self.exam = exam # removed commas from all 3 because thats what making em all tuple
        # decided to remove sum and grade because both are derived from 3

    def quiz_marks(self, x):
        """
            Add/Update new quiz marks for student
        """
        if not 0 <= x <= 40:
            raise Exception("Invalid Marks")
        self.quiz = x

    def assignment_marks(self, x):
        """
            Add/Update new assignment marks for student
        """
        if not 0 <= x <= 30:
            raise Exception("Invalid Marks")
        self.assignment = x

    def exam_marks(self, x):
        """
            Add/Update new exam marks for student  
        """

        if not 0 <= x <= 30: # negative value should not be possible
            raise Exception("Invalid Marks")
        self.exam = x

    def sum_marks(self):
        # refactored becasue it should return total not add a total to the student class
        return self.quiz + self.assignment + self.exam

    def student_grade(self):
        if (90 <= self.sum_marks() <= 100):
            x = 1
        elif (80 <= self.sum_marks() <= 89):
            x = 2
        elif (70 <= self.sum_marks() <= 79):
            x = 3
        elif (60 <= self.sum_marks() <= 69):
            x = 4
        elif (50 <= self.sum_marks() <= 59):
            x = 5
        else:
            x = 6

        return self.Grade(x).name

    class Grade(Enum):
        A = 1
        B = 2
        C = 3
        D = 4
        E = 5
        F = 6

students = int(input("Number of students:"))
students_list = []

for i in range(students):
    
    print(f"Student {i + 1}")
    student = Student()
    quizM = int(input("Enter quiz marks:"))
    student.quiz_marks(quizM)
    assignmentM = int(input("Enter assignment marks:"))
    student.assignment_marks(assignmentM)
    examM = int(input("Enter exam marks:"))
    student.exam_marks(examM)

    students_list.append(student)

## Calculate students sum score
for i in students_list:
    print(i.student_grade())

if __name__ == "__main__": # it is main genius
    main()
