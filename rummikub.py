import inflect

from typing import List, Dict

from classes import Player, Tile, Joker, Board
from game_functions import draw_tiles, place_tile, rearrange_board

STARTING_HAND_SIZE = 14


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


def main():
    global STARTING_HAND_SIZE

    num_players = 1 #set_players()
    players = []
    draw_pile = generate_draw_pile()

    for player in range(num_players):
        # start players at 1
        player_name = str(player + 1)

        # draw tiles to player's hand (14 to start the game)
        player_tiles_str = draw_tiles(draw_pile, num_to_draw = STARTING_HAND_SIZE)

        # creates player and appends to player list
        players.append(Player(player_name,player_tiles_str))
    
    # print boards
    for player in players:
        print(player,'\n')

    # create inflect engine here to save memory
    # used for ordinal formatting
    inflect_engine = inflect.engine()

    # create game board
    board = Board([])

    # main game loop
    while True:
        for player in players:

            print(f"It is player {player.name}'s turn.")
            print(f"Here is player {player.name}'s board: {player.print_hand_tiles()}")
            move = input("Enter a move (draw, place, rearrange): ")
            while move not in ['draw', 'place', 'rearrange']:
                move = input("Try again:")
            
            match move:
                case 'draw':
                    print("Drawing a tile...")
                    # appends drawn tile into hand tiles
                    player.hand_tiles += draw_tiles(draw_pile, num_to_draw = 1)
                    print(player.print_hand_tiles())
                case 'place':
                    place_tile(board, player, inflect_engine)
                case 'rearrange':
                    rearrange_board(player)
        break

if __name__ == '__main__':
    main()