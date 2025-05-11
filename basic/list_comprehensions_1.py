# Double the numbers inside the list and create another list

numbers = [1,2,3,4,5,6]

doubled_numbers = [number*2 
                   for number in numbers]

print(doubled_numbers)

# Create list of strings

ages = [30, 40, 50]

friends_ages = [
    f"My friend is {age} years old"
    for age in ages
]

print(friends_ages)