# The FizzBuzz challenge
# In this exercise, print out 100 numbers, from 1 to 100 (both inclusive). But:
# Instead of printing multiples of 3, print "Fizz"
# Instead of printing multiples of 5, print "Buzz"
# Instead of printing multiples of both 3 and 5, print "FizzBuzz".
# That means your program will print a combination of numbers, Fizz , Buzz , and FizzBuzz .
# For example:
# 1 
# 2 
# Fizz , since  3 is a multiple of 3
# 4 
# Buzz , since  5 is a multiple of 5
# Fizz , since  6 is a multiple of 3
# 7 
# 8 
# Fizz , since  9 is a multiple of 3
# Buzz , since  10 is a multiple of 5
# 11 
# Fizz , since  12 is a multiple of 3
# 13 
# 14 
# FizzBuzz , since  15 is a multiple of BOTH 3 AND 5
# 16
# Continue up to (and including) 100

# Make sure your program prints from 1 to 100, both inclusive!


for i in range(1,101):
    if i%5 == 0 and i%3 == 0:
        print(f"{i} : FizzBuzz")
    elif i%5 == 0:
        print(f"{i} : Buzz")
    elif i%3 == 0:
        print(f"{i} : Fizz")
    else: 
        print(i)