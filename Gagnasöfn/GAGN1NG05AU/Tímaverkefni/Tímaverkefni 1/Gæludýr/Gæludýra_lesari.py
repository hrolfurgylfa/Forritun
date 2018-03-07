'''
Tímaverkefni 1 Gæludýr
Hrólfur Gylfason
7/2/2018
'''
valmynd = ""

while valmynd != "4":

	for tel in range(50):
		print("-",end="")
	print("\n")

	print("Ýttu á 1 til þess að bæta í skránna")
	print("Ýttu á 2 til þess að birta alla skránna")
	print("Ýttu á 3 til þess að birta upplýsingar um ákveðið dýr eftir nafni þess")
	print("Ýttu á 4 til þess að hætta")
	valmynd = input("-------------------->>> ")

	print()
	for tel in range(50):
		print("-",end="")
	print()

	if valmynd == "1":
		eigandi = input("Sláðu inn nafn eigandans ")
		nafn_dyrs = input("Sláðu inn nafn dýrsins ")
		tegund_dyrs = input("Sláðu inn tegund dýrsins ")

		gaeludyr = open("Gæludýr.txt","a")
		strengur = (eigandi+"|"+nafn_dyrs+"|"+tegund_dyrs+"\n")
		gaeludyr.write(strengur)
		gaeludyr.close()

	elif valmynd == "2":
		gaeludyr = open("Gæludýr.txt","r")

		print("Eigandi\t\tNafn dýrsins\tTegund dýrsins\n")
		for line in gaeludyr:
			lina = line.split("|")
			tegund = lina[2].replace("\n","")

			if len(lina[0]) >= 8:
				if len(lina[1]) >= 8:
					print(lina[0]+"\t"+lina[1]+"\t"+tegund)
				else:
					print(lina[0]+"\t"+lina[1]+"\t\t"+tegund)

			else:
				if len(lina[1]) >= 8:
					print(lina[0]+"\t\t"+lina[1]+"\t"+tegund)
				else:
					print(lina[0]+"\t\t"+lina[1]+"\t\t"+tegund)

		gaeludyr.close()

	elif valmynd == "3":
		allir = []
		tel = 0

		nafn_dyrs = input("Sláðu inn nafn dýrsins sem þér langar að skoða ")

		print()

		gaeludyr = open("Gæludýr.txt","r+")

		for line in gaeludyr:
			lina = line.split("|")
			allir.append(lina)

		gaeludyr.close()

		tel = 0
		for tel_2 in allir:
			if tel_2[1] == nafn_dyrs:
				print("Eigandi:",allir[tel][0],"\nNafn dýrsins:",allir[tel][1],"\nTegud dýrs:",allir[tel][2])
				break
			else:
				tel += 1

	elif valmynd == "4":
		pass

	else:
		print("ERROR\tSláðu inn tölu á milli 1 og 4")
