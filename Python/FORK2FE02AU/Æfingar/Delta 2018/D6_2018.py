strengur = input()

strengur = strengur.split(" ")

a = int(strengur[0])
b = int(strengur[1])
c = int(strengur[2])

if a**2 + b**2 == c**2:
    print(round(a*b/2))
else:
    print(-1)