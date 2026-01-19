import os
from flask import Flask
from flask import render_template

Base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__, template_folder=os.path.join(Base_dir, "templates"),static_folder=os.path.join(Base_dir, "static"),)

@app.route("/")
def HomePage():
    return render_template("HomePage.html")
if __name__ == "__main__":
 app.run()
