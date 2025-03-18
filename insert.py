from modules import db
from modules.modals import User_mgmt
from werkzeug.security import generate_password_hash
from datetime import datetime

# Sample user entries
sample_users = [
#     User_mgmt(username="john_doe", email="john@example.com", password=generate_password_hash("password1"), 
#               followers_count=200, friends_count=180, statuses_count=150, 
#               account_age_days=1200, verified=True, bot_status="Human"),
    
#     User_mgmt(username="bot_1234", email="bot1234@example.com", password=generate_password_hash("password2"), 
#               followers_count=10, friends_count=5, statuses_count=10000, 
#               account_age_days=90, verified=False, bot_status="Bot"),

#     User_mgmt(username="alice_wonder", email="alice@example.com", password=generate_password_hash("password3"), 
#               followers_count=500, friends_count=400, statuses_count=1200, 
#               account_age_days=2000, verified=True, bot_status="Human"),

#     User_mgmt(username="news_aggregator", email="newsbot@example.com", password=generate_password_hash("password4"), 
#               followers_count=15, friends_count=8, statuses_count=20000, 
#               account_age_days=50, verified=False, bot_status="Bot"),

#     User_mgmt(username="crypto_trader", email="crypto@example.com", password=generate_password_hash("password5"), 
#               followers_count=1100, friends_count=1050, statuses_count=800, 
#               account_age_days=1400, verified=True, bot_status="Human"),

#     User_mgmt(username="spam_bot_007", email="spam@example.com", password=generate_password_hash("password6"), 
#               followers_count=3, friends_count=1, statuses_count=30000, 
#               account_age_days=25, verified=False, bot_status="Bot"),

#     User_mgmt(username="susan_tech", email="susan@example.com", password=generate_password_hash("password7"), 
#               followers_count=400, friends_count=350, statuses_count=500, 
#               account_age_days=1000, verified=True, bot_status="Human"),

#     User_mgmt(username="deepfake_news", email="fake_news@example.com", password=generate_password_hash("password8"), 
#               followers_count=7, friends_count=2, statuses_count=25000, 
#               account_age_days=60, verified=False, bot_status="Bot"),

#     User_mgmt(username="elonmusk_real", email="elon@example.com", password=generate_password_hash("password9"), 
#               followers_count=5000000, friends_count=2000, statuses_count=4500, 
#               account_age_days=5000, verified=True, bot_status="Human"),

#     User_mgmt(username="unknown_bot", email="unknownbot@example.com", password=generate_password_hash("password10"), 
#               followers_count=1, friends_count=0, statuses_count=50000, 
#               account_age_days=15, verified=False, bot_status="Bot"),
            User_mgmt(
                username="bo_account",
                email="boooo@example.com",
                password=generate_password_hash("securepassword"), 
                default_profile=1,  # Bots often use default profile settings
                default_profile_image=1,  # Bots often don't change profile pictures
                favourites_count=3,  # Bots rarely like tweets
                followers_count=15,  # Bots have very few or artificially high followers
                friends_count=5000,  # Bots follow many accounts
                statuses_count=25000,  # Bots tweet excessively
                verified=0,  # Bots are usually not verified
                average_tweets_per_day=250,  # Bots tweet frequently
                account_age_days=10,  # Bots are usually newly created
                bot_status="Bot"  # Marked as a bot
            ),
            
 ]

# Function to insert users into the database
def insert_users():
    db.create_all()  # Ensure tables are created
    db.session.bulk_save_objects(sample_users)  # Add multiple users
    db.session.commit()
    print("✅ 10 Sample Users Inserted Successfully!")

if __name__ == "__main__":
    insert_users()
