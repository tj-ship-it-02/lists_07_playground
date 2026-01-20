# First, start by creating a variable with an empty list to contain the tasks.
# Create a function that lets users input items to be appended to the list.
# Create a second function that lets users remove items from a list by entering the index. Try using .pop() instead of .remove() this time. 
# Use a longer condition (with elif) to check if the user input is numeric. Also, check that the input number is greater than or equal to 0 and lesser than the length of the task list.
# Remember: To perform comparisons with user input you need to work with numbers - not strings! And the same is true with the .pop() method.
# You can use len() to count items in a list.
# Lastly, create an application loop. Display a message to the user asking them to choose whether they want to add a task, remove a task, or exit the program. Depending on the user's input, either execute one of the two functions, repeat the question, or exit the loop (and the application).
# After every time you add or remove a task, print the current version of the to-do list on the screen.

to_do_list = []

def add_to_dos(to_do_list):
    user_to_do = input("What is most important for you right now? Add it here: ")
    to_do_list.append(user_to_do)
    print(to_do_list)

def remove_to_dos(to_do_list):
    print(to_do_list)
    user_remove = input("Which To Do would you like to remove? Tell me the index (number): ")
    if user_remove.isnumeric() and int(user_remove) >= 0 and int(user_remove) < len(to_do_list):
        to_do_list.pop(int(user_remove))
        print(to_do_list)
    else:
        print("Your input needs to be numeric, greater/equal to 0 and less than the len of your To Do List")


print("Welcome to your new to do app!")

while True:
    user_navigation = input("What would you like to do now? Add an item, remove one or exit? ")
    if user_navigation == "add":
        add_to_dos(to_do_list)
    elif user_navigation == "remove":
        remove_to_dos(to_do_list)
    elif user_navigation == "exit":
        print("Alrighty, see you soon! Still your to do's for today are:")
        print(to_do_list)
        break

     
    