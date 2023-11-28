import os

# clear
clear = lambda: os.system('cls')

name = input("Enter your name: ")

def reply():
    while (True):
        print("yes/no")
        reply = input("Reply: ").lower()
        if (reply == "yes" or reply == "no"):
            return "yes" if reply == "yes" else "no"
        else:
            clear()
            print("Invalid input")


while (True):
    print("\nKen is asking if you want to play League of Legends instead of studying.\n")
    print(f"Ken: Hello {name}, do you want to play with me. UWU")

    if (reply() == "yes"):
        print("It's late, but Ken still wants to play.")
        print("Lettuce play one more till we win")
        if (reply() == "yes"):
            print("You stayed all night playing, didn't win a game, and got a failing score.")
            print("Bad Ending")
            break
        else:
            print("You didn't win a single game, but managed to pass the quiz.")
            print("Good Ending")
            break
            
    else:
        print("Instead of playing, he asked you to study.")
        print("Ken: What about studying?")
        if (reply() == "yes"):
            print("You studied all night and got a perfect score.")
            print("Best Ending")
            break
        else:
            print("You never studied, played all night alone, and got a failing score.")
            print("Worst Ending")
            break

