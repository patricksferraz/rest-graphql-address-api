def _format_n0(tuple: list):
    result = {}

    result["id_estado"] = tuple[0]
    result["nome_estado"] = tuple[1]
    result["sigla_estado"] = tuple[2]

    if len(tuple) > 3:
        result["cidades"] = list(map(_format_n1, tuple[3]))

    return result


def _format_n1(tuple: list):
    result = {}

    result["id_cidade"] = int(tuple[0])
    result["id_estado"] = int(tuple[1])
    result["nome_cidade"] = tuple[2]

    if len(tuple) > 3:
        result["places"] = list(map(_format_n2, tuple[3].split(";")))

    return result


def _format_n2(tuple: list):
    result = {}
    tuple = tuple.split(",")

    result["cep"] = int(tuple[0])
    result["id_estado"] = int(tuple[1])
    result["id_cidade"] = int(tuple[2])
    result["bairro"] = tuple[3]
    result["logradouro"] = tuple[4]

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
