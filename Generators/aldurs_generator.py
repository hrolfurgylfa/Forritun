import random

hversu_mikid = int(input("Sláðu inn hversu mikið af öldrum þér vantar: "))
laegsti_aldur = int(input("Sláðu inn lægsta aldurinn: "))
haesti_aldur = int(input("Sláðu inn hæsta aldurinn: "))

for tel in range(hversu_mikid):
    print(random.randint(laegsti_aldur,haesti_aldur))
