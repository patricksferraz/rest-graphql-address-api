from psycopg2 import connect


def tables(path_in: str, struct_file: dict, con: connect):
    try:
        cur = con.cursor()

        keys = struct_file.keys()
        for key in keys:
            print("[INFO] Creating table {}".format(key))
            schema = struct_file[key]
            fields = schema.keys()

            SQL = "CREATE TABLE {} (".format(key)
            for field in fields:
                SQL += "{} {}".format(field, schema[field])
            SQL += ");"

            cur.execute(SQL)
        con.commit()

    except Exception as e:
        print("[ERROR: {}] Create table".format(e))
        return e


def tuples(struct_file: dict, tuples: list, con: connect):
    try:
        cur = con.cursor()

        key = list(struct_file.keys())[0]

        print("[INFO] Inserting tuples in {}".format(key))
        schema = struct_file[key]
        fields = schema.keys()

        for tuple in tuples:
            SQL = "INSERT INTO {} (".format(key)
            for field in fields:
                SQL += "{},".format(field)
            SQL += ") "

            SQL += "VALUES ("
            for value in tuple:
                SQL += "{},".format(value)
            SQL += ");"

            cur.execute(SQL)
        con.commit()

    except Exception as e:
        print("[ERROR: {}] Insert tuple".format(e))
        return e
