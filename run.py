import random


def select_move():
    """
    The user should add the input here,
    which should be R or P or S with a capital letter,
    then the computer will choose randomly from the list.
    """
    win = 0
    lose = 0
    while True:
        list = ["R", "P", "S"]
        while True:
            move_player = input(f'select a move {name}\n"R" or "P" or "S":\n')
            move_player = move_player .upper()
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
                print("tie")
            elif move_computer == "S":
                print("won")
                win += 1
            elif move_computer == "P":
                print("lost")
                lose += 1
        elif move_player == "P":
            if move_computer == "P":
                print("tie")
            elif move_computer == "R":
                print("won")
                win += 1
            elif move_computer == "S":
                print("lost")
                lose += 1
        elif move_player == "S":
            if move_computer == "S":
                print("tie")
            elif move_computer == "P":
                print("won")
                win += 1
            elif move_computer == "R":
                print("lost")
                lose += 1
        print(f'you got {win} and computer got {lose}')
        print("--------------------------")
        """the result of the game"""
        if win >= 5:
            print(f'congratulations {name}, you won the game')
            break
        elif lose >= 5:
            print(f"Sorry {name}, you lost >>> no worries {name} try again")
            break
        else:
            continue


print("in this game use 'R' for Rock, 'P' for Paper and 'S' for scissors\n")
# here where the user enter name
name = input('Choose Name:\n')
print("The battle started\n")

select_move()
