loka_verk = []
verk = []
for x in range(int(input())): verk.append(input())
for hlutur in verk:
    if hlutur not in loka_verk:
        loka_verk.append(hlutur)
        print(hlutur)