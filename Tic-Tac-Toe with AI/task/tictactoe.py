# write your code here
import random


def board_from_string(input_: str):
    board_string = input_
    board_list = [x for x in board_string]
    board_list = [board_list[i:i + 3] for i in range(0, len(board_list), 3)]
    return board_list


# write your code here

def gen_board(placeholder_char='-'):
    '''Returns matrix[3][3] with placeholder - as empty field'''
    board = [[placeholder_char for i in range(3)] for j in range(3)]
    return board


def print_board(board):
    """Prints board"""
    print('---------')
    for el in board:
        print('| ' + ' '.join(el) + ' |')
    print('---------')


def take_move(board,player):
    'Takes input validate it and return as list of pos'
    while True:
        input_ = input('Enter the coordinates:')
        input_ = input_.split()
        if input_[0].isdigit() and input_[1].isdigit():  # checks if contains 2 digits
            input_ = [int(x) - 1 for x in input_]
            if all([x in range(3) for x in input_]):  # checks if inputet ints in board range
                if ('X' in board[input_[0]][input_[1]]) or (
                        "O" in board[input_[0]][input_[1]]):  # checks if field is ocupied
                    print("This cell is occupied! Choose another one!")
                else:  # if not failed before return input
                    insert_move(board,input_,player)
                    return None
            else:
                print('Coordinates should be from 1 to 3!')
        else:
            print('You should enter numbers!')


def insert_move(board, pos, identyfier):
    """Inserts in :pos in :board ;identifier"""
    board[pos[0]][pos[1]] = identyfier


def check_state(board):
    win_board = []
    input_ = ''.join([y for x in board for y in x])
    def get_winning(el):
        """Takes el as list and count if """
        if el.count('X') == 3:
            return 'X'
        if el.count('O') == 3:
            return 'O'

    for pos, el in enumerate(board):
        win = get_winning(el)  # checks if theres win in line
        win_board.append(win) if win is not None else None  # appends win board if theres win
        column = [row[pos] for row in board]  # gens column
        win = get_winning(column)  # checks if theres win in column
        win_board.append(win) if win is not None else None  # appends win board if theres win
    main_diagonal = [board[0][0], board[1][1], board[2][2]]  # gens main diagonal
    win = get_winning(main_diagonal)  # checks if theres win in main diagonal
    win_board.append(win) if win is not None else None  # appends win board if theres win
    anti_diagonal = [board[2][0], board[1][1], board[0][2]]  # gens anti diagonal
    win = get_winning(anti_diagonal)# checks if theres win in anti diagonal
    win_board.append(win) if win is not None else None # appends win board if theres win
    # print('win obard',win_board) # DEBUG:prints win board
    win_state = False # holds state of win [DRAW,X WINS,O WINS]
    if len(win_board)!=0:
        if win_board.count('X') == win_board.count('O'):  # checks if same both sides has same wins
            win_state = False #
        elif win_board.count('X') > win_board.count('O'): # checks if x has more wins than o
            win_state = 'X wins'
        elif win_board.count('X') < win_board.count('O'):# checks if o has more wins than x
            win_state = 'O wins'
    # saves state of game its absolute of dif of count x and o in input
    state = abs([x for x in input_].count('X') - [x for x in input_].count('O'))
    # print('state:',state)  #  Debug
    c = [x for x in input_].count('_')
    # print('c:',c,c <= 1 and len(win_board)==0)  #  Debug
    if c == 0 and len(win_board)==0:
        win_state = False

    return win_state


def check_witch_player(board_string: str):
    if board_string.count('O') == board_string.count('X'):
        return 'X'
    else:
        return 'O'


def game():
    board = gen_board()

    while True:
        tokens = ['X', 'O']
        for el in tokens:
            print_board(board)
            next_move = take_move()
            insert_move(board, next_move, el)
            win_state = check_state(board)
            if win_state:
                print_board(board)
                print(win_state)
                break
        if win_state:
            break

def medium_move(board, player):
    print('Making move level "medium"')
    while True:
            break


def easy_move(board, player):
    print('Making move level "easy"')
    while True:
        move = (random.randint(0, 2), random.randint(0, 2))
        if ('X' in board[move[0]][move[1]]) or (
                'O' in board[move[0]][move[1]]):  # checks if field is occupied
            pass
        else:
            insert_move(board, move, player)
            break

def get_start_command():
    LEVELS = ('user','easy')
    while True:
        input_ = input('Input command:').split()
        if input_[0] in ['start', 'exit']:
            if input_[0] == 'exit':
                return False
            else:
                if len(input_) == 3:
                    if (input_[1] in LEVELS) and (input_[2] in LEVELS):
                        return (input_[1],input_[2])
        print('Bad parameters!')
def stage_3():
    board = gen_board(' ')
    start_command = get_start_command()
    if start_command:
        # start_command = ('easy','easy')
        players = [None,None]
        players[0] = take_move if start_command[0] == 'user' else easy_move
        players[1] = take_move if start_command[1] == 'user' else easy_move
        print_board(board)
        while True:
            for x, player in enumerate(players):
                figure = 'X' if x == 0 else 'O'
                player(board,figure)
                print_board(board)
                win_state = check_state(board)
                if win_state:
                    break
            if win_state:
                break
        print(win_state)


def stage_4():
    pass


def stage_2():
    board = gen_board(' ')
    player = ('X', 'O', ' ')
    while True:
        print_board(board)
        move = take_move(board)  # player turn
        insert_move(board, move, player[0])  # insert player move
        print_board(board)
        win_state = check_state(board, player)
        if win_state:
            break
        easy_move(board, player)
        win_state = check_state(board, player)
        if win_state:
            break
    print(win_state)


def test():
    board = gen_board()
    """Test function"""
    moves = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 2], [3, 1]]
    moves = [[el[0] - 1, el[1] - 1] for el in moves]
    for pos, el in enumerate(moves):
        if pos % 2 == 0:
            insert_move(board, el, 'X')
        else:
            insert_move(board, el, 'O')
        print_board(board)


def stage_1():
    board_string = input('Enter the cells:')
    # board_string = '_XO_OX___'  # DEBUG
    player = check_witch_player(board_string)
    print(f'Enter the cells: > {board_string}')
    board = board_from_string(board_string)
    print_board(board)
    coords = take_move(board)
    insert_move(board, coords, player)
    print_board(board)
    state = check_state(board)
    if state:
        print(state)
    else:
        print('Game not finished')


if __name__ == '__main__':
    stage_4()
