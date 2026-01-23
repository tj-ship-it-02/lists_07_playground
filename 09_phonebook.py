# Your task is to create a small phonebook application. The user should be able to add multiple contacts to their phonebook. For each contact, they can add a name, phone number, and email address. (Feel free to expand on that idea and add extra fields if you want!)

# Create a new Python file.
# Your application should have a basic loop to run the program. Start by asking the user to enter the name of a new contact.
# Follow the question by asking for additional fields such as phone number and email address.
# Add a dictionary per contact to a list. Then, ask the user if they'd like to add another new contact and allow them to do so if they answer "yes."
# Once the user is done adding contacts, print the entire list of contacts in a visually appealing way (using a for-loop). Add icons such as 📞 or 📧 to display the contact details on separate lines. (You may have to think hard about how to get the individual data points during each iteration of the for-loop. Work with print statements to try getting close to the solution if you get stuck!)
# Finally, use another loop to ask the user if they want to delete any of the contacts. Allow them to delete items by naming the position (index) of the contact.

contacts = []

def add_contact(contacts):
    name = input("What's the name of the current you want to add? ")
    age = input("Age? ")
    city = input("What city? ")
    phone = input("What phone number? ")
    email = input("What email adress? ")
    
    new_contact = {
        "name": name,
        "age": age,
        "city": city,
        "phone": phone,
        "email": email
    }

    contacts.append(new_contact)
    print(f"You've successfullyl added {name} to your contacts!")
    show_contacts(contacts)
    
def show_contacts(contacts):
    for index, contact in enumerate(contacts):
        print(f"{'=' * 30}\n")
        print(f" {index + 1}. 👋 Name: {contact['name']}")
        print(f"    👵 Age: {contact['age']}")
        print(f"    🌆 City: {contact['city']}")
        print(f"    📞 phone: {contact['phone']}")
        print(f"    📧 Email: {contact['email']}\n")

def remove_contact(contacts):
    remove_index = input("Which contact do you want to delete? Type the given index: ")
    if remove_index.isnumeric():
        human_index = int(remove_index)
        computer_index = human_index - 1
        if computer_index < 0 and computer_index > (len(contacts)):
            print("That contact doesn't work. Work with the numbers that exist.")
        else:
            deleted_contact = contacts.pop(computer_index)
            show_contacts(contacts)
            print(f"You have removed {deleted_contact['name']} from your contacts.")
            return
    else:
        print("No text allowed. Only the index number of the contact can be removed.")
    

# add_contact(contacts)
# add_contact(contacts)
# remove_contact(contacts)

while True:
    navigation = input("What do you want to do? 'add', 'remove' or 'exit'? ")
    if navigation == "add":
        add_contact(contacts)
    elif navigation == "remove":
        remove_contact(contacts)
    elif navigation == "exit":
        show_contacts(contacts)
        break
    else:
        print("Don't understand. Try again.")