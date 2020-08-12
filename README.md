# TwitOff
a fun web application for comparing and predicting tweet authorship


This is the class notes and work for DSPT6 
WebApp101 is based off of DS15

https://github.com/bruno-janota/DSPT6-Twitoff

TODO: base.html

export FLASK_APP=twitoff:APP
flask shell

from twitoff.db_model import db, User, Tweet
db.create_all()
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




LECTURE # 


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



========================
video 2

pipenv install






Lecture 3

pipenv install --dev jupyter matplotlib
pipenv install scikit-learn pandas


Bruno is explaining the flow of the app from runtime 0:06:34

with you set the environment variable 
>>> export FLASK_APP=TwitOff:APP
>>> flask run

go to __init.py__ will initatize the TwitOff
APP = create_app() is created

@app.route('/')
root():  is rendering 'base.html'
title is 'Home'
users is the list of users from our users table in database

base.html is the style of our homepage

0:07:37 talking about update tweets and Reset Database(admin stats)
for sprint challenge
#### SEE MIKES NOTES
#### SECTION 0

methods=['POST'] ADDING USERS
methods=['GET']  QUERY AND FETCHING USERS and TWEETS

1. open a jupyter notebook with the pipenv settings 0:22:54

pipenv run jupyter notebook

tweets and username : SQL statement
SELECT
    tweet.id,
    tweet.text,
    tweet.embedding,
    user.username
FROM tweet
JOIN user on tweet.user_id = user.id







