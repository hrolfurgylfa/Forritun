import json

def range1(end):
    return range(1, end+1)

def er_tala(strengur):
    try:
        int(strengur)
        return True
    except ValueError:
        return False

def first(iterable, condition = lambda x: True):
    """
    Returns the first item in the `iterable` that
    satisfies the `condition`.

    If the condition is not given, returns the first item of
    the iterable.

    Raises `StopIteration` if no item satysfing the condition is found.

    >>> first( (1,2,3), condition=lambda x: x % 2 == 0)
    2
    >>> first(range(3, 100))
    3
    >>> first( () )
    Traceback (most recent call last):
    ...
    StopIteration
    """

    return next(x for x in iterable if condition(x))


harpan_json = []

# Síðasta talan í listunum er alltaf hversu margar sætisraðir eru
allar_haedir = {
    "Salur": {
        "Raðir": [25, 26, 27, 26, 25, 28, 28, 28, 26, 26, 26, 26, 26, 26, 26, 26, 25, 25, 23, 26, 26, 26, 26, 26, 26, 26, 26, 20, 28],
        "Hliðar_raðir": {
            "A1": 11,
            "A2": 11,
            "B1": 11,
            "B2": 9,
            "C1": 11,
            "C2": 11,
            "D1": 11,
            "D2": 9
        },
        "Frátekin sæti": {
            "HjolastolaFratekid": [
                "B1 10 11", "B2 8 9", "D1 10 11", "D2 8 9",
                "4 1 2", "14 1 2", "15 1 2"
            ],
            "SoundMixerFratekid": [
                "19 9 10 11 12 13 14 15",
                "18 10 11 1 2 13 14 15 16",
                "17 10 11 12 13 14 15 16"
            ],
            "SviðaExtention": ["1", "2", "3"]
        }
    },
    "Svalir 1":{
        "Raðir": [16, 33, 34, 35, 36, 35, 6],
        "Hliðar_raðir": {
            "F": 9,
            "G": 11,
            "I": 9,
            "J": 11
        },
        "Frátekin sæti": { "ErHjolastola": [ "G 11", "J 11" ] }
    },
    "Svalir 2": {
        "Raðir": [16, 36, 35, 34, 33, 32, 6],
        "Hliðar_raðir": {
            "M": 4,
            "N": 15,
            "P": 4,
            "R": 15
        },
        "Frátekin sæti": { "ErHjolastola": [ "N 15", "R 15" ] }
    },
    "Svalir 3": {
        "Raðir": [24, 40, 37, 34, 33, 30, 27, 22, 8],
        "Hliðar_raðir": {
            "S": 9,
            "T": 13,
            "U": 9,
            "V": 13
        }
    }
}


for haed in allar_haedir.keys():

    current_radir = allar_haedir[haed]["Raðir"][0:-1]
    print("Current raðir:",current_radir)
    current_hlidar_radir = allar_haedir[haed]["Hliðar_raðir"]
    print("Current hliðar raðir:",current_radir)

    # Check the checksum
    if len(current_radir) != allar_haedir[haed]["Raðir"][-1]:
        print("Checksum failed in",haed)
        print("Count:", len(allar_haedir[haed]["Raðir"][0:-1]), "Expecting:",allar_haedir[haed]["Raðir"][-1])
        print("Exiting...")
        exit()


    # Búa til sætis raðirnar
    saetis_radir = []
    for radar_numer in range1(len(current_radir)):

        current_rod = current_radir[radar_numer-1]
        print("Röð:", radar_numer, " Sæti í röð:", current_rod)

        oll_saeti = []
        for saeti in range1(current_rod):
            # print("Sætis númer:", saeti)
            oll_saeti.append({
                "Sætis_númer": saeti
            })

        saetis_radir.append({
            "Raðar_númer": radar_numer,
            "Sæti": oll_saeti
        })


    # Búa til hliðar raðirnar
    hlidar_radir = []
    for hlidar_rod in current_hlidar_radir.keys():

        current_rod = current_hlidar_radir[hlidar_rod]
        print("Röð:", hlidar_rod, " Sæti í röð:", current_rod)

        oll_saeti = []
        for saeti in range1(current_rod):
            oll_saeti.append({
                "Sætis_númer": saeti
            })

        hlidar_radir.append({
            "Raðar_númer": hlidar_rod,
            "Sæti": oll_saeti
        })


    # Setja sérstöku sætin
    try:
        fratekin_saeti = allar_haedir[haed]["Frátekin sæti"]
        print("Frátekin sæti:",fratekin_saeti)
        for fratekin_gerd in fratekin_saeti.keys():
            for stadsetning in fratekin_saeti[fratekin_gerd]:

                stadsetning_split = stadsetning.split()
                print("stadsetning_split:",stadsetning_split)

                # Finna réttu röðina
                if er_tala(stadsetning_split[0]):
                    rod = next(filter( lambda x: x["Raðar_númer"] == int(stadsetning_split[0]), saetis_radir ))
                    radar_gerd = "Raðir"
                else:
                    rod = next(filter( lambda x: x["Raðar_númer"] == stadsetning_split[0], hlidar_radir ))
                    radar_gerd = "Hliðar_raðir"
                print("Rod:",rod)

                for saeti in rod["Sæti"]:
                    if len(stadsetning_split) == 1:
                        # Bæta sérstaka hlutnum við sætið
                        saeti[fratekin_gerd] = True
                    if len(stadsetning_split) > 1:
                        if str(saeti["Sætis_númer"]) in stadsetning_split[1::]:
                            # Bæta sérstaka hlutnum við sætið
                            saeti[fratekin_gerd] = True
    except KeyError: pass


    harpan_json.append({
        "Svæði": haed,
        "Raðir": saetis_radir,
        "Hliðar_raðir": hlidar_radir
    })

with open('harpa.json', 'w', encoding='utf-8') as f:
    json.dump(harpan_json, f, ensure_ascii=False, indent=4)

print("Done!")