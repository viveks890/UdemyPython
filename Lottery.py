lottery_numbers = {13, 21, 22, 5, 8}


"""
A player looks like this:

{
    'name': 'PLAYER_NAME',
    'numbers': {1, 2, 3, 4, 5}
}

Define a list with two players (you can come up with their names and numbers).
"""

players = [
    {"name":"Vivek", "numbers":{13,21,0,9,6}},
    {'name':'Anu', 'numbers':{22,8,5,6,7,1,90}}
]

"""
For each of the two players, print out a string like this: "Player PLAYER_NAME got 3 numbers right.".
Of course, replace PLAYER_NAME by their name, and the 3 by the amount of numbers they matched with lottery_numbers.
You'll have to access each player's name and numbers, and calculate the intersection of their numbers with lottery_numbers.
Then construct a string and print it out.

Remember: the string must contain the player's name and the amount of numbers they got right!
"""
for player in players:
    player_num = player['numbers']
    win_num = lottery_numbers.intersection(player_num)
    print(f"Player {player['name']} got {len(win_num)} numbers right")