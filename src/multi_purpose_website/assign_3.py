class Students:
    def __init__(self, quiz, assignment, exam):
        self.quiz = 0,
        self.assignment = 0,
        self.exam = 0,

    def quiz_marks(self, x):
        if x > 40:
            return -1
        self.quiz = x

    def assignment_marks(self, x):
        if x > 30:
            return -1
        self.assignment = x

    def exam_marks(self, x):
        if x > 30:
            return -1
        self.exam = x

students = int(input("Number of students:"))
students_array = []

for i in range(students-1):
    
    print(f"Student {i + 1}")

    quizM = int(input("Enter quiz marks:"))
    assignmentM = int(input("Enter assignment marks:"))
    examM = int(input("Enter exam marks:"))

    student = Students()
    student.quiz_marks(quizM)
    student.assignment_marks(assignmentM)
    student.exam_marks(examM)
    students_array.append(student)

print(students_array)
