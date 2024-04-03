import random
import math

def select_move():
  """
  the user should add the input here,
  which it sould be R or P or S in capital letter,
  then the computer will choose randomlly from the list
  """
  
  while True:
    list=["R","P","S"]

    player = input(f'select your move {name} \n>>>>  "R" or "P" or "S": \n')
    player = player.upper()
    
    computer = random.choice(list)
    print(computer)
    
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
      print ("tied")
    elif move_computer == "S":
      print ("winner")
    elif move_computer == "R":
      print ("lost")

  elif move_player == "P":
    if move_computer == "P":
      print ("tied")
    elif move_computer == "R":
      print ("winner")
    elif move_computer == "S":
      print ("lost")

  elif move_player == "S":
    if move_computer == "S":
      print ("tied")
    elif move_computer == "P":
      print ("winner")
    elif move_computer == "R":
      print ("lost")
  else:
    print(f'{name}, you enterd incorrect input/n')
    print(f'please {name} choose one of "R" or "P" or "S"')


print ("in this Game, we use 'R' for Rock, 'P' for Paper and 'S' for scissors\n")

print ("The battle started\n")

# here where the user enter name
name = input('Choose Name:\n')

select_move()
  
