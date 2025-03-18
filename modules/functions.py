from modules import app
from modules import app
from modules.model_loader import botguard_model
import datetime
import numpy as np
import secrets
import os

def save_profile_picture(form_pic):
    random_hex = secrets.token_hex(8)
    f_name,f_ext = os.path.splitext(form_pic.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/Images/Users/profile_pics', picture_fn)
    form_pic.save(picture_path)
    return picture_fn

def save_bg_picture(form_pic):
    random_hex = secrets.token_hex(8)
    f_name,f_ext = os.path.splitext(form_pic.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/Images/Users/bg_pics', picture_fn)
    form_pic.save(picture_path)
    return picture_fn

def delete_old_images(image, bg_image):
    profile_pic_path = os.path.join(app.root_path, 'static/Images/Users/profile_pics', image)
    bg_pic_path = os.path.join(app.root_path, 'static/Images/Users/bg_pics', bg_image)
    if image!='default.jpg' and image!='':
        try:
            os.remove(profile_pic_path)
        except OSError:
            pass
    if bg_image!='default_bg.jpg' and bg_image!='':
        try:
            os.remove(bg_pic_path)
        except OSError:
            pass

def save_tweet_picture(form_pic):
    random_hex = secrets.token_hex(8)
    f_name,f_ext = os.path.splitext(form_pic.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/Images/Tweets', picture_fn)
    form_pic.save(picture_path)
    return picture_fn


def get_user_features(user):
    """Extract relevant features from the user object for bot detection."""
    account_age = (datetime.datetime.utcnow() - user.created_at).days
    tweet_freq = user.statuses_count / max(1, account_age)

    # ✅ Convert method calls to attribute values
    followers = user.followers_count() if callable(user.followers_count) else user.followers_count
    friends = user.friends_count() if callable(user.friends_count) else user.friends_count
    following = user.following_count() if callable(user.following_count) else user.following_count

    favourites_per_tweet = user.favourites_count / max(1, user.statuses_count)
    followers_to_friends_ratio = followers / max(1, friends)

    features = np.array([
        int(user.default_profile),
        followers,
        friends,
        user.statuses_count,
        user.favourites_count,
        account_age,
        tweet_freq,
        followers_to_friends_ratio,
        favourites_per_tweet,
        int(user.verified),
        user.average_tweets_per_day,
        following  # ✅ Corrected: Ensure it's an integer
    ]).reshape(1, -1)

    return features


def detect_bot(user):
    """Predict if a user is a bot."""
    features = get_user_features(user)
    prediction = botguard_model.predict(features)
    return "Bot" if prediction[0] == 1 else "Human"
# def detect_bot(user):
#      """Predict if a user is a bot using the trained model."""
#      features = get_user_features(user)

#     # ✅ Debugging: Print each feature and its type
#      print("DEBUG: Feature array before prediction:")
#      for i, feature in enumerate(features[0]):
#         print(f"Feature {i}: {feature} (Type: {type(feature)})")

#     # ✅ Ensure all values are numbers
#      features = features.astype(float)  # Convert to float explicitly

#      prediction = botguard_model.predict(features)  # Predict bot/human
#      return "Bot" if prediction[0] == 1 else "Human"
