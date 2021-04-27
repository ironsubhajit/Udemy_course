##udemy_python
##sub: improved Lottery game

import random

# This line creates a set with 6 random numbers
lottery_numbers = set(random.sample(range(22), 6))

# Here are your players; find out who has the most numbers matching lottery_numbers!
players = [
    {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
    {'name': 'Charlie', 'numbers': {2, 7, 9, 22, 10, 5}},
    {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
    {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
]

# Then, print out a line such as "Jen won 1000.".
# The winnings are calculated with the formula:
# 100 ** len(numbers_matched)
top_player = players[0]
for player in players:
    numbers_matched = len(player["numbers"].intersection(lottery_numbers))
    top_player_matched = len(top_player['numbers'].intersection(lottery_numbers))
    if numbers_matched > top_player_matched:
        top_player = player
winnings = 100 ** top_player_matched
print(top_player['name'] + " won " + str(winnings))

