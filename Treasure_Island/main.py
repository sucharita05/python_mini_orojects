print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

step1 = input("You are a cross road.Where do you want to go? left(L) or right(R)? Type: ").lower()

if (step1 == "left" or step1 == "l"):
    step2 = input("You have come to a Lake.There is an Island in the middle of the lake.Type wait(W) to wait for a boat ot Type swim(S) to swim across: ").lower()
    if (step2 == "wait" or step2 == "w"):
        step3 = input("You have arrived at the island unharmed.There is a house with 3 doors. One red(R),one yellow(Y) and one blue(B). Which colour do you choose?").lower()
        if (step3 == "red" or step3 == "r"):
            print("It's a room full of fire. GAME OVER.")
        elif (step3 == "blue" or step3 == "b"):
            print("You entered a room of beasts. GAME OVER.")
        elif (step3 == "yellow" or step3 == "y"):
            print("You found the treasure! YOU WIN!")
        else:
            print("You chose a door that doesn't exist. GAME OVER.")
    else:
      print("You get attacked by an angry trout. GAME OVER.")
else:
  print("Fall into a hole. GAME OVER")