from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class Test(db.Model):
      __tablename__="book"
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

class hello(db.Model):
    __tablename__="bookss"
    isbn = db.Column(db.String(100),  primary_key=True)
    title = db.Column(db.String(100))
    author = db.Column(db.String(100))
    year = db.Column(db.String(100))
    
    def __init__(self, isbn,title,author,year):
        self.isbn = isbn
        self.title= title
        self.author = author
        self.year = year

class Review(db.Model):
    __tablename__="review"
    user = db.Column(db.String(80),nullable=False)
    isbn = db.Column(db.String(80), primary_key=True, nullable=False)
    
    rating = db.Column(db.String(80),unique=False,nullable=False)
    review = db.Column(db.String(80),unique=False,nullable=False)

def __init__(self,user,isbn,rating,review):
    self.user = user
    self.isbn=isbn
    self.rating=rating
    self.review=review 

class Bookshelf(db.Model):
    __tablename__="book_shelf"
    user = db.Column(db.String(80), nullable=False)
    book = db.Column(db.String(80) , primary_key=True,nullable=False)
    
  

def __init__(self,user,book):
    self.user = user
    self.book=book
