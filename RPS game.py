import random


def printScore(computer, user):
    print("Computer: ", computer)
    print("User: ", user)


def showChoices(a, b):
    print("User plays ", b)
    print("Computer plays", a)


choices = {0: 'Quit', 1: 'Rock', 2: 'Paper', 3: 'Scissors'}
welcome_1 = "Welcome to Rock, Paper, Scissors"
welcome = "\nTo play this game, press 1 for Rock, 2 for Paper, 3 for Scissors and 0 to quit."
game_choices = {'Rock': {'Paper': 0, 'Scissors': 1}, 'Paper': {'Rock': 1, 'Scissors': 0},
                'Scissors': {'Paper': 1, 'Rock': 0}}
computer_points = 0
user_points = 0
print(welcome_1)
while True:
    print(welcome)
    choice = int(input('Enter your choice here: '))
    if choice == 0:
        print("\nExiting game...")
        print("Final scores")
        printScore(computer_points, user_points)
        quit()
    user_choice = choices[choice]
    computer_choice = choices[random.randint(1, 3)]
    showChoices(computer_choice, user_choice)
    if user_choice == computer_choice:
        print("\nTie!")
    else:
        computer_points += game_choices[computer_choice][user_choice]
        user_points += game_choices[user_choice][computer_choice]
        if game_choices[user_choice][computer_choice]:
            print("\nYou scored a point!")
        else:
            print("\nComputer scored a point!")
    printScore(computer_points, user_points)