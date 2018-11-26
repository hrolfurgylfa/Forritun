import pymysql.cursors
import sys

class Skraning:
    def executeSQL(self, kodi):# Keyrir SQL kóða og tengist gagnagrunni til þess að gera það
        try:# Þetta reynir að tengjast gagnagrunninnum
            connection = pymysql.connect(host='tsuts.tskoli.is',
                                        user='2109013290',
                                        password='mypassword',
                                        db='2109013290_afangaskraning',
                                        charset='utf8mb4',
                                        cursorclass=pymysql.cursors.DictCursor,
                                        autocommit=True)
        except pymysql.err.OperationalError as error:
            host = ""
            for stafur in str(error)[42::]:# Þessi for slaufa byrjar á staf 42 og bætir stöfunum við strenginn host þangað til hún finnur aðra kommu (')
                if stafur != "'":
                    host += stafur
                else:
                    break

            if str(error) == """(2003, "Can't connect to MySQL server on '"""+str(host)+"""' ([Errno -2] Name or service not known)")""" or str(error) == """(2003, "Can't connect to MySQL server on '"""+str(host)+"""' (timed out)")""":# Þetta gerist bara ef það koma ákveðin error skilaboð
                print("Náði ekki í "+str(host)+"\nHætti...")
                sys.exit()
            else:
                print(error)
                print("Hætti...")
                sys.exit()

        cursor = connection.cursor()

        try:# Þetta reynir að keyra kóðann sem kom inn sem breyta
            cursor.execute(kodi)
        except pymysql.err.ProgrammingError as error:
            sql_error_kodi = ""
            skilabod = ""
            for stafur in str(error)[1::]:# Þessi for slaufa byrjar á staf 1 og bætir stöfunum við strenginn sql_error_kodi þangað til hún finnur eitthvað annað en tölu
                if stafur in "1234567890":
                    sql_error_kodi += stafur
                else:
                    break
            for stafur in str(error)[8::]:# Þessi for slaufa byrjar á staf 8 og bætir stöfunum við strenginn host þangað til hún finnur aðra kommu ('). Þessi error skilaboð virka ekki alveg svo að forritið prentar alltaf líka fullu skilaboðin
                if stafur != '"':
                    skilabod += stafur
                else:
                    break

            if sql_error_kodi == "1064":
                fjoldi_komma_fundnar = 0
                sql_error = ""
                for stafur in str(error)[7::]:# Þetta finnur akkurat hvað SQL 1064 errorskilaboðin voru að kvarta yfir
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
                print("Full error skilaboð:",error)
                print("Hætti...")
            else:
                print("SQL villa")
                print("SQL error kóði:",sql_error_kodi)
                print("SQL error skilaboð:",skilabod)
                print("Full error skilaboð:",error)
                print("Hætti...")
            sys.exit()

        result = cursor.fetchall()
        connection.close()
        return result# Þetta skilar öllu sem kom, raðir eru í ysta listanum og svo inni í honum eru dictionary-s með nafn dálksins sem key og það sem er í dæalkinum sem value

    def nyr_medlimur(self, nafn):# Bætir við notanda
        s = Skraning()
        s.executeSQL("INSERT INTO notendur(nafn) VALUES ('"+str(nafn)+"')")

    def nyr_afangi(self, afangi):# Bætir við áfanga
        s = Skraning()
        s.executeSQL("INSERT INTO namskeid(afangaheiti) VALUES ('"+str(afangi)+"')")

    def prenta(self, nafntoflu):# Prentar út töflu
        s = Skraning()
        tafla = s.executeSQL("SELECT * FROM "+str(nafntoflu))

        try:# Þetta klikkar ef taflan er tóm og þá fer forritið útúr fallinu
            lyklar = list(tafla[0].keys())
        except IndexError:
            return ""

        for lykill in lyklar:# Þetta prentar út alla top dálkana
            print(lykill,end="\t|\t")
        print()

        for rod in tafla:# Þetta fer í gegnum hverja röð fyrir sig
            for hlutur in rod:# Þetta fer í gegnum hvern hlut í hverri röð og prentar hann út með | fyrir aftan sig
                print(rod[hlutur],end="\t|\t")
            print()

    def skradurIafanga(self, nafn):# Skilar öllum áföngum sem ákveðinn notandi er skráður í
        s = Skraning()
        return s.executeSQL("""
        SELECT afangaheiti 
        FROM namskeid 
            JOIN skradir
                ON namskeid.namskeid_id = skradir.namskeid_id
            JOIN notendur
                ON notendur.notandi_id = skradir.notandi_id
        WHERE notendur.nafn='"""+str(nafn)+"""'""")# Þetta skilar öllu og svo getur lokaendinn sem kallaði á fallið ákveðið hvort að hann vilji prenta þetta út eða gera eitthvað annað með þetta

    def skraning(self, nafn, afangi):# Bætir notanda í áfanga
        s = Skraning()
        try:
            notandi_id = s.executeSQL('SELECT notandi_id FROM notendur WHERE nafn="'+str(nafn)+'"')
            namskeid_id = s.executeSQL('SELECT namskeid_id FROM namskeid WHERE afangaheiti="'+str(afangi)+'"')
            s.executeSQL('INSERT INTO skradir(notandi_id,namskeid_id) VALUES('+str(notandi_id[0]["notandi_id"])+','+str(namskeid_id[0]["namskeid_id"])+')')

        except IndexError as e:
            print("Viðkomandi ekki skráður, notandi eða áfangaheiti rangt\n",e)

    def FaraUrAfanga(self, nafn, afangi):# Tekur notanda úr áfanga
        s = Skraning()
        try:
            notandi_id = s.executeSQL('SELECT notandi_id FROM notendur WHERE nafn="'+str(nafn)+'"')
            namskeid_id = s.executeSQL('SELECT namskeid_id FROM namskeid WHERE afangaheiti="'+str(afangi)+'"')
            s.executeSQL('DELETE FROM skradir WHERE notandi_id = '+str(notandi_id[0]["notandi_id"])+' AND namskeid_id = '+str(namskeid_id[0]["namskeid_id"]))

        except IndexError as e:
            print("Viðkomandi ekki skráður, notandi eða áfangaheiti rangt\n",e)

    def haetta(self, nafn):# Eyðir notanda og tekur hann úr öllum áföngum
        s = Skraning()
        s.executeSQL("""
        DELETE 
        FROM skradir 
        WHERE notandi_id = (
            SELECT notandi_id 
            FROM notendur 
            WHERE nafn = '"""+str(nafn)+"""')""")# Hérna nota ég svigann til þess að senda niðurstöðunna úr einni leit beint í aðra til þess að þurfa ekki að tengjast gagnagrunninnum tvisvar og til þess að taka minna pláss

        s.executeSQL("""
        DELETE
        FROM notendur
        WHERE nafn = '"""+str(nafn)+"""'""")
