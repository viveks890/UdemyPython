# Print out numbers from 1 to 100 (including 100).
# But, instead of printing multiples of 3, print "Fizz"
# Instead of printing multiples of 5, print "Buzz"
# Instead of printing multiples of both 3 and 5, print "FizzBuzz".

number = 1

while number <= 100:
    if number % 3 == 0:
        if number % 5 == 0:
            print('FizzBuzz')
        else:
            print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)
    number += 1
    