from flask import Flask, session, request, render_template, jsonify
from flask.helpers import flash
from model import *
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, time
from sqlalchemy import or_
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:Navya@0@localhost:5432/project'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "baukfb13256$%^sfqu3oeghroq"

db.init_app(app)

def main() :
    db.create_all()
# @app.route("/")
# def api():
#     return render_template("api.html")


@app.route("/api/search/<string:a>", methods=["GET","POST"])
def apisearch(a):
    # a=request.form.get("search")
    d= hello.query.filter(or_(hello.isbn==a, hello.author==a, hello.title==a, hello.year==a))
    b =[]
    for c in d:
        value={}
        value["isbn"]=c.isbn
        value["author"]=c.author
        value["title"]=c.title
        value["year"]=c.year
        b.append(value)
    s=len(b)
    return jsonify({'books':b}),200

