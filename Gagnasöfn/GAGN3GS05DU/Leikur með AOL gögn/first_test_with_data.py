####################
# Imports
####################

import csv
from os import path

# Plotting
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


####################
# Global Variables
####################

file_name = "science_data/user-ct-test-collection-%n.csv"
test_file_name = "science_data/first-few-users-test.csv"
all_words = {}


####################
# Functions
####################

def is_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

# This function loops through CSV files, reads them one at a time and passes
# each row into a specified function one at a time to save on memory.
def process_files(file_name, number_of_files, function_to_run):
    print("Before loop")
    # Loop through all the files passed in
    for file_num in range(1, number_of_files+1):
        
        # Get the file num string
        if file_num < 10: file_num_str = "0" + str(file_num)
        else: file_num_str = str(file_num)

        # Replace the file with the current number
        replaced_file_name = file_name.replace("%n", file_num_str)
        
        # Get the file
        print("Processing file: " + replaced_file_name + ". This might take a while...")
        csv_reader = None
        with open(replaced_file_name, "r") as csv_data_file:
            csv_reader = csv.reader(csv_data_file)

            # Run the function for each row
            for row in csv_reader:
                function_to_run(row)

def process_data(line):

    if is_int(line[3]) is False: return
    # elif int(line[3]) < 400: return

    for word in set(line[1].split()):
        try:
            all_words[word] += 1
        except KeyError:
            all_words[word] = 1


####################
# Code
####################

# Keyra í gegnum allar CSV skrárnar og kannar þær.
process_files(file_name, 10, process_data)

# Gera plot
all_words_sorted = [(k, v) for k, v in sorted(all_words.items(), key=lambda item: item[1], reverse=True)]
print(all_words_sorted)

ax = plt.subplot(111)
width=0.5
bins = list( map( lambda x: x-width/2, range( 1, len(all_words_sorted) + 1 ) ) )
ax.bar( bins, [x[1] for x in all_words_sorted], width=width )
ax.set_xticks( list( map( lambda x: x, range( 1, len(all_words_sorted) + 1 ) ) ) )
ax.set_xticklabels( [x[0] for x in all_words_sorted], rotation=90 )

# Sýna plot
plt.show()


####################
# Temporary tests
####################