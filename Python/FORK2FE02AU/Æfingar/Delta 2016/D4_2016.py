strengur = input()

backspace_counter = 0
nyr_strengur = ""

for stafur in strengur+" ":
    if stafur == "<":
        backspace_counter += 1
    else:
        for i in range(backspace_counter):
            try:
                nyr_strengur = nyr_strengur[0:-1]
                backspace_counter -= 1
            except:
                backspace_counter = 0
        nyr_strengur += stafur

print(nyr_strengur[0:-1])