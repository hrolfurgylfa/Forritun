listi=[1,2,3,4,5]#bý til lista með heiltölum
#útskrift 1
print(listi)
print(listi[2])#Prentast út 3
#útskrift 2
print("1. ",end="")
for tel in listi:
    print(tel,end=">>>>>   ")
print("2. Summa talnana er",sum(listi))
print("3. lægsta talan er",min(listi))
print("4. hæðsta talan er",max(listi))
print("5. Fjöldi talnana í listanum er",len(listi))
print("6. Meðaltal talnana er",(sum(listi)/len(listi)))
listi.append(3)#set 3 in
print("7. ",listi)
listi.remove(1)
print("8. ",listi)
del(listi[2])
print("9. ",listi)
print("10. ",listi.count(3))#telur hversu margir þristar eru í listanum
listi.sort()
print("9. ",listi)
listi.reverse()#snýr listanum við
print("9. ",listi)
