from flask import Flask , render_template, request


app = Flask(__name__)

@app.route("/")
def hello_world():
    marks = {
        "John" : 45,
        "Sourabh" : 99,
        "jeff" : 100,
        "Alex" : 50
    }
    return render_template("index.html",marks=marks)

app.run(debug=True)    