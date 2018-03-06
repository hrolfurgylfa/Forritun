'''
Hrolfur Gylfason
13/1/2018
Password-Generator
'''
import random

valmynd = ""
stafir = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
la_stafir = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
ha_stafir = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
takn = ["!","#","$","%","&","/","(",")","=","-","_","{","}","[","]","+","*","'","?","~","<",">","|"]

while valmynd != "2":
	valmynd = ""
	print("Sláðu inn 1 til þess að búa til aðgangsorð")
	print("Sláðu inn 2 til þess að hætta")
	valmynd = input("------------------------------>>> ")

	print()
	for tel in range(50):
		print("-",end="")
	print()

	if valmynd == "1":
		pass_lengd = ""
		while pass_lengd != "0":
			print("Sláðu inn hversu langt aðgangsorðið á að vera eða 0 til þess að fara til baka")
			pass_lengd = int(input("------------------------------>>> "))

			print()
			for tel in range(50):
				print("-",end="")
			print()

			if valmynd == "0":
				pass

			else:
				for tel in range(pass_lengd):
					tal_sta_mer = random.randint(1,3)
					if tal_sta_mer == 1:
						print(random.randint(0,9),end="")
					elif tal_sta_mer == 2:
						print(stafir[random.randint(0,51)],end="")
					elif tal_sta_mer == 3:
						print(takn[random.randint(0,22)],end="")
				print("\n")

	elif valmynd == "2":
		pass

	else:
		print("ERROR\tVinsamlegast sláðu inn 1 eða 2")