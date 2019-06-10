from psycopg2 import connect


def tables(path_in: str, struct_file: dict, con: connect):
    try:
        cur = con.cursor()

        keys = struct_file.keys()
        for key in keys:
            print("[INFO] Creating table {}".format(key))
            schema = struct_file[key]
            values = schema.keys()

            SQL = "CREATE TABLE {} (".format(key)
            for value in values:
                SQL += "{} {}".format(value, schema[value])
            SQL += ");"

            cur.execute(SQL)
        con.commit()

    except Exception as e:
        return e
