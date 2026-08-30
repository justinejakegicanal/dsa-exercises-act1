guess_str = input("Guess a number: ")
guess = int(guess_str)
number = 9
while 0 <= guess <= 100:
    if guess > number:
        print("Guessed too high!")
    elif guess < number:
        print("Guessed too low.")
    else:
        print("Bingo")
        break
    guess_str = input("Guess a number: ")
    guess = int(guess_str)
else:
    print("You quit early!")

# Output behavior based on user input:
# - If guess > 9 (and <= 100):  Guessed too high!
# - If guess < 9 (and >= 0):    Guessed too low.
# - If guess == 9:              Bingo
# - If guess < 0 or guess > 100: You quit early!