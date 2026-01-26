# Your goal is to build the classic game Tic-Tac-Toe! If you’re not familiar, you can review the rules here. For this assessment, the game is simplified to be played in the terminal, with the computer as your opponent.
# Example (What the game could look like)
# Welcome to Tic-Tac-Toe! Here is the board: 

#   a b c
# 1 _ _ _
# 2 _ _ _
# 3 _ _ _

# Which cell do you choose? (Enter in the format 'a1')
# > b2

# Great! The computer chose a1.

#   a b c
# 1 o _ _
# 2 _ x _
# 3 _ _ _

# Which cell do you choose?  (Enter in the format 'a1')
# > b1

#   a b c
# 1 o _ _
# 2 _ x _
# 3 _ _ _

# Great! The computer chooses c1.

#   a b c
# 1 o x o
# 2 _ x _
# 3 _ _ _

# Which cell do you choose?  (Enter in the format 'a1')
# > b3

# You won!

#   a b c
# 1 o x o
# 2 _ x _
# 3 _ x _
# Tasks
# The assignment is broken down into separate tasks. They are designed to help you complete only parts of the game step by step. It’s recommended you read through all the tasks first to get an idea of how the game is progressively built. Then, start on completing only one task at a time.
# Task 1) The first task is to create the game grid and let the player select a cell once. There is no computer opponent, yet, and there are no win conditions. Here is what you should implement first:
# - Display a welcome message to the user.
# - Display an empty three-by-three grid with coordinates.
# - Ask the player to enter a string with the coordinates.
# - Validate that the user-entered string is a valid coordinate. If it isn’t ask the user to enter a valid coordinate.
# - Create an updated version of the grid with the selected cell and display it to the user.
# Hint: Instead of using coordinates like “a1”, or “b3", it might be simpler to only work with numbers like this:
# Enter the coordinates as numbers like this: "21"

#   0 1 2
# 0 _ _ _
# 1 _ _ x
# 2 _ _ _

print("Welcome to TikTakToe!")

rows = [[" ", "0", "1", "2"], ["0", "_", "_", "_"], ["1", "_", "_", "_"], ["2", "_", "_", "_"]]

# valid_coordinates = {
#     "00": rows[1][1], 
#     "01": rows[2][1], 
#     "02": rows[3][1],
#     "10": rows[1][2],
#     "11": rows[2][2],
#     "12": rows[3][2],
#     "20": rows[1][3],
#     "21": rows[2][3],
#     "22": rows[3][3]
#     }

# print(valid_coordinates)

def display_field():
    for row in rows:
        print(f"\n")
        for value in row:
            print(f"{value}", end="  ")
    print(f"\n")


display_field()

def validate_player_choice():
    while True:
        player_choice = input(f"Name the field you want to select! Start with the Y (vertical), then X (horizontal) coordinate, like '02' for example. ")

        if player_choice.isnumeric() and len(player_choice) == 2:
            row, column = list(player_choice)
            y_coordinate = int(row)
            x_coordinate = int(column)
            
        else:
            print("Your input needs to be a 2 digit number.")
            continue
        
        if x_coordinate > 2 or x_coordinate < 0:
            print("Your X coordinate needs to be between 0 and 2.")
            continue
        elif y_coordinate > 2 or y_coordinate < 0:
            print("Your Y coordinate needs to be between 0 and 2.")
            continue
        else:
            print("It worked!")
            y_coordinate = y_coordinate + 1
            x_coordinate = x_coordinate + 1
            rows[y_coordinate][x_coordinate] = "x"
            display_field()
            break
            


validate_player_choice()




# Task 2) Next, let the user choose a cell more than once and evaluate for errors.
# - After the user has selected a cell, ask them to select another.
# - Ensure that on every turn, the user input is validated again.
# - If the user enters a coordinate that is already selected, display an error to the user and ask them to enter a different coordinate.
# - Allow the player to exit the game any time - e.g., by entering the word ‘exit’.
# Task 3) Evaluate for win conditions. Check each win condition separately to make things a bit easier.
# - After every valid user input, check if three cells in a row are selected.
# - After every valid user input, check if three cells in the same column are selected.
# - After every valid user input, check if either of the two diagonals are entirely selected.
# - If any of those three win conditions are true, end the game and display a victory message to the user.
# Task 4) As a bonus task, add a computer opponent to the game. (This is an extra task and if you’ve gotten this far you’re probably going to do fine. But for the fun of it or the extra practice I still recommend trying this last step as well)
# - After every valid user input, let the computer choose a coordinate at random.
# - Ensure that coordinate isn’t already occupied.
# - Return and display an updated grid to the user including the user’s and the computer’s choice.
# - Check for victory conditions not only for the user but also for the user.
# - If the computer meets the victory conditions display a losing message to the player.
# Don’t forget: For this assessment, being able to work with git is a hard requirement. You’ll be expected to make several smaller commits throughout the exam. So if you’re not very familiar with git, yet, ensure to learn and practice it now.
