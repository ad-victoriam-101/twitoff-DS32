from flask import Flask ,render_template

def create_app():
    #initialized our app
    app = Flask(__name__)
    #listen to a route
    #DECORATOR FUNCTION
    @app.route('/')
    def root():
        #what happens when someone goes to the homepage.
        return render_template('base.html', title='Home')

    @app.route('/test')
    def test():
        return 'TEST'

    return app