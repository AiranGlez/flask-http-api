import requests, json
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# @app.route("/returnjson", methods=['GET', 'POST'])
# def return_json():
#     if(request.method == 'GET'):
#         data = {
#             "Modules" : 15,
#             "Subject" : "Data Structures and Algorithms",
#         }
#     if(request.method == 'POST'):
#         data = {
#             "Modules" : 15,
#             "Subject" : " POST Data Structures and Algorithms",
#         }

#     return jsonify(data)

@app.route("/steam")
def steam_api():
    
    response = requests.get('https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/', params={'appid': '440', 'count': 3})

    return jsonify(response.content.decode())