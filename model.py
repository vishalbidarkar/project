
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class Test(db.Model):
      __tablename__="books"
      name = db.Column(db.String(100),primary_key=True)
      password = db.Column(db.String(120), nullable=False)
      mobile = db.Column(db.String(15),primary_key=True,nullable=False)
      dob = db.Column(db.String,nullable=False)
      email = db.Column(db.String(80), nullable=False)
      gender = db.Column(db.String(80), nullable=False)
      timestamp= db.Column(db.String(80), nullable=False)




      def __init__(self, name,password,mobile,dob,email,gender,timestamp):
          self.name = name
          self.password = password
          self.mobile = mobile
          self.dob = dob
          self. email= email
          self.gender = gender
          self.timestamp=timestamp

class title(db.Model):
    __tablename__="book1"
    isbn = db.Column(db.String(100), primary_key=True)
    title = db.Column(db.String(100))
    author = db.Column(db.String(100))
    year = db.Column(db.String(100))
    
    def __init__(self, isbn,title,author,year):
        self.isbn = isbn
        self.title= title
        self.author = author
        self.year = year



