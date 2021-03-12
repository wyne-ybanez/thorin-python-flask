# Imports
import os
import json
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env 
 
# Flask App
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

# Decorators
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data: 
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj['url'] == member_name:
                member = obj 
    return render_template('member.html', member=member)


""" 
Flask only accepts GET - need to create code for POST
Request refers to contact form request 
"""
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Come Work With Us!")


# Run app on server
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)