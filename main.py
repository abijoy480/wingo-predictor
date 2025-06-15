import requests
import random
from datetime import datetime
from flask import Flask
import os

# Telegram Configuration
BOT_TOKEN = "7751314755:AAFXmYJ2lW7xZhU7Tx1lJuqCxG8LfbKnNZM"
CHAT_ID = "6848807471"

# Dummy data fetch
def fetch_data():
    return [random.randint(0, 9) for _ in range(100)]

# Simple prediction
def train_and_predict(data):
    return max(set(data), key=data.count)

# Telegram sender
def send_to_telegram(prediction):
    color = "Green" if prediction in [1, 3, 7, 9] else "Red" if prediction in [2, 4, 6, 8] else "Violet"
    big_small = "Big" if prediction >= 5 else "Small"
    msg = f"📊 Wingo 1 Min Prediction\n\n🌀 Period: {datetime.now().strftime('%Y%m%d%H%M%S')}\n🔮 Result: {prediction} ({big_small})\n🎨 Color: {color}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

# Flask App
app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Wingo Predictor Bot is Running!"

@app.route('/predict')
def predict():
    past_data = fetch_data()
    prediction = train_and_predict(past_data)
    send_to_telegram(prediction)
    return f"✅ Prediction sent to Telegram! Predicted: {prediction}"

# For Render.com
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
