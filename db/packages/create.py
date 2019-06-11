def tables(path_in: str, struct_file: dict, path_out: str):
    try:
        out = open(path_out, "w")

        keys = struct_file.keys()
        for key in keys:
            print("[INFO] Creating table {}".format(key))
            schema = struct_file[key]
            fields = schema.keys()

            SQL = "CREATE TABLE {} (".format(key)
            for field in fields:
                SQL += "{} {}".format(field, schema[field])
            SQL += ");\n"

            out.write(SQL)
        out.close()

    except Exception as e:
        print("[ERROR] {}".format(e))
        return e


def tuples(struct_file: dict, tuples: list, path_out: str):
    try:
        out = open(path_out, "w")
        key = list(struct_file.keys())[0]

        print("[INFO] Creating tuples for {}".format(key))
        schema = struct_file[key]
        fields = schema.keys()
        len_fields = len(fields)

        for tuple in tuples:
            SQL = "INSERT INTO {} (".format(key)
            for idx, field in enumerate(fields):
                SQL += (
                    "{},".format(field)
                    if idx < len_fields - 1
                    else "{}".format(field)
                )
            SQL += ") "

            len_tuple = len(tuple)
            SQL += "VALUES ("
            for idx, value in enumerate(tuple):
                SQL += (
                    "'{}',".format(value)
                    if idx < len_tuple - 1
                    else "'{}'".format(value)
                )
            SQL += ");\n"

            out.write(SQL)
        out.close()

    except Exception as e:
        print("[ERROR] {}".format(e))
        return e
