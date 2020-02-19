import json

def range1(end):
    return range(1, end+1)

def er_tala(strengur):
    try:
        int(strengur)
        return True
    except ValueError:
        return False


harpan_json = []

# Síðasta talan í listunum er alltaf hversu mörg sæti eru alls
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
        "ErHjolastola": [
            "B1 10 11", "B2 8 9", "D1 10 11", "D2 8 9",
            "4 1 2", "14 1 2", "15 1 2"
        ],
        "ErSoundMixerFratekid": [
            "19 9 10 11 12 13 14 15",
            "18 10 11 12 13 14 15 16",
            "17 10 11 12 13 14 15 16"
        ],
        "ErSviðaExtention": ["1", "2", "3"]
    },
    "Svalir 1":{
        "Raðir": [4, 2, 3, 1, 4],
        "Hliðar_raðir": {
            "A1": 9
        }
    },
    "Svalir 2": {
        "Raðir": [4, 2, 3, 1, 4],
        "Hliðar_raðir": {
            "A1": 9
        }
    },
    "Svalir 3": {
        "Raðir": [4, 2, 3, 1, 4],
        "Hliðar_raðir": {
            "A1": 9
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
            "Raðar_stafur": hlidar_rod,
            "Sæti": oll_saeti
        })


    harpan_json.append({
        "Svæði": haed,
        "Raðir": saetis_radir,
        "Hliðar_raðir": hlidar_radir
    })

with open('harpa.json', 'w', encoding='utf-8') as f:
    json.dump(harpan_json, f, ensure_ascii=False, indent=4)

print("Done!")