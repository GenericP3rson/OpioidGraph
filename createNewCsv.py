import pandas as pd 
import requests 
import json

npi_id = pd.read_csv("data/prescriber-info-full.csv")["NPI"]
opioid = pd.read_csv("data/prescriber-info-full.csv")["Opioid.Prescriber"]

npi_list = []
lat = []
lon = []
op = []

for npi in range(0, 50):
    # try:
        x = requests.get(
            "https://npiregistry.cms.hhs.gov/api/?version=2.0&number=" + str(npi_id[npi]))
        x = json.loads(x.text)

        print(x["results"][0]["addresses"][0]["postal_code"])


        x1 = requests.get(
            "https://www.zipcodeapi.com/rest/CJg6T9u8GREBBXPn9hiE4KkdBdJKMto78G3biCaSBYvGNqmJuEoB7jRSQ03JHt8b/info.json/" + x["results"][0]["addresses"][0]["postal_code"] + "/degrees")
        x1 = json.loads(x1.text)
        print(x1["lat"], x1["lng"])
        npi_list.append(npi_id[npi])
        lat.append(x1["lat"])
        lon.append(x1["lng"])
        op.append(opioid[npi])
    # except: 
    #     pass


d = {'npi': npi_list, 'lat': lat, 'lon': lon, "opioids": op}
df = pd.DataFrame(data=d)
print(df)
df.to_csv("NPI_Location.csv")
