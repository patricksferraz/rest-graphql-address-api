import matplotlib.pyplot as plt
import pandas as pd
import argparse

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument(
    "-r",
    "--input-file-rest",
    required=True,
    help="path to input files with json structure of results",
)
ap.add_argument(
    "-g",
    "--input-file-graphql",
    required=True,
    help="path to input files with json structure of results",
)
args = vars(ap.parse_args())

# REST
file = pd.read_json(args["input_file_rest"])
out = {
    "local": file["time"][0],
    "border": file["time"][1],
    "global": file["time"][2],
}
out = pd.DataFrame(out, columns=["local", "border", "global"])
out = out.reset_index()

plot = out.plot(kind="box", x="index", y="local")
plt.legend(["local"])
plt.ylabel("Latência (ms)")
plt.savefig("out/rest/local_rest.png")

out.plot(kind="box", x="index", y="border")
plt.legend(["border"])
plt.ylabel("Latência (ms)")
plt.savefig("out/rest/border_rest.png")

out.plot(kind="box", x="index", y="global")
plt.legend(["global"])
plt.ylabel("Latência (ms)")
plt.savefig("out/rest/global_rest.png")
# plt.show()


# GRAPHQL
file = pd.read_json(args["input_file_graphql"])
out = {
    "local-min": file["time"][0],
    "local-med": file["time"][1],
    "local-max": file["time"][2],
    "border-min": file["time"][3],
    "border-med": file["time"][4],
    "border-max": file["time"][5],
    "global-min": file["time"][6],
    "global-med": file["time"][7],
    "global-max": file["time"][8],
}
out = pd.DataFrame(
    out,
    columns=[
        "local-min",
        "local-med",
        "local-max",
        "border-min",
        "border-med",
        "border-max",
        "global-min",
        "global-med",
        "global-max",
    ],
)
out = out.reset_index()

# Local scope
plot = out.plot(kind="box", x="index", y="local-min")
plt.legend(["local-min"])
plt.ylabel("Latência (ms)")
plt.savefig("out/graphql/local_graphql-min.png")
plot = out.plot(kind="box", x="index", y="local-med")
plt.legend(["local-med"])
plt.ylabel("Latência (ms)")
plt.savefig("out/graphql/local_graphql-med.png")
plot = out.plot(kind="box", x="index", y="local-max")
plt.legend(["local-max"])
plt.ylabel("Latência (ms)")
plt.savefig("out/graphql/local_graphql-max.png")

# Border scope
out.plot(kind="box", x="index", y="border-min")
plt.legend(["border-min"])
plt.ylabel("Latência (ms)")
plt.savefig("out/graphql/border_graphql-min.png")
out.plot(kind="box", x="index", y="border-med")
plt.legend(["border-med"])
plt.ylabel("Latência (ms)")
plt.savefig("out/graphql/border_graphql-med.png")
out.plot(kind="box", x="index", y="border-max")
plt.legend(["border-max"])
plt.ylabel("Latência (ms)")
plt.savefig("out/graphql/border_graphql-max.png")

# Global scope
out.plot(kind="box", x="index", y="global-min")
plt.legend(["global-min"])
plt.ylabel("Latência (ms)")
plt.savefig("out/graphql/global_graphql-min.png")
out.plot(kind="box", x="index", y="global-med")
plt.legend(["global-med"])
plt.ylabel("Latência (ms)")
plt.savefig("out/graphql/global_graphql-med.png")
out.plot(kind="box", x="index", y="global-max")
plt.legend(["global-max"])
plt.ylabel("Latência (ms)")
plt.savefig("out/graphql/global_graphql-max.png")
# plt.show()
