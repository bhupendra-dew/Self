import random
import math

# Taking the input

lower = int(input("Enter the lower bound : "))
upper = int(input("Enter the upper bound : "))

# Generating a rnadom number between the lower and the upper 

x = random.randint(lower, upper)
print("\n\t You have only ", round(math.log(upper - lower + 1, 2)), "chances to geuss the integer!\n")

# Initializing the number of geusses.

count = 0

# for calculation of the minimum number of geusses depends upon the range.

while count < math.log(upper - lower + 1, 2):
    count += 1

    # taking the geussing number as input
    guess = int(input("Guess the number : "))

    # Condition testing 
    if x == guess:
        print("Congratulations you did it in ",count, " try.")
        break
    elif x > guess:
        print("You guess a small number.")
    elif x < guess:
        print("You guess too big number.")
    else:
        print("Error please put only numbers.")

# If Guessing is more than the required guesses, shows the output.

if count >= math.log(upper - lower + 1, 2):
    print("\n The numebr is %d" % x)
    print("\t Better luck next time!")

