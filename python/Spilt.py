#split function is used for creat string in to list of String's

String="10 11 12 13 14 15 16"

#we have to give Raguler Expression as argument of split function
#Know split function will split over string with respact" "
#l=["10","11","12","13","14","15","16"]

l=String.split(" ")

String="   10 12 13   "

#strip function is used for remove Extra space in given string
#befor function String ="   10 12 13   "
#after function String="10 12 13"

String.strip()
