print("Edwin discovered an ancient method called The Binding of Rooms, a ritual meant to trap memories inside physical spaces. At first, it worked:")
print("The library remembered knowledge.")
print("The study remembered secrets.")
print("The basement remembered fear.")

print("But memories began to pile up, bleed together, and awaken.")
print("On the night of the final ritual, Edwin tried to bind himself to the house so his mind could live on forever. The ritual failed.")
print("He never left the house")
print("The house never forgot him")
#Item Key
item_key={
    'name':'Brass Key',
    'description':'A tarnished Key/cold to the touch.',
    'can_be_picked_up':True
}
item_heavystatue={
    'name':"Heavy Statue",
    'description':'A very heavy statue that sits in the corner of the hallway',
    'can_be_picked_up':False

}
item_book_unforgetting={
    'name':'Brand new book',
    'description':'The books leather cover is barely worn, unlike the others. Its spine is warm to the touch, as if it has been handled recently.',
    'can_be_picked_up':True
    
}

item_key_libary={
    'name':'libary key',
    'description':'A small brass key, A tiny engraving of a desk drawer is etched into its bow.',
    'can_be_picked_up':True
}
item_knife={
    'name':'Rusty Knife',
    'description':'An old knife with a rusty blade. It looks sharp enough to cut through something soft.',
    'can_be_picked_up':True
}
item_bread={
    'name':'Stale Bread',
    'description':'A loaf of bread that has gone stale. It is hard and dry to the touch.',
    'can_be_picked_up':True
}
item_painting={
    'name':'Faded Painting',
    'description':'An old painting of a landscape. The colors have faded over time, but you can still make out the details.',
    'can_be_picked_up':False
}
#Original room 
room_foyer={
    'id':'foyer',
    'name':'The Grand Entrance',
    'description':'A vast, marble hall...',
    'exits':{},
    'items':[]
    }

#Hallway
room_hallway={
    'id':'hallway',
    'name':'Dusty hallway',
    'description':'This Long,narrow passage is lined with cobweb-covered portraits.The marble'
    'ends here,replaced by rough wood. An exit leads back east',
    'exits':{},
    'items':[]
}

room_libary = {
    'id':'libary',
    'name':'grand libary',
    'description':'Edwin believed knowledge could be preserved forever if the room itself remembered it.'
    '  A single book brand new catches your eye',
    'exits':{},
    'items':[]
}
room_kitchen={
    'id':'kitchen',
    'name':'kitchen',
    'description':'A large kitchen with pots and pans hanging from the ceiling. A long wooden table sits in the center of the room.'
    'The smell of old food lingers in the air.',
    'exits':{},
    'items':[]
}
room_staircase={
    'id':'staircase',
    'name':'grand staircase',
    'description':'A grand staircase leading to the upper floors of the house. The steps creak underfoot.',
    'exits':{}, 
}
room_second_hallway={
    'id':'second_hallway',
    'name':'Upstairs hallway',
    'description':'A narrow hallway with doors on either side. The walls are lined with old portraits.',
    'exits':{},
}



#Global State
WORLD = {'foyer':room_foyer, 'hallway':room_hallway, 'libary':room_libary, 'kitchen':room_kitchen,'staircase':room_staircase,'second_hallway':room_second_hallway}
PLAYER_INVENTORY = [item_key]
CURRENT_ROOM_ID = 'foyer'

#Connecting Rooms
WORLD['foyer']['exits']={'west':'hallway'}
WORLD['hallway']['exits']={'east':'foyer','north':'libary','south':'kitchen','west':'staircase'}
WORLD['libary']['exits']={'south':'hallway'}
WORLD['kitchen']['exits']={'north':'hallway'}
WORLD['staircase']['exits']={'east':'hallway'}
WORLD['second_hallway']['exits']={'west':'staircase'}


#Placing items 
item_map = {'name': "Old Map", 'description': 'A crinkled piece of parchment.', 'can_be_picked_up': True} 
WORLD['hallway']['items']=[]
WORLD['hallway']['items'].append(item_map)
WORLD['hallway']['items'].append(item_heavystatue)
WORLD['libary']['items']=[]
WORLD['libary']['items'].append(item_book_unforgetting)
WORLD['libary']['items'].append(item_key_libary)
WORLD['kitchen']['items']=[]
WORLD['kitchen']['items'].append(item_knife)
WORLD['kitchen']['items'].append(item_bread)


#code to say where you are
current_room = WORLD['foyer']
for item in current_room['items']:
    print(f"- {item['name']}: {item['description']}")


#listing all exits from a location in every direction
print("Exits from Foyer:")
for direction in WORLD['foyer']['exits']:
    target_id = WORLD['foyer']['exits'][direction]
    print(f"* To the {direction} is {WORLD[target_id]['name']}")


#list all items in a location
print("\nItems in Hallway:")
for item in WORLD['hallway']['items']:
    print(f"- {item['name']}")
print("-" * 40)


#What is in inventory
print("Your current inventory: ")
for item in PLAYER_INVENTORY:
    print(f"-{item['name']}")

def display_room_info(room_id):
    """Displays the current room's details."""
    current_room = WORLD[room_id]

    print(f"\n########################################")
    print(f"  {current_room['name'].upper()}")
    print(f"########################################")
    print(current_room['description'])

    # Display items in the room
    if current_room['items']:
        print("\nYou see:")
        for item in current_room['items']:
            print(f"- {item['name']} ({item['description']})")

    # Display available exits
    print("\nAvailable Exits:", list(current_room['exits'].keys()))


def try_move(direction):
    """Checks if a move is valid and updates the player's location."""
    global CURRENT_ROOM_ID # Required to change the external variable

    current_exits = WORLD[CURRENT_ROOM_ID]['exits']

    # move in requested direction, if possible
    if direction in current_exits:
        CURRENT_ROOM_ID = current_exits[direction]
        display_room_info(CURRENT_ROOM_ID)
    else:
        print("You can't go that way!")

#test code 
'''
print("\n--- Exercise 6 & 7: Movement Logic Check ---")
print("Starting Location:")
display_room_info(CURRENT_ROOM_ID) # Test Ex. 6

print("\nAttempting successful move (WEST):")
try_move('west')  # Test Ex. 7 successful move

print("\nAttempting unsuccessful move (NORTH):")
try_move('north') # Test Ex. 7 unsuccessful move
print("-" * 40)
'''


#Command Parser

def parse_command(command_string): 
    words = command_string.strip().lower().split() 
    verb = words[0] if len(words) >= 1 else None 
    noun = ' '.join(words[1:]) if len(words) >= 2 else None 
    return verb, noun 


def handle_action(verb,noun):
    if verb =='take':
        if not noun:
            print("Take what?")
            return
        room_items = WORLD[CURRENT_ROOM_ID]['items']
        item_to_take = None
        for item in room_items:
            if item['name'].lower() == noun:
                item_to_take = item
                break
        if item_to_take:
            if item['can_be_picked_up']:
                room_items.remove(item_to_take)
                PLAYER_INVENTORY.append(item_to_take)
                print(f"You take the {item_to_take['name']}.")
            else:
                print("Cannot be taken")
        else:
            print(f"There is no {noun} here.")
    elif verb =='look':
        display_room_info(CURRENT_ROOM_ID)
    elif verb == 'inventory':
        print("\n--- Your Backpack ---")
        if not PLAYER_INVENTORY:
            print("It's empty.")
        else:
            for item in PLAYER_INVENTORY:
                print(f"* {item['name']}")
    elif verb == 'go':
        if noun:
            try_move(noun)
        else:
            print("Go where? You must specify a direction (e.g., 'go west').")
    elif verb == 'drop':
        if not noun:
            print("Drop what?")
            return
        item_to_drop = None
        for item in PLAYER_INVENTORY:
            if item['name'].lower() == noun:
                item_to_drop = item
                break
        if item_to_drop:
            PLAYER_INVENTORY.remove(item_to_drop)
            WORLD[CURRENT_ROOM_ID]['items'].append(item_to_drop)
            print(f"You drop the {item_to_drop['name']}.")
        else:
            print(f"You aren't carrying a {noun}.")
    else:
        print(f"I don't understand the command '{verb}'.")
    







#Test code
''''
print("\n--- Exercise 9, 11, 12, 13: Command Tests ---")
print(f"'Go North' parsed: {parse_command('Go North')}") # Ex 9 Test


# Initial position is Hallway (from Ex 7 test)
# Current Room: Hallway (has Old Map). Inventory: Brass Key.

# Ex 12 Test: Take the map
print(f"'TAKE old map' parsed: {parse_command('TAKE old map')}") # Ex 9 Test
print("\nTaking Old Map:")
handle_action('take', 'old map')
handle_action('inventory', None)

# Ex 13 Test: Drop the key
print("\nDropping Brass Key:")
handle_action('drop', 'brass key')
handle_action('look', None)
print("-" * 40)
'''

import json
def save_game(world_data, filename='savegame.json'):
    json_data=json.dumps(world_data, indent=4)
    with open(filename,'w') as file:
        file.write(json_data)
def load_game(filename='savegame.json'):
    with open(filename,'r') as file:
        loaded_json_data = file.read()
    LOADED_WORLD = json.loads(loaded_json_data)
    return LOADED_WORLD
def start_game_loop():
    global WORLD, CURRENT_ROOM_ID
    while True:
        command = input("\nWhat do you do? > ")
        if command.lower() == 'quit':
            print("Goodbye! Thanks for playing.") 
            break 

        verb,noun = parse_command(command)
        if verb:
            handle_action(verb, noun )
        else:
            print("Please enter a command.")

save_game(WORLD, 'savegame.json')
start_game_loop()