menu={'chicken karai':1500,'pasta':700,'biryani':300,'pizza':1000,'coffee cup':200,'ice cream':300}
order_item = 0

while True:
    print("chicken karai= 1500Rs\npasta= 700Rs\nbiryani= 300Rs\npizza= 1000Rs\ncoffee cup= 200Rs\nice cream = 300Rs" )
    item_1 = input("Enter your item=\n")
    if item_1 in menu:
     order_item+=menu[item_1]
    
     print(f"Your item {item_1} added successfuly")
    else:
     print(f"{item_1} this item  not found")

     
    item_2 = input("Do you want to make another order(yes/no)\n")
    if item_2 == ("yes"):
      continue
    elif item_2 == ("no"):
      break

print(f"Your total amount = {order_item}")

 