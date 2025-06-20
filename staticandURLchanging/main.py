from flask import Flask render_template

# app = Flask(__name__, static_url_path="/public") #This is how we can change the static file url path.
app = Flask(__name__, static_folder="/assets") # This is how we can change the folder path

@app.route("/")
def hello_world():
    return render_template("")

app.run(debug=True)    