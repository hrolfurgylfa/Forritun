from math import sqrt as rot
from math import pi
from time import sleep

def langhlid(a, b):
    a_i_odru = int(a) ** 2
    b_i_odru = int(b) ** 2

    a_plus_b = a_i_odru + b_i_odru

    rot_a_plus_b = rot(a_plus_b)

    return rot_a_plus_b

def margfeldi_af(tala1, tala2):
    if tala1 % tala2 == 0:
        return True
    else:
        return False

def ferningur_ur_stjornum(staerd_kassa):
    for haed in range(staerd_kassa):
        for breidd in range(staerd_kassa):
            print("★",end="")
        print()

def er_slett_tala(tala1):
    if tala1 % 2 == 0:
        return True
    else:
        return False

def flatramal_hrings(radius):
    flatarmal = pi * radius ** 2

    return flatarmal

def bank_bank(sekundur):
    while sekundur > 0:
        print("Bank")
        sleep(.2)
        sekundur -= .2
