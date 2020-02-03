import matplotlib.pyplot as plt
import numpy as np

#data
data = [4, 2, 8, 2, 3]
names = ['A:GBC_1233','C:WERT_423','A:LYD_342','B:SFS_23','D:KDE_2342']

ax = plt.subplot(111)
width=0.3
bins = list(map(lambda x: x-width/2,range(1,len(data)+1)))
ax.bar(bins,data,width=width)
ax.set_xticks(list(map(lambda x: x, range(1,len(data)+1))))
ax.set_xticklabels(names,rotation=45, rotation_mode="anchor", ha="right")

plt.show()
