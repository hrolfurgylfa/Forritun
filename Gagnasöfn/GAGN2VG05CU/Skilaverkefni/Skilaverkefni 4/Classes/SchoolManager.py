from .MySQLConnector import MySQLConnector
import json

class SchoolManager():
    def __init__(self, password_filename):

        try:
            with open(password_filename, "r") as json_file:
                passwordFile = json.load(json_file)
        except FileNotFoundError: passwordFile = None

        # Sækja aðgangsorðið
        if passwordFile is None:
            print("Það vantar password file sem geymir DataBase passwordið")
            exit()
        else: password = passwordFile["password"]

        # Tengja við gagnagrunninn
        self.SQL = MySQLConnector("127.0.0.1", "root", password, "progresstracker")


    def new_student(self, skirnarnafn, eftirnafn, faedingar_dagur, byrjunar_onn):
        return self.SQL.run_stored_procedure("CreateStudent", skirnarnafn, eftirnafn, faedingar_dagur, byrjunar_onn)
    def get_student(self, id):
        return self.SQL.run_stored_procedure("GetStudent", id)
    def update_student(self, id, skirnarnafn):
        return self.SQL.run_stored_procedure("ChangeStudent", id, skirnarnafn)
    def remove_student(self, id):
        return self.SQL.run_stored_procedure("RemoveStudent", id)