
val = input("Sláðu inn 1 eða 2 ")

if val == 1:
	listi = []

	print("Gjöld ríkissjóðs")

	skra = open("gjold1.txt","r")

	for line in skra:
		lina = line.split(";")
		listi.append(lina)

	print(listi)

	print("Yfirflokkur\tUndirflokkur\tJanúar\tFebrúar\tMars\tApríl\tJúní\tÁgúst\tSeptember\tOktóber\tNóvember\tDesember\n\n")

	for tel in range(1,31):
		for tel2 in range(0,14):
			print(listi[tel][tel2],end=", ")
		print()
elif val == 2:
	os.makedirs("LoL")

	