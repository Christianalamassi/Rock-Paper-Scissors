import random


def welcome():
    print("Welcome to Rock, Paper, Scissors\n")
    print("In this game you need to collect five points to win\n")
    print("use 'R' for Rock, 'P' for Paper and 'S' for scissors\n")


def user_name():
    """here where the user enter name"""
    while True:
        name = input('Choose Name:\n').strip()
        if (len(name) == 0):
            print("Please enter a name")
        else:
            return name
            break


def select_move(name):
    """
    The user should add the input here,
    which should be R or P or S with a capital letter,
    then the computer will choose randomly from the list.
    """
    print("The battle started\n")
    win = 0
    lose = 0
    while True:
        list = ["R", "P", "S"]
        while True:
            move_player = input(f'select a move {name}\n"R" or "P" or "S":\n')
            move_player = move_player.upper()
            if(move_player == "R" or move_player == "S" or move_player == "P"):
                break
            else:
                print(f'{name}, you entered incorrect input')
                print(f'please {name} choose one of "R" or "P" or "S"')
        move_computer = random.choice(list)
        print(move_computer)
        """ There are three odds for each throw"""
        if move_player == "R":
            if move_computer == "R":
                print("You >> Rock / Computer >> Rock => you tie")
            elif move_computer == "S":
                print("You >> Rock / Computer >> Scissors => you won")
                win += 1
            elif move_computer == "P":
                print("You >> Rock / Computer >> Paper => you lost")
                lose += 1
        elif move_player == "P":
            if move_computer == "P":
                print("You >> Paper / Computer >> Paper => you tie")
            elif move_computer == "R":
                print("You >> Paper / Computer >> Rock => you won")
                win += 1
            elif move_computer == "S":
                print("You >> Paper / Computer >> Scissors => you lost")
                lose += 1
        elif move_player == "S":
            if move_computer == "S":
                print("You >> Scissors / Computer >> Scissors => you tie")
            elif move_computer == "P":
                print("You >> Scissors / Computer >> Paper => you won")
                win += 1
            elif move_computer == "R":
                print("You >> Scissors / Computer >> Rock => you lost")
                lose += 1
        print(f'you got {win} and computer got {lose}')
        print("--------------------------")
        """the result of the game"""
        if win >= 5:
            print(f'congratulations {name}, you won the game')
            print("**********************************")
            plays = input(f'To play agian {name},type "YES" pleas:\n')
            play = plays.upper()
            if play == "YES":
                select_move(name)
            else:
                print("You didn't enter Yes.\n See you soon.")
                break
        elif lose >= 5:
            print(f"Sorry {name}, you lost >>> no worries {name} try again")
            print("**********************************")
            plays = input(f'To play agian {name},type "YES" pleas:\n')
            play = plays.upper()
            if play == "YES":
                select_move(name)
            else:
                print(f"See you soon {name}.")
            break
        else:
            continue


welcome = welcome()
name = user_name()
move = select_move(name)


def main():
    welcome
    name
    move


main()
