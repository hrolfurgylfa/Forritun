'''
Verkefni 2 - Gagnasöfn
Hrólfur Gylfason
17/1/2018
'''
valmynd = ""

while valmynd != "5":

	for tel in range(50):
		print("-",end="")
	print("\n")

	print("Ýttu á 1 til þess að bæta við færslu")
	print("Ýttu á 2 til þess að breyta nafni og símanúmeri færslu")
	print("Ýttu á 3 til þess að eyða færslu")
	print("Ýttu á 4 til þess að birta allar færslur")
	print("Ýttu á 5 til þess að hætta")
	valmynd = input("-------------------->>> ")

	print()
	for tel in range(50):
		print("-",end="")
	print()

	if valmynd == "1":
		nafn = input("Sláðu inn fyrsta nafn nýja einstaklingssins ")
		kennitala = input("Sláðu inn kennitölu nýja einstaklingssins ")
		simanumer = input("Sláðu inn simanúmer nýja einstaklingssins ")

		simaskra = open("simaskra.txt","a")
		strengur = (nafn+"|"+kennitala+"|"+simanumer+"\n")
		simaskra.write(strengur)
		simaskra.close()

	elif valmynd == "2":
		allir = []
		tel = 0

		kennitala = input("Sláðu inn kennitölu tengiliðsins sem þér langar að breyta ")

		print()

		simaskra = open("simaskra.txt","r+")

		for line in simaskra:
			lina = line.split("|")
			allir.append(lina)

		simaskra.close()

		nafn = input("Sláðu inn fyrsta nafn einstaklingssins ")
		simanumer = input("Sláðu inn simanúmer einstaklingssins ")

		tel = 0
		for tel_2 in allir:
			if tel_2[1] == kennitala:
				allir[tel][0] = nafn
				allir[tel][1] = kennitala
				allir[tel][2] = simanumer
				break
			else:
				tel += 1

		simaskra = open("simaskra.txt","w")

		for tengiliður in allir:
			simi = tengiliður[2].replace("\n","")
			texti = tengiliður[0]+"|"+tengiliður[1]+"|"+simi+"\n"
			simaskra.write(texti)
		simaskra.close()

	elif valmynd == "3":
		kennitala = input("Sláðu inn kennitölu notandans sem þér langar að eyða eða . til þess að hætta við ")

		if kennitala == ".":
			pass

		else:
			allir = []
			tel = 0

			simaskra = open("simaskra.txt","r+")

			for line in simaskra:
				lina = line.split("|")
				allir.append(lina)

			simaskra.close()

			for tengiliður in allir:
				if tengiliður[1] == kennitala:
					del allir[tel]
					break

				else:
					tel += 1

			simaskra = open("simaskra.txt","w")

			for tengiliður in allir:
				simi = tengiliður[2].replace("\n","")
				texti = tengiliður[0]+"|"+tengiliður[1]+"|"+simi+"\n"
				simaskra.write(texti)
			simaskra.close()

	elif valmynd == "4":
		simaskra = open("simaskra.txt","r")

		print("Nafn\t\tKennitalan\tSímanúmer\n")
		for line in simaskra:
			lina = line.split("|")
			simi = lina[2].replace("\n","")

			if len(lina[0]) >= 8:#Hérna notaði ég þessa if/else setningu til þess að geta haft nafnið fremmst eins og mér finnst réttast en samt kemur þetta allt í röð
				print(lina[0]+"\t"+lina[1]+"\t"+simi)

			else:
				print(lina[0]+"\t\t"+lina[1]+"\t"+simi)

		simaskra.close()

	elif valmynd == "5":
		pass

	else:
		print("ERROR\tSláðu inn tölu á milli 1 og 5")
