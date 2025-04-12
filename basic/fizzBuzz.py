# Print out numbers from 1 to 100 (including 100).
# But, instead of printing multiples of 3, print "Fizz"
# Instead of printing multiples of 5, print "Buzz"
# Instead of printing multiples of both 3 and 5, print "FizzBuzz".

start_point = 1

while start_point <= 100:
    if start_point % 3  ==0 and start_point%5 == 0:
        print("FizzBuzz")
    elif start_point % 5 == 0:
        print("Buzz")
    elif start_point % 3  ==0:
        print("Fizz")
    else:
        print(start_point)
    start_point += 1