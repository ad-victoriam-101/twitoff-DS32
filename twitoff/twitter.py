    """Handles connection to twitter API via tweepy, 
    Installs required packages to read env files and secure load keys. 
    """
    
from os import getenv
import tweepy
import spacy
from .models import DB,Tweet,User

#get API KEYS and assign them to local vars
key = getenv('TWITTER_API_KEY')
secret = getenv('TWITER_API_KEY_SECRET')

#connect to the twitter API 
TWITTER_AUTH = tweepy.OAuthHandler(key,secret)
TWITER = tweepy.API(TWITTER_AUTH)

def add_or_update_uer(username):
    """Takes Username and pulls user twitter data from API

    Args:
        username ([string]): [unique twitter handle]
    """
    twitter_user = TWITTER.get_user(screen_name=username)
    #check if there is a User in our db with this id,
    #if not create user and generate with this id
    db_user = (User.query.get(twitter_user.id)) or User(id=twitter_user.id,username=username)
    
    #add user the DB
    DB.session.add(db_user)
    
    tweets = twitter_user.timeline(count= 200, exclude_replies= True, include_rts= False, tweet_mode= 'extended')
    
    #add each tweet for a user to the DB.
    
    for tweet in tweets:
        db_tweet= Tweet(id= tweet.id, text= tweet.full_text[:300])
        db_user.tweets.append(db_tweet)
        DB.session.add(db_tweet)
        
    DB.session.commit()