# Liður 1
weigh_loss[5] - weigh_loss[16]

#Liður 2
(weigh_loss[4] / weigh_loss[5]) * 100

#Liður 3a
value = weigh_loss[5] - weigh_loss[16]
weigh_loss[which.max(apply(value, MARGIN=1, FUN=max)),]
rm(value)

#Liður 3b
value = (weigh_loss[16]/weigh_loss[5])*100
weigh_loss[which.min(apply(value, MARGIN=1, FUN=min)),]
rm(value)

#Liður 4
mars_success = weigh_loss[6] >= weigh_loss[7]
september_success = weigh_loss[12] >= weigh_loss[13]
hverjir = mars_success==TRUE & september_success==FALSE

weigh_loss[which(hverjir %in% TRUE),]

rm(mars_success)
rm(september_success)
rm(hverjir)

# Liður 5
install.packages("dplyr")
library(dplyr)
new_col_values = round(
  ((weigh_loss[4]/weigh_loss[5])*100)[[1]],
  digits=1
)
weight_loss_extended=mutate(weigh_loss,success_rate=new_col_values)
rm(new_col_values)

View(weight_loss_extended)
