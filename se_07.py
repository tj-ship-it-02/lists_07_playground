shopping_list = []

def add_item():
  new_item = input("What item you wanna add to the list? ")
  shopping_list.append(new_item)

while True:
  add_item()
  ask_another_item = input("Do you want to add another item? ")
  
  if ask_another_item == "yes":
    continue


  elif ask_another_item == "no":
    if (len(shopping_list) < 3):
        print("shoping lists need to have atleast 3 items!")
        continue
    else:
        break

  else:
    break

print(shopping_list)