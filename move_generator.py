from functions import *


def get_moves(board, color):
    """
    Returns a list of possible moves for the white player.
    """

    moves = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j][0] == color:
                piece = board[i][j][1]

                if piece == 'N':
                    moves += knight_moves(board, color)

                elif piece == 'B':
                    moves += bishop_moves(board, color)

                elif piece == 'K':
                    moves += king_moves(board, color)

                elif piece == 'Q':
                    moves += queens_moves(board, color)

                elif piece == 'R':
                    moves += rook_moves(board, color)

                elif piece == 'P':
                    moves += pawn_moves(board, color)

    # Formats moves in order (letter, number) ->  a8, e4, etc
    updated_moves_b = [[(b, a) for a, b in inner_tup] for inner_tup in moves]
    updated_moves = remove_duplicates(updated_moves_b)

    return updated_moves


def pawn_moves(board, color):
    moves = []
    direction = -1 if color == 'w' else 1
    for i in range(8):
        for j in range(8):
            if board[i][j] == color + 'P':
                # Pawn move forward
                if board[i + direction][j] == '  ':
                    moves.append(((i, j), (i + direction, j)))
                    # Double move on first move
                    if i == 1 or i == 6:
                        if board[i + 2 * direction][j] == '  ':
                            moves.append(((i, j), (i + 2 * direction, j)))
                # Pawn capture right
                if j < 7 and board[i + direction][j + 1][0] == ('b' if color == 'w' else 'w'):
                    moves.append(((i, j), (i + direction, j + 1)))
                # Pawn capture left
                if j > 0 and board[i + direction][j - 1][0] == ('b' if color == 'w' else 'w'):
                    moves.append(((i, j), (i + direction, j - 1)))

    return moves


def knight_moves(board, color):
    """
    Finds all legal moves for knights of the given color on the board.
    """
    moves = []
    offsets = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

    for i in range(8):
        for j in range(8):
            piece = board[i][j]
            if piece.startswith(color + 'N'):
                for offset in offsets:
                    row, col = i + offset[0], j + offset[1]
                    if 0 <= row < 8 and 0 <= col < 8:
                        if board[row][col] == '  ' or board[row][col][0] != color:
                            moves.append([(i, j), (row, col)])

    return moves


def bishop_moves(board, color):
    moves = []

    for r in range(8):
        for c in range(8):
            if board[r][c][0] == color and board[r][c][1] == 'B':
                for r_offset, c_offset in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                    r_new, c_new = r + r_offset, c + c_offset
                    while 0 <= r_new < 8 and 0 <= c_new < 8:
                        if board[r_new][c_new] == '  ':
                            moves.append([(r, c), (r_new, c_new)])
                        elif board[r_new][c_new][0] != color:
                            moves.append([(r, c), (r_new, c_new)])
                            break
                        else:
                            break
                        r_new += r_offset
                        c_new += c_offset
    return moves


def rook_moves(board, color):
    moves = []
    for r in range(8):
        for c in range(8):
            if board[r][c][0] == color and board[r][c][1] == 'R':
                for r_offset, c_offset in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    r_new, c_new = r + r_offset, c + c_offset
                    while 0 <= r_new < 8 and 0 <= c_new < 8:
                        if board[r_new][c_new] == '  ':
                            moves.append([(r, c), (r_new, c_new)])
                        elif board[r_new][c_new][0] != color:
                            moves.append([(r, c), (r_new, c_new)])
                            break
                        else:
                            break
                        r_new += r_offset
                        c_new += c_offset
    return moves


def queens_moves(board, color):
    moves = []
    for r in range(8):
        for c in range(8):
            if board[r][c][0] == color and board[r][c][1] == 'Q':
                for r_offset, c_offset in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                    r_new, c_new = r + r_offset, c + c_offset
                    while 0 <= r_new < 8 and 0 <= c_new < 8:
                        if board[r_new][c_new] == '  ':
                            moves.append([(r, c), (r_new, c_new)])
                        elif board[r_new][c_new][0] != color:
                            moves.append([(r, c), (r_new, c_new)])
                            break
                        else:
                            break
                        r_new += r_offset
                        c_new += c_offset
    return moves


def king_moves(board, color):
    # Find the position of the king
    for row in range(8):
        for col in range(8):
            if board[row][col] == color + 'K':
                king_pos = (row, col)

    valid_moves = []

    # Define all possible moves for a king
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    # CASTLING
    # White
    if color == 'w':
        # Kingside
        if king_pos == (7, 4) and board[7][7] == color + 'R' and board[7][5] == '  ' and board[6][7] == '  ':
            moves.append((0, 2))

        # Queenside
        if king_pos == (7, 4) and board[7][7] == color + 'R' and board[7][3] == '  ' and board[7][2] == '  ' and board[
            7][1] == '  ':
            moves.append((0, - 2))

    # Black
    else:
        # Kingside
        if king_pos == (0, 4) and board[0][7] == color + 'R' and board[0][5] == '  ' and board[0][6] == '  ':
            moves.append((0, 2))

        # # Queenside
        # if king_pos == (0, 4) and board[0][0] == color + 'R' and board[0][3] == '  ' and board[0][2] == '  ' and board[
        #     0][1] == '  ':
        #     moves.append((0, - 2))

    # Check if each possible move is valid
    for move in moves:
        row, col = king_pos[0] + move[0], king_pos[1] + move[1]
        if row < 0 or col < 0 or row >= 8 or col >= 8:
            continue
        if board[row][col] == '  ' or board[row][col][0] != color:
            valid_moves.append((king_pos, (row, col)))

    return valid_moves


###


def order_moves(board, moves):
    captures = []

    pieces_to_center = []
    central_pawns = []
    near_center = []

    checks = []
    threats = []

    quiet = []

    # Define center squares
    center_squares = [(3, 3), (3, 4), (4, 3), (4, 4)]

    for move in moves:
        start = move[0]
        if board[start[1]][start[0]] == '  ':
            continue
        end = move[1]
        end_piece = board[end[1]][end[0]]
        if end_piece != '  ':
            captures.append(move)
            # elif is_check(move, board, color):
            #     checks.append(move)
            # elif is_threat(move, board, color):
            threats.append(move)
        else:
            piece = board[start[1]][start[0]]

            # Knights to advanced squares
            if piece in ['wN', 'bN'] and end[0] in [2, 3, 4, 5]:
                pieces_to_center.append(move)

            # Knight to center
            elif piece in ['wN', 'bN'] and end in center_squares:
                pieces_to_center.append(move)

            # Other pieces to center
            elif piece in ['wB', 'wQ', 'bB', 'bQ'] and end in center_squares:
                pieces_to_center.append(move)

            # Pieces near center
            elif piece not in ['wP', 'wR', 'wK', 'bP', 'bR', 'bK'] and start[0] in [2, 3, 4, 5]:
                near_center.append(move)

            # Pawns to center
            elif piece in ['wP', 'bP'] and end in center_squares:
                central_pawns.append(move)

            # d3. e3.
            elif piece == 'wP' and start[0] in [3, 4] and end[1] in [4, 5]:
                central_pawns.append(move)

            # d7. e7.
            elif piece == 'bP' and start[0] in [3, 4] and end[1] in [2, 3]:
                central_pawns.append(move)

            # C and F pawns
            elif piece in ['wP', 'bP'] and start[0] in [2, 5]:
                near_center.append(move)

            else:
                quiet.append(move)

    ordered_moves = captures + checks + threats + pieces_to_center + central_pawns + near_center + quiet

    return ordered_moves
