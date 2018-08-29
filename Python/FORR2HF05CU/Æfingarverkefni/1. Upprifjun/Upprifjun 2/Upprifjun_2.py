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

