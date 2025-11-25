import random
while True:
    valid_choices = ["r", "p", "s"]

    while True:
     users_choice = input("Rock, paper or scissors [r,p,s]: ").lower()
     if users_choice in valid_choices:
        break
    else:
        print("Invalid choice, please choose again [r,p,s]: ")

    choices = ["r", "p", "s"]
    computer_choice = random.choice(choices)

    emojis = {
    "r": "🎱",
    "p": "📃",
    "s": "✂"
    }

    print("You chose:", emojis[users_choice])
    print("Computer chose:", emojis[computer_choice])

    #determine the winner
    if users_choice==computer_choice:
        print("Tie")
    elif users_choice=="r" and computer_choice=="s":
        print("you wins")
    elif users_choice=="p" and computer_choice=="r":
        print("you win")
    elif users_choice=="s" and computer_choice=="p":
        print("you win")
    else:
        print("computer wins")
    play_again=input("Do you want to play again[y/n]: ").lower()
    if play_again!="y":
        print("Thank you for playing")
        break
    
    