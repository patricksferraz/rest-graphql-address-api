from psycopg2 import connect


def tables(path_in: str, struct_file: dict, con: connect):
    try:
        cur = con.cursor()

        keys = struct_file.keys()
        for key in keys:
            schema = struct_file[key]

            SQL = "CREATE TABLE {} (".format(key)
            for value in schema:
                SQL += value
            SQL += ");"

            cur.execute(SQL)
        con.commit()

    except Exception as e:
        return e
