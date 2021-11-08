from flask import Flask
#initialized our app
app = Flask(__name__)
#listen to a route
#DECORATOR FUNCTION
@app.route('/')
def root():
    #what happens when someone goes to the homepage.
    return 'HELLO WORLD'

@app.route('/test')
def test():
    return "TEST WORLD"
    