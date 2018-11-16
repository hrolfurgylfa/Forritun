listi = [x for x in range(1,9999) if x % 10 == 0]
for tala in listi:
    if str(tala)[-1] != "0":
        print("ERROR", tala)