import random

def select_move():
  """
  the user should add the input here,
  which it sould be R or P or S in capital letter,
  then the computer will choose randomlly from the list
  """
  win = 0
  lose = 0
  
  while True:
    list=["R","P","S"]
    
    move_player  = input(f'select your move {name} \n>>>>  "R" or "P" or "S": \n')
    move_player  = move_player .upper()
    
    move_computer = random.choice(list)
    print(move_computer)

    """ there is three odds for each throw"""
    if move_player == "R":
      if move_computer == "R":
        print ("tied")
      elif move_computer == "S":
        print ("winner")
        win += 1
      elif move_computer == "P":
        print ("lost")
        lose += 1

    elif move_player == "P":
      if move_computer == "P":
        print ("tied")
      elif move_computer == "R":
        print ("winner")
        win += 1
      elif move_computer == "S":
        print ("lost")
        lose += 1

    elif move_player == "S":
      if move_computer == "S":
        print ("tied")
      elif move_computer == "P":
        print ("winner")
        win += 1
      elif move_computer == "R":
        print ("lost")
        lose += 1
        
    else:
      print(f'{name}, you enterd incorrect input/n')
      print(f'please {name} choose one of "R" or "P" or "S"')

    print(f'you got {win} and computer got {lose}')

    if win >= 5:
      print(f'congratulation {name}, you won the game')
      break
    elif lose >= 5:
      print(f"Sorry {name}, you lost >>> no worries {name} try agian")
      break
    else:
      continue

print ("in this Game, We use 'R' for Rock, 'P' for Paper and 'S' for scissors\n")

print ("The battle started\n")

# here where the user enter name
name = input('Choose Name:\n')

select_move()
