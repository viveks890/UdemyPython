# Get the list of ages which are odd

ages = [1,2,3,4,5,6,7,8,9]

odd_ages = [
    age
    for age in ages
    if age%2 == 1
]

print(odd_ages)


# We have a list of friends in which elements are both uppercase and lowercase

friends = ["Rolf", "ruth", "Charlie", "Jen"]

# We have another list of guests

guests = ["jose", "Bob", "Rolf", "charlie", "michael"]

# We want a list of friends that are present as guests

########################## Approach 1 : Using sets ########################

friends_lower = [friend.lower() 
                 for friend in friends]
print(friends_lower)

guests_lower = [guest.lower() 
                for guest in guests]
print(guests_lower)

# Now we can create both as sets and do an intersection

friends_lower = set(friends_lower)
guests_lower = set(guests_lower)

# Do an intersection to check which are common

friends_in_guests = friends_lower.intersection(guests_lower)
print(friends_in_guests)
# But the above operation will give set as output which in unorder and we can slice it to make them uppercase again, 
# so have to convert this set into a list back again

friends_in_guests = list(friends_in_guests)
friends_in_guests = [common.title() for common in friends_in_guests]
print(friends_in_guests)


########################## Approach 1 : Using List comprehension ########################

friends_in_guests = [
    common.title()
    for common in friends_lower
    if common in guests_lower
]
print(friends_in_guests)