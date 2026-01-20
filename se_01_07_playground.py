# Create a function called remove_item().
# Inside the function, declare a variable (e.g., user_choice) and assign it to the input() of the user. Ask the user to enter the exact shopping item they'd like to remove.
# Then (still inside the function), remove the item from the shopping_list list.
# Below and outside of the function, create a loop.
# Inside the loop, execute remove_item().
# Afterward, inside the loop, ask the user if they'd like to remove another item. If they say "yes", restart the loop. If not, stop the loop.
# At the end of the program (outside of any function or loop), print the remaining list.
# Run your code and remove a couple of list items to check it works.

shopping_list = ["cookies", "chocolate", "potatoes", "bananas", "flowers", "beans"]

def remove_item(shopping_list):
    print(shopping_list)
    user_choice = input("What item from the shopping list would you like to remove? ")
    if user_choice in shopping_list:
        shopping_list.remove(user_choice)
        print(shopping_list)
    else:
        print("The item you selected is not part of the list.")
    

while True:
    remove_item(shopping_list)
    remove_another_item_question = input("Would you like to remove another item? ")
    if remove_another_item_question == "yes":
        continue
    if remove_another_item_question == "no":
        print("Your leftover items on the list are:")
        print(shopping_list)
        break

