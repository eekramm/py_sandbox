from random import randint

correct = 1

while correct < 6:
    number = randint(1, 10)
    while True:
        guess = int(input("Guess a number between 1 and 10:"))
        if guess == number:
            winsToGo = 5 - correct
            print(f"You are correct! {correct} of 5 correct guesses needed to win!")
            break
        elif guess < number:
            print("Too Low!")
        elif guess > number:
            print("Too High!")
    correct += 1

print("YOU WON!")

