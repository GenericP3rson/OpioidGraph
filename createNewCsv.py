import pandas as pd 
import requests 
import json

npi_id = pd.read_csv("data/prescriber-info-full.csv")["NPI"]

col = pd.read_csv("data/prescriber-info-full.csv").columns[5:]
# print(col)

for item in col:

    opioid = pd.read_csv("data/prescriber-info-full.csv")[item]

    npi_list = []
    lat = []
    lon = []
    op = []

    for npi in range(0, 50):
        try:
            x = requests.get(
                "https://npiregistry.cms.hhs.gov/api/?version=2.0&number=" + str(npi_id[npi]))
            x = json.loads(x.text)

            # print(x["results"][0]["addresses"][0]["postal_code"])

            x1 = requests.get("https://api.opencagedata.com/geocode/v1/json?q=" +
                              x["results"][0]["addresses"][0]["city"] + "&key=fae007d10df64d6c837bac257b6307bc")
            x1 = json.loads(x1.text)
            print(x1)

            # print(x1["results"][0]["bounds"][list(x1["results"][0]["bounds"])[0]]["lat"],
            #     x1["results"][0]["bounds"][list(x1["results"][0]["bounds"])[0]]["lng"])
            x1 = x1["results"][0]["bounds"][list(x1["results"][0]["bounds"])[0]]
            print(opioid[npi])
            if (opioid[npi] != 0):
                print("Added")
                npi_list.append(npi_id[npi])
                lat.append(x1["lat"])
                lon.append(x1["lng"])
                op.append(opioid[npi])
        except: 
            print("something's wrong")
            pass


    d = {'npi': npi_list, 'lat': lat, 'lon': lon, "opioids": op}
    df = pd.DataFrame(data=d)
    # print(df)
    df.to_csv("streamlit_csv/" + "_".join(item.split()) + ".csv")
