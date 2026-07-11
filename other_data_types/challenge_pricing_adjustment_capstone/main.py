grocery_inventory={
    "Milk":("Dairy", 3.50,8),
    "Eggs":("Dairy",5.50,30),
    "Bread":("Bakery",2.99,15),
    "Apples":("Produce",1.50,50)
}
Eggs = {"Eggs":("Dairy",4.50,30)}
if  grocery_inventory["Eggs"][1] >5 :
    grocery_inventory.update(Eggs)
    print("Eggs are too expensive, reducing the price by $1.")
else:
    print("The price of Eggs is reasonable.")
tomatoes={"Tomatoes":("Produce",1.20,30)}
grocery_inventory.update(tomatoes)
print("Inventory after adding Tomatoes:",grocery_inventory)
milk_stock= grocery_inventory["Milk"][2]
if milk_stock<10:
    milk={"Milk":("Dairy", 3.50,28)}
    grocery_inventory.update(milk)
    print("Milk needs to be restocked. Increasing stock by 20 units.")
else:
    print("Milk has sufficient stock.")
if grocery_inventory["Apples"][1]>2:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")
print("Updated inventory:",grocery_inventory)