import pymysql.cursors
import sys

class Skraning:
    def executeSQL(self, kodi):
        try:
            connection = pymysql.connect(host='tsuts.tskoli.is',
                                        user='2109013290',
                                        password='mypassword',
                                        db='2109013290_afangaskraning',
                                        charset='utf8mb4',
                                        cursorclass=pymysql.cursors.DictCursor,
                                        autocommit=True)
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

    def nyr_medlimur(self, nafn):
        s = Skraning()
        s.executeSQL("INSERT INTO notendur(nafn) VALUES ('"+str(nafn)+"')")

    def nyr_afangi(self, afangi):
        s = Skraning()
        s.executeSQL("INSERT INTO namskeid(afangaheiti) VALUES ('"+str(afangi)+"')")

    def prenta(self, nafntoflu):
        s = Skraning()
        tafla = s.executeSQL("SELECT * FROM "+str(nafntoflu))

        try:
            lyklar = list(tafla[0].keys())
        except IndexError:
            return ""

        for lykill in lyklar:
            print(lykill,end="\t|\t")
        print()

        for rod in tafla:
            for hlutur in rod:
                print(rod[hlutur],end="\t|\t")
            print()

    def skradurIafanga(self, nafn):
        s = Skraning()
        return s.executeSQL("""
        SELECT afangaheiti 
        FROM namskeid 
            JOIN skradir
                ON namskeid.namskeid_id = skradir.namskeid_id
            JOIN notendur
                ON notendur.notandi_id = skradir.notandi_id
        WHERE notendur.nafn='"""+str(nafn)+"""'
        """)

    def skraning(self, nafn, afangi):
        s = Skraning()
        try:
            notandi_id = s.executeSQL('SELECT notandi_id FROM notendur WHERE nafn="'+str(nafn)+'"')
            namskeid_id = s.executeSQL('SELECT namskeid_id FROM namskeid WHERE afangaheiti="'+str(afangi)+'"')
            s.executeSQL('INSERT INTO skradir(notandi_id,namskeid_id) VALUES('+str(notandi_id[0]["notandi_id"])+','+str(namskeid_id[0]["namskeid_id"])+')')

        except IndexError as e:
            print("Viðkomandi ekki skráður, notandi eða áfangaheiti rangt\n",e)

    def FaraUrAfanga(self, nafn, afangi):
        s = Skraning()
        try:
            notandi_id = s.executeSQL('SELECT notandi_id FROM notendur WHERE nafn="'+str(nafn)+'"')
            namskeid_id = s.executeSQL('SELECT namskeid_id FROM namskeid WHERE afangaheiti="'+str(afangi)+'"')
            s.executeSQL('DELETE FROM skradir WHERE notandi_id = '+str(notandi_id[0]["notandi_id"])+' AND namskeid_id = '+str(namskeid_id[0]["namskeid_id"]))

        except IndexError as e:
            print("Viðkomandi ekki skráður, notandi eða áfangaheiti rangt\n",e)

    def haetta(self, nafn):
        s = Skraning()
        s.executeSQL("""
        DELETE 
        FROM skradir 
        WHERE notandi_id = (
            SELECT notandi_id 
            FROM notendur 
            WHERE nafn = '"""+str(nafn)+"""')""")

        s.executeSQL("""
        DELETE
        FROM notendur
        WHERE nafn = '"""+str(nafn)+"""'""")
