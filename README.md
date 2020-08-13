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
JOIN user on tweet.user_id = user.id;




2. 1:08:55 In build week and many data science projects
Paradighm if you are in a big enough team
not full stack data scientist doing everything end to end
common paradign similar to this build week

You will play the role of data engineer
1. set up the database
2. deploy the model

Unit Four person 
- notebook model developement
- train model

support them by 
- making sure they use a pipenv
- or conda environment
- so that you can re-create their enviroment

their ideal delivery to you 
- here is a notebook
- here is the things i did
- best teammate ever will have everything factored into funcitons
give you a 
- notebook
- pickle file

you will train a model off line
use it to make predictions
1:10:28   1:15:00
what ever preprocessing to get the data into the format needed for prediction



3. 21:25:29 Discussion about pickle

decision to train on the fly
the model will be trained 

TODO check bruno repo 
twitter.py
def add_user_history(username):

# TODO: check bruno repo 
# twitter.py
# def add_user_history(username):
# he used this in the flask shell to collect tweets for the database
def add_user_history(username):
    '''Add a user and their tweets to database'''
    try:
        # Get user info from tweepy
        twitter_user = TWITTER.get_user(username)
        # Add to User table (or check if existing)
        db_user = (User.query.get(twitter_user.id) or
                   User(id=twitter_user.id,
                        username=username,
                        follower_count=twitter_user.followers_count))
        db.session.add(db_user)
        # Get tweets ignoring re-tweets and replies
        tweets = twitter_user.timeline(count=200, 
                                       exclude_replies=True, 
                                       include_rts=False, 
                                       tweet_mode='extended')
        oldest_max_id = tweets[-1].id - 1
        tweet_history = []
        tweet_history += tweets
        # Add newest_tweet_id to the User table
        if tweets:
            db_user.newest_tweet_id = tweets[0].id
        # Continue to collect tweets using max_id and update until 3200 tweet max
        while True:
            tweets = twitter_user.timeline(count=200,
                                        exclude_replies=True,
                                        include_rts=False,
                                        tweet_mode='extended',
                                        max_id=oldest_max_id)
            if len(tweets) == 0:
                break
            oldest_max_id = tweets[-1].id - 1
            tweet_history += tweets 
        print(f'Total Tweets collected for {username}: {len(tweet_history)}')
        # Loop over tweets, get embedding and add to Tweet table
        for tweet in tweet_history:
            # Get an examble basilica embedding for first tweet
            embedding = BASILICA.embed_sentence(tweet.full_text, model='twitter')
            # Add tweet info to Tweet table
            db_tweet = Tweet(id=tweet.id,
                             text=tweet.full_text[:300],
                             embedding=embedding)
            db_user.tweet.append(db_tweet)
            db.session.add(db_tweet)
    except Exception as e:
        print('Error processing {}: {}'.format(username, e))
        raise e
    else:
        # If no errors happend than commit the records
        db.session.commit()
        print('Successfully saved tweets to DB!')

    
4. twittoff/app.py/create_app()
add

    @app.route('/compare', methods=['POST'])  ########## will be a POST because we will post 3 inputs

? this is where a bar chart or a pie graph to show what is going on here.
? how do we get the data that the front end is passing in?
    @app.route('/compare', methods=['POST'])
    def compare(message='')
    ############ Look in base.html for the variable names
        user1  =
        user2  = 
        tweet_text = 
ans.
    @app.route('/compare', methods=['POST'])
    def compare(message='')
        user1  = request.values['user1']
        user2  = request.values['user2']
        tweet_text = request.values['tweet_text']


5. next add prediction
    @app.route('/compare', methods=['POST'])
    def compare(message='')
        user1  = request.values['user1']
        user2  = request.values['user2']
        tweet_text = request.values['tweet_text']

        prediction = predict_user(user1, user2, tweet_text)



6. predict_user() in separate file
twitoff/predict.py

'''Prediction of Users based on Tweet embeddings'''
from sklearn.linear_model import LogisticRegression
from .db_model import User
from .twitter import BASILICA

def predict_user(user1, user2, tweet_text):
    '''Determine and return which user is more likely to say a given tweet.
    
    # Arguments:
        user1: str, twitter user name for user 1 in comparison from web form
        user2: str, twitter user name for user 2 in comparison from web form
        tweet_text: str, tweet text to evaluate

    # Returns:
        prediction from logistic regression model
    '''
    user1 = User.query.filter(User.username == user1).one()  #one() == fetch() in sqlite
    user2 = User.query.filter(User.username == user2).one()
    user1_embeddings = np.array([tweet.embedding for tweet in user1.tweet]) # return all user1 embeddings
    user2_embeddings = np.array([tweet.embedding for tweet in user2.tweet])
    
    # Combine embeddings and crate labels
    embeddings = np.vstack([user1_embeddings, user2_embeddings])
    labels = np.concatenate([np.ones(len(user1_embeddings)),
                             np.zeros(len(user2_embeddings))])

    # Train model and convert input text to embedding
    lr = LogisticRegression().fit(embeddings, labels)
    tweet_embedding = BASILICA.embed_sentence(tweet_text, model='twitter')

    # return lr.predict([tweet_embedding])
    return lr.predict([tweet_embedding])[0]





7. prediction.html

{% extends "base.html" %}
{% block content %}
<div id="prediction">
  <h2>{{ title }}</h2>
  <p>{{ message }}</p>    ############## you can add a probability here or something else or images  1:49:55?
</div>
{% endblock %}



8. back to app.py

    @app.route('/compare', methods=['POST'])
    def compare(message='')
        user1  = request.values['user1']
        user2  = request.values['user2']
        tweet_text = request.values['tweet_text']

        prediction = predict_user(user1, user2, tweet_text)

        return render_template() ################ working on render_template()


9. anticapate how people are going to break this.
- wierd non sencsical results
- user1 == user2

    @app.route('/compare', methods=['POST'])
    def compare(message=''):
        user1  = request.values['user1']
        user2  = request.values['user2']
        tweet_text = request.values['tweet_text']

        if user1 == user2:
            message = 'Cannot compare a user to themselves'
        else:
            prediction = predict_user(user1, user2, tweet_text)
            message = '"{}" is more likely to be said by {} than {}'.format(
                tweet_text, user1 if prediction else user2, user2 if prediction else user1
            )

        return render_template('prediction.html', title='Prediction', message=message)

10. import to app.py.
from .predict import predict_user



11. import to predict.py
import numpy as np


12. 1:56:54




41-44
      <div id="prediction">
        <h2>{{ title }}</h2>
        <p>{{ message }}</p>
      </div>