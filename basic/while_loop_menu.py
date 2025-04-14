# A menu is something that repeats over and over again until the user types something that makes the program terminate.
# In our menu, the user will be able to choose from two options:
# If they type p , we will print "Hello"
# If they type q , we will terminate the program
# If they type something else, we will ask them for input again
# How will we go about it?
# First, we'll ask the user for what they want to do first. Do they want to print (p ), or do they want to exit without printing (q )?
# Then we'll have a while  loop that will repeat until the user types q .
# Inside the while loop, we'll have an if  statement that checks whether the user typed p . If they did, we'll print "Hello" .
# Inside the loop but outside the if statement, we'll ask the user again whether they want to print or quit.

user_input = input("Enter p to start : \n")

while user_input == "p":
    print("You have type 'p' ")
    user_input = input("Enter p to keep going and q to quit : \n")

print("You have typed q to quit!")
