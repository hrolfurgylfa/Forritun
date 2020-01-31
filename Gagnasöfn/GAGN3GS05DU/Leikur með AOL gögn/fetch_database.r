# Init connection to local mongod
library(mongolite)
m <- mongo(collection = "AOLSearchData")

# Perform a query and retrieve data
out <- m$find('{ "Query": "google" }')
print(out)
rm(out)

# Eyða tengingunni við MongoDB
rm(m)

