import requests, json
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/test")
def test_app():
    return "<p>OK</p>"

@app.route("/steam")
def steam_api():
    response = requests.get('https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/', params={'appid': '440', 'count': 3})

    return jsonify(response.content.decode())