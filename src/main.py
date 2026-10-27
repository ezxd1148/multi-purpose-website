"""
main.py

input: Route
Process: Identify route inputted
Output: Display .html file based on route and logic for website based on what is entered

by: ezxd1148 (afdhal)
"""

from flask import Flask, render_template, request

from multi_purpose_website.assign_1 import calculates_flour
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
    PROGRESS: Done

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
@app.route("/tool2", methods=["GET", "POST"])
def tool2():
    """
    PROGRESS: Done

    Return tool2 page for route /tool2

    assign_1.py
    """

    result = None
    error = None

    if request.method == "POST":
        try:
            raw_weights = request.form.getlist("weights")

            weights = [float(x) for x in raw_weights]

            if len(weights) != 10:
                raise ValueError("Exactly 10 weights is required")

            if any(not 0 <= x < 100 for x in weights):
                raise ValueError("weights must be from 0 to 100 kg")

            total, average, heaviest = calculates_flour(weights)

            result = {"total": total, "average": average, "heaviest": heaviest}

        except ValueError as e:
            error = str(e)

    return render_template("tool2.html", result=result, error=error)


# a1
@app.route("/tool3")
def tool3():
    """
    PROGRESS: Ongoing

    Return tool3 page for route /tool3

    assign_2.py
    """
    return render_template("tool3.html")


@app.route("/tool4", methods=["GET", "POST"])
def tool5():
    """
    PROGRESS: Done

    Return tool4 page for route /tool4

    assign_3.py
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

    return render_template("tool4.html", result=result, error=error)


@app.route("/tool5")
def tool4():
    """
    PROGRESS: Not Started

    Return tool5 page for route /tool5

    add_tool1.py
    """
    return render_template("tool5.html")
