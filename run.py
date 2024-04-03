
  
def name_player():
  """
  Here where the player choose a name for it
  """
  name = input('Choose Name:\n')
  return name

def select_move():
    while True:

        player = input(f'select your move {name} \n>>>>  "R" or "P" or "S": \n')

        return player
        
def vaild_move(validation):

  """
  I raised unvaild error here if the user throw anything not P or R or S
  """
  try:
    if  validation != str("P"):
      raise ValueError(
        f'you should enter either "R" or "P" or "S" in capital letter.\n'
         )

  except ValueError as e:
    print(f"incorrect move:{e}, please try agian.\n")
    return False
  return True

  try:
    if  validation != str("R"):
      raise ValueError(
        f'you should enter either "R" or "P" or "S" in capital letter.\n'
         )
  except ValueError as e:
    print(f"incorrect move:{e}, please try agian.\n")
    return False
  return True

  try:
    if  validation != str("S"):
      raise ValueError(
        f'you should enter either "R" or "P" or "S" in  capital letter.\n'
         )
  except ValueError as e:
    print(f"incorrect move:{e}, please try agian.\n")
    return False
  return True


print ("in this Game, we use R for Rock, P for Paper and S for scissors\n")

print ("The battle started\n")

name = name_player()
move =select_move()
validations = vaild_move(move)
      
    
    
         
       

"""
  if p1r == "R":
    if p2r == "R":
      print ("tied")
    elif p2r == "S":
      print ("winner")
    elif p2r == "P":
      print ("lost")
    else:
      print ("somthing went wrong")
  elif p1r == "P":
    if p2r == "P":
      print ("tied")
    elif p2r == "S":
      print ("lost")
    elif p2r == "R":
      print ("winner")
    else:
      print ("somthing went wrong")
  elif p1r == "S":
    if p2r == "S":
      print ("tied")
    elif p2r == "P":
      print ("winer")
    elif p2r == "R":
        print ("lost")
    else:
       print ("somthing went wrong")
  break
while True:
  print ("select your move")
  print()
  p1r = input ("p1 > ")
  print ()
  p2r = input ("pc > ")
  print ()
  if p1r == "R":
    if p2r == "R":
      print ("tied")
    elif p2r == "S":
      print ("winner")
    elif p2r == "P":
      print ("lost")
    else:
      print ("somthing went wrong")
  elif p1r == "P":
    if p2r == "P":
      print ("tied")
    elif p2r == "S":
      print ("lost")
    elif p2r == "R":
      print ("winner")
    else:
      print ("somthing went wrong")
  elif p1r == "S":
    if p2r == "S":
      print ("tied")
    elif p2r == "P":
      print ("winer")
    elif p2r == "R":
        print ("lost")
    else:
       print ("somthing went wrong")
  break
while True:
  print ("select your move")
  print()
  p1r = input ("p1 > ")
  print ()
  p2r = input ("pc > ")
  print ()
  if p1r == "R":
    if p2r == "R":
      print ("tied")
    elif p2r == "S":
      print ("winner")
    elif p2r == "P":
      print ("lost")
    else:
      print ("somthing went wrong")
  elif p1r == "P":
    if p2r == "P":
      print ("tied")
    elif p2r == "S":
      print ("lost")
    elif p2r == "R":
      print ("winner")
    else:
      print ("somthing went wrong")
  elif p1r == "S":
    if p2r == "S":
      print ("tied")
    elif p2r == "P":
      print ("winer")
    elif p2r == "R":
        print ("lost")
    else:
       print ("somthing went wrong")
  break
if p1r == "winner + winner":
  print ("won")
elif p1r == "winner + teid":
  print ("tied")
else:
  print ("game over")
  exit ()
"""







  
