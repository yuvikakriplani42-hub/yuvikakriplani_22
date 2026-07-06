#define the menu of restaurant
menu={
   'pizza':450,
   'pasta':340,
   'salad':250,
   'prons':500,
   'cheesecake':450,
   'bebilica':320,
}

#greet
print("welcome to FAT FISH goa")
print("pizza: rs450\npasta: rs340\nsalad: rs250\nprons: rs500\ncheesecake: rs450\nbebilica: rs320" )

order_total=0
#80+70=150

item_1=input("enter the name of item you want to order=")
if item_1 in menu:
   order_total += menu[item_1]#0+450
   print("your item{item_1} has been added to your order")

else:
   print("ordered item{item_1} is not available yet!")

another_order=input("do you want to add another item? (yes/no)") 
if another_order == "yes":
   item_2=input("enter the name of second item you want to order=")
   if item_2 in menu:
      order_total += menu[item_2]
      print(f"your item{item_2} has been added to your order")

   else:
      print("ordered item{item_2} is not available yet!")

print(f"the total amount of items to pay is {order_total}")
print(menu)
     

