skiptaLista = lambda listi, staerd: [listi[i:i+staerd] for i in range(0, len(listi), staerd)]

tel = int(input())
strengur = input()
oskipturListi = strengur.split(" ")

oskipturListi = list(map(int, oskipturListi))

oskipturListi.sort()

skipturListi = skiptaLista(oskipturListi, int(tel/3))

skilaListi = [skipturListi[1], skipturListi[0], skipturListi[2]]
skilaStrengur = ""

for i in skilaListi:
    for i2 in i:
        skilaStrengur += str(i2) + " "

print(skilaStrengur[0:-1])