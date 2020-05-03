import os
import csv
import json

def get_col_num(row, value):
    if isinstance(value, list):
        for i in range(0, len(row)):
            if row[i] in value:
                return i
    else:
        for i in range(0, len(row)):
            if row[i] == value:
                return i
    print(row)
    raise Exception(value+" not found in "+filename)

running = True
while running == True:

    # Setup the variables
    directory_str = "./science_data/"
    country = input("Choose a country (empty for all countries)(type exit to leave)\n>>>  ")
    summary = []

    # Exit if the country is exit
    if country == "exit": exit()

    # This sets up an efficient way to take the whole earth if country = ""
    if country == "": country_check = lambda x: True
    else: country_check = lambda x: x == country

    # Get the directory
    directory = os.fsencode(directory_str)

    # Loop through all the files in the directory_str
    for file in os.listdir(directory):

        # Make sure the current file is a csv file, otherwise skip it
        filename = os.fsdecode(file)
        if filename.endswith(".csv"): 

            print("Reading: ",filename)

            # Open the current file
            with open(directory_str+filename) as skra:
                reader = csv.reader(skra)
                
                # Find witch column number the country identifier is in
                header_row = next(reader)
                country_col = get_col_num(header_row, ["Country_Region", "Country/Region"])
                confirmed_col = get_col_num(header_row, "Confirmed")
                deaths_col = get_col_num(header_row, "Deaths")
                recovered_col = get_col_num(header_row, "Recovered")
                
                # Loop through the file and collect the data
                day = [filename[0:-4], 0, 0, 0]
                for row in reader:
                    if country_check(row[country_col]):
                        try: day[1] += int(row[confirmed_col])
                        except ValueError: pass
                        try: day[2] += int(row[deaths_col])
                        except ValueError: pass
                        try: day[3] += int(row[recovered_col])
                        except ValueError: pass

                summary.append(day)

    # Make sure their were some results for the selected country
    for day in summary:
        if sum(day[1:4]) != 0:
            running = False
            break
    else:
        print("There were no results for the country you selected, are you sure you spelled it correctly?\n")

# Create the output filename
if country == "": out_filename = "world"
else: out_filename = country
out_filename += "_covid19_history.csv"

# Create and write to the CSV file
with open(out_filename, "w") as out_file:
    csv_writer = csv.writer(out_file, lineterminator='\n')
    csv_writer.writerow(["date", "confirmed", "deaths", "recovered"])
    csv_writer.writerows(summary)

print("The results have been written to the file",out_filename)