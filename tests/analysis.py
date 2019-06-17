import matplotlib.pyplot as plt
import pandas as pd
import argparse

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument(
    "-i",
    "--input-file",
    required=True,
    help="path to input files with json structure of results",
)
args = vars(ap.parse_args())

file = pd.read_json(args["input_file"])
out = {
    "local": file["time"][0],
    "border": file["time"][1],
    "global": file["time"][2],
}
out = pd.DataFrame(out, columns=["local", "border", "global"])
out = out.reset_index()
plt.ylabel("Latência (ms)")

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
