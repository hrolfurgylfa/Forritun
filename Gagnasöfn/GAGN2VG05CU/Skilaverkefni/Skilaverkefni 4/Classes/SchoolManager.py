from .MySQLConnector import MySQLConnector
import json

class SchoolManager():
    def __init__(self):

        filename = "GAGN2VG05CU\\Skilaverkefni\\Skilaverkefni 4\\SQLPassword.json"

        try:
            with open(filename, "r") as json_file:
                passwordFile = json.load(json_file)
        except FileNotFoundError: passwordFile = None

        # Sækja aðgangsorðið
        if passwordFile is None:
            print("Það vantar password file sem geymir DataBase passwordið")
            exit()
        else: password = passwordFile["password"]

        # Tengja við gagnagrunninn
        self.SQL = MySQLConnector("127.0.0.1", "root", password, "progresstracker")

    def new_student(self, sql):
        pass
