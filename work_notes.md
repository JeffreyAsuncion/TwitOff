# Web app
1. type in a tweet
2. compare who is more likely to say that tweet


video https://www.youtube.com/watch?v=yKyS6_OHs_I
notes https://github.com/JeffreyAsuncion/lambda-ds-3-3
# Lecture 1       
1. build framework API
2. database

class work

1. github setup a repo for twit off
2. get url for git
3. git clone <repo>
4. cd <repo> code .
5. in git.bash 
conda deactivate
6. pipenv install .... or pipenv shell

BONUS!!!!!
# twitter scraper
https://github.com/bisguzar/twitter-scraper

1. pipenv install flask FLASK-SQLAlchemy
2. hello.py (flask example doc) function and @app.route is the decorator
3. to run hello.py
... export FLASK_APP=hello.py
... flask run

3a. https://docs.google.com/presentation/d/1K83U0VjYob6dgdRodbidWBtFxK4Q_9h8zojzmto2wJY/edit#slide=id.g5846519fbe_0_1904
    discussion about front end, back end and database, API

3b. BUILD WEEK STUFF 0:52:52
    postman is to test api


SETUP TwitOFf webApp

4. new file : __init__.py
5. new file : app.py with def create_app()
6. to run twitoff
... export FLASK_APP=twitoff:APP
... flask run


CONFIGURE DATABASE 

7. create database https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

... create db_model.py
... class User(db.Model) will setup(not create) table user
... class Tweet(db.Model) will setup(not create) table tweet
one-to-many
many-to-many 1:28:50

in SQL we do a JOIN 
... in flask-sqlalchemy we do db.relationship


CREATE DATABASE in FLASK SHELL

8. flask shell - assignment add to db
```py
>>> from twitoff.db_model import db, User, Tweet
>>> db.init_app(app) ######### associate db.model with the FLASK_APP : this is also in create_app
>>> db.create_all()     ################################### this creates the db
>>> u1 = User(username='Austen', follower_count=135000)
>>> db.session.add(u1)
>>> u2 = User(username='Trump', follower_count=1000000)
>>> db.session.add(u2)
>>> u3 = User(username='Michael Jackson', follower_count=50000000)
>>> db.session.add(u3)
>>> u4 = User(username='George Jetson', follower_count=10000)
>>> db.session.add(u4)
>>> u5 = User(username='OMD', follower_count=235000)
>>> db.session.add(u5)
>>> u6 = User(username='Yankees', follower_count=6000000)
>>> db.session.add(u6)
>>> db.session.commit()
>>> t1 = Tweet(text='Yeah, Baby. the spy who shagged me.')
>>> db.session.add(t1)
>>> t2 = Tweet(text='Make America Great Again!')
>>> db.session.add(t2)
>>> t3 = Tweet(text='Just Beat It!')
>>> db.session.add(t3)
>>> t4 = Tweet(text='Meet the Jetsons!')
>>> db.session.add(t4)
>>> t5 = Tweet(text='When you leave dont think twice.')
>>> db.session.add(t5)
>>> t6 = Tweet(text='Derek Jeter!')
>>> db.session.add(t6)
>>> db.session.commit()

8 a. setup db in webapp
def create_app():
    '''Create and configure an instance of the Flask application'''

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)


NOTE any variable not defined in the file must be 
from .file import variable



9. connect to user table and tweet table with TablePlus
... confirm inserts to db





Lecture 2 





