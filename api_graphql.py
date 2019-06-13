from flask import Flask, jsonify
from flask_graphql import GraphQLView
from db.postgres import connect
import models.graphql_model as gm
import graphene

# app initialization
app = Flask(__name__)
con = connect()
cur = con.cursor()
# con.close()


# Schema Objects
class Query(graphene.ObjectType):
    pass


#     name = graphene.String()
#     version = graphene.String()

#     def resolve_name(_, info):
#         return "My API"

#     def resolve_version(_, info):
#         return "v1.0"


schema = graphene.Schema(query=Query)

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
    return jsonify(api_name="rest-osm", version="1.0", author="Patrick Ferraz")
