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
SchoolDB = SchoolManager("GAGN2VG05CU\\Skilaverkefni\\Skilaverkefni 4\\SQLPassword.json")


valmynd = ""

while valmynd != "4":

    for tel in range(50):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
        print("-",end="")
    print("\n")#Þetta er til þess að gera tvö enter

    print("Ýttu á 1 til þess að prufa nemenda functionality")
    print("Ýttu á 2 til þess að prufa áfanga functionality")
    print("Ýttu á 3 til þess að prufa skóla functionality")
    print("Ýttu á 4 til þess að hætta")
    valmynd = input("-------------------->>> ")#Hérna velur notandinn hvaða lið hann ætlar að fara í

    print()#Þetta er til þess að gera enter
    for tel in range(50):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
        print("-",end="")
    print()#Þetta er til þess að gera enter

    # -------------------- Prufa nemenda föll ------------------------------
    if valmynd == "1":

        student_id = SchoolDB.new_student("Bjarni", "Ben", "2018-3-5", 9)
        print("Búið til nemenda með",student_id,"sem nemenda ID\n")

        SchoolDB.update_student(student_id, "Kalli")
        print("Nafn uppfært á nemendanum sem var verið að búa til\n")

        student_info = SchoolDB.get_student(student_id)[0]
        print("Upplýsingar um nemenda:")
        for column in student_info:
            print(str(column) + ": " + str(student_info[column]))
        print()

        SchoolDB.remove_student(student_id)
        print("Nemendanum sem var verið að búa til hefur verið eytt")


    # -------------------- Prufa course föll ------------------------------
    elif valmynd == "2":
        
        brautar_numer = input("Veldu brautar númer\n-------------------->>> ")
        brautar_nafn = input("\nVeldu brautar nafn\n-------------------->>> ")
        print()

        SchoolDB.new_course(brautar_numer, brautar_nafn, 5)
        print("Búið til áfanga með brautar númerið ",brautar_numer, end="\n\n")

        SchoolDB.update_course(brautar_numer, "Skemmtilegi áfanginn")
        print("Nafn uppfært á áfanganum sem var verið að búa til\n")

        brautar_info = SchoolDB.get_course(brautar_numer)[0]
        print("Upplýsingar um áfanga:")
        for column in brautar_info:
            print(str(column) + ": " + str(brautar_info[column]))
        print()

        SchoolDB.remove_course(brautar_numer)
        print("Áfanganum sem var búið til hefur verið eytt")

        
    # -------------------- Prufa skóla föll ------------------------------
    elif valmynd == "3":

        skola_id = SchoolDB.new_school("Menntaskólinn í Tumaville")
        print("Búið til skóla með",skola_id,"sem skóla ID\n")

        SchoolDB.update_school(skola_id, "MT")
        print("Nafn uppfært á skólanum sem var verið að búa til\n")

        skola_info = SchoolDB.get_school(skola_id)[0]
        print("Upplýsingar um skóla:")
        for column in skola_info:
            print(str(column) + ": " + str(skola_info[column]))
        print()

        SchoolDB.remove_school(skola_id)
        print("Skólanum sem var verið að búa til hefur verið eytt")


    elif valmynd == "4":#Þetta er til þess að það komi ekki "ERROR Sláðu inn tölu á milli 1 og 4" þegar maður er að hætta í forritinu
        pass

    else:
        print("ERROR\tSláðu inn tölu á milli 1 og 4")

