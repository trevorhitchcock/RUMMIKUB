import random
from classes import Player, Tile, Joker
from typing import Dict, List

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

def place_tile(player: Player):
    print('place') # placeholder

def rearrange_board(player: Player):
    print('rearrange') # placeholder