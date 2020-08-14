import folium
import pandas as pd 
import json
import requests

# npi_id = pd.read_csv("data/prescriber-info-full.csv")["NPI"]
npi_id = pd.read_csv("data/prescriber-info-full.csv")["NPI"]
df = pd.read_csv("data/prescriber-info-full.csv")

col = pd.read_csv("data/prescriber-info-full.csv").columns[5:]

for item in col:
    data = df[item]

    map = folium.Map(location=[40.693943, -73.985880], default_zoom_start=-5)


    for point in range(0, 50):
        try: 
            if (data[point] != 0):
                x = requests.get(
                    "https://npiregistry.cms.hhs.gov/api/?version=2.0&number=" + str(npi_id[point]))
                x = json.loads(x.text)

                print(x["results"][0]["addresses"][0]["postal_code"])

                x1 = requests.get("https://api.opencagedata.com/geocode/v1/json?q=" +
                                x["results"][0]["addresses"][0]["city"] + "&key=3b05bfc38d1949b8a2d4e52dd21932ad")
                x1 = json.loads(x1.text)

                print(x1["results"][0]["bounds"][list(x1["results"][0]["bounds"])[0]]["lat"],
                    x1["results"][0]["bounds"][list(x1["results"][0]["bounds"])[0]]["lng"])
                x1 = x1["results"][0]["bounds"][list(x1["results"][0]["bounds"])[0]]
                # npi_list.append(npi_id[npi])        
                # print(x1)
                # print(x1["lat"], x1["lng"])

                folium.Marker([x1["lat"], x1["lng"]], popup=x["results"]
                            [0]["basic"]["first_name"] + " " + x["results"][0]["basic"]["last_name"] + ": " + str(data[point])).add_to(map)
        except:
            pass

    map.save('html_maps/'+ "_".join(item.split()) + '.html')
