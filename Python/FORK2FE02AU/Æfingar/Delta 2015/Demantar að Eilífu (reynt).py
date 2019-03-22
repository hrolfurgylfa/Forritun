inntak = input()

inntak = inntak.split()
fjoldi = int(inntak[0])
stafur = inntak[1]

v = fjoldi
h = fjoldi

for x in range(1, fjoldi + 1):
    if x == v and x == h: print(stafur,end="\n")
    elif x == v: print(stafur,end="")
    elif x == h - 1: print(stafur,end="\n")
    else: print(" ",end="")
    v -= 1
    h += 1

print()