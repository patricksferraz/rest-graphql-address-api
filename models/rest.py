from psycopg2.psycopg1 import cursor


def get_state(state: str, limit: int, page: int, cur: cursor) -> list:
    """Return all states of postgres database

    Arguments:
        state {str} -- State name for search
        limit {int} -- Results limit
        page {int} -- Results page
        cur {cursor} -- Cursor postgres for database

    Returns:
        list -- all states from database
    """
    sql = f"""
        SELECT id, nome, sigla
        FROM estado WHERE nome ILIKE '%{state}%'
        ORDER BY nome
        LIMIT {limit} OFFSET {page * limit};
        """

    cur.execute(sql)
    return cur.fetchall()


def get_city(data: dict, limit: int, page: int, cur: cursor) -> list:
    """Return all cities of postgres database

    Arguments:
        data {dict} -- Dictionary with {"state": state, "city": city}
            key-value pair
        limit {int} -- Results limit by state
        page {int} -- Results page
        cur {cursor} -- Cursor postgres for database

    Returns:
        list -- all cities from database
    """
    sql = f"""
        SELECT es.id,
            es.nome,
            es.sigla,
            array_agg(array[
                cast(ci.id as TEXT),
                cast(ci.id_estado as TEXT),
                ci.nome])
        FROM estado es INNER JOIN (
            SELECT c.id, c.id_estado, c.nome
            FROM cidade c INNER JOIN estado e
                ON c.id_estado = e.id
            WHERE e.nome ILIKE '%{data["state"]}%'
                AND c.nome ILIKE '%{data["city"]}%'
            ORDER BY c.nome ASC
            LIMIT {limit} OFFSET {page * limit}) as ci
            ON es.id = ci.id_estado
        WHERE es.nome ILIKE '%{data["state"]}%'
        GROUP BY es.id, es.nome, es.sigla;
        """

    cur.execute(sql)
    return cur.fetchall()
