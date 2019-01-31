skraarnafn = "test1.txt"
skra = open(skraarnafn,"w")
skra.write("")
skra.close()

skra = open(skraarnafn,"a")
for y in range([x for x in range(100) if x % 3 == 0]):
    skra.write(str(y)+",")

skra.close()

skra = open("test1.txt","r")
for line in skra:
    tala = line.split(",")