from flask import Flask, jsonify, request
from db.postgres import connect
from models.rest import get_state
from utils.rest import state_format

# app initialization
app = Flask(__name__)
con = connect()
cur = con.cursor()
# con.close()

# Routes
@app.route("/")
def index():
    return jsonify(api_name="rest-osm", version="1.0", author="Patrick Ferraz")


@app.route("/state")
@app.route("/state/<path:state>")
def state(state=None):
    result = get_state(
        state,
        int(request.args.get("limit", 10)),
        int(request.args.get("page", 0)),
        cur,
    )
    return jsonify(state_format(result))


@app.route("/state/<path:state>/city")
@app.route("/state/<path:state>/city/<path:city>")
def city(id):
    cur.execute(
        # """
        # SELECT *
        # FROM planet_osm_line line WHERE name LIKE '%Bairro%' LIMIT 10;
        # """
    )
    result = cur.fetchall()
    return jsonify(result)


@app.route("/state/<id_state>/city/<id_city>/neighborhood")
def neighborhood(id_state, id_city):
    cur.execute(
        # """
        # SELECT *
        # FROM planet_osm_line line WHERE name LIKE '%Bairro%' LIMIT 10;
        # """
    )
    result = cur.fetchall()
    return jsonify(result)


# line (logradouro), point (bairro), polygon, roads
# estado, cidade, bairro, rua
@app.route(
    "/state/<id_state>/city/<id_city>/neighborhood/<id_neighborhood>/place"
)
def place(id_state, id_city, id_neighborhood):
    cur.execute(
        # """
        # SELECT *
        # FROM planet_osm_line line WHERE name LIKE '%Bairro%' LIMIT 10;
        # """
    )
    result = cur.fetchall()
    return jsonify(result)
