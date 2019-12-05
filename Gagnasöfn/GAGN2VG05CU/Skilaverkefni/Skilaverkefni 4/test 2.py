######################
#       Import       #
######################
from Classes.SchoolManager import SchoolManager
import json


######################
#        Föll        #
######################
def getJsonFile(file_name):
    if file_name[-5::] != ".json": file_name += ".json"

    try: 
        with open(file_name+"", "r") as json_file: 
            data = json.load(json_file)
    except FileNotFoundError:
        data = None
    
    return data


######################
#        Kóði        #
######################
School = SchoolManager("GAGN2VG05CU\\Skilaverkefni\\Skilaverkefni 4\\SQLPassword.json")