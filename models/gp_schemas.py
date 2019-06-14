from graphene import Int, ObjectType, String


class State(ObjectType):
    id = Int(required=True)
    name = String(required=True)
    acronym = String(required=True)


class City(ObjectType):
    pass


class Place(ObjectType):
    pass
