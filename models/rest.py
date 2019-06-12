from psycopg2.psycopg1 import cursor


def get_state(state: str, limit: int, page: int, cur: cursor):
    if state:
        sql = f"""
            SELECT id, nome, sigla
            FROM estado WHERE nome ILIKE '%{state}%'
            LIMIT {limit} OFFSET {page * limit};
            """
    else:
        sql = f"""
            SELECT id, nome, sigla
            FROM estado LIMIT {limit} OFFSET {page * limit};
            """

    cur.execute(sql)
    return cur.fetchall()


def get_city(data: dict, limit: int, page: int, cur: cursor):
    if data["city"]:
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
    else:
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
                ORDER BY c.nome ASC
                LIMIT {limit} OFFSET {page * limit}) as ci
                ON es.id = ci.id_estado
            WHERE es.nome ILIKE '%{data["state"]}%'
            GROUP BY es.id, es.nome, es.sigla;
            """

    cur.execute(sql)
    return cur.fetchall()
