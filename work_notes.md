# Web app
1. type in a tweet
2. compare who is more likely to say that tweet


video https://www.youtube.com/watch?v=yKyS6_OHs_I
notes https://github.com/JeffreyAsuncion/lambda-ds-3-3
# Lecture 1       
1. build framework API
2. database

Topics / Agenda:

HTTP, Client-server architecture; Web Application Routing
Web Application Views and View Templates
Adding a database w/ Flask SQL Alchemy



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

Topics / Agenda:

Integrating with an example API (bonus)
Integrating with the Twitter API
Integrating with the Basilica API
Storing API data in the database


1. Deploying API 
common way is render_template
as Data Scientists we will be returning data : in the from of a .json 


2. explain the flow of base.html
['POST'] requests == adding data or contributing data to be stored in the database
['GET'] requests == pull data from the database and populate on the front end

3. db.model built on flask-sqlalchemy 
review of the Classes and the values that they store and types
and the foreign key and relationships many-to-many

4. work_notes.md to record 
the workflow of different projects 
... small
... large
... significant




1. get access to Twitter API as developer
... get approved
... create app
... application description - An application to pull user tweets and predict tweet authorship based on historical tweets
... website url - https://twitoff-nyc.herokuapp.com/
... Tell us how this app will be used - This app will not display analysis of Tweets, Twitter users, or their content. It will not tweet, retweet, or otherwise push new data to Twitter. It will be used for instructional purposes to learn how to develop web apps with third party APIs.

2. API Access
... API Keys and Tokens they have been truncated because they are my credentials

TWITTER_CONSUMER_API_KEY='IK'
TWITTER_CONSUMER_API_SECRET='md'
TWITTER_ACCESS_TOKEN='12'
TWITTER_ACCESS_TOKEN_SECRET='iO'


3. Basilica API key
... just open account and get access
BASILICA_KEY='29'

4. instagram or facebook API access is similar to Twitter
... apply
... wait
... get access

5. working in ColabNotebook

import tweepy 
import basilica

TWITTER = tweepy.API(TWITTER_AUTH)
dir(TWITTER) ### to see the methods available

twitter_user = TWITTER.get_user("elonmusk")
twitter_user #### look at the output

twitter_user.id


tweets = twitter_user.timeline()
tweets ### list of tweets


BASILICA has alot of different things # 1:03:41

BASILICA.embed_image
BASILICA.embed_image_file
BASILICA.embed_image_files
BASILICA.embed_sentence
BASILICA.embed_sentences




6. add to twitter.py
from colab notebook

def add_user_tweepy(username):
    '''Add a user and their tweets to database'''
    try:
        # Get user info from tweepy
        twitter_user = TWITTER.get_user(username)

        # Get tweets ignoring re-tweets and replies
        tweets = twitter_user.timeline(count=200,
                                   exclude_replies=True,
                                   include_rts=False,
                                   tweet_mode='extended')
    
        # Get an examble basilica embedding for first tweet
        embedding = BASILICA.embed_sentence(tweets[0].full_text, model='twitter')
    except Exception as e:
        print('Error processing {}: {}'.format(username, e))
        raise e
    
    return tweets, embedding


7. twitter scraper demo - 1:15:29



8. db.model.py
#for tweet table
class Tweet(db.Model):

    #add user_id
    user_id = db.Column(db.BigInteger, db.ForeignKey('user.id'), nullable=False)
    embedding = db.Column(db.PickleType, nullable=False)


9. flask shell 1:46:29
from twitoff.db_model import db, User, Tweet
# here in the video he deleted the sqlite3 file in windows explorer
# use this instead
db.drop_all()
db.create_all() # creates tables with updated schema . Check in TablePlus
exit()



10. pipenv install tweepy basilica python-dotenv twitter_scraper



11.  create twitter.py

# copy to .env    ### NOTE this are not the real credentials
# TWITTER_CONSUMER_API_KEY='IKc6Ly6uK4X'
# TWITTER_CONSUMER_API_SECRET='mdggKpM7djbtWY'
# TWITTER_ACCESS_TOKEN='12864893012330'
# TWITTER_ACCESS_TOKEN_SECRET='iOuavCdDFRJW'
# BASILICA_KEY='296448251bd20'

from os import getenv
import basilica
import tweepy  # or twitter_scraper
from dotenv import load_dotenv
from .db_model import db, User, Tweet

load_dotenv()

TWITTER_AUTH = tweepy.OAuthHandler(getenv('TWITTER_CONSUMER_API_KEY'),
                                   getenv('TWITTER_CONSUMER_API_SECRET'))
TWITTER_AUTH.set_access_token(getenv('TWITTER_ACCESS_TOKEN'),
                              getenv('TWITTER_ACCESS_TOKEN_SECRET'))
TWITTER = tweepy.API(TWITTER_AUTH)
BASILICA = basilica.Connection(getenv('BASILICA_KEY'))




12. add to 
def add_user_tweepy(username):
    #
    #
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
                                    tweet_mode='extended',
                                    since_id=db_user.newest_tweet_id)

    # Add newest_tweet_id to the User table
    if tweets:
        db_user.newest_tweet_id = tweets[0].id
    
    # Loop over tweets, get embedding and add to Tweet table
    for tweet in tweets:

        # Get an examble basilica embedding for first tweet
        embedding = BASILICA.embed_sentence(tweet.full_text, model='twitter')

        # Add tweet info to Tweet table
        db_tweet = Tweet(id=tweet.id,
                            text=tweet.full_text[:300],
                            embedding=embedding)
        db_user.tweet.append(db_tweet)
        db.session.add(db_tweet)
    #
    #
    #


13. add a route to app.py to implement twitter.py

    @app.route('/user', methods=['POST'])
    @app.route('/user/<name>', methods=['GET'])
    def user(name=None, message=''):
        name = name or request.values['user_name']
        if '@' in name:
            name = name.replace('@','')
        try:
            if request.method == 'POST':
                add_user_tweepy(name)
                message = "User {} successfully added!".format(name)
            tweets = User.query.filter(User.username == name).one().tweet
        except Exception as e:
            message = "Error adding {}: {}".format(name, e)
            tweets = []
        return render_template('user.html', title=name, tweets=tweets, message=message)


14. assignment make this work and 
export FLASK_APP=twitoff:APP
flask run







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






Lecture 4 - https://www.youtube.com/watch?v=QnLusV7Tn0w

Web Application Deployment

At the end of this module, you should be able to:
deploy a basic (single-server) web application to common cloud services
securely connect a deployed web application to a relational database back-end



1. Twitter Scraper has errors already it was broken because they have team 3:10
they have a team to break popular scrapers

2. API access is more reliable.

3. conda deactivate
pipenv shell
export FLASK_APP=twitoff:APP
flask run


4. test your API with postman 0:11:28  to 0:20:45
you will do this in build week Build Week



5. we will be creating 2 more routes to    0:20:46
... update users AND 
... admin route to reset the database 

@app.route('/update') # if you do not specific method the default is ['GET']

#in app.py create_app
from .twitter import add_user_tweepy, update_all_users

    @app.route('/update', methods=['GET'])
    def update():
        update_all_users()
        return render_template('base.html', title='All Tweets Updated!', users=User.query.all())


#define it in twitter.py
def update_all_users():
    '''Update all tweets for all users in the User database'''
    for user in User.query.all():
        add_user_tweepy(user.username)



6. add the admin route to reset the database
#in app.py create_app
    @app.route('/reset')
    def reset():
        db.drop_all()
        db.create_all()
        return render_template('base.html', title='Database has been Reset!', users=User.query.all()) 



DEPLOYING TO HEROKU - https://dashboard.heroku.com/apps

1. download and setup Heroku CLI

2. Run in ANACONDA PROMPT

3. goto project folder  cd/mystuff/twitoff code .

4. log in to heroku from cli
> heroku login

5. https://dashboard.heroku.com/apps
> new
> create new app
# on deployment page options for heroku git, github, container Registry

6. anaconda prompt

heroku git:remote -a <nameOfApp>

git remote --verbose to see what is going on #### This set not necessery to deploy


7. in VSCODE

git add .
git commit -m 'Initial commit before deploying to heroku'
git push origin master


8. back in anaconda prompt

git push heroku master


9. still a procfile will not run 0:50:47 #######################################################


10. pipenv install gunicorn psycopg2


11. create procfile in base dir

Procfile
web: gunicorn twitoff:APP -t 300


12. to ignore your sqlite3 database
in your .env file
add 
# Ignore sqlite DB
*.sqlite









Switch out local database to 

