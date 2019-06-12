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
