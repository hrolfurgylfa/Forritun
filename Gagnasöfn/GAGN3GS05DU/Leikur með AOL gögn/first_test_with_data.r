####################
# Imports
####################

require(stringr)


####################
# Global Variables
####################

file_name = "science_data/user-ct-test-collection-%n.csv"


####################
# Functions
####################

# This function loops through CSV files, reads them one at a time and passes
# them into a specified function one at a time to save on memory.
process_files <- function(file_name, number_of_files, function_to_run) {
  
  # Loop through all the files passed in
  for (file_num in c(1:number_of_files)) {
    
    # Get the file num string
    file_num_str <- ""
    if (file_num < 10) {
      file_num_str <- paste(file_num_str, "0", file_num, sep="")
    } else {
      file_num_str <- paste(file_num_str, file_num, sep="")
    }

    # Replace the file with the current number
    replaced_file_name <- str_replace(file_name, "%n", file_num_str)
    
    # Get the file
    print(paste("Fetching file: ", replaced_file_name, ". This might take a while...", sep=""))
    data <- read.csv(replaced_file_name, header = TRUE)

    # Run the function
    function_to_run(data)

    # Hreinsa upp
    rm(file_num_str)
    rm(replaced_file_name)
    rm(data)
  }
}


####################
# Code
####################

# Keyra í gegnum allar CSV skrárnar og kannar þær.
process_files(file_name, 10, function(data) {print(data)})


####################
# Temporary tests
####################