from packages.extract import extract
from packages.create import tables
from postgres import connect
import argparse
import json

# import re

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument(
    "-p",
    "--path-tables",
    required=True,
    help="path to input tables of database",
)
ap.add_argument(
    "-s",
    "--file-structure",
    required=True,
    help="path to input file with database structure",
)
args = vars(ap.parse_args())

# generates the path for output
path_out = args["path_tables"].split("/")[:-1]
path_out = "/".join(path_out)
path_out = "{}/preprocessing".format(path_out)

# Extract zip files
extract(args["path_tables"], path_out)

#
con = connect()
structure = json.loads(open(args["file_structure"], "r").read())
tables(path_out, structure, con)

# if re.search(exclude, d) is None:
# f_in = "{mdir}/{dirs}/{dirs}.py".format(mdir=file, dirs=d)
# f_out = "{}/{}/.out".format(file, d)
# param = "<{}/{}/in".format(file, d)
# cmd = "python3 {} {}".format(f_in, param)

# buffer = open(f_out, "w")
# subprocess.call([cmd], stdout=buffer, shell=True)
# buffer.close()

# buffer_result = open(f_out, "r")
# result = buffer_result.read()

# f_expected = "{}/{}/expected".format(file, d)
# buffer_expected = open(f_expected, "r")
# expected = buffer_expected.read()
