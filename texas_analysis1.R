dataSold <- read.csv("recently_sold_texas.txt",row.names=NULL)
cols <- c("address","zip","bed","bath","built","sq_ft","lot","type","sold_date","sold_price")
data <- data[complete.cases(dataSold[,"sold_price"]),]

input_value = 50000
purchase_value_min = 0.9*input_value*5
purchase_value_max = 1.1*input_value*5
subset <- dataSold1[which(!is.na(dataSold1$sold_price)),]
band <- subset[subset$sold_price > purchase_value_min & subset$sold_price < purchase_value_max,]
