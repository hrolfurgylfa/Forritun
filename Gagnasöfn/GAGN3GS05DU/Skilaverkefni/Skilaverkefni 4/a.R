# Setja upp nemenda upplýsingarnar
id = c(1001, 1002, 1003, 1004, 1005, 1006)
nafn = c(
  "Gillian Keene",
  "Guðmundur Jónsson",
  "Marla Dröfn Diego",
  "Konráð Guðmundsson",
  "Renate Hertzenslust",
  "Sigurður Sívertssen"
)
utskrift = as.Date(c(
  "2012-05-25",
  "2013-12-17",
  "2014-05-15",
  "2014-05-15",
  "2014-12-19",
  "2015-05-27"
))

# Gera loka einkunnirnar
edlisfraedi_lokaeinkunn = c(9.4, 7.5, 9.5, 5.0, 6.6, 8.1)
efnafraedi_lokaeinkunn = c(8.4, 6.9, 5.5, 9.8, 4.0, 8.8)
staerdfraedi_lokaeinkunn = c(9.0, 6.7, 8.5, 5.0, 9.0, 9.7)

# Búa til data frame-inn
nemendur = data.frame(
  id,
  nafn,
  edlisfraedi_lokaeinkunn,
  efnafraedi_lokaeinkunn,
  staerdfraedi_lokaeinkunn,
  utskrift
)

# Eyða óðarfa breytunum
rm(
  id,
  nafn,
  utskrift,
  edlisfraedi_lokaeinkunn,
  efnafraedi_lokaeinkunn,
  staerdfraedi_lokaeinkunn
)

# Opna data frame-inn
View(nemendur)