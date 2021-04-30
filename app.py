# from flask import Flask, session, request, render_template
# from flask.helpers import flash
# from model import *
# from werkzeug.security import generate_password_hash, check_password_hash
# from datetime import datetime, time

# app = Flask(__name__)

# app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:Vishal@0@localhost:5432/imdb'
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.config["SECRET_KEY"] = "qoiefhnvjhdahkvbeahbdvnvm165vdvf1v5sd4v515dvc"

# db.init_app(app)

# def main() :
#     db.create_all()
# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/register")
# def register():
#   return render_template("register.html")



# @app.route("/login")
# def login():
#   return render_template("login.html")

# @app.route("/submit1", methods = ["POST"])
# def submit1(): 
#     session['name'] = request.form.get("name")
#     password = request.form.get("password")
#     users=Test.query.all()
#     for user in users:
#         if user.name==session['name'] and check_password_hash(user.password, password):
#             return render_template("hello.html",names=session['name'])
#         # elif user.name!=name or user.password!=password:
#         # else:
#         #     return render_template("error.html",names=name)
#         # else:
#     return render_template('register.html')

# @app.route("/back")
# def back():
#     return render_template("hello.html")


# @app.route("/delete/<string:book>")
# def delete(book):
#     print(book)
#     title_delete = Bookshelf.query.get_or_404(book)

    
#     db.session.delete(title_delete)
#     db.session.commit()
#     return render_template("shelf.html")


# @app.route("/search", methods=["POST"])
# def search():
#     name = request.form.get("search")
#     user = hello.query.all()
#     # for i in user:
#     #     if i.isbn==name or i.author==name or i.title==name or i.year==name :
#     #         return render_template("hello.html",isbn = i.isbn,title=i.title,author=i.author,year=i.year)
#         # else:
#     return render_template("hello.html", users=user, name=name)


# # @app.route("/review")
# # def review():
# #     return render_template("review.html")

# @app.route("/review/<string:id>")
# def review(id):
#     print(id)
#     usr = hello.query.all()
#     for i in usr:
#         if id == i.isbn:
#             a = i.isbn
#             b = i.title
#             c = i.author
#             d = i.year
#     return render_template("review.html", isbn = a, title=b,author=c,year=d)

# @app.route("/review/<string:isbn>/<string:title>/<string:id>",methods=["POST"])
# def bookshelf(isbn,title,id):
#     print(isbn,id)
#     star = request.form.get("rate")
#     Feedback = request.form.get("text")
#     response = request.form.get("shelf")
#     rev = Review( user=id,isbn=isbn,rating=star,review=Feedback)
#     db.session.add(rev)
#     db.session.commit()
#     if response == "Yes":
        
#         sh = Bookshelf(user=id,book=title)
#         db.session.add(sh)
#         db.session.commit()
#     else:
#         return render_template("hello.html")
#     return render_template("bookshelf.html", isbn=isbn,y=id,star=star,Feedback=Feedback)



# @app.route("/shelf/<string:id>")
# def shelf(id):
#     print(id)
#     x=Bookshelf.query.all()

#     return render_template ('shelf.html', y=id , a=x )




# @app.route("/submit", methods = ["GET","POST"])
# def submit(): 
#     session['name'] = request.form.get("name")
#     password = request.form.get("password")
#     mobile = request.form.get("mobile")
#     dob = request.form.get("dob")
#     email = request.form.get("email")
#     gender = request.form.get("gender")
#     timestamp=datetime.now()
#     s= Test(session['name'],password=generate_password_hash(password, method='sha256'),mobile=mobile,dob=dob,email=email,gender=gender, timestamp=timestamp)

#     usern = Test.query.filter_by(email=email).first()
#     if usern:  # if a user is found, we want to redirect back to signup page so user can try again
#         flash('Email address already exists')
#         return render_template("login.html")


#     db.session.add(s)
#     db.session.commit()


#     return render_template("login.html",users = Test.query.all())
    

from flask import Flask, session, request, render_template, jsonify
from flask.helpers import flash
from model import *
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, time
from sqlalchemy import or_
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:Vishal@0@localhost:5432/imdb'
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
    flag = 0
    for c in d:
        value={}
        value["isbn"]=c.isbn
        value["author"]=c.author
        value["title"]=c.title
        value["year"]=c.year
        b.append(value)
        flag = 2
    s=len(b)
    if flag == 0:
        return jsonify({'ERROR':'BOOKS NOT FOUND!'}),400

    return jsonify({'books':b}),200

@app.route("/api/review/<string:a>", methods=["GET","POST"])
def reviewsearch(a):
    # a=request.form.get("search")
    d= Review.query.filter(Review.user==a)
    b =[]
    flag = 0
    for c in d:
        value={}
        value["user"]=c.user
        value["isbn"]=c.isbn
        value["rating"]=c.rating
        value["review"]=c.review
        b.append(value)
        flag = 2
    s=len(b)
    if flag == 0:
        return jsonify({'ERROR':'Review NOT FOUND!'}),400

    return jsonify({'Reviews':b}),200


if __name__ == "__main__" :

    with app.app_context() :
        main()




