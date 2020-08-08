# Web app
1. type in a tweet
2. compare who is more likely to say that tweet


# Lecture 1
1. build framework API
2. database

class work
1. pipenv install flask FLASK-SQLAlchemy
2. hello.py (flask example doc) function and @app.route is the decorator
3. to run hello.py
... export FLASK_APP=hello.py
... flask run
4. new file : __init__.py
5. new file : app.py with def create_app()
6. to run twitoff
... export FLASK_APP=twitoff:APP
... flask run
7. create database https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
... create db_model.py
... class User(db.Model) will create table user
... class Tweet(db.Model) will create table tweet
8. flask shell - assignment add to db
```py
>>> from twitoff.db_model import db, User, Tweet
>>> db.create_all()
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
'''
9. connect to user table and tweet table with TablePlus
... confirm inserts to db
10. 