from flask import Flask, render_template
from datetime import datetime 

app = Flask(__name__)

@app.context_processor
def inject_now():
    return {'now': datetime.now()}

@app.route("/")
@app.route("/index.html")
def home():
    return render_template("index.html")

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/projects.html")
def projects():
    return render_template("projects.html")

@app.route("/skills.html")
def skills():
    return render_template("skills.html")

@app.route("/contact.html")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)