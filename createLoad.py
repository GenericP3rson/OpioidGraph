import pandas as pd

df = pd.read_csv("data/prescriber-info-full.csv")

opioids = (list(df.columns))

with open("test.txt", "w") as f:
    f.write(
        "drop job loadNewData\ncreate loading job loadNewData for graph @graphname@ {\ndefine filename f1;\nload f1\n")
    f.write(',\n'.join(["to vertex _Medicine" +
                        " values(\"" + "_".join(val.split(".")) + "\", $" + str(num) + ")" for num, val in enumerate(opioids)]))
    f.write(",\n\n")
    f.write(',\n'.join(["to edge _NPI_MEDICINE values($0, \"" + "_".join(val.split(".")) + "\")" for num, val in enumerate(opioids)]))

    f.write("\nusing header=\"false\", separator=\", \";\n}")
