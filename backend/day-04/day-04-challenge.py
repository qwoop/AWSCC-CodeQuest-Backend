import random

print("Rock, Paper, Scissors\n")
player2 = random.choice(["rock", "paper", "scissors"])

while (True):
    player1 = input("Player1: ").lower()
    if (player1 in ["rock", "paper", "scissors"]):
        print(f"Player2: {player2}")
        if player1 == player2: print("\nDraw")
        elif player1 == "rock": print("\nPlayer1 Wins") if player2 == "scissors" else print("\nPlayer2 Wins")
        elif player1 == "paper": print("\nPlayer1 Wins") if player2 == "rock" else print("\nPlayer2 Wins")
        break
    else: print("Invalid Input")