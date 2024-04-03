import random
  
def name_player():
  """
  Here where the player choose a name for it
  """
  name = input('Choose Name:\n')
  return name



def select_move_player():
  """
  the user should add the input here, which it sould be R or P or S in capital letter
  """
  player = input(f'select your move {name} \n>>>>  "R" or "P" or "S": \n')
  return player


def select_move_computer():
  """
  the computer will choose randomlly from the list
  """
  list=["R","P","S"]

  sel = random.choice(list) 
  print(sel)
  return sel
        

def vaild_move(validation):

  """
  I raised unvaild error here if the user throw anything not P or R or S
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
    print ("somthing went wrong")

"""def game_over():
  if move_player== "winner + winner":
    print ("won")
  elif move_player == "winner + teid":
    print ("tied")
  else:
    print ("game over, sorry you lost")
    exit ()"""



  


print ("in this Game, we use R for Rock, P for Paper and S for scissors\n")

print ("The battle started\n")




print ("in this Game, we use R for Rock, P for Paper and S for scissors\n")

print ("The battle started\n")

name = name_player()

def main():
  player = select_move_player()
  computer = select_move_computer()
  result = results(player, computer)
  #game_overs = game_over(result)


main()









  
