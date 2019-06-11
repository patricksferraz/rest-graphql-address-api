def state_format(states: list):
    return list(
        map(lambda s: {"id": s[0], "nome": s[1], "sigla": s[2]}, states)
    )
