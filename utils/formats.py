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
    result["idState"] = int(tuple[1])
    result["nome"] = tuple[2]

    if len(tuple) > 3:
        result["places"] = list(map(_format_n2, tuple[3].split(";")))

    return result


def _format_n2(tuple: list):
    result = {}
    tuple = tuple.split(",")

    result["cep"] = int(tuple[0])
    result["idState"] = int(tuple[1])
    result["idCity"] = int(tuple[2])
    result["district"] = tuple[3]
    result["publicPlace"] = tuple[4]

    return result


def _format(addresses: list) -> list:
    """Return all addresses formated as a dictionary

    Arguments:
        addresses {list} -- List of addresses retuned of database

    Returns:
        list -- addresses formated
    """
    return list(map(_format_n0, addresses))
