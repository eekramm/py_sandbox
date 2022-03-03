print("...simple version of...")
print("...rock...")
print("...paper...")
print("...scissors...")
print("enter player ones choice:")
player1 = input()
print("enter player two choice:")
player2 = input()

if (player1 == player2):
    print("its a tie")
elif (player1 == "rock" and player2 == "scissors"):
    print("player1 wins!")
elif (player1 == "scissors" and player2 == "paper"):
    print("player1 wins!")
elif (player1 == "paper" and player2 == "rock"):
    print("player1 wins!")
else:
    print("player2 wins!")


import random
import enum

print("...bot version of...")
print("...rock...")
print("...paper...")
print("...scissors...")
print("enter player ones choice:")
player1 = input()

num = random.randrange(0,3)
print(num)

botChoices = ["rock", "paper", "scissors"]

bot = botChoices[num]

print(bot)

if (player1 == bot):
    print("its a tie")
elif (player1 == "rock" and bot == "scissors"):
    print("player1 wins!")
elif (player1 == "scissors" and bot == "paper"):
    print("player1 wins!")
elif (player1 == "paper" and bot == "rock"):
    print("player1 wins!")
else:
    print("bot wins!")




