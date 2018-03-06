'''
Símanúmera Generator
Hrólfur Gylfason
2/3/2018
'''
import random

print()
hve_morg_run = int(input("Sláðu inn hversu mörg símanúmer þér vantar "))
print()
print("----------------------------------")

for tel in range(hve_morg_run):
    print(random.randint(6,8),end="")
    for tel in range(6):
        print(random.randint(0,9),end="")
    print()
    
print("----------------------------------")
print()