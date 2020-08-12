import folium
import pandas as pd 
import json
import requests

npi_id = pd.read_csv("data/prescriber-info-full.csv")["NPI"]


map = folium.Map(location=[40.693943, -73.985880], default_zoom_start=-5)


for point in range(0, 50):
    try: 
        x = requests.get(
            "https://npiregistry.cms.hhs.gov/api/?version=2.0&number=" + str(npi_id[point]))
        x = json.loads(x.text)

        # print(x["results"][0]["addresses"][0]["postal_code"])


        x1 = requests.get(
            "https://www.zipcodeapi.com/rest/CJg6T9u8GREBBXPn9hiE4KkdBdJKMto78G3biCaSBYvGNqmJuEoB7jRSQ03JHt8b/info.json/" + x["results"][0]["addresses"][0]["postal_code"] + "/degrees")
        x1 = json.loads(x1.text)
        # print(x1)
        # print(x1["lat"], x1["lng"])

        folium.Marker([x1["lat"], x1["lng"]], popup=x["results"]
                    [0]["basic"]["first_name"] + " " + x["results"][0]["basic"]["last_name"] + ": " + str(npi_id[point])).add_to(map)
    except:
        pass

map.save('index.html')
