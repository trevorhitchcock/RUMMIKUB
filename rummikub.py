import random
from typing import List, Dict

STARTING_HAND_SIZE = 14

# base class to represent a generic tile
class Tile:
    def __init__(self, color: str, value: int):
        self.color = color
        self.value = value

# subclass to represent a joker
class Joker(Tile):
    def __init__(self):
        super().__init__(color="JOKER", value=float('inf'))

class Player:
    def __init__(self, name: str, hand_tiles: List[Tile]):
        self.name = name
        self.hand_tiles = hand_tiles

    def __str__(self):
        tiles_str = ", ".join(
            [f"{tile.color} {tile.value}" for tile in self.hand_tiles]
        )
        return f"Player: {self.name}\nTiles: {tiles_str}"

def set_players() -> int:
    print("How many players would like to play? (2-4)")
    num_players = -1
    while num_players == -1:
        try:
            user_input = int(input())
            if 2 <= user_input <= 4:
                num_players = user_input
            else:
                print("Invalid input. Please enter an integer between 2 and 4.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    print(f"{num_players} players selected.")
    return num_players

def generate_draw_pile() -> Dict[str,int]:
    colors = ['Red', 'Blue', 'Yellow', 'Black']

    # in the form
    # tile_name : count remaining in draw pile
    draw_pile = {}
    
    # generate numbered tiles (1-13) for each color
    for color in colors:
        for number in range(1, 14):
            tile_name = f"{color}_{number}"
            draw_pile[tile_name] = 2 # initially 2 of each numbered tile
    
    # add jokers
    draw_pile["joker"] = 2
    
    return draw_pile

def draw_tiles(draw_pile: Dict[str,int]) -> List[str]:
    current_hand = []
    
    while len(current_hand) != STARTING_HAND_SIZE:
        # pick random tile
        random_tile = random.choice(list(draw_pile.keys()))

        # if there are any of the picked tiles left in the draw pile
        if draw_pile[random_tile] > 0:
            draw_pile[random_tile] -= 1 # subtract 1 because it has been picked
            current_hand.append(random_tile) # add to player hand
        
    return current_hand

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

def main():
    global STARTING_HAND_SIZE

    num_players = 2 #set_players()
    players = []
    draw_pile = generate_draw_pile()

    for player in range(num_players):
        # start players at 1
        player_name = str(player + 1)

        # draw tiles to player's hand
        player_tiles_str = draw_tiles(draw_pile)

        # convert generated tile names to Tile objects
        player_tiles_Tile = convert_str_to_Tile(player_tiles_str)

        # creates player and appends to player list
        players.append(Player(player_name,player_tiles_Tile))
    
    for player in players:
        print(player,'\n')

if __name__ == '__main__':
    main()