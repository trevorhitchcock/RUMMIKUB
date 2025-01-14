import random
from classes import Player, Tile, Joker
from typing import Dict, List, Any

def draw_tiles(draw_pile: Dict[str,int], num_to_draw: int) -> List[str]:
    current_hand = []
    
    while len(current_hand) != num_to_draw:
        # pick random tile
        random_tile = random.choice(list(draw_pile.keys()))

        # if there are any of the picked tiles left in the draw pile
        if draw_pile[random_tile] > 0:
            draw_pile[random_tile] -= 1 # subtract 1 because it has been picked
            current_hand.append(random_tile) # add to player hand
        
        # convert list of strings to list of Tile's
    return convert_str_to_Tile(current_hand)

def convert_str_to_Tile(player_tiles_str: str) -> List[Tile]:
    player_tiles_Tile = []

    for tile in player_tiles_str:
        if tile == 'joker':
            player_tiles_Tile.append(Joker())
        else:
            arr = tile.split('_')
            color = arr[0]
            value = int(arr[1])
            player_tiles_Tile.append(Tile(color,value,))
    return player_tiles_Tile

def place_tile(player: Player, inflect_engine: Any):
    """
    Handles placing a tile for a player.

    Parameters:
    - player (Player): The player taking their turn.
    - inflect_engine (Any): The inflect engine used for ordinal formatting.
    """
    print("1. Place tiles on board")
    print("2. Place tiles from hand")

    move = -1
    while move not in [1,2]:
        try:
            user_input = int(input("Enter 1 or 2: "))
            if user_input in [1, 2]:
                move = user_input
                if move == 1:
                    print(f"\nPlayer {player.name} is placing tiles on the board")
                else:
                    print(f"\nPlayer {player.name} is placing tiles from their hand.")
                    place_tiles_from_hand(player, inflect_engine)
            else:
                print("Invalid input. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def place_tiles_from_hand(player: Player, inflect_engine: Any):
    #print(f"Here is your board: {player.print_hand_tiles()}")
    i = 1 # for printing purposes
    move_array = []
    
    while True:
        tile_picked = input("Enter the name of the tile to play (done to stop): ").capitalize()
        if(tile_picked == 'done'):
            # CHECK IF VALID MOVE HERE
            break
        # check if tile is in user's board
        
        str_array_of_hand = player.create_string_list_of_board()
        if tile_picked not in str_array_of_hand:
            print("You don't have that tile. Try again.")
        else: # tile was found in hand
            move_array.append(tile_picked)
        print(f"Your {inflect_engine.ordinal(i)} tile is {tile_picked}")
        i += 1


def place_tiles_on_board(player: Player):
    print('place tiles on board')

def rearrange_board(player: Player):
    print('rearrange') # placeholder