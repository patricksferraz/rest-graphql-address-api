from flask import Flask, jsonify, request
from db.postgres import connect
from models.db_models import get_state, get_city, get_place
from utils.formats import state_format, city_format, place_format

# app initialization
app = Flask(__name__)
con = connect()
cur = con.cursor()
# con.close()

# Routes
@app.route("/")
def index():
    return jsonify(
        api_name="rest-address", version="1.0", author="Patrick Ferraz"
    )


@app.route("/state")
@app.route("/state/<state>")
def state(state="%"):
    result = get_state(
        state,
        int(request.args.get("limit", 10)),
        int(request.args.get("page", 0)),
        cur,
    )
    return jsonify(state_format(result))


@app.route("/state/<state>/city")
@app.route("/state/<state>/city/<city>")
def city(state, city="%"):
    result = get_city(
        {"state": state, "city": city},
        int(request.args.get("limit", 10)),
        int(request.args.get("page", 0)),
        cur,
    )
    return jsonify(city_format(result))


@app.route("/state/<state>/city/<city>/place")
@app.route("/state/<state>/city/<city>/place/<place>")
def neighborhood(state, city, place="%"):
    result = get_place(
        {"state": state, "city": city, "place": place},
        int(request.args.get("limit", 10)),
        int(request.args.get("page", 0)),
        cur,
    )
    return jsonify(place_format(result))
