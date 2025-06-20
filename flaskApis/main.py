from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/")
def json():
   salary = {
     "Arun" : 50000,
     "Prashant" :100000,
     "Madhu" : 50000
   }
   values = [1, salary, 3]
   return jsonify(values)

app.run(debug=True)    