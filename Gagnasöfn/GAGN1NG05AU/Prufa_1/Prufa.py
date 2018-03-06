#Gæti þurft að nota encoding="cp1252" eða frekar encoding="utf-8"
file = open("prufuskra.txt","w")#Býr til nýja skrá sem heitir simaskra.txt 
file.write("Prufa1\nPrufa2 Prufa3\tPrufa4")
file.write("Prufá5\nPrufæ6 Prufí7\tPrufö8")
file.close()


#Gæti þurft að nota encoding="cp1252" eða frekar encoding="utf-8"
skra = open("prufuskra.txt","r")#Býr til nýja skrá sem heitir simaskra.txt 

for line in skra:
	print(line)
skra.close()
