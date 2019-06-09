from flask import Flask, jsonify
import psycopg2
import os

POSTGRES_URL = os.environ["POSTGRES_URL"]
POSTGRES_USER = os.environ["POSTGRES_USER"]
POSTGRES_PW = os.environ["POSTGRES_PW"]
POSTGRES_DB = os.environ["POSTGRES_DB"]


def connect():
    return psycopg2.connect(
        host=POSTGRES_URL,
        database=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PW,
    )


app = Flask(__name__)
con = connect()
cur = con.cursor()
# con.close()


@app.route("/")
def index():
    return jsonify(api_name="rest-osm", version="1.0", author="Patrick Ferraz")


@app.route("/state")
def state():
    cur.execute(
        # """
        # SELECT *
        # FROM planet_osm_line line WHERE name LIKE '%Bairro%' LIMIT 10;
        # """
    )
    result = cur.fetchall()
    return jsonify(result)


@app.route("/state/<id>/city")
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
