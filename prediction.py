import pickle
from typing import Dict
import numpy as np

# Load the trained model and scaler
#load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)
# Load the scaler later
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

def predict_price(device: Dict) -> int:
    # Extract features
    features = [
        device['battery_power'],
        device['blue'],
        device['clock_speed'],
        device['dual_sim'],
        device['fc'],
        device['four_g'],
        device['int_memory'],
        device['m_dep'],
        device['mobile_wt'],
        device['n_cores'],
        device['pc'],
        device['px_height'],
        device['px_width'],
        device['ram'],
        device['sc_h'],
        device['sc_w'],
        device['talk_time'],
        device['three_g'],
        device['touch_screen'],
        device['wifi']
    ]

    # Apply scaling
    scaled_features = scaler.transform([features])
    predicted_price = model.predict(scaled_features)
    return int(predicted_price[0])
