from flask import Flask, jsonify, request
from db.postgres import connect

# app initialization
app = Flask(__name__)
con = connect()
cur = con.cursor()
# con.close()

# Routes
@app.route("/", methods=["GET"])
def index():
    return jsonify(api_name="rest-osm", version="1.0", author="Patrick Ferraz")


@app.route("/state", methods=["GET"])
@app.route("/state/<int:id>")
def state(id=None):
    if id:
        sql = f"""
            SELECT *
            FROM estado WHERE id = {id};
            """
    else:
        limit = int(request.args.get("limit", 10))
        page = int(request.args.get("page", 0)) * limit

        sql = f"""
            SELECT *
            FROM estado LIMIT {limit} OFFSET {page};
            """

    cur.execute(sql)

    result = []
    for r in cur.fetchall():
        result.append({"id": r[0], "nome": r[1], "sigla": r[2]})

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
