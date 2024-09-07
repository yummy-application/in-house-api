import flask
from flask import Blueprint, Response
import database.auth
import database.restaurant
full_restaurant_info = Blueprint("full_restaurant_info", __name__)

@full_restaurant_info.route("/api/restaurant/info", methods=["POST"])
def info():
    password_hash = flask.request.headers.get('passwordHash')
    if not database.auth.check_password(password_hash):
        return Response("Wrong password", status=401)
    restaurant_data = database.restaurant.full_restaurant_info()
    return flask.jsonify({"name":restaurant_data[0], "image":restaurant_data[1]})