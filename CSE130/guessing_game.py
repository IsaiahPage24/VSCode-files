# 1. Name:
#      Isaiah Page
# 2. Assignment Name:
#      Lab 01: Guessing Game
# 3. Assignment Description:
#      A game where you attempt to guess a random number. You decide the range, and when you guess wrong you will get a hint.
#      At the end, the program will return the number of guesses you took and all of your guesses.
# 4. What was the hardest part? Be as specific as possible.
#      There were several parts that were more difficult than others, and I ended up doing some google searches to resolve those parts. 
#      They were:
#      How the heck do I get random numbers again?
#      LISTS. How to add to them and how to count the length.
#      However, all of these issues were extremely easy once I looked them up and reminded myself how to do them.
# 5. How long did it take for you to complete the assignment?
#      Two hours
import random

print("This is the 'guess a number' game.\n You try to guess a random number in the smallest number of attempts.\n")
range = int(input("Please enter a positive integer:\n>"))
target_number = random.randint(1,range)
guess = int(input(f"Guess a number between 1 and {range}.\n>"))
history = []

while guess != target_number:
    if guess < target_number:
        history.append(guess)
        guess = int(input("\tToo low!\n>"))
    elif guess > target_number:
        history.append(guess)
        guess = int(input("\tToo High!\n>"))
    else:
        print("error of some sort call Isaiah and tell him he sucks at coding.")

history.append(guess)
print(f"You were able to find the number in {len(history)} guesses.")
print(f"The numbers you guessed were: {history}")
