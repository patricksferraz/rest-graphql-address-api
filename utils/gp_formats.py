from models.gp_schemas import State, City


def _format_n0(tuple: list):
    state = State(id=tuple[0], name=tuple[1], acronym=tuple[2])

    if len(tuple) > 3:
        state.cities = list(map(_format_n1, tuple[3]))

    return state


def _format_n1(tuple: list):
    city = City(id=tuple[0], id_state=tuple[1], name=tuple[2])

    return city


def city_format(cities: list) -> list:
    """Return all states and cities formated as a dictionary

    Arguments:
        cities {list} -- List of cities retuned of database

    Returns:
        list -- cities formated
    """
    return list(map(_format_n0, cities))
