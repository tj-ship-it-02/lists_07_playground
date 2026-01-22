shopping_list = {}

def validate_input_amount():
    while True:
        user_amount_input = input(f"How much/many {user_add_item} do you want to add? ")
        if user_amount_input.isnumeric():
            return int(user_amount_input)
        else:
            print("You can only enter int/numbers. No text.")
            continue

while True:
    user_add_item = input("What item do you want to add? ")
    item_name = user_add_item

    item_amount = validate_input_amount()

    shopping_list[item_name] = item_amount
  
    print(shopping_list)
    
    while True:
        another_input = input("Do you want to add another item? ")

        if another_input == "yes":
            break
        elif another_input == "no":
            print(shopping_list)
            exit()
        else:
            print("It's a 'yes' or 'no' question.")
            continue
