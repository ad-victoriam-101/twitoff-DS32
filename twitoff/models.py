from flask_sqlalchemy import SQLAlchemy

#create db object

DB = SQLAlchemy 

#Make a user table by creating user class
class User(DB.Model):
    #id column
    id = DB.Column(DB.BigInteger,primary_key = True)
    #username column
    user_name = DB.Column(DB.String,nullable = False)

#Make a tweet table by creating a tweet class
class Tweet(DB.Model):
    #create a tweet ID column
    id = DB.Column(DB.BigInteger,primary_key = True)
    #create a text column Unicode allows for Emoji's and links/strings
    text = DB.Column(DB.Unicode(300))
    #create a relationship between tweet and user a ONE TO MANY (one user many tweets)

    user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.id',nullable=False))

    #finalize the relationship (TWO WAY)
    user = DB.relationship('User',backref=DB.backref('tweets',lazy=True))
