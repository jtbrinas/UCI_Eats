from flask import Flask, jsonify
from flask_cors import CORS
from flask import request
import json


class menu_item:
    name = ""
    description = ""
    rating = 0.0

    def __init__(self, name: str, description: str, rating: float):
        self.name = name
        self.description = description
        self.rating = rating

b_menu_dict = {}
b_ratings_dict = {}
a_menu_dict = {}
a_ratings_dict = {}



app = Flask(__name__)
CORS(app)




@app.route('/receiveFormData',methods=['POST', 'GET'])
def receiveFormData():
    if request.method == "POST":
        food_name = request.form["food_name"]
        rating = float(request.form["rating"])
        item = menu_item(food_name, "temp", rating)
        if item.name not in b_menu_dict:
            b_menu_dict.update({item.name: item.rating})
            b_ratings_dict.update({item.name: 1})
        else:
            num_ratings = b_ratings_dict[item.name]
            rating = b_menu_dict[item.name]
            rating = (rating * num_ratings + item.rating) / (num_ratings + 1)
            b_menu_dict.update({item.name: rating})
            b_ratings_dict.update({item.name: num_ratings + 1})

        print(b_menu_dict)
        return json.dumps(b_menu_dict)

    return json.dumps(b_menu_dict)


@app.route('/receiveFormData2',methods=['POST', 'GET'])
def receiveFormData2():
    if request.method == "POST":
        food_name = request.form["food_name"]
        rating = float(request.form["rating"])
        item = menu_item(food_name, "temp", rating)
        if item.name not in a_menu_dict:
            a_menu_dict.update({item.name: item.rating})
            a_ratings_dict.update({item.name: 1})
        else:
            num_ratings = a_ratings_dict[item.name]
            rating = a_menu_dict[item.name]
            rating = (rating * num_ratings + item.rating) / (num_ratings + 1)
            a_menu_dict.update({item.name: rating})
            a_ratings_dict.update({item.name: num_ratings + 1})

        print(a_menu_dict)
        return json.dumps(a_menu_dict)

    return json.dumps(a_menu_dict)
