import pickle

# Load bot detection model
with open("botguard_model.pkl", "rb") as f:
    botguard_model = pickle.load(f)
