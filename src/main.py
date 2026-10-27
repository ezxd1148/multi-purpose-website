"""
main.py

input: Route
Process: Identify route inputted
Output: Display .html file based on route and logic for website based on what is entered

by: ezxd1148 (afdhal)
"""

from flask import Flask, render_template, request

from multi_purpose_website.assign_3 import Student
from multi_purpose_website.prac_2 import count_number

app = Flask(__name__)


@app.route("/")
def index():
    """
    Return homepage for route root or /
    """
    return render_template("index.html")


@app.route("/tool1", methods=["GET", "POST"])
def tool1():
    """
    Return tool1 page for route /tool1

    prac_2.py
    """
    result = None
    error = None

    if request.method == "POST":
        try:
            num = int(request.form["num"])
            result = count_number(num)

        except ValueError as e:
            error = "Error:" + e

    return render_template("tool1.html", result=result, error=error)


# p2
@app.route("/tool2")
def tool2():
    """
    Return tool2 page for route /tool2
    """
    return render_template("tool2.html")


# a1
@app.route("/tool3")
def tool3():
    """
    Return tool3 page for route /tool3
    """
    return render_template("tool3.html")


# a2
@app.route("/tool4")
def tool4():
    """
    Return tool4 page for route /tool4
    """
    return render_template("tool4.html")


# a3
@app.route("/tool5", methods=["GET", "POST"])
def tool5():
    """
    Return tool5 page for route /tool5
    """
    result = None
    error = None

    if request.method == "POST":
        try:
            quiz = int(request.form["quiz"])
            assignment = int(request.form["assignment"])
            exam = int(request.form["exam"])

            student = Student()
            student.quiz_marks(quiz)
            student.assignment_marks(assignment)
            student.exam_marks(exam)

            result = {
                "total": student.sum_marks(),
                "grade": student.student_grade(),
            }

        except (ValueError, KeyError):
            error = "Please enter valid marks!"

    return render_template("tool5.html", result=result, error=error)


@app.route("/tool6")
def tool6():
    """
    Return tool6 page for route /tool6
    """
    return render_template("tool6.html")
