from typing import List, Dict
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

    # default print method
    def __str__(self):
        tiles_str = ", ".join(
            [f"{tile.color} {tile.value}" for tile in self.hand_tiles]
        )
        return f"Player: {self.name}\nTiles: {tiles_str}"
    
    # doesn't include player name in print
    def print_hand_tiles(self):
        return ", ".join(
            [f"{tile.color} {tile.value}" for tile in self.hand_tiles]
        )
    
    # convert Tile list into string list
    def create_string_list_of_board(self):
        return ["Joker" if isinstance(x, Joker) else f"{x.color} {x.value}" for x in self.hand_tiles]