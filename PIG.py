import random

def roll():
  value = random.randint(1,6)

  return value

while True:
  players = input("Do we have 2 players,3 players or 4 players here?")

  if players.isdigit():
    players = int(players)
    if 2 <= players <= 4:
      break
    else:
      print("Please enter a number between 2 and 4.")
  else:
    print("Please enter a valid number.")

max_score = 50

players_scores = [0 for i in range(players)]

while max(players_scores) < max_score:

  current_score = 0

  want_roll = input("Would you like to roll (y)")

  if want_roll.lower != "y":
    break
  value = roll()

  if value == 1:
    print("You rolled a 1, you're done!")
    break
  else:
    current_score += value
    print("You rolled a :", value)

  print("Your current score is:", current_score)