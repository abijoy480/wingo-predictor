from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return "Wingo Prediction Bot is live!"

@app.route('/predict')
def predict():
    result = subprocess.run(["python3", "main.py"], capture_output=True, text=True)
    return result.stdout