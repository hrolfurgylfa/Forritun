'''
Verkefni 3 Tónlystamenn
Hrólfur Gylfason
41/1/2018
'''
#Hérna bæti ég við 10 tónlystamönnum

import json

gogn = {}  
gogn["tónlystamenn"] = []

gogn["tónlystamenn"].append({  
    "nafn": "Jhon Driller",
    "tegund tónlystar": "Rokk",
    "frægt lag": "My phone",
    "þjóðerni": "Spánn",
})
gogn["tónlystamenn"].append({  
    "nafn": "Lilly",
    "tegund tónlystar": "Þungarokk",
    "frægt lag": "The Death",
    "þjóðerni": "USA",
})
gogn["tónlystamenn"].append({  
    "nafn": "Angus",
    "tegund tónlystar": "Jass",
    "frægt lag": "The move",
    "þjóðerni": "Breskur",
})
gogn["tónlystamenn"].append({  
    "nafn": "Callum",
    "tegund tónlystar": "Popp",
    "frægt lag": "just dance",
    "þjóðerni": "Breskur",
})
gogn["tónlystamenn"].append({  
    "nafn": "Lan",
    "tegund tónlystar": "Róleg tónlyst",
    "frægt lag": "Sin-Jan",
    "þjóðerni": "Kína",
})
gogn["tónlystamenn"].append({  
    "nafn": "Ju-long",
    "tegund tónlystar": "Bluse",
    "frægt lag": "To fish",
    "þjóðerni": "Kína",
})
gogn["tónlystamenn"].append({  
    "nafn": "Jacob",
    "tegund tónlystar": "Blues",
    "frægt lag": "My fish",
    "þjóðerni": "USA",
})
gogn["tónlystamenn"].append({  
    "nafn": "Mia",
    "tegund tónlystar": "Jass",
    "frægt lag": "A sir",
    "þjóðerni": "USA",
})
gogn["tónlystamenn"].append({  
    "nafn": "William",
    "tegund tónlystar": "Hip hop",
    "frægt lag": "The lama",
    "þjóðerni": "USA",
})
gogn["tónlystamenn"].append({  
    "nafn": "Olivia",
    "tegund tónlystar": "blues",
    "frægt lag": "The duck",
    "þjóðerni": "USA",
})

with open("gogn.txt","w") as outfile:  
    json.dump(gogn, outfile)


#Hérna les ég skjalið sem ég bjó til 

print()

with open("gogn.txt") as json_file:
    data = json.load(json_file)
    for x in gogn["tónlystamenn"]:
        print("Nafn: " + x["nafn"])
        print("Tegund tónlystar: " + x["tegund tónlystar"])
        print("frægt lag: " + x["frægt lag"])
        print("Þjóðerni: " + x["þjóðerni"])
        print("")