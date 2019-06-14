from flask import Flask, jsonify
from flask_graphql import GraphQLView
from db.postgres import connect
from models.gp_schemas import State
from utils.gp_formats import state_format
from graphene import ObjectType, Int, String, List, Schema
import models.db_models as db

# app initialization
app = Flask(__name__)
con = connect()
cur = con.cursor()
# con.close()


# Schema Objects
class Query(ObjectType):
    get_state = List(
        State,
        name=String(default_value="%"),
        city=String(default_value="%"),
        place=String(default_value="%"),
        limit=Int(default_value=10),
        page=Int(default_value=0),
    )

    def resolve_get_state(_, info, name, city, place, limit, page):
        places = db.get_place(
            {"state": name, "city": city, "place": place}, limit, page, cur
        )
        return state_format(places)


schema = Schema(query=Query)

# Routes
app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view(
        "graphql",
        schema=schema,
        graphiql=True,  # for having the GraphiQL interface
    ),
)


@app.route("/")
def index():
    return jsonify(
        api_name="graphql-address", version="1.0", author="Patrick Ferraz"
    )
