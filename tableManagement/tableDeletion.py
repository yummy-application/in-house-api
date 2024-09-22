import json
import flask
from flask import Response
import database.auth
import database.tableManagement

delete_table_blueprint = flask.Blueprint("delete_table", __name__)


@delete_table_blueprint.route("/api/table/delete", methods=["POST"])
def delete_table():
    request_data = json.loads(flask.request.data)
    password = request_data.get('password')
    table_name = request_data.get('tableName')
    if not database.auth.check_password(password):
        return Response("Wrong password", status=401)
    database.tableManagement.deleteTable(table_name)
    return Response("Ok", 200)
