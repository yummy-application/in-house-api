import json
import flask
from flask import Response

import database.auth
import database.tableManagement

create_table_blueprint = flask.Blueprint("create_table", __name__)


def validate_values(table_name, number_of_seats, table_region):
    try:
        number_of_seats = int(number_of_seats)
    except ValueError:
        return False
    if number_of_seats < 1:
        return False
    if len(table_name) < 1:
        return False
    if len(table_region) < 1:
        return False
    return True

@create_table_blueprint.route("/api/table/create", methods=["POST"])
def create_table():
    request_data = json.loads(flask.request.data)
    password = request_data.get('password')
    table_name = request_data.get('tableName')
    number_of_seats = request_data.get('seats')
    table_region = request_data.get('tableRegion')
    if not database.auth.check_password(password):
        return Response("Wrong password", status=401)
    if not validate_values(table_name, number_of_seats, table_region):
        return Response("Invalid values", status=400)
    if database.tableManagement.table_exists(table_name):
        return Response("Table already exists", status=409)
    database.tableManagement.create_table(table_name, number_of_seats, table_region)
    return Response("Ok", 200)
