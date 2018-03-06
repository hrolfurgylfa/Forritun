'''
Kennitölu Generator
Hrólfur Gylfason
28/2/2018
'''
import random

print()
hve_morg_run = int(input("Sláðu inn hversu margar kennitölur þér vantar "))
print()
print("----------------------------------")

for tel in range(hve_morg_run):

	#Manudir
	þrju_og_fjogur = random.randint(1,12)

	#Dagar
	if þrju_og_fjogur == 2:
		fyrstu_tveir = random.randint(1,28)
	else:
		fyrstu_tveir = random.randint(1,30)

	#Aftasta tala
	aftasta_tala_ticker = random.randint(0,1)
	if aftasta_tala_ticker == 0:
		aftasta_tala = 9
	else:
		aftasta_tala = 0

	#Ar
	if aftasta_tala == 9:
		fimm_og_sex = random.randint(40,99)

	else:
		fimm_og_sex = random.randint(1,15)
	#Þrjár random tölur
	þrjar_random_tolur = random.randint(100,999)

	#Dagar Prenntaðir
	if fyrstu_tveir <= 9:
		print("0"+str(fyrstu_tveir),end="")
	else:
		print(fyrstu_tveir,end="")

	#Mánuðir Prenntaðir
	if þrju_og_fjogur <= 9:
		print("0"+str(þrju_og_fjogur),end="")
	else:
		print(þrju_og_fjogur,end="")

	#Ár Prenntuð
	if fimm_og_sex <= 9:
		print("0"+str(fimm_og_sex),end="")
	else:
		print(fimm_og_sex,end="")

	#3 Random prenntaðar
	print(þrjar_random_tolur,end="")

	#Aftasta prenntuð
	print(aftasta_tala)
print("----------------------------------")
print()