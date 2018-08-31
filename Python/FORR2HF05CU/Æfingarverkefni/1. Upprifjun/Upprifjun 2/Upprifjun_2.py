import random

def buaTilDict():
    dictionary = {"A": "Armur", "B": "Bófi", "C": "Cristmas", "D": "Dreki", "E": "Ermar", "F": "Farangur", "G": "Banani", "H": "Hamar", "I": "Indjáni", "J": "Jól", "K": "Kanína", "L": "Lína", "M": "Matur", "N": "Nál", "P": "Pumpa"}
    
    return dictionary

def prentaDict(tempDict):
    for key in tempDict:
        print(key+str(" er fyrir ")+tempDict[key])

def prentaE(tempDict):
    print(tempDict["E"])

def breytaH(tempDict):
    tempDict2 = tempDict.copy()
    tempDict2["H"] = "Hrólfur"

    return tempDict2

def prentaDictS(tempDict):
    for key in tempDict:
        print(key+str(", ")+tempDict[key])

def eydaC(tempDict):
    dictEkkiC = {}

    for key in tempDict:
        if key != "C":
            dictEkkiC[key] = tempDict[key]

    return dictEkkiC

def popRandom(tempDict):
    tempDict2 = tempDict.copy()
    
    tempDict2.popitem()#Popitemp eyðir alltaf aftasta stakinu svo að það er ekki hægt að gera random

    return tempDict2

def copyDict(tempDict):
    return tempDict.copy()

def buaTilDict2():
    nytt_dict = {}

    for tala in range(1,6):
        nytt_dict[tala] = random.randint(99999999999999999999999999999999999999999,999999999999999999999999999999999999999999999999)
    
    return nytt_dict


#1
dictionary = buaTilDict()
print("1. ")
print(dictionary)

#2
print("\n2.")
prentaDict(dictionary)

#3
print("\n3. ",end="")
prentaE(dictionary)

#4
print("\n4.")
print(breytaH(dictionary))

#5
print("\n5.")
prentaDictS(breytaH(dictionary))

#6
print("\n6.")
print(eydaC(dictionary))

#7
print("\n7.")
prentaDictS(eydaC(dictionary))

#8
print("\n8.")
print(popRandom(dictionary))

#9
print("\n9.")
prentaDictS(popRandom(dictionary))

#10
print("\n10.")
dict2 = copyDict(dictionary)
print(dict2)

#11/12
print("\n11/12.")
val = input("Viltu eyða dict2, reyna að lesa það og crasha forritinu, j/n: ")

if val == "j":
    del dict2
    print(dict2)

#13
dict3 = buaTilDict2()
print("\n13. ")
print(dict3)

#14 items()
print("\n14(items). ")
print(dict3.items())

#14 keys()
print("\n14(keys). ")
print(dict2.keys())

#14 values()
print("\n14(values). ")
print(dictionary.values())

#14 clear()
print("\n14(clear). ")
print(dict3.clear())