import requests 
import json

x = requests.get(
    "https://npiregistry.cms.hhs.gov/api/?version=2.0&number=1124197108")
x = json.loads(x.text)

print(x["results"][0]["addresses"][0])


# x1 = requests.get(
#     "https://www.zipcodeapi.com/rest/WNmb2CK4dd8TgTZcJc0mfOFm5bV8ysOTC3f7KY0OyxRvUXGr1ZFGbO2sGLQiFqjb/info.json/" + x["results"][0]["addresses"][0]["postal_code"]+ "/degrees")
# x1 = json.loads(x1.text)
# print(x1["lat"], x1["lng"])

x1 = requests.get("https://api.opencagedata.com/geocode/v1/json?q=" +
                  x["results"][0]["addresses"][0]["city"] + "&key=3b05bfc38d1949b8a2d4e52dd21932ad")
x1 = json.loads(x1.text)

print(x1["results"][0]["bounds"][list(x1["results"][0]["bounds"])[0]]["lat"],
      x1["results"][0]["bounds"][list(x1["results"][0]["bounds"])[0]]["lng"])

