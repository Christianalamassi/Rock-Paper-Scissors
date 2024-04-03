import random

def select_move():
  """#the user should add the input here,
  which it sould be R or P or S in capital letter,
  then the computer will choose randomlly from the list"""

  list=["R","P","S"]

  player = input(f'select your move {name} \n>>>>  "R" or "P" or "S": \n')

  computer = random.choice(list)
  print(computer)

  return  results(player,computer)



def results(move_player, move_computer):
  """ there is three odds for each throw"""
  if move_player == "R":
    if move_computer == "R":
      print ("tied")
    elif move_computer == "S":
      print ("winner")
    elif move_computer == "R":
      print ("lost")
    else:
      print ("somthing went wrong")

  elif move_player == "P":
    if move_computer == "P":
      print ("tied")
    elif move_computer == "R":
      print ("winner")
    elif move_computer == "S":
      print ("lost")
    else:
      print ("somthing went wrong")

  elif move_player == "S":
    if move_computer == "S":
      print ("tied")
    elif move_computer == "P":
      print ("winner")
    elif move_computer == "R":
      print ("lost")
    else:
      print ("somthing went wrong")
  else:
    print('incorrect, sorry choose ("R" or "P" or "S")')


print ("in this Game, we use R for Rock, P for Paper and S for scissors\n")

print ("The battle started\n")

# here where the user enter name
name = input('Choose Name:\n')

select_move()
  
