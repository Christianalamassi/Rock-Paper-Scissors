import random
import math

def select_move():
  """#the user should add the input here,
  which it sould be R or P or S in capital letter,
  then the computer will choose randomlly from the list"""
    list=["R","P","S"]

    player = input(f'select your move {name} \n>>>>  "R" or "P" or "S": \n')
    player = player.upper()
      return 0

    computer = random.choice(list)
    print(computer)
      return 0

    return  results(player,computer)
"""
    if player >= 5:
      break
    print(f'congratulation {name}, you won the game')
    elif player == computer:
      break
    print(f'{name} you have tied the game')
    else:
      break
    print(f"Sorry {name}, you lost>>>no worries {name} try agian")
"""

def results(move_player, move_computer):
  """ there is three odds for each throw"""
  if move_player == "R":
    if move_computer == "R":
      move_player +=0
      print ("tied")
    elif move_computer == "S":
      move_player +=1
      print ("winner")
    elif move_computer == "R":
      move_computer +=1
      print ("lost")

  elif move_player == "P":
    if move_computer == "P":
      move_player +=0
      print ("tied")
    elif move_computer == "R":
      move_player +=1
      print ("winner")
    elif move_computer == "S":
      move_computer +=1
      print ("lost")

  elif move_player == "S":
    if move_computer == "S":
      move_player +=0
      print ("tied")
    elif move_computer == "P":
      move_player +=1
      print ("winner")
    elif move_computer == "R":
      move_computer +=1
      print ("lost")
  else:
    print(f'{name}, you enterd incorrect input/n')
    print(f'please {name} choose one of "R" or "P" or "S"')


print ("in this Game, we use 'R' for Rock, 'P' for Paper and 'S' for scissors\n")

print ("The battle started\n")

# here where the user enter name
name = input('Choose Name:\n')

select_move()
  
