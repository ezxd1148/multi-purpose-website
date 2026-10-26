"""
main.py

input: Route
Process: Identify route inputted
Output: Display .html file based on route and logic for website based on what is entered

by: ezxd1148 (afdhal)
"""

from flask import Flask, render_template, request
from multi_purpose_website import assign_3

app = Flask(__name__)

@app.route("/")
def index():
    """
        Return homepage for route root or /
    """
    return render_template('index.html')

@app.route("/tool1")
def tool1():
    """
        Return tool1 page for route /tool1
    """
    return render_template('tool1.html')

#p2
@app.route("/tool2")
def tool2():
    """
        Return tool2 page for route /tool2
    """ 
    return render_template('tool2.html')

#a1
@app.route("/tool3")
def tool3():
    """
        Return tool3 page for route /tool3
    """
    return render_template('tool3.html')

#a2
@app.route("/tool4")
def tool4():
    """
        Return tool4 page for route /tool4
    """
    return render_template('tool4.html')

#a3
@app.route("/tool5")
def tool5():
    """
        Return tool5 page for route /tool5
    """
    return render_template('tool5.html')

@app.route("/tool6")
def tool6():
    """
        Return tool6 page for route /tool6
    """
    return render_template('tool6.html')

@app.route("/test", methods=["GET", "POST"])
def test():
    """
        Debug route at /test
    """
    test = None
    
    if request.method == "POST":
        text = request.form.get("student_count", "")
        print(text)

    return render_template('tool5.html')


