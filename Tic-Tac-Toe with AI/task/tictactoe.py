# write your code here
import random


def board_from_string(input_: str):
    board_string = input_
    board_list = [x for x in board_string]
    board_list = [board_list[i:i + 3] for i in range(0, len(board_list), 3)]
    return board_list


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


def take_move(board, player):
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
                    insert_move(board, input_, player)
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
    win = get_winning(anti_diagonal)  # checks if theres win in anti diagonal
    win_board.append(win) if win is not None else None  # appends win board if theres win
    # print('win obard',win_board) # DEBUG:prints win board
    win_state = False  # holds state of win [DRAW,X WINS,O WINS]
    if len(win_board) != 0:
        if win_board.count('X') == win_board.count('O'):  # checks if same both sides has same wins
            win_state = 'Draw'  #
        elif win_board.count('X') > win_board.count('O'):  # checks if x has more wins than o
            win_state = 'X wins'
        elif win_board.count('X') < win_board.count('O'):  # checks if o has more wins than x
            win_state = 'O wins'
    # saves state of game its absolute of dif of count x and o in input
    state = abs([x for x in input_].count('X') - [x for x in input_].count('O'))
    # print('state:',state)  #  Debug
    c = [x for x in input_].count(' ')
    # print('c:',c,c <= 1 and len(win_board)==0)  #  Debug
    if c == 0 and len(win_board) == 0:
        win_state = 'Draw'

    return win_state


def check_witch_player(board_string: str):
    if board_string.count('O') == board_string.count('X'):
        return 'X'
    else:
        return 'O'


def get_win_pos(board, player):
    """Returns list of possible wins for player"""
    for i in range(3):
        # checks horizontal lines
        horizontal_line = ''.join(board[i])
        if player * 2 + ' ' == horizontal_line:  # last left
            return i, 2
        if ' ' + player * 2 == ''.join(board[i]):  # right
            return i, 0
        if player + ' ' + player == ''.join(board[i]):  # middle
            return i, 1
        # checks vertical lines
        vertical_line = ([board[0][i], board[1][i], board[2][i]])
        if player * 2 + ' ' == ''.join(vertical_line):  # down
            return 2, i
        if ' ' + player * 2 == ''.join(vertical_line):  # top
            return 0, i
        if player + ' ' + player == ''.join(vertical_line):  # middle
            return 1, i
    else:
        # checks diagonal lines
        main_diag = [board[0][0], board[1][1], board[2][2]]
        if player * 2 + ' ' == ''.join(main_diag):
            return 2, 2
        if ' ' + player * 2 == ''.join(main_diag):
            return 0, 0
        if player + ' ' + player == ''.join(main_diag):  # middle
            return 1, 1
        anti_diag = [board[2][0], board[1][1], board[0][2]]
        if player * 2 + ' ' == ''.join(anti_diag):
            return 0, 2
        if ' ' + player * 2 == ''.join(anti_diag):
            return 2, 0
        if player + ' ' + player == ''.join(anti_diag):  # middle
            return 1, 1
        return False


def minimax(board, depth, isMaximizing, player):
    opponent = 'X' if player == 'O' else 'O'
    win_state = check_state(board)
    if win_state:
        win_state = 'X' if win_state.find('X') else 'O' if win_state.find('O') else 'D'
        if win_state == 'X':
            return 1
        elif win_state == 'O':
            return -1
        elif win_state == 'D':
            return 0

    if isMaximizing:
        best_score = -800
        for row_id, row in enumerate(board):
            for el_id, el in enumerate(row):
                if el == '' or el == ' ':
                    board[row_id][el_id] = player
                    score = minimax(board, depth + 1, False, opponent)
                    board[row_id][el_id] = ' '
                    if score > best_score:
                        best_score = score
        return best_score

    else:
        best_score = 800
        for row_id, row in enumerate(board):
            for el_id, el in enumerate(row):
                if el == '' or el == ' ':
                    board[row_id][el_id] = opponent
                    score = minimax(board, depth + 1, True,player)
                    board[row_id][el_id] = ' '
                    if score < best_score:
                        best_score = score
        return best_score


def hard_move(board, player):
    """Makes hard computer move using minimax algorith to choose"""
    print('Making move level "Hard"')
    opponent = 'X' if player == 'O' else 'O'
    best_score = -800
    best_move = (0, 0)
    for row_id, row in enumerate(board):
        for el_id, el in enumerate(row):
            if el == '' or el == ' ':
                board[row_id][el_id] = player
                score = minimax(board, 0, False, player)
                board[row_id][el_id] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (row_id, el_id)
    if best_move == 0:
        easy_move(board,player,True)
    else:
        insert_move(board, best_move, player)


def medium_move(board, player, silent=False):
    """
    Makes medium dificulty move.
    Only checks if player or opponent has winning position
    If no one has uses easy move func
    """
    if not silent: #
        print('Making move level "Medium"')
    opponent = 'X' if player == 'O' else 'O'  # defines opponent
    win_pos = get_win_pos(board, player)  # generates winning positions for player
    opponent_win_pos = get_win_pos(board, opponent)  # generates winning positions for opponent
    if win_pos:  # if player has winning pos
        insert_move(board, win_pos, player)  # insert move
    elif opponent_win_pos:    # if opponent has winning move
        insert_move(board, opponent_win_pos, player)  # insert move
    else:
        easy_move(board, player, silent=True)  # use easy_move


def easy_move(board, player, silent=False):
    """
    Makes easy move only by randomly choosing free field on board
    """
    if not silent:
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
    """
    Takes from user proper start command
    :return:
    """
    LEVELS = ('user', 'easy', 'medium','hard')
    while True:
        input_ = input('Input command:').split()
        if input_[0] in ['start', 'exit']:
            if input_[0] == 'exit':
                return False
            else:
                if len(input_) == 3:
                    if (input_[1] in LEVELS) and (input_[2] in LEVELS):
                        return (input_[1], input_[2])
        print('Bad parameters!')



def game():
    """
    Main game loop
    """
    board = gen_board(' ')
    start_command = get_start_command()
    # start_command = ('hard', 'hard')  # DEBUG
    if start_command:
        players = [None, None]
        for pos, comm in enumerate(start_command):
            if comm == 'easy':
                players[pos] = easy_move
            elif comm == 'medium':
                players[pos] = medium_move
            elif comm == 'hard':
                players[pos] = hard_move
            elif comm == 'user':
                players[pos] = take_move

        print_board(board)
        while True:
            for x, player in enumerate(players):
                figure = 'X' if x == 0 else 'O'
                player(board, figure)
                print_board(board)
                win_state = check_state(board)
                if win_state:
                    break
            if win_state:
                break
        print(win_state)








if __name__ == '__main__':
    game()
