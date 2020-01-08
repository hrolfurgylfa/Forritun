######################
#       Import       #
######################
from Classes.MySQLConnector import MySQLConnector
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
# Sækja aðgangsorðið
passwordFile = getJsonFile("GAGN2VG05CU\\Skilaverkefni\\Skilaverkefni 4\\SQLPassword.json")
if passwordFile is None:
    print("Það vantar password file sem geymir DataBase passwordið")
    exit()
else: password = passwordFile["password"]

# Tengja við gagnagrunninn
SQL = MySQLConnector("127.0.0.1", "root", password, "progresstracker")

# Keyra commands
print(SQL.run_stored_procedure("Test"))