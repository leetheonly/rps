
#olumns = int((input("how many columns do you want?: ")))
#symbol = input("which symbol do you want?")

#for i in range(rows):
  #  for j in range(columns):
 #       print(symbol, end="")
   # print()

#cars ={"lambo", "jeep", "ford", "ferrari", "nissan", "subaru"}

#for i in cars:
 #   print(i , end=" ")


import random

choices = ["rock","paper","scissors"]
computer = random.choice(choices)
player = None

while player not in choices:
  player = input("rock paper or scissors?").lower()

if player == computer:
    print("computer picked: ",computer)
    print("you picked: ",player)
    print("you tied!")

elif player == "rock":
  if computer == "scissors":
    print("computer picked: ",computer)
    print("you picked: ",player)
    print("you won")
  if computer == "paper":
    print("computer picked: ",computer)
    print("you picked: ",player)
    print("you lost")

elif player == "paper":
  if computer == "scissors":
    print("computer picked: ",computer)
    print("you picked: ",player)
    print("you lost")
  if computer == "rock":
    print("computer picked: ",computer)
    print("you picked: ",player)
    print("you won")

elif player == "scissors":
  if computer == "paper":
    print("computer picked: ",computer)
    print("you picked: ",player)
    print("you won")
  if computer == "rock":
    print("computer picked: ",computer)
    print("you picked: ",player)
    print("you lost")

      
  
  

