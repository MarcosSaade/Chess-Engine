from settings import *
import math


def print_move(move):
    start = list(move[0])
    end = list(move[1])

    cols = {
        0: 'a',
        1: 'b',
        2: 'c',
        3: 'd',
        4: 'e',
        5: 'f',
        6: 'g',
        7: 'h',
    }

    rows = {
        0: 8,
        1: 7,
        2: 6,
        3: 5,
        4: 4,
        5: 3,
        6: 2,
        7: 1,
    }

    start[0] = cols[start[0]]
    start[1] = rows[start[1]]

    end[0] = cols[end[0]]
    end[1] = rows[end[1]]

    start = f'{start[0]}{str(start[1])}'
    end = f'{end[0]}{str(end[1])}'

    return start, end


def generate_pieces():
    w_pieces = []
    b_pieces = []

    for i in range(8):
        w_pieces.append(('P', 'w'))
        b_pieces.append(('P', 'b'))

    w_pieces.append(('R', 'w'))
    w_pieces.append(('R', 'w'))
    w_pieces.append(('N', 'w'))
    w_pieces.append(('N', 'w'))
    w_pieces.append(('B', 'w'))
    w_pieces.append(('B', 'w'))
    w_pieces.append(('K', 'w'))
    w_pieces.append(('Q', 'w'))

    b_pieces.append(('R', 'b'))
    b_pieces.append(('R', 'b'))
    b_pieces.append(('N', 'b'))
    b_pieces.append(('N', 'b'))
    b_pieces.append(('B', 'b'))
    b_pieces.append(('B', 'b'))
    b_pieces.append(('Q', 'b'))
    b_pieces.append(('K', 'b'))

    return w_pieces, b_pieces


def mouse_to_square(mX, mY):
    sX = math.floor(mX / square_width)
    sY = math.floor(mY / square_width)

    return sX, sY


def clicked_on(square, board):
    x = square[1]
    y = square[0]

    piece = board[x][y]

    if piece.__contains__('w'):
        return 0
    elif piece.__contains__('b'):
        return 1
    else:
        return -1


def straight_obstacles(direction, start_x, start_y, end_x, end_y, target, turn, board):
    # Returns 1 for can't move, 0 for can move

    obstacle = -1

    # right
    if direction == 'r':
        available = 7 - start_y  # How many spaces in front
        distance = end_y - start_y  # How many spaces tries to travel
        for i in range(available):
            i = i + 1  # not zero
            if board[start_x][start_y + i] != '  ':
                obstacle = i  # i means how many movements until it touches an obstacle
                break
            else:
                obstacle = 7  # No obstacles on row

        #  To blank space
        if target == '  ':
            if distance > obstacle:
                return 1

        # Can't eat piece behind other piece
        if turn == 0:
            if distance > obstacle and target.__contains__('b'):
                return 1
        else:  # turn == 1
            if distance > obstacle and target.__contains__('w'):
                return 1

        # To existing piece
        if turn == 0:
            if distance >= obstacle and not target.__contains__('b'):
                return 1
        else:
            if distance >= obstacle and not target.__contains__('w'):
                return 1

    # left
    elif direction == 'l':
        available = start_y
        distance = start_y - end_y
        for i in range(available):
            i = i + 1
            if board[start_x][start_y - i] != '  ':
                obstacle = i
                break
            else:
                obstacle = 7

        if target == '  ':
            if distance > obstacle:
                return 1

        if turn == 0:
            if distance > obstacle and target.__contains__('b'):
                return 1
        else:
            if distance > obstacle and target.__contains__('w'):
                return 1

        if turn == 0:
            if distance >= obstacle and not target.__contains__('b'):
                return 1
        else:
            if distance >= obstacle and not target.__contains__('w'):
                return 1

    # up
    elif direction == 'u':
        available = start_x
        distance = start_x - end_x
        for i in range(available):
            i = i + 1
            if board[start_x - i][start_y] != '  ':
                obstacle = i
                break
            else:
                obstacle = 7

        if target == '  ':
            if distance > obstacle:
                return 1

        if turn == 0:
            if distance > obstacle and target.__contains__('b'):
                return 1
        else:
            if distance > obstacle and target.__contains__('w'):
                return 1

        if turn == 0:
            if distance >= obstacle and not target.__contains__('b'):
                return 1
        else:
            if distance >= obstacle and not target.__contains__('w'):
                return 1

    # down
    elif direction == 'd':
        available = (7 - start_x)
        distance = end_x - start_x
        for i in range(available):
            i = i + 1
            if board[start_x + i][start_y] != '  ':
                obstacle = i
                break
            else:
                obstacle = 7

        if target == '  ':
            if distance > obstacle:
                return 1

        if turn == 0:
            if distance > obstacle and target.__contains__('b'):
                return 1
        else:
            if distance > obstacle and target.__contains__('w'):
                return 1

        if turn == 0:
            if distance >= obstacle and not target.__contains__('b'):
                return 1
        else:
            if distance >= obstacle and not target.__contains__('w'):
                return 1

        return 0


def diagonal_obstacles(direction, start_x, start_y, turn, diff_x, board):
    obstacle = 8

    try:
        if direction == 'ur':
            for i in range(7):
                i = i + 1  # Start at 1, not 0

                target = (start_x - i, start_y + i)  # check diagonally for obstacles

                if target[1] < 8:
                    current_square = board[target[0]][target[1]]

                try:
                    if current_square != '  ':
                        obstacle = i
                        break
                except:
                    pass

        elif direction == 'ul':
            for i in range(7):
                i = i + 1

                target = (start_x - i, start_y - i)

                if target[1] < 8:
                    current_square = board[target[0]][target[1]]

                try:
                    if current_square != '  ':
                        obstacle = i
                        break
                except:
                    pass

        elif direction == 'dr':
            for i in range(7):
                i = i + 1

                target = (start_x + i, start_y + i)

                try:
                    if target[1] < 8:
                        current_square = board[target[0]][target[1]]
                except:
                    pass

                try:
                    if current_square != '  ':
                        obstacle = i
                        break
                except:
                    pass

        elif direction == 'dl':
            for i in range(7):
                i = i + 1

                target = (start_x + i, start_y - i)

                if target[1] < 8:
                    current_square = board[target[0]][target[1]]

                try:
                    if current_square != '  ':
                        obstacle = i
                        break
                except:
                    pass
    except:
        pass

    if turn == 0 and current_square.__contains__('w'):
        obstacle = obstacle - 1
    elif turn == 1 and current_square.__contains__('b'):
        obstacle = obstacle - 1

    if diff_x > obstacle:
        return 1  # can't move
    else:
        return 0  # can move


def castle_unobstructed_q(color, board):
    if color == 0:
        if board[7][1] == '  ' and board[7][2] == '  ' and board[7][3] == '  ':
            return True
    else:  # 1
        if board[0][1] == '  ' and board[0][2] == '  ' and board[0][3] == '  ':
            return True

    return False


def castle_unobstructed_k(color, board):
    if color == 0:
        if board[7][5] == '  ' and board[7][6]:
            return True
    else:  # 1
        if board[0][5] == '  ' and board[0][6]:
            return True

    return False


def castle_rook_q(color, board):
    if color == 0:
        board[7][0] = '  '
        board[7][3] = 'wR'
    else:  # 1
        board[0][0] = '  '
        board[0][3] = 'bR'


def castle_rook_k(color, board):
    if color == 0:
        board[7][7] = '  '
        board[7][5] = 'wR'
    else:  # 1
        board[0][7] = '  '
        board[0][5] = 'bR'


def inside_board(end):
    # Only checks for out of the board moves
    if end[0] < 0 or end[1] < 0:
        return False
    if end[0] > 7 or end[1] > 7:
        return False

    return True


def remove_duplicates(lst):
    unique = set()
    result = []
    for pair in lst:
        # Use a tuple to hash each pair
        pair_tuple = tuple(pair)
        if pair_tuple not in unique:
            result.append(pair)
            unique.add(pair_tuple)
    return result


def process_moves(moves):
    for move in moves:
        move[1] = list(move[1])

    return moves


def make_move(board, move):
    if move is None or len(move) == 1:
        return

    # move is a tuple of two tuples, representing the starting and ending position of the move
    start_pos, end_pos = ((move[0][1], move[0][0]), (move[1][1], move[1][0]))

    # Make a copy of the board so we don't modify the original
    new_board = [row[:] for row in board]

    # Move the piece from the starting position to the ending position
    new_board[end_pos[0]][end_pos[1]] = new_board[start_pos[0]][start_pos[1]]
    new_board[start_pos[0]][start_pos[1]] = '  '

    # Check if this is a castling move
    if new_board[end_pos[0]][end_pos[1]] == 'wK' and abs(start_pos[1] - end_pos[1]) == 2:
        # This is a white king castling move
        # TODO check castling rights
        if end_pos[1] > start_pos[1]:
            # This is a kingside castle
            new_board[7][5] = 'wR'  # Move the rook
            new_board[7][7] = '  '
        else:
            # This is a queenside castle
            new_board[7][3] = 'wR'  # Move the rook
            new_board[7][0] = '  '
    elif new_board[end_pos[0]][end_pos[1]] == 'bK' and abs(start_pos[1] - end_pos[1]) == 2:
        # This is a black king castling move
        if end_pos[1] > start_pos[1]:
            # This is a kingside castle
            new_board[0][5] = 'bR'  # Move the rook
            new_board[0][7] = '  '
        else:
            # This is a queenside castle
            new_board[0][3] = 'bR'  # Move the rook
            new_board[0][0] = '  '

    return new_board


def board_to_fen(board, turn):
    fen = ""
    for rank in range(8):
        empty_squares = 0
        for file in range(8):
            piece = board[rank][file]
            if piece == '  ':
                empty_squares += 1
            else:
                if empty_squares > 0:
                    fen += str(empty_squares)
                    empty_squares = 0
                if piece[0] == 'b':
                    fen += piece[1].lower()
                else:
                    fen += piece[1].upper()
        if empty_squares > 0:
            fen += str(empty_squares)
        if rank < 7:
            fen += '/'

    fen += ' '
    if turn == 0:
        fen += 'w'
    else:
        fen += 'b'

    return fen


def x0_to_move(move):
    files = 'abcdefgh'
    start, end = move
    start_col, start_row = files.index(start[0]), 8 - int(start[1])
    end_file, end_rank = files.index(end[0]), 8 - int(end[1])
    return [(start_col, start_row), (end_file, end_rank)]
