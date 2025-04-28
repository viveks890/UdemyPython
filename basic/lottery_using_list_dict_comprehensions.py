# Find out the player with the most correct numbers, and print out their winnings and their name.
# The random numbers are generated in a separate file called `config.py`. You don't need to modify this file. (I know we've not looked at the import keyword yet, bear with me on that one!):
# import config 
# # This line loads a set of 6 random numbers from the config file
# lottery_numbers = config.lottery_numbers
# And the list of players we've given you are:
# players = [
#     {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
#     {'name': 'Charlie', 'numbers': {2, 7, 9, 21, 10, 5}},
#     {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
#     {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
# ]
# Your task is to find who matched the most numbers, and print out a string with their name and the amount they won. For this exercise, assume there will only be 1 winner. Don't worry about two players matching the same amount of numbers.
# For example:
# Jen won 1000. 
# The winnings are calculated with this formula:
# winnings = 100 ** len(numbers_matched)

import random

win_list = []

for n in range(10):
    


print(win_nums)