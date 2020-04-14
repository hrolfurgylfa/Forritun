import matplotlib.pyplot as plt
import numpy as np
import csv


##################
# Fetch Data 
##################

gogn = {}
with open("GAGN3GS05DU/Skilaverkefni/Skilaverkefni 3/a/Lögbýlaskrá 2019.csv", "r", encoding="UTF-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=";")
    next(csv_reader)
    for line in csv_reader:
        try: gogn[line[0]] += 1
        except KeyError: gogn[line[0]] = 1


##################
# Sort Data 
##################

sorted_gogn = {k: v for k, v in sorted(gogn.items(), key=lambda item: item[1], reverse=True)}

names = sorted_gogn.keys()
data = sorted_gogn.values()


##################
# Plot the data
##################

ax = plt.subplot(111)
width=.3
bins = list(map(lambda x: x-width/2,range(1,len(data)+1)))
ax.bar(bins,data,width=width)
ax.set_xticks(list(map(lambda x: x, range(1,len(data)+1))))
ax.set_xticklabels(names,rotation=-90, rotation_mode="anchor", ha="left")

plt.show()
