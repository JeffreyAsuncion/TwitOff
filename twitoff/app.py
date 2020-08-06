from flask import Flask, render_template
from .db_model import db

def create_app():
    '''Create and configure an instance of the Flask application'''

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:\\Users\\jeffr\\mystuff\\TWITOFF\\twitoff\\twitoff.sqlite" 
    # using absolute filepath on Windows (recommended) h/t: https://stackoverflow.com/a/19262231/670433
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    @app.route('/')
    def root():
        return render_template('base.html')
    
    return app
