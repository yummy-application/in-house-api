import json
import flask
from flask import Response
import globalApiCommunication.restaurantCreation
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
    backend_address = request_data.get('backendAddress')
    if database.restaurant.restaurant_already_exists():
        return Response("There is already another restaurant registered at this ip", status=409)
    database.auth.set_password(password)
    database.restaurant.create_restaurant(restaurant_name, restaurant_image)
    globalApiCommunication.restaurantCreation.create_restaurant(restaurant_name, restaurant_image, password,backend_address)
    return Response("Ok",200)
