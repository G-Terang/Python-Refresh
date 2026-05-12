from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def helloworld():
    marks = {
        "alan":90,
        "brian": 91,
        "calvin": 88,
        "dict": 96,
        "elies": 92,
        "franklin": 83,
        "G.Terang": 100
    }
    return render_template("index.html", marks=marks)

app.run(debug=True)