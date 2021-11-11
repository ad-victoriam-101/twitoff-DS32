from flask import Flask, render_template
from .models import DB, User, Tweet
from .env import TWITTER_API_KEY,TWITTER_API_KEY_SECRET

def create_app():
    # initializes our app
    app = Flask(__name__)

    # Database configurations
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///db.sqlite3'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Give our APP access to our database
    DB.init_app(app)

    # Listen to a "route"
    # '/' is the home page route
    @app.route('/')
    def root():
        # query the DB for all users
        users = User.query.all()
        #what I want to happen when somebody goes to home page
        return render_template('base.html', title="Home", users=users)

    @app.route('/populate')
    def populate():
        ryan = User(id=1, username='Ryan')
        DB.session.add(ryan)
        julian = User(id=2, username='Julian')
        DB.session.add(julian)
        brogan = User(id=3, username='Brogan')
        DB.session.add(brogan)
        derick = User(id=4, username='Derick')
        DB.session.add(derick)
        steve = User(id=5, username='Steve')
        DB.session.add(steve)
        danielle = User(id=6, username='Danielle')
        DB.session.add(danielle)
        tweet1 = Tweet(id=1, text='tweet text', user=ryan)
        DB.session.add(tweet1)
        tweet2 = Tweet(id=2, text="julian's tweet", user=julian)
        DB.session.add(tweet2)
        tweet3 = Tweet(id= 3, text= 'Who put this rock here?', user= brogan)
        DB.session.add(tweet3)
        tweet4 = Tweet(id=1, text='New phone who dis', user=ryan)
        DB.session.add(tweet1)
        tweet5 = Tweet(id=2, text="Just drove my car into a lake", user=julian)
        DB.session.add(tweet2)
        tweet6 = Tweet(id= 3, text= 'Who has a car in the lake?', user= brogan)
        # save the database
        DB.session.commit()
        return '''Created some users. 
        <a href='/'>Go to Home</a>
        <a href='/reset'>Go to reset</a>
        <a href='/populate'>Go to populate</a>'''
        
    @app.route('/reset')
    def reset():
        # remove everything from the database
        DB.drop_all()
        # Creates the database file initially.
        DB.create_all()
        return '''The database has been reset. 
        <a href='/'>Go to Home</a>
        <a href='/reset'>Go to reset</a>
        <a href='/populate'>Go to populate</a>'''




    return app