from models.gp_schemas import State


def _format_n0(tuple: list):
    result = State(id=tuple[0], name=tuple[1], acronym=tuple[2])
    return result


def state_format(states: list) -> list:
    """Return all states formated as a dictionary

    Arguments:
        states {list} -- List of states retuned of database

    Returns:
        list -- states formated
    """
    return list(map(_format_n0, states))
