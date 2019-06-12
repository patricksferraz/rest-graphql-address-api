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

    return result


def state_format(states: list):
    return list(map(_format_n0, states))


def city_format(cities: list):
    return list(map(_format_n0, cities))
