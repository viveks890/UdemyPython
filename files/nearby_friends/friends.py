# Ask the user for the list of 3 friends
# For each friend, we'll tell the user whether they are in the same city
# For each friend in same city, we will save those on nearby_friends

import typing

class NearbyFriends:
    def __init__(self, file, mode) -> None:
        self.file = file
        self.mode = mode

    @property
    def read_file(self) -> typing.Union[typing.List, str]:
        try:
            my_file = open(self.file, self.mode)
            my_data = my_file.readlines()
            my_file.close()
        except Exception as e:
            print(str(e))
        else:
            return my_data

def user_input() -> typing.List:
    prompt = "Enter 3 Friends : "
    user_friends = input(prompt)
    user_friends = user_friends.split(',')
    return set(user_friends)

def compare_friends(friends_check : typing.Set, my_friends: typing.Set) -> typing.Set:
    nearby_friends = friends_check.intersection(my_friends)
    return nearby_friends


my_data =  NearbyFriends("./people.txt", 'r').read_file

friends_check = user_input()

my_friends = set(friend.strip() for friend in my_data)

print(my_friends)




