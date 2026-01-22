import random

# 👇 Add your code below

players = ["Tahnee", "Thorge", "Tjark"]
dice_rolls = []

for player_roll in players:
  random_number = random.randint(1, 6)
  dice_rolls.append(random_number)
  print(dice_rolls)