from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def hello_world():
    return render_template("index.html")


app.run(port=8080,debug=True)    