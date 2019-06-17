import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import argparse
import json


def _removeOutlier(array):
    fator = 1.5
    q1, q3 = np.percentile(array, [25, 75])
    iqr = q3 - q1
    lower_bound = q1 - (iqr * fator)
    upper_bound = q3 + (iqr * fator)

    return [v for v in array if upper_bound > v > lower_bound]


def _clean(array, name):
    # Ordenando
    array = array.sort_values()

    # Média e desvio padrão
    mean = np.mean(array, axis=0)
    sd = np.std(array, axis=0)
    mean_current = np.mean(_removeOutlier(array))

    print(
        "[INFO] {}: mean={} sd={} mean_current={}".format(
            name, mean, sd, mean_current
        )
    )
    return {
        "scope": name,
        "blockSize": "min | med | max",
        "mean": mean,
        "sd": sd,
        "mean current": mean_current,
    }


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

f_out_ms = open("out/mean_std.json", "w")
v_out_ms = []

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
v_out_ms.append(_clean(out["local"], "rest-local"))

out.plot(kind="box", x="index", y="border")
plt.legend(["border"])
plt.ylabel("Latência (ms)")
plt.savefig("out/rest/border_rest.png")
v_out_ms.append(_clean(out["border"], "rest-border"))

out.plot(kind="box", x="index", y="global")
plt.legend(["global"])
plt.ylabel("Latência (ms)")
plt.savefig("out/rest/global_rest.png")
v_out_ms.append(_clean(out["global"], "rest-global"))
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
v_out_ms.append(_clean(out["local-min"], "graphql-local-min"))

plot = out.plot(kind="box", x="index", y="local-med")
plt.legend(["local-med"])
plt.ylabel("Latência (ms)")
plt.savefig("out/graphql/local_graphql-med.png")
v_out_ms.append(_clean(out["local-med"], "graphql-local-med"))

plot = out.plot(kind="box", x="index", y="local-max")
plt.legend(["local-max"])
plt.ylabel("Latência (ms)")
plt.savefig("out/graphql/local_graphql-max.png")
v_out_ms.append(_clean(out["local-max"], "graphql-local-max"))


# Border scope
out.plot(kind="box", x="index", y="border-min")
plt.legend(["border-min"])
plt.ylabel("Latência (ms)")
plt.savefig("out/graphql/border_graphql-min.png")
v_out_ms.append(_clean(out["border-min"], "graphql-border-min"))

out.plot(kind="box", x="index", y="border-med")
plt.legend(["border-med"])
plt.ylabel("Latência (ms)")
plt.savefig("out/graphql/border_graphql-med.png")
v_out_ms.append(_clean(out["border-med"], "graphql-border-med"))

out.plot(kind="box", x="index", y="border-max")
plt.legend(["border-max"])
plt.ylabel("Latência (ms)")
plt.savefig("out/graphql/border_graphql-max.png")
v_out_ms.append(_clean(out["border-max"], "graphql-border-max"))

# Global scope
out.plot(kind="box", x="index", y="global-min")
plt.legend(["global-min"])
plt.ylabel("Latência (ms)")
plt.savefig("out/graphql/global_graphql-min.png")
v_out_ms.append(_clean(out["global-min"], "graphql-global-min"))

out.plot(kind="box", x="index", y="global-med")
plt.legend(["global-med"])
plt.ylabel("Latência (ms)")
plt.savefig("out/graphql/global_graphql-med.png")
v_out_ms.append(_clean(out["global-med"], "graphql-global-med"))

out.plot(kind="box", x="index", y="global-max")
plt.legend(["global-max"])
plt.ylabel("Latência (ms)")
plt.savefig("out/graphql/global_graphql-max.png")
v_out_ms.append(_clean(out["global-max"], "graphql-global-max"))
# plt.show()

f_out_ms.write(json.dumps(v_out_ms))
f_out_ms.close()
