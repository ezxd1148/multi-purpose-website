from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/tool1")
def tool1(): 
    return render_template('tool1.html')

@app.route("/tool2")
def tool2():
    return render_template('tool2.html')

@app.route("/tool3")
def tool3():
    return render_template('tool3.html')

@app.route("/tool4")
def tool4():
    return render_template('tool4.html')

@app.route("/tool5")
def tool5():
    return render_template('tool5.html')

@app.route("/tool6")
def tool6():
    return render_template('tool6.html')



