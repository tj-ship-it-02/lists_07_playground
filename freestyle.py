import random


print("Welcome to TikTakToe!")


rows = [[" ", "0", "1", "2"], ["0", "_", "_", "_"], ["1", "_", "_", "_"], ["2", "_", "_", "_"]]

player = "player"
computer = "computer"
tie = "tie"

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
            print("Your input needs to be a number, no text.")
            continue
        elif len(player_choice) != 2:
            print("Your coordindate needs to be 2 digit.")
            continue
        
        row, column = list(player_choice)

        y_coordinate = int(row) + 1
        x_coordinate = int(column) + 1
        
        if y_coordinate > 3 or y_coordinate < 0:
            print("Your y coordinate needs to be between 0 and 2.")
            continue
        elif x_coordinate > 3 or x_coordinate < 0:
            print("Your x coordinate needs to be between 0 and 2.")
            continue
        else:
            return y_coordinate, x_coordinate

def print_player_choice():
    while True:
        y_coordinate, x_coordinate = get_validated_player_choice()
        if rows[y_coordinate][x_coordinate] == "x" or rows[y_coordinate][x_coordinate] == "o":
            print("\n The cell is selected already. Choose another one.")
            continue
        else:
            rows[y_coordinate][x_coordinate] = "x"
            break
    

def print_computer_choice():
    while True:
        computer_choice_y = random.randint(1, 3)
        computer_choice_x = random.randint(1, 3)

        if rows[computer_choice_y][computer_choice_x] == "x" or rows[computer_choice_y][computer_choice_x] == "o":
            continue
        else:
            rows[computer_choice_y][computer_choice_x] = "o"
            show_field()
            break





def evaluate_winner():
    # checken ob die drei horizontal win-cond eintreten bei x (Spieler)
    if rows[1][1] == "x" and rows[1][2] == "x" and rows[1][3] == "x":
        return player
    elif rows[2][1] == "x" and rows[2][2] == "x" and rows[2][3] == "x":
        return player
    elif rows[3][1] == "x" and rows[3][2] == "x" and rows[3][3] == "x":
        return player
    # checken ob die drei horizontal win-cond eintreten bei o (computer)
    elif rows[1][1] == "o" and rows[1][2] == "o" and rows[1][3] == "o":
        return computer
    elif rows[2][1] == "o" and rows[2][2] == "o" and rows[2][3] == "o":
        return computer
    elif rows[3][1] == "o" and rows[3][2] == "o" and rows[3][3] == "o":
        return computer
    # checken ob die drei vertical win-cond eintreten bei x (Spieler)
    elif rows[1][1] == "x" and rows[2][1] == "x" and rows[3][1] == "x":
        return player
    elif rows[1][2] == "x" and rows[2][2] == "x" and rows[3][2] == "x":
        return player
    elif rows[1][3] == "x" and rows[2][3] == "x" and rows[3][3] == "x":
        return player
    # checken ob die drei vertical win-cond eintreten bei o (Computer)
    elif rows[1][1] == "o" and rows[2][1] == "o" and rows[3][1] == "o":
        return computer
    elif rows[1][2] == "o" and rows[2][2] == "o" and rows[3][2] == "o":
        return computer
    elif rows[1][3] == "o" and rows[2][3] == "o" and rows[3][3] == "o":
        return computer
    # checken ob die zwei diagonal win-cond eintreten bei x (spieler)
    elif rows[1][1] == "x" and rows[2][2] == "x" and rows[3][3] == "x":
        return player
    elif rows[1][3] == "x" and rows[2][2] == "x" and rows[3][1] == "x":
        return player
    # checken ob die zwei diagonal win-cond eintreten bei o (computer)
    elif rows[1][1] == "o" and rows[2][2] == "o" and rows[3][3] == "o":
        return computer
    elif rows[1][3] == "o" and rows[2][2] == "o" and rows[3][1] == "o":
        return computer
    
    has_empty_cell = any("_" in row for row in rows[1:])
    if not has_empty_cell:
        return tie
    
    return None

while True:
    print_player_choice() 
    winner = evaluate_winner()

    if winner == player:
        show_field()
        print(f"\n\n and the winner is: {winner}")
        break
    elif winner == computer:
        show_field()
        print(f"\n\n and the winner is: {winner}")
        break
    elif winner == tie:
        show_field()
        print(f"\n\n and the winner is: {winner}")
        break

    print_computer_choice()
    winner = evaluate_winner()

    if winner == player:
        show_field()
        print(f"\n\n and the winner is: {winner}")
        break
    elif winner == computer:
        show_field()
        print(f"\n\n and the winner is: {winner}")
        break
    elif winner == tie:
        show_field()
        print(f"\n\n and the winner is: {winner}")
        break


    
        



