import json

def range1(end):
    return range(1, end+1)

harpan_json = []

# Síðasta talan í listunum er alltaf hversu mörg sæti eru alls
allar_haedir = {
    "Salur": [25, 26, 27, 26, 25, 28, 28, 28, 26, 26, 26, 26, 26, 26, 26, 26, 25, 25, 23, 26, 26, 26, 26, 26, 26, 26, 26, 20, 28],
    "Svalir 1": [1, 2, 3, 3],
    "Svalir 2": [3, 2, 1, 3],
    "Svalir 3": [4, 5, 2, 1, 4]
}

for haed in allar_haedir.keys():

    current_haed = allar_haedir[haed][0:-1]
    print("Current hæð:",current_haed)

    # Check the checksum
    if len(current_haed) != allar_haedir[haed][-1]:
        print("Checksum failed in",haed)
        print("Count:", len(allar_haedir[haed][0:-1]), "Expecting:",allar_haedir[haed][-1])
        print("Exiting...")
        exit()

    # Búa +til sætis raðirnar
    saetis_radir = []
    for radar_numer in range1(len(current_haed)):

        current_rod = current_haed[radar_numer-1]
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

    harpan_json.append({
        "Svæði": haed,
        "Raðir": saetis_radir
    })

with open('harpa.json', 'w', encoding='utf-8') as f:
    json.dump(harpan_json, f, ensure_ascii=False, indent=4)

print("Done!")