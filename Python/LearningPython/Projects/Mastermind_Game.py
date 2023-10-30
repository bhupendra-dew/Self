import random

# The .randrange() function generates a random number within the specified rnage.

num = random.randrange(1000, 10000)

n  = int(input("Guess the 4 digit number : "))

# condition to test equality of the guess mode. Program terminates if true.

if (n == num):
    print("Great! You guessed the number in just 1 try ! You're a Mastermind!")
else:
    