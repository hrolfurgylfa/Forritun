'''
Tímaverkefni 1 Hljómsveit
Hrólfur Gylfason
7/2/2018
'''

import json

print()

with open("Hljómsveitir.json") as json_file:
    data = json.load(json_file)
    for x in data["tónlystamenn"]:
        print("Gítar: " + x["Gítar"])
        print("Bassi: " + x["Bassi"])
        print("Trommur: " + x["Trommur"])
        print("Söngur: " + x["Söngur"])
        print("")