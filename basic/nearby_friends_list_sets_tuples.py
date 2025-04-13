# We have provided you with two variables:
# nearby_people = {'Rolf', 'Jen', 'Anna'}
# user_friends = set() # This is an empty set, like {}
# In this exercise, ask the user for the name of a friend. Add this name to the user_friends set provided.
# Finally, print out a set that contains only the name of the friend if the friend is in the nearby_people set.
# You'll want to calculate the intersection between two sets, and print the result out.


nearby_people = {'Rolf', 'Jen', 'Anna'}
user_friends = set()  # This is an empty set, like {}

# Ask the user for the name of a friend
new_friend = input("Enter Name : \n").capitalize()
# Add the name to the empty set
user_friends.add(new_friend)
# Print out the intersection between both sets. This gives us a set with those friends that are nearby.
print(user_friends.intersection(nearby_people))