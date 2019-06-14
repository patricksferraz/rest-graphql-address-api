from models.gp_schemas import State, City, Place


def _format_n0(tuple: list):
    state = State(id=tuple[0], name=tuple[1], acronym=tuple[2])

    if len(tuple) > 3:
        state.cities = list(map(_format_n1, tuple[3]))

    return state


def _format_n1(tuple: list):
    city = City(id=tuple[0], id_state=tuple[1], name=tuple[2])

    if len(tuple) > 3:
        city.places = list(map(_format_n2, tuple[3].split(";")))

    return city


def _format_n2(tuple: list):
    tuple = tuple.split(",")

    place = Place(
        cep=tuple[0],
        id_state=tuple[1],
        id_city=tuple[2],
        district=tuple[3],
        public_place=tuple[4],
    )

    return place


def state_format(states: list) -> list:
    """Return all states formated as a dictionary

    Arguments:
        states {list} -- List of states retuned of database

    Returns:
        list -- states formated
    """
    return list(map(_format_n0, states))
