import json

import flask
from flask import Response, jsonify

import database.auth
import database.tableManagement

get_tables_blueprint = flask.Blueprint("get_tables", __name__)


@get_tables_blueprint.route("/api/table/request/all", methods=["POST"])
def create_table():
    request_data = json.loads(flask.request.data)
    password = request_data.get('password')
    if not database.auth.check_password(password):
        return Response("Wrong password", status=401)
    return jsonify(database.tableManagement.get_all_tables())
