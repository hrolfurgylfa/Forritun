'''
Verkefni 3
Hrólfur Gylfason
?/1/2018
'''
import csv

skra = open("postnumer.csv")
csv_skra = csv.reader(skra)

for lina in csv_skra:
    oneRow = lina[0].split(";")

    print(oneRow[0],"\t",oneRow[1])