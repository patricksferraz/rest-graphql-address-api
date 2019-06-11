from psycopg2.psycopg1 import cursor


def get_state(name: str, limit: int, page: int, cur: cursor):
    if name:
        sql = f"""
            SELECT *
            FROM estado WHERE nome ILIKE '%{name}%'
            LIMIT {limit} OFFSET {page * limit};
            """
    else:
        sql = f"""
            SELECT *
            FROM estado LIMIT {limit} OFFSET {page * limit};
            """

    cur.execute(sql)
    return cur.fetchall()
