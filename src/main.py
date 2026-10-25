from flask import Flask, render_template, request
from multi_purpose_website import assign_3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

# p1
@app.route("/tool1")
def tool1(): 
    return render_template('tool1.html')

#p2
@app.route("/tool2")
def tool2():
    return render_template('tool2.html')

#a1
@app.route("/tool3")
def tool3():
    return render_template('tool3.html')

#a2
@app.route("/tool4")
def tool4():
    return render_template('tool4.html')

#a3
@app.route("/tool5")
def tool5():
    return render_template('tool5.html')

#WHY AM I MAD tool
@app.route("/tool6")
def tool6():
    return render_template('tool6.html')

@app.route("/test", methods=["GET", "POST"])
def test():
    test = None
    
    if request.method == "POST":
        text = request.form.get("student_count", "")
        print(text)

    return render_template('tool5.html')


