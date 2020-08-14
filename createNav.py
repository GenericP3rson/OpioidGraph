import os 
from os import listdir
from os.path import isfile, join


onlyfiles = [f for f in listdir("html_maps") if isfile(join("html_maps", f))]

print(onlyfiles)

with open("nav.html", "w") as f:
    f.write("<!DOCTYPE html>\n<html>\n<body>")
    for i in onlyfiles:
        f.write("<a href=\"html_maps/"+i+"\">" + i[:-5] + "</a><br>")
    f.write("</body></html>")
