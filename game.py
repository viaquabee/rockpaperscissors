import random
playerScore = 0
cpuScore = 0
draws = 0
while True:
    begin = input(("Welcome to RPS! Type 'start' to begin, 'quit' to quit, or 'scores' to view the scoreboard!"))
    if begin == "start":
        playerHand = input("Do you want to play rock, paper, or scissors?").lower()
        cpuHand = random.choice(['rock', 'paper', 'scissors'])
        if playerHand == cpuHand:
            print("You tied with the computer!")
            draws += 1
        elif (playerHand == "rock" and cpuHand == "scissors") or \
            (playerHand == "paper" and cpuHand == "rock") or \
            (playerHand == "scissors" and cpuHand == "paper"):
                print("You won!")
                playerScore += 1
        else:
            print("You lost!")
            cpuScore += 1
        print(f"You chose {playerHand} and the computer chose {cpuHand}!")
    elif begin == "quit":
        print("Goodbye!")
        break
    elif begin == "scores":
        if playerScore == 0 and cpuScore == 0 and draws == 0:
            print("You haven't played yet!")
        else:
            playerWord = "time" if playerScore == 1 else "times"
            cpuWord = "time" if cpuScore == 1 else "times"
            drawWord = "draw" if draws == 1 else "draws"
            print(f"You have won {playerScore} {playerWord}, the computer has won {cpuScore} {cpuWord}, and there's {draws} {drawWord}.")
            
    else:
        print("Invalid answer. Idiot.")
