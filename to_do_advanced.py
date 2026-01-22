# First, create a simple to-do list application (in its own Python file) with the following main features:
    # The user can choose whether to add an item, remove an item (by its index), or exit the application.
    # The user may perform any of the first two actions multiple times without exiting the program.
    # Errors are handled gracefully, so that the application doesn't crash if the user, e.g., enters an index that's not in the list or enters something other than "add", "remove", or "exit".
# New: Add a third option to the application. Let the user also choose to "show" the current list of tasks (and remember to add "show" to your error case line!)
# When the user chooses to "show" the list, print each individual list item on its own line on the screen. At the start of each line write the index followed by a dot before displaying the actual task. It should end up looking like a numbered list (like the one you're reading right now).
# While computers start counting at 0, humans don't tend to do that. Add 1 to each of the displayed indexes in the loop. And when the user enters a number to remove something from the list, let them enter the displayed number and not the index. You'll need to do some simple math operations in a couple of places to achieve this.
# If you like, you can turn the last step into a function (show_list(), for example) and then call this function instead of the print statements you used after adding or remove items.

todo_list = []
print("Welcome to your To Do 'advanced' application!")

def add_todo_item(todo_list):
    new_todo = input("What To Do would you like to add? ")
    if new_todo:
        todo_list.append(new_todo)
        show_todo_list(todo_list)
    else:
        print("You haven't entered a To Do. Try again.")

def remove_todo_item(todo_list):

    if not todo_list:
        print("Your list is empty. Try adding some To Do's before and come back.")
        return
    
    remove_todo = input("What To Do would you like to remove from the list? Tell me the index: ")
    

    if remove_todo.isnumeric():
        human_index = int(remove_todo)
        computer_index = human_index - 1
        if human_index > 0 and human_index < len(todo_list):
            todo_list.pop(computer_index)
            show_todo_list(todo_list)    
        else:
            print("You can't remove your item number since it's LESS or MORE than your actual list of items which is: " + str(len(todo_list)))
    else:
        print("Your input needs to be numeric!")
        

def show_todo_list(todo_list):
    
    if not todo_list:
        print("Your list is empty. Try adding some To Do's before and come back.")
        return
    
    for i, todo in enumerate(todo_list):
        print(f"{i + 1}. {todo}")


while True:

    user_navigation = input("What would you like to do now? Add an item, remove one, show your list or exit? ")
    
    if user_navigation == "add":
        add_todo_item(todo_list)
    elif user_navigation == "remove":
        remove_todo_item(todo_list)
    elif user_navigation == "show":
        show_todo_list(todo_list)
    elif user_navigation == "exit":
        print("Goodbye! Here are your open To Do's:")
        show_todo_list(todo_list)
        break
    else:
        print("You can only choose 'add', 'remove', 'show' or 'exit'. Nothing else.")


