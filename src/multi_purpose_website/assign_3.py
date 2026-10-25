from enum import Enum

def main():
    print("Assignment 3")

class Students:
    def __init__(self, quiz = 0, assignment = 0, exam = 0):
        self.quiz = quiz,
        self.assignment = assignment,
        self.exam = exam,
        self.sum = 0,
        self.grade = "",

    def quiz_marks(self, x):
        if x > 40:
            raise Exception("Invalid Marks")
        self.quiz = x

    def assignment_marks(self, x):
        if x > 30:
            raise Exception("Invalid Marks")
        self.assignment = x

    def exam_marks(self, x):
        if x > 30:
            raise Exception("Invalid Marks")
        self.exam = x

    def sum_marks(self):
        self.sum = self.quiz + self.assignment + self.exam

    def student_grade(self, x):
        self.grade = self.Grade(x).name

    class Grade(Enum):
        A = 1
        B = 2
        C = 3
        D = 4
        E = 5
        F = 6
        


students = int(input("Number of students:"))
students_array = []

for i in range(students):
    
    print(f"Student {i + 1}")
    student = Students()
    quizM = int(input("Enter quiz marks:"))
    student.quiz_marks(quizM)
    assignmentM = int(input("Enter assignment marks:"))
    student.assignment_marks(assignmentM)
    examM = int(input("Enter exam marks:"))
    student.exam_marks(examM)

    students_array.append(student)

## Calculate students sum score

student_A = 0
student_B = 0
student_C = 0
student_D = 0
student_E = 0
student_F = 0

print(students_array[0].sum[0])

for i in range(len(students_array)):
    print(f"Student {i+1} Grade")
    students_array[i].sum_marks
    if 90 <= int(students_array[i].sum[0]) <= 100:
        students_array[i].student_grade(1)
        student_A += 1
    elif 80 <= int(students_array[i].sum[0]) <= 89:
        students_array[i].student_grade(2)
        student_B += 1
    elif 70 <= int(students_array[i].sum[0]) <= 79:
        students_array[i].student_grade(3)
        student_C += 1
    elif 60 <= int(students_array[i].sum[0]) <= 69:
        students_array[i].student_grade(4)
        student_D += 1
    elif 50 <= int(students_array[i].sum[0]) <= 59:
        students_array[i].student_grade(5)
        student_E += 1
    elif int(students_array[i].sum[0]) <= 50:
        students_array[i].student_grade(6)
        student_F += 1

count_A = []
count_B = []
count_C = []
count_D = []
count_E = []
count_F = []


for i in students_array:
    i.sum_marks
    if i.grade == 'A':
        count_A.append(int(i.sum[0]))
        print(int(i.sum[0]))
    if i.grade == 'B':
        count_B.append(int(i.sum[0]))
        print(int(i.sum[0]))
    if i.grade == 'C':
        count_C.append(int(i.sum[0]))
        print(int(i.sum[0]))
    if i.grade == 'D':
        count_D.append(int(i.sum[0]))
        print(int(i.sum[0]))
    if i.grade == 'E':
        count_E.append(int(i.sum[0]))
        print(int(i.sum[0]))
    if i.grade == 'F':
        count_F.append(int(i.sum[0]))
        print(int(i.sum[0]))

grade_array = [count_A, count_B, count_C, count_D, count_E, count_F]
sum_array = []
sum = 0

for i in grade_array:
    for j in i:
        sum += j
    sum_array.append(sum)

print(sum_array)

print(f"Grade A: {student_A} student(s)")
print("Average Mark of Grade:", count_A)

print(f"Grade B: {student_B} student(s)")
print("Average Mark of Grade:", )

print(f"Grade C: {student_C} student(s)")
print("Average Mark of Grade:", )

print(f"Grade D: {student_D} student(s)")
print("Average Mark of Grade:", )

print(f"Grade E: {student_E} student(s)")
print("Average Mark of Grade:", )

print(f"Grade F: {student_F} student(s)")
print("Average Mark of Grade:", )

if __name__ == "__init__":
    main()
