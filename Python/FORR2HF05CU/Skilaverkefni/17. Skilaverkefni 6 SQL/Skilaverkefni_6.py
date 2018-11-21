'''
Skilaverkefni 6 MySQL
Hrólfur Gylfason
16/11/2018
'''
import pymysql.cursors
import sys

def executeSQL(kodi):
    try:
        connection = pymysql.connect(host='tsuts.tskoli.is',
                                    user='2109013290',
                                    password='mypassword',
                                    db='2109013290_afangaskraning',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)
    except pymysql.err.OperationalError as error:
        host = ""
        for stafur in str(error)[42::]:
            if stafur != "'":
                host += stafur
            else:
                break

        if str(error) == """(2003, "Can't connect to MySQL server on '"""+str(host)+"""' ([Errno -2] Name or service not known)")""" or str(error) == """(2003, "Can't connect to MySQL server on '"""+str(host)+"""' (timed out)")""":
            print("Náði ekki í "+str(host)+"\nHætti...")
            sys.exit()
        else:
            print(error)
            print("Hætti...")
            sys.exit()

    cursor = connection.cursor()

    try:
        cursor.execute(kodi)
    except pymysql.err.ProgrammingError as error:
        sql_error_kodi = ""
        skilabod = ""
        for stafur in str(error)[1::]:
            if stafur in "1234567890":
                sql_error_kodi += stafur
            else:
                break
        for stafur in str(error)[8::]:
            if stafur != '"':
                skilabod += stafur
            else:
                break

        if sql_error_kodi == "1064":
            fjoldi_komma_fundnar = 0
            sql_error = ""
            for stafur in str(error)[7::]:
                if stafur != "'" and fjoldi_komma_fundnar == 0:
                    pass
                elif stafur != "'" and fjoldi_komma_fundnar == 1:
                    sql_error += stafur
                elif stafur == "'" and fjoldi_komma_fundnar == 0:
                    fjoldi_komma_fundnar += 1
                else:
                    break

            print("SQL Stafsetningarvilla")
            print("SQL error kóði:",sql_error_kodi)
            print('Það er stafsetningarvilla nálægt "'+str(sql_error)+'".')
            print("Hætti...")
        else:
            print("SQL villa")
            print("SQL error kóði:",sql_error_kodi)
            print("SQL error skilaboð:",skilabod)
            print("Hætti...")
        sys.exit()

    result = cursor.fetchall()
    connection.close()
    return result

valmynd = ""

while valmynd != "14":

    for tel in range(50):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
        print("-",end="")
    print("\n")#Þetta er til þess að gera tvö enter

    print("Ýttu á 1 til þess að fá dæmi 1")
    print("Ýttu á 2 til þess að fá dæmi 2")
    print("Ýttu á 3 til þess að fá dæmi 3")
    print("Ýttu á 4 til þess að fá dæmi 4")
    print("Ýttu á 5 til þess að fá dæmi 5")
    print("Ýttu á 6 til þess að fá dæmi 6")
    print("Ýttu á 7 til þess að fá dæmi 7")
    print("Ýttu á 8 til þess að fá dæmi 8")
    print("Ýttu á 9 til þess að fá dæmi 9")
    print("Ýttu á 10 til þess að fá dæmi 10")
    print("Ýttu á 11 til þess að fá dæmi 11")
    print("Ýttu á 12 til þess að fá dæmi 12")
    print("Ýttu á 13 til þess að fá dæmi 13")
    print("Ýttu á 14 til þess að hætta")
    valmynd = input("-------------------->>> ")#Hérna velur notandinn hvaða lið hann ætlar að fara í

    print()#Þetta er til þess að gera enter
    for tel in range(50):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
        print("-",end="")
    print()#Þetta er til þess að gera enter

    if valmynd == "1":#Liður 1
        print(executeSQL("SELECT * FROM namsked;"))

    elif valmynd == "2":#Liður 2
        pass
        
    elif valmynd == "3":#Liður 3
        pass

    elif valmynd == "4":#Liður 4
        pass
        
    elif valmynd == "5":#Liður 5
        pass

    elif valmynd == "6":#Liður 6
        pass

    elif valmynd == "7":#Liður 7
        pass

    elif valmynd == "8":#Liður 8
        pass

    elif valmynd == "9":#Liður 9
        pass
        
    elif valmynd == "10":#Liður 10
        pass

    elif valmynd == "11":#Liður 11
        pass
        
    elif valmynd == "12":#Liður 12
        pass

    elif valmynd == "13":#Liður 13
        pass

    elif valmynd == "14":#Þetta er til þess að það komi ekki "ERROR Sláðu inn tölu á milli 1 og 14" þegar maður er að hætta í forritinu
        pass

    else:
        print("ERROR\tSláðu inn tölu á milli 1 og 14")
