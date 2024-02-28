library(dplyr)

#import dataset
Original_Cash_Contributor_Dataset <- read.csv("../2022 Christina Stephenson Campaign/Datasets/Contributors 2011-2022.csv")
View(Original_Cash_Contributor_Dataset)
df <- Original_Cash_Contributor_Dataset


##Remove unneccessary columns
df <- select(df, -Foreign.Postal.Code, -Purpose.Codes, -Exp.Date)

View(df)

##Remove rows with null values in specific columns
df <- df %>%
  filter(!is.na(Amount) & !is.na(Contributor.Payee))

