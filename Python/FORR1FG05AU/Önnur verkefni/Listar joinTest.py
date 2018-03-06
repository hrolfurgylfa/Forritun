#Hvernig unnið er með fallið join

#Dæmi 1
merki="-"
rod=("a","b","c")
print(merki.join(rod))

#Dæmi 2
listi=["Konni","Sponni","Nonni"]
tolur="123"
print(tolur.join(listi))

#Dæmi 3
strengur="Hrólfur er hér að forrita"#strengur
listi2=strengur.split(" ")#Splittar up á bili og setur í lista
print(listi2)
listi2.sort()
print(listi2)
print("&".join(listi2))

#Dæmi 4
print("K".join("043604789123647890"))

#Dæmi 5
print("&".join(strengur))

#Replace prufa, p málið
strengur2=input("Sláðu inn streng")
strengur2=strengur2.replace('a', 'pa')
strengur2=strengur2.replace('á', 'pá')
strengur2=strengur2.replace('e', 'pe')
strengur2=strengur2.replace('é', 'pé')
strengur2=strengur2.replace('i', 'pi')
strengur2=strengur2.replace('u', 'pu')
print(strengur2)
