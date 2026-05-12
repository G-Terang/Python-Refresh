from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(BASE_DIR, "file.txt")

        with open(file_path, "w") as f:
            f.write(f"The name is {request.form['name']} and email is {request.form['email']}")

    return render_template('index.html')

app.run(debug=True)