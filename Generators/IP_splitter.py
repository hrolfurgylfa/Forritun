'''
IP_splitter
Hrólfur Gylfason
1/11/2018
'''
def buaTilPlusSjalftLista(stopp=256, x=1, listi=[]):
    if x <= stopp:
        listi.append(x)
        x += x
        return buaTilPlusSjalftLista(stopp, x, listi)
    else:
        return listi

def faHeiltolu(texti):
    try:
        heiltala = int(input(texti))
    except ValueError:
        print("Sláðu inn heiltölu")
    return heiltala

oll_taeki = []
allar_ip_staerdir = buaTilPlusSjalftLista()
print(allar_ip_staerdir)
ip_tala = input("Sláðu inn IP töluna: ")
bit = faHeiltolu("Sláðu inn hversu mörg bit eru fyrir networkið: ")
net = faHeiltolu("Sláðu inn hversu mörg net þú þarft: ")

for tel in range(net):
    magn_taekja = faHeiltolu("Sláðu inn hversu mörg tæki eru á neti "+str(tel)+"\n--->")
    oll_taeki.append(magn_taekja)

