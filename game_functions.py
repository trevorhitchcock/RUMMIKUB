import random
import copy
from classes import Player, Tile, Joker, Board
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

def place_tile(board: Board, player: Player, inflect_engine: Any):
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
                    place_tiles_from_hand(board, player, inflect_engine)
            else:
                print("Invalid input. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def place_tiles_from_hand(board: Board, player: Player, inflect_engine: Any):
    #print(f"Here is your board: {player.print_hand_tiles()}")
    i = 1 # for printing purposes
    current_set = []

    temp_board = copy.deepcopy(board) # modify and validate move using temporary board
    
    while True:
        tile_picked = input("Enter the name of the tile to play (done to stop): ").capitalize()
        if(tile_picked == 'Done'):
            temp_board.add_set_to_board(current_set)
            print(f'Checking board:\n{temp_board}')
            # CHECK IF BOARD VALID HERE
            if(temp_board.valid_board):
                print("valid move")
                board = copy.deepcopy(temp_board)
                return board
            break

        # check if tile is in user's hand
        str_array_of_hand = player.create_string_list_of_hand()

        if tile_picked not in str_array_of_hand:
            print("You don't have that tile. Try again.")
        else: # tile was found in hand
            # BUGGY; MUST TEST
            str_array_of_hand.remove(tile_picked )# remove it from hand so same tile can't be played twice
            current_set.append(tile_picked) # add it to current move array
            print(f"Your {inflect_engine.ordinal(i)} tile is {tile_picked}.\n")
            i += 1


def place_tiles_on_board(player: Player):
    print('place tiles on board')

def rearrange_board(player: Player):
    print('rearrange') # placeholder