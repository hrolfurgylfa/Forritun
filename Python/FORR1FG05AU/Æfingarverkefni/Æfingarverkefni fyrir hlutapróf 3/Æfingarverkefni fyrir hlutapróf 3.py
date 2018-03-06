'''
#Liður 1
tel=0
afram="ja"
while afram=="ja":
    tel+=1
    print("Nú er búið að keyra while slaufuna",tel,"sinni")
'''
'''
#Liður 2
for tel in range(1,99999999999999999999999999999999999999999999999999999999999999999999999999999999999):
    print("Nú er búið að keyra for slaufuna",tel,"sinni")
'''
'''
#liður 3
keyra=1
index=0
listi=["A","B","C","D","E","F"]
hve_oft=int(input("Sláðu inn hversu margar línur á að skrifa "))
for tel in range(hve_oft):
    strengur=""
    for z in range(keyra):
        strengur+=listi[index]
    keyra+=1
    print(strengur)
    if index>=(len(listi)-1):
        index=0
    else:
        index+=1
'''
'''
#Liður 4
o_flokkad=["konni",12,3.4,"sponni",23,34,4,"anna",12.34]
listi_str=[]
listi_int=[]
listi_float=[]
for flokka in o_flokkad:
    if isinstance(flokka,str):
        print(flokka,"er strengur")
        listi_str.append(flokka)
    elif isinstance(flokka,int):
        print(flokka,"er integer")
        listi_int.append(flokka)
    elif isinstance(flokka,float):
        print(flokka,"er kommutala")
        listi_float.append(flokka)
    else:
        print("ERROR")
print("Þetta eru allir strengirnir:",end=" ")
for tel in listi_str:
    print(tel,end=", ")
print()
print("Þetta eru allar integer tölurnar:",end=" ")
for tel in listi_int:
    print(tel,end=", ")
print()
print("Þetta eru allar kommutölurnar:",end=" ")
for tel in listi_float:
    print(tel,end=", ")
print()
'''

#Liður 5
listi=[10,12,33,4,53,6,17,8,39,103]
summa=listi[4]+listi[5]+listi[6]





























