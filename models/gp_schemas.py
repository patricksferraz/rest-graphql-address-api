from graphene import Int, ObjectType, String, List


class Place(ObjectType):
    cep = Int(required=True)
    id_state = Int(required=True)
    id_city = Int(required=True)
    district = String(required=True)
    public_place = String(required=True)


class City(ObjectType):
    id = Int(required=True)
    id_state = Int(required=True)
    name = String(required=True)
    places = List(Place)


class State(ObjectType):
    id = Int(required=True)
    name = String(required=True)
    acronym = String(required=True)
    cities = List(City)
