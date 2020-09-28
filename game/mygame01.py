#!/usr/bin/python3
"""

Author: Emeke Opute
Sep 2020
"""
# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]

How to win Game:
  Get to the Garden with a key and a potion to win! Avoid the monsters!
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
rooms = {

                   'Hall' : { 
                  'south' : 'Kitchen',
                   'east' : 'Dining Room',
                   'item' : 'key'
                },

                ß'Kitchen' : {
                  'north' : 'Hall',
                   'east' : 'Garden',
                   'item' : 'monster'
                },

                 'Garden' : {
                  'north' : 'Dining Room',
                   'west' : 'Kitchen',
                   'east' : 'Death Trap',
                  'south' : 'Family Room',
                   'item' : 'potion'
                },

            'Dining Room' : {
                   'west' : 'Hall',
                  'south' : 'Garden'
                },

             'Death Trap' : {
                   'west' : 'Garden',
			       'east' : 'Booze',
                   'item' : 'explosives'
                },

                  'Booze' : {
                   'west' : 'Death Trap',
                  'north' : 'Rewards',
                  'south' : 'Secrets',
                   'item' : 'booze'
                },

                'Rewards' : {
                   'east' : 'Jackpot',
                  'south' : 'Booze'
                },

                'Jackpot' : {
                   'west' : 'Rewards',
                  'south' : 'Underground Room',
                   'item' : 'potion'
                },

                'Secrets' : {
                   'west' : 'Family Room',
                  'north' : 'Booze'
                },

            'Family Room' : {
                  'north' : 'Garden',
                   'east' : 'Secrets',
                  'south' : 'Pool'
            },

       'Underground Room' : {
                  'north' : 'Family Room',
                   'west' : 'Praying Room'
                }

         }

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':  
    move = input(' enter a mov >') ## Comment to improve UX
  
  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')

    ## Cheat to Player decides to cheat their way to Jackpot
  if move[0] == 'cheat':
    currentRoom == 'Jackpot'
    inventory.append('potion')

    ## If a player enters a room with a monster or with eexplosives
  if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item'] or 'explosives' in rooms[currentRoom['item']]: ## Death Trap offers more risk yet quicker path to Rewards
    if 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you... GAME OVER!')
        break

    if 'explosives' in rooms[currentRoom]['item']:
        print('Explosives!!!! BOOOOM!!!!... GAME OVER!')
        break


## Define how a player can win
  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
    break
## Define how a player can hit JACKPOT
  if 'potion' in inventory and currentRoom == 'Jackpot': 
    print('You Wizard... JACKPOT')
    break
