
print("Welcome to TikTakToe!")


rows = [[" ", "0", "1", "2"], ["0", "_", "_", "_"], ["1", "_", "_", "_"], ["2", "_", "_", "_"]]

def show_field():
    for row in rows:
        print("\n")
        for value in row:
            print(f"{value}", end="  ")

show_field()

def get_validated_player_choice():

    while True: 
        print("\n")
        player_choice = input("What coordinate would you like to choose? Start with Y, then X coordinate: ")

        if player_choice == "exit":
            exit()
        elif not player_choice.isnumeric():
            print("\nYour input needs to be a number, no text.")
            continue
        elif len(player_choice) != 2:
            print("\nYour coordindate needs to be 2 digit.")
            continue
        
        row, column = list(player_choice)

        y_coordinate = int(row) + 1
        x_coordinate = int(column) + 1
        
        if y_coordinate > 3 or y_coordinate < 0:
            print("\nYour y coordinate needs to be between 0 and 2.")
            continue
        elif x_coordinate > 3 or x_coordinate < 0:
            print("\nYour x coordinate needs to be between 0 and 2.")
            continue
        else:
            return y_coordinate, x_coordinate

def print_player_choice():
    y_coordinate, x_coordinate = get_validated_player_choice()
    if rows[y_coordinate][x_coordinate] == "x" or rows[y_coordinate][x_coordinate] == "o":
        print("\n The cell is selected already. Choose another one.")
    else:
        rows[y_coordinate][x_coordinate] = "x"
        show_field()
    

while True:
    print_player_choice() 

        



