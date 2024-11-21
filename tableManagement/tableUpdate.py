import json
import flask
from flask import Response
import database.auth
import database.tableManagement
import globalApiCommunication.userAuth

update_table_blueprint = flask.Blueprint("update_table", __name__)


@update_table_blueprint.route("/api/table/update/status", methods=["POST"])
def update_table_status():
    request_data = json.loads(flask.request.data)
    password = request_data.get('password')
    table_name = request_data.get('tableName')
    new_status = request_data.get('newStatus').lower()
    if not database.auth.check_password(password):
        return Response("Wrong password", status=401)
    database.tableManagement.update_table_status(table_name, new_status)
    return Response("Ok", 200)

@update_table_blueprint.route("/api/client/table/update", methods=["POST"])
def update_table_client_request():
    request_data = json.loads(flask.request.data)
    jwt = request_data.get('jwt')
    table_name = request_data.get('tableName')
    if not globalApiCommunication.userAuth.validate_jwt(jwt):
        return Response("Invalid jwt", status=401)
    database.tableManagement.update_table_status(table_name, "occupied")
    return Response("Ok", 200)