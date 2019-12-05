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
        output = self.SQL.run_stored_procedure("CreateStudent", skirnarnafn, eftirnafn, faedingar_dagur, byrjunar_onn)
        try:
            return output[0]["ID"]
        except (KeyError, IndexError):
            print("Output from last command:", output)
            return None
    def get_student(self, id):
        return self.SQL.run_stored_procedure("GetStudent", id)
    def update_student(self, id, skirnarnafn):
        return self.SQL.run_stored_procedure("ChangeStudent", id, skirnarnafn)
    def remove_student(self, id):
        return self.SQL.run_stored_procedure("RemoveStudent", id)


    def new_course(self, brautarnumer, brautar_nafn, einingar):
        return self.SQL.run_stored_procedure("CreateCourse", brautarnumer, brautar_nafn, einingar)
    def get_course(self, id):
        return self.SQL.run_stored_procedure("GetCourse", id)
    def update_course(self, id, brautar_nafn):
        return self.SQL.run_stored_procedure("ChangeCourse", id, brautar_nafn)
    def remove_course(self, id):
        return self.SQL.run_stored_procedure("RemoveCourse", id)


    def new_school(self, skola_nafn):
        output = self.SQL.run_stored_procedure("CreateSchool", skola_nafn)
        try:
            return output[0]["ID"]
        except (KeyError, IndexError):
            print("Output from last command:", output)
            return None
    def get_school(self, id):
        return self.SQL.run_stored_procedure("GetSchool", id)
    def update_school(self, id, brautar_nafn):
        return self.SQL.run_stored_procedure("ChangeSchool", id, brautar_nafn)
    def remove_school(self, id):
        return self.SQL.run_stored_procedure("RemoveSchool", id)