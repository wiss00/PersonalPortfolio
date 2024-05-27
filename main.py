from flask import render_template, redirect, url_for, flash, request
from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route("/")
def home():
    main_page = True
    return render_template("index.html", main_page=main_page)

@app.route("/about")
def about():
    main_page = False
    return render_template("about.html",main_page=main_page)
@app.route("/contact")
def contact():
    main_page = False

    return render_template("contact.html",main_page=main_page)

@app.route("/projects")
def projects():
    main_page = False

    return render_template("projects.html",)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
