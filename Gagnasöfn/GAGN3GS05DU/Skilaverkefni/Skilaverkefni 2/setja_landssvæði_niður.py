import csv

def is_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

current_lands_svaedi = ""
new_file = []

with open("fjoldi_eftir_sveitafelogum_1feb2020.csv") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    for row in csv_reader:
        if is_int(row[0]) is False:
            current_lands_svaedi = row[0]
        else:
            new_row = []

            for i in range(0, len(row)):
                if i == 2:
                    new_row.append(current_lands_svaedi)
                new_row.append(row[i])

            new_file.append(new_row)


with open("cleaned_output.csv", "w", newline="", encoding="UTF8") as f:
    writer = csv.writer(f)
    writer.writerows(new_file)