
# twitter scraper
https://github.com/bisguzar/twitter-scraper

pipenv install Flask Flask-SQLAlchemy



8/5/2020 10:58

from flask import Flask
def create_app():
    '''Create and configure an instance of the Flask application'''
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:\\Users\\bruno\\Desktop\\DSPT6-Twitoff\\twitoff\\twitoff.sqlite"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    @app.route('/')
    def root():
        return 'Welcome to Twitoff!'
    return app



see work notes about added to the db

data_to_add = table_name(column1, column2, col3, ...)
db.session.add(data_t0_add)
db.session.commit()