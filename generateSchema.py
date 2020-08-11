import pandas as pd

df = pd.read_csv("data/prescriber-info.csv")

opioids = (list(df.columns))

with open('db_scripts/schema/bigSchema.gsql', 'w') as f:
    for i in opioids:
        f.write("CREATE VERTEX " + "_".join(i.split(".")) + "(PRIMARY_ID id STRING) with primary_id_as_attribute=\"true\"\n")
    
    f.write("\n\n\n")

    for i in opioids:
        f.write("CREATE UNDIRECTED EDGE NPI_" +
                "_".join(i.split(".")) + "(FROM NPI, To " + "_".join(i.split(".")) + ")\n") 
    
    f.write("\n\n\nCREATE GRAPH @graphname@(" + ", ".join(["_".join(j.split(
        ".")) for j in opioids]) + ", " + ", ".join(["NPI_" + "_".join(j.split(".")) for j in opioids]) + ")")
with open("db_scripts/load/loadBigData.gsql", "w") as f:
    f.write("drop job loadBigData\ncreate loading job loadBigData for graph @graphname@ {\ndefine filename f1;\nload f1\n")
    f.write(',\n'.join(["to vertex " + "_".join(val.split(".")) +
                        " values($" + str(num) + ")" for num, val in enumerate(opioids)]))
    f.write(",\n\n")
    f.write(',\n'.join(["to edge NPI_" + "_".join(val.split(".")) + " values($0, $" +
                        str(num) + ")" for num, val in enumerate(opioids)]))

    f.write("\nusing header=\"false\", separator=\", \";\n}")
