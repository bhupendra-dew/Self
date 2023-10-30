import random       # library that we use in order to choose on random words from a list of words

name = input("What is your name? ")         # Here the user is asked to enter the name first

print("Good Luck! ", name)
words = ['rainbow', 'computer', 'science', 'programming', 'python', 'mathematics', 'player', 'condition', 'reverse', 'water', 'board', 'geeks']

word = random.choice(words)         # Function will choose one random word form this list of words
print("Guess the characters")
guesses = ''

turns = 12          # any number of term can be used here

while turns > 0:
    failed = 0      # for counting the number of times a user fails 
    for char in word:           # all characters from the input word takin one at a time
        if char in guesses:
            print(char, end = " ")
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("You Win")
        print("The word is : ", word)
        break
    print()
    guess =input("guess a character : ")
    guesses += guess
    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have", + turns, 'more guesses')
        if turns == 0:
            print("You Loooseee")
        