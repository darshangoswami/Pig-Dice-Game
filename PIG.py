import random

def roll():
  roll = random.randint(1,6)
  return roll

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
  for player_id in range(players):
    print("\nPlayer number", player_id + 1, "'s turn to roll.\n")
    current_score = 0

    while True:
      want_roll = input("Would you like to roll (y)")
      if want_roll.lower() != "y":
        break
      value = roll()

      if value == 1:
        print("You rolled a 1, you're done!")
        current_score = 0
        break
      else:
        current_score += value
        print("You rolled a :", value)

      print("Your current score is:", current_score)

    players_scores[player_id] += current_score
    print("Your total score is:", players_scores[player_id])