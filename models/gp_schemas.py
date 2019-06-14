from graphene import Int, ObjectType, String, List


class City(ObjectType):
    id = Int(required=True)
    id_state = Int(required=True)
    name = String(required=True)


class State(ObjectType):
    id = Int(required=True)
    name = String(required=True)
    acronym = String(required=True)
    cities = List(City)


class Place(ObjectType):
    pass
