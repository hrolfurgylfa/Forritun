stafir = {}
stig = []
linur = []
while True:
    x = input()
    lina = list(x)
    linur.append(lina)
    if x[0] != " " and x[0] != "|":
        break

for stafur in linur[-1]:
    stafir[stafur] = 0

x = 0
for stafur in stafir:
    for lina in linur:
        if lina[x] == "|":
            stafir[stafur] += 1
    x += 1

for stafur in stafir:
    print(stafur,end=": ")
    print(stafir[stafur])