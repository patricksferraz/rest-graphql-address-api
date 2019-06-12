def state_format(states: list):
    return list(
        map(
            lambda s: {
                "id_estado": s[0],
                "nome_estado": s[1],
                "sigla_estado": s[2],
            },
            states,
        )
    )
