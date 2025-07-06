from flask import Flask,render_template,url_for
from user import user_data
app = Flask (__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",title="Home",user=user_data)

@app.route("/about")
def about():
    return render_template("about.html",title="About",user=user_data)

@app.route("/contact")
def contact():
    return render_template("contact.html",title="contact",user=user_data)

@app.route("/projects")
def projects():
    return render_template("projects.html",title="projects",user=user_data)


if __name__ == "__main__":
    app.run(debug=True)