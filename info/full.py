import flask
from flask import Blueprint, Response
import database.auth
import database.restaurant
full_restaurant_info = Blueprint("full_restaurant_info", __name__)

@full_restaurant_info.route("/api/restaurant/info", methods=["POST"])
def info():
    restaurant_data = database.restaurant.full_restaurant_info()
    return flask.jsonify({"name":restaurant_data[0], "image":restaurant_data[1]})