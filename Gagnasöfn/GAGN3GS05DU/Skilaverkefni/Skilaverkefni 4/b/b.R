# Sækja gögnin sem ég exportaði frá CSSE með Python
# forritinu mínu, gögnin sem ég exportaði frá eru
# fáanleg hérna:
# https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports
library(readr)
world_covid19_history = read_csv("C:/Users/Hrolfur/Desktop/Forritun/Gagnasöfn/GAGN3GS05DU/Skilaverkefni/Skilaverkefni 4/b/world_covid19_history.csv")
covid19_df = data.frame(world_covid19_history)
rm(world_covid19_history)
View(covid19_df)


# Þetta breytir labelunum sem ég fæ frá CSV yfir í einhvað
# sem plot() skilur, það tók mig marka klukkutíma að fatta
# þetta vegna þess að covid19_df[1] 1*101 en ekki 101*1 og
# það er ekki einhvað sem mér hefði dottið í hug vegna
# þess að ég hélt að c() væri venjulegur Python listi ekki
# multi dementional array.
covid19_labels = c(1:101)
for (i in c(1:101)) {
  covid19_labels[i] = covid19_df[1][i,]
  rm(i)
}


###############
# Liður 1
###############

# Correct plot with working date display
par(mar=c(5.1, 3.1, 3.1, 2.1))
plot.ts(covid19_df[2], xaxt = "n", xlab='Covid 19')
axis(
  1,
  at=1:101,
  labels=covid19_labels
)

# Plottið er í möppunni og kallað plot_1.png


####################
# Liður 1 Prufur
####################

# Correct plot with a bad but working date display
par(mar=c(5.1, 3.1, 3.1, 2.1))
plot.ts(covid19_df[2], xaxt = "n", xlab='Covid 19')
for (i in c(1:101)) {
  axis(
    1,
    at=i,
    labels=covid19_df[1][i,]
  )
  rm(i)
}

# Test plot
par(mar=c(5.1, 3.1, 3.1, 2.1))
plot(1:10, xaxt = "n", xlab='Some Letters')
axis(
  1,
  at=1:10,
  labels=c("a", "b", "c", "d", "e", "f", "g", "h", "i", "j")
)


###############
# Liður 2
###############

