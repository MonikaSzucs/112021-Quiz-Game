from tabulate import tabulate

print("Welcome to my computer quiz!")

playing = input("Do you want to play (Yes or No)? Do you need help (type: Help): ")
score = 0

while True:
    if playing.lower() == "yes":
        print("Okay! Lets play! ")

        answer = input("What does CPU stand for? ")
        if answer.lower() == "central processing unit":
            print("Correct!")
            score += 1
        else:
            print("Incorrect")

        answer = input("What does GPU stand for? ")
        if answer.lower() == "graphics processing unit":
            print("Correct!")
            score += 1
        else:
            print("Incorrect")

        answer = input("What does RAM stand for? ")
        if answer.lower() == "random access memory":
            print("Correct!")
            score += 1
        else:
            print("Incorrect")

        answer = input("What does PSU stand for? ")
        if answer.lower() == "power supply":
            print("Correct!")
            score += 1
        else:
            print("Incorrect")

        print("You got " + str(score) + ", or " + str((score/4)*100) + "% questions correct!")

        continue_game = input("Do you want to start the game again? ")
        if continue_game.lower() != "yes":
            quit()
        else:
            score = 0
            continue

    if playing.lower() == "help":
        print("Here is how to play the game")
        table = [["Yes/yes", "Will allow you to continue the game"], ["No/no", "Will quit the game"]]
        headers = ["Answers Typed", "What the game will do"]
        print(tabulate(table, headers, tablefmt="plain"))
        playing = input("Do you want to play (Yes or No)? ")
    else:
        quit()