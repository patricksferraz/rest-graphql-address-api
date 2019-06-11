from packages.extract import extract
from packages.create import tables, tuples
from postgres import connect
import subprocess
import argparse
import pandas
import json
import os


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument(
    "-z",
    "--zip-tables",
    required=True,
    help="path to input tables of database zip",
)
ap.add_argument(
    "-s",
    "--file-structure",
    required=True,
    help="path to input file with database structure",
)
ap.add_argument(
    "-t",
    "--path-tables",
    required=True,
    help="path to input folder with database tables in csv",
)
args = vars(ap.parse_args())

# generates the path for output
path_out = args["zip_tables"].split("/")[:-1]
path_out = "/".join(path_out)
path_out = "{}/preprocessing".format(path_out)


con = connect()


# EXTRAXT ZIP FILES
extract(args["zip_tables"], path_out)

# CREATE TABLES
structure = json.loads(open(args["file_structure"], "r").read())
tables(path_out, structure, con)


# Get path where is the tables folder
tables_folder = args["path_tables"]
# Get all
tables_files = subprocess.os.listdir(tables_folder)
tables_files = list(filter(lambda x: x.split(".")[-1] == "csv", tables_files))
# Get all path of tables
path_tables_files = list(
    map(lambda x: "{}/{}".format(tables_folder, x), tables_files)
)


# ADDS TUPLES
# Adds tuples of states
path_tables_files.remove("db/preprocessing/states.csv")
states = pandas.read_csv(
    "db/preprocessing/states.csv", delimiter=",", header=None
)
tuples({"estado": structure["estado"]}, states.values, con)

# Adds tuples of cities
path_tables_files.remove("db/preprocessing/cities.csv")
cities = pandas.read_csv(
    "db/preprocessing/cities.csv", delimiter=",", header=None
)
tuples({"cidade": structure["cidade"]}, cities.values, con)

# Adds tuples of places
for ptf in path_tables_files:
    places = pandas.read_csv(ptf, delimiter=",", header=None)
    out = ptf.split("/")[-1]
    tuples({"cep": structure["cep"]}, places.values, con)

con.close()
