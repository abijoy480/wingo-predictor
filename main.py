import requests
import time
import random
from datetime import datetime

# Telegram Configuration
BOT_TOKEN = "7751314755:AAFXmYJ2lW7xZhU7Txl1JuqCxG8LfbKmNZM"
CHAT_ID = "6848807471"

def fetch_data():
    # Dummy data simulation
    return [random.randint(0, 9) for _ in range(100)]

def train_and_predict(data):
    return max(set(data), key=data.count)

def send_to_telegram(prediction):
    color = "Green" if prediction in [1, 3, 7, 9] else "Red" if prediction in [2, 4, 6, 8] else "Violet"
    big_small = "Big" if prediction >= 5 else "Small"
    msg = f"🧠 Wingo 1 Min Prediction\n\n📊 Period: {datetime.now().strftime('%Y%m%d%H%M%S')}\n🎯 Result: {prediction} ({big_small})\n🎨 Color: {color}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

def main():
    past_data = fetch_data()
    prediction = train_and_predict(past_data)
    send_to_telegram(prediction)

if __name__ == "__main__":
    main()