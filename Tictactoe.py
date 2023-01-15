
class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol



def tictactoe():
    player1name = input("Player 1 name: ")
    x_or_o_first_player = input(f"{player1name}, witch symbol do you chose? ('X' or 'O'): ").upper()

    if x_or_o_first_player == 'X' or x_or_o_first_player == 'O':
        print(f"{player1name}, you've chosen '{x_or_o_first_player}'\n")
    else:
        print("Invalid symbol")
        return

    player_1 = Player(player1name, x_or_o_first_player)


    player2name = input("Player 2 name: ")

    def symbol_assignment():
        if x_or_o_first_player == 'X':
            return 'O'
        elif x_or_o_first_player == 'O':
            return 'X'

    x_or_o_second_player = symbol_assignment().upper()
    print(f"{player2name}, you've been assigned '{x_or_o_second_player}'\n")

    player_2 = Player(player2name, x_or_o_second_player)

    grid_lib = {'1': 'NICE',
                '2': ' ',
                '3': ' ',
                '4': ' ',
                '5': ' ',
                '6': ' ',
                '7': ' ',
                '8': ' ',
                '9': ' '
                }

    used_spaces_list = []

    def placing_mark(witch_player):
        symbol = witch_player.symbol
        name = witch_player.name

        while True:

            inp = input(f"{name} pls select your position (1-9):")


            if inp in used_spaces_list:
                print('occupied field')
                continue


            if 1 <= int(inp) <= 9:
                used_spaces_list.append(inp)
                grid_lib[inp] = symbol
                print(f"| {grid_lib['1']} | {grid_lib['2']} | {grid_lib['3']} |\n-------------\n"
                      f"| {grid_lib['4']} | {grid_lib['5']} | {grid_lib['6']} |\n-------------\n"
                      f"| {grid_lib['7']} | {grid_lib['8']} | {grid_lib['9']} |")
                return False

            else:
                print("invalid placement")
                continue



    def grid_check(player):
        if grid_lib['1'] == grid_lib['2'] == grid_lib['3'] == player.symbol \
                or grid_lib['4'] == grid_lib['5'] == grid_lib['6'] == player.symbol \
                or grid_lib['7'] == grid_lib['8'] == grid_lib['9'] == player.symbol \
                or grid_lib['1'] == grid_lib['4'] == grid_lib['7'] == player.symbol \
                or grid_lib['2'] == grid_lib['5'] == grid_lib['8'] == player.symbol \
                or grid_lib['3'] == grid_lib['6'] == grid_lib['9'] == player.symbol \
                or grid_lib['1'] == grid_lib['5'] == grid_lib['9'] == player.symbol \
                or grid_lib['3'] == grid_lib['5'] == grid_lib['7'] == player.symbol:
            print(f"{player.name}, You won!")
            return True

    run = True
    turn_count = 0
    while run:

        
        placing_mark(player_1)
        player_one_win = grid_check(player_1)
        turn_count += 1

        if player_one_win is True:
            break

        if turn_count == 9:
            print("\nIt's a draw!")
            return False

        placing_mark(player_2)
        player_two_win = grid_check(player_2)
        turn_count += 1

        if player_two_win is True:
            break


def game():
    while True:
        start = input("Would you like to play a new game? y/n: ")

        if start == 'y':
            tictactoe()
        if start == 'n':
            quit()
        else:
            continue



game()





