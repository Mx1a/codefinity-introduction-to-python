# Lists of items and categories for slicing
items = "Bubblegum, Chocolate, Pasta"
categories = "Candy Aisle, Pasta Aisle"
candy1= items[0:9]
candy2= items[10:20]
dry_goods= items[21:]
catagory1= categories[0:11]
catagory2 = categories[13:]
#print(canday1,candy2,dry_goods,catagory1,catagory2)
bubblegum_price = "$1.50"
chocolate_price = "$2.00"
pasta_price = "$5.40"
print(f"we have {candy1} for {bubblegum_price} in the {catagory1}")
print(f"we have {candy2} for {chocolate_price} in the {catagory1}")
print(f"we have {dry_goods} for {pasta_price} in the {catagory2}")