def get_item(item_number):
  if item_number == 1:
    return("cheeseburger")
  elif item_number == 2:
    return("fries")
  elif item_number == 3:
    return("soda")
  elif item_number == 4:
    return("Ice Cream")
  elif item_number == 5:
    return("cookie")
  else:
    return("Sorry, we don't have that number")

def welcome():
  print("Welcome to my restaurant")
  print("1. Cheeseburger")
  print("2. Fries")
  print("3. Soda")
  print("4. Ice Cream")
  print("5. Cookie")

welcome() 

option = int(input("Can I take your order?"))

print(get_item(option))
