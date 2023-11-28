import random

print("Rock, Paper, Scissors\n")
name = input("Enter your name: ").lower()
player2 = random.choice(["rock", "paper", "scissors"])

while (True):
    player1 = input(f"{name}: ").lower()
    if (player1 in ["rock", "paper", "scissors"]):
        print(f"Computer: {player2}")
        if player1 == player2: print("\nDraw")
        elif player1 == "rock": print(f"\n{name} Wins") if player2 == "scissors" else print("\nComputer Wins")
        elif player1 == "paper": print(f"\n{name} Wins") if player2 == "rock" else print("\nComputer Wins")
        break
    else: print("Invalid Input")