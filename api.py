import flask
import database.database
import info.full
import setup.CreateRestaurant

app = flask.Flask(__name__)
app.register_blueprint(setup.CreateRestaurant.create_restaurant)
app.register_blueprint(info.full.full_restaurant_info)

@app.route("/test", methods=["GET"])
def register_table():
    return "valid"


if __name__ == '__main__':
    database.database.default_db_setup()
    app.run(host='0.0.0.0', port=4000, debug=True)
