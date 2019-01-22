frumtolur = [2]
tala = 1
print(2)

while len(frumtolur) < 100:
    frumtala = True
    tala += 2

    for tala2 in range(2,tala):
        if tala % tala2 == 0:
            frumtala = False
            break

    if frumtala == True:
        frumtolur.append(tala)
        print(tala)
