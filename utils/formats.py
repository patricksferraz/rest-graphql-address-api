def _format_n0(tuple: list):
    result = {}

    result["id"] = tuple[0]
    result["name"] = tuple[1]
    result["acronym"] = tuple[2]

    if len(tuple) > 3:
        result["cities"] = list(map(_format_n1, tuple[3]))

    return result


def _format_n1(tuple: list):
    result = {}

    result["id"] = int(tuple[0])
    result["id_state"] = int(tuple[1])
    result["nome"] = tuple[2]

    if len(tuple) > 3:
        result["places"] = list(map(_format_n2, tuple[3].split(";")))

    return result


def _format_n2(tuple: list):
    result = {}
    tuple = tuple.split(",")

    result["cep"] = int(tuple[0])
    result["id_state"] = int(tuple[1])
    result["id_city"] = int(tuple[2])
    result["district"] = tuple[3]
    result["public_place"] = tuple[4]

    return result


def state_format(states: list) -> list:
    """Return all states formated as a dictionary

    Arguments:
        states {list} -- List of states retuned of database

    Returns:
        list -- states formated
    """
    return list(map(_format_n0, states))


def city_format(cities: list) -> list:
    """Return all cities formated as a dictionary

    Arguments:
        cities {list} -- List of cities retuned of database

    Returns:
        list -- cities formated
    """
    return list(map(_format_n0, cities))


def place_format(places: list) -> list:
    """Return all places formated as a dictionary

    Arguments:
        places {list} -- List of places retuned of database

    Returns:
        list -- places formated
    """
    return list(map(_format_n0, places))
