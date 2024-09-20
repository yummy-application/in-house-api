import json
import flask
from flask import Response

import database.auth
import database.restaurant
import validation.HashPassword
create_restaurant = flask.Blueprint("create_restaurant", __name__)


@create_restaurant.route("/api/restaurant/register", methods=["POST"])
def register_restaurant():
    request_data = json.loads(flask.request.data)
    restaurant_name = request_data.get('name')
    restaurant_image = request_data.get('image')
    password = request_data.get('password')
    if database.restaurant.restaurant_already_exists():
        return Response("There is already another restaurant registered at this ip", status=409)
    with open("config.json", "r") as f:
        json_data = json.load(f)
        json_data["name"] = restaurant_name
        json_data["image"] = restaurant_image
    with open("config.json", "w") as f:
        json.dump(json_data,f)
    database.auth.set_password(password)
    database.restaurant.create_restaurant(restaurant_name, restaurant_image)
    return Response("Ok",200)
