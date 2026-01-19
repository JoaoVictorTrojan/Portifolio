from flask import Flask
from flask import render_template
app = Flask(__name__,static_folder="static", template_folder="templates")

@app.route("/")
def HomePage():
    return render_template("HomePage.html")
if __name__ == "__main__":

 app.run()
