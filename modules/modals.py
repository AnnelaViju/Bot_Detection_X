from modules import db,login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User_mgmt.query.get(int(user_id))

class User_mgmt(UserMixin, db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(15),nullable=False,unique=True)
    email = db.Column(db.String(50),nullable=False,unique=True)
    password = db.Column(db.String(80),nullable=False)
    default_profile_image = db.Column(db.String(20),nullable=False,default='default.jpg')
    bg_file = db.Column(db.String(20),nullable=False,default='default_bg.jpg')
    bio = db.Column(db.String(200))
    bday = db.Column(db.String(10))
    statuses_count = db.Column(db.Integer, nullable=False, default=0)
    account_age_days = db.Column(db.Integer, nullable=False, default=1)
    default_profile = db.Column(db.Boolean, nullable=False, default=True)
    verified = db.Column(db.Boolean, nullable=False, default=False)
    followers_count = db.Column(db.Integer, nullable=False, default=0)  # ✅ Ensure this is an integer column
    friends_count = db.Column(db.Integer, nullable=False, default=0)
    favourites_count = db.Column(db.Integer, nullable=False, default=0)
    average_tweets_per_day = db.Column(db.Float, nullable=False, default=0.0)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    bot_status = db.Column(db.String(10), nullable=False, default="Unknown")
    following_count = db.Column(db.Integer, default=0)  # Add this

    posts = db.relationship('Post',backref='author',lazy=True)
    retwitted = db.relationship('Retweet',backref='retwitter',lazy=True)
    bookmarked = db.relationship('Bookmark',backref='saved_by',lazy=True)
    followers = db.relationship('Follow', 
                                foreign_keys='Follow.following_id', 
                                backref='followed_user', 
                                lazy=True)
    
    following = db.relationship('Follow', 
                                foreign_keys='Follow.follower_id', 
                                backref='follower_user', 
                                lazy=True)

    # Dynamic follower/following count properties
    
    def followers_count(self):
        return Follow.query.filter_by(following_id=self.id).count()

    
    def following_count(self):
        return Follow.query.filter_by(follower_id=self.id).count()

class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    tweet = db.Column(db.String(500),nullable=False)
    stamp = db.Column(db.String(20),nullable=False)
    post_img = db.Column(db.String(20))
    user_id = db.Column(db.Integer,db.ForeignKey('user_mgmt.id'),nullable=False)

    retweets = db.relationship('Retweet',backref='ori_post',lazy=True)
    timeline = db.relationship('Timeline',backref='from_post',lazy=True)
    bookmark = db.relationship('Bookmark',backref='saved_post',lazy=True)

class Retweet(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    tweet_id = db.Column(db.Integer,db.ForeignKey('post.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('user_mgmt.id'),nullable=False)
    retweet_stamp = db.Column(db.String(20),nullable=False)
    retweet_text = db.Column(db.String(500),nullable=False)

    timeline = db.relationship('Timeline',backref='from_retweet',lazy=True)

class Timeline(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    post_id = db.Column(db.Integer,db.ForeignKey('post.id'),default=None)
    retweet_id = db.Column(db.Integer,db.ForeignKey('retweet.id'),default=None)

class Bookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'),default=None)
    user_id = db.Column(db.Integer, db.ForeignKey('user_mgmt.id'),default=None)
class Follow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    follower_id = db.Column(db.Integer, db.ForeignKey('user_mgmt.id'), nullable=False)
    following_id = db.Column(db.Integer, db.ForeignKey('user_mgmt.id'), nullable=False)


db.create_all()