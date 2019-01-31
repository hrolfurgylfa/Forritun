allir = {}
fjoldi = int(input())
for x in range(fjoldi):
    nafn = input()
    baer = input()
    fundinn = False
    for notandi in allir:
        if baer == notandi:
            fundinn = True
            allir[notandi] += 1
    if fundinn is False:
        allir[baer] = 1
for y in allir:
    print(y, allir[y])