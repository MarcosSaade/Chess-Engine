import pygame
import random
import pickle
from move_generator import *
from functions import *
from openings import *


# TODO AI and human format moves

class Main:
    def __init__(self):
        self.board = Board()
        self.mover = Mover()
        self.ai = AI()

        self.w_props, self.b_props = generate_pieces()  # List with name, colour of all pieces
        self.w_pieces, self.b_pieces = [], []  # Lists with Piece objects

        self.w_ids = []  # List with Ids -> (W0, W1, ..., W16)
        self.b_ids = []  # (B0, ..., B16)

        self.ai_turn = 1

    def start(self):
        self.board.generate_board()
        self.board.represent_pieces()

        if self.ai_turn == 0:
            self.ai.move('w')

        for i in self.w_props:
            self.w_pieces.append(Piece(i[0], i[1]))

        for i in self.b_props:
            self.b_pieces.append(Piece(i[0], i[1]))

    def update(self):
        self.board.draw()
        self.board.gui_pieces()
        self.mover.check_move()


class Board:
    def __init__(self):
        self.tile_size = WIDTH / 8
        self.tiles = []

        self.w_pawn = pygame.image.load('data/img/wP.png').convert_alpha()
        self.w_rook = pygame.image.load('data/img/wR.png').convert_alpha()
        self.w_knight = pygame.image.load('data/img/wN.png').convert_alpha()
        self.w_bishop = pygame.image.load('data/img/wB.png').convert_alpha()
        self.w_queen = pygame.image.load('data/img/wQ.png').convert_alpha()
        self.w_king = pygame.image.load('data/img/wK.png').convert_alpha()

        self.b_pawn = pygame.image.load('data/img/bP.png').convert_alpha()
        self.b_rook = pygame.image.load('data/img/bR.png').convert_alpha()
        self.b_knight = pygame.image.load('data/img/bN.png').convert_alpha()
        self.b_bishop = pygame.image.load('data/img/bB.png').convert_alpha()
        self.b_queen = pygame.image.load('data/img/bQ.png').convert_alpha()
        self.b_king = pygame.image.load('data/img/bK.png').convert_alpha()

        self.row0 = []
        self.row1 = []
        self.row2 = []
        self.row3 = []
        self.row4 = []
        self.row5 = []
        self.row6 = []
        self.row7 = []

        self.rows = [self.row0, self.row1, self.row2, self.row3, self.row4, self.row5, self.row6, self.row7]

        self.can_castle_k = [True, True]  # W, B
        self.can_castle_q = [True, True]  # W, B

        # tablero
        self.gameboard = \
            [
                ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
                ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
                ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
                ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
            ]

        self.ggameboard = \
            [
                ['bR', '  ', '  ', '  ', 'bK', '  ', '  ', 'bR'],
                ['bP', '  ', '  ', '  ', '  ', '  ', '  ', 'bP'],
                ['wP', '  ', '  ', '  ', '  ', '  ', '  ', 'wP'],
                ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
                ['wR', '  ', '  ', '  ', 'wK', '  ', '  ', 'wR'],
            ]

    def generate_board(self):
        for i in range(8):
            for j in range(8):
                self.tiles.append(
                    pygame.rect.Rect(self.tile_size * i, self.tile_size * j, self.tile_size, self.tile_size))

    def draw(self):
        count = 1
        zebra = 1
        for index, i in enumerate(self.tiles):
            if index % 2 == 1:
                if zebra == 1:
                    color = COLOR_1
                else:
                    color = COLOR_2
            else:
                if zebra == 1:
                    color = COLOR_2
                else:
                    color = COLOR_1
            pygame.draw.rect(screen, color, i)
            if count == 8:
                zebra = zebra * -1
                count = 1
            else:
                count += 1

    def represent_pieces(self):
        # Delete past piece representation
        for i in range(8):
            self.rows[i] = []

        # Create new piece representation
        for col in range(8):
            for row in range(8):
                current_row = self.rows[row]
                current_piece = main.board.gameboard[row][col]
                if current_piece.__contains__('w'):
                    current_row.append(((0 + (col * WIDTH / 8), 0 + (row * HEIGHT / 8) + 5), current_piece))
                elif current_piece.__contains__('b'):
                    current_row.append(((0 + (col * WIDTH / 8), 0 + (row * HEIGHT / 8) + 5), current_piece))

    def gui_pieces(self):
        # Draw pieces from representation map
        for i in range(8):
            current_row = self.rows[i]  # different from variable above
            for j in range(len(current_row)):
                current_piece = current_row[j][1]
                if current_piece.__contains__('w'):
                    if current_piece.__contains__('P'):
                        screen.blit(self.w_pawn, (current_row[j][0]))
                    elif current_piece.__contains__('R'):
                        screen.blit(self.w_rook, (current_row[j][0]))
                    elif current_piece.__contains__('N'):
                        screen.blit(self.w_knight, (current_row[j][0]))
                    elif current_piece.__contains__('B'):
                        screen.blit(self.w_bishop, (current_row[j][0]))
                    elif current_piece.__contains__('Q'):
                        screen.blit(self.w_queen, (current_row[j][0]))
                    elif current_piece.__contains__('K'):
                        screen.blit(self.w_king, (current_row[j][0]))
                elif current_piece.__contains__('b'):
                    if current_piece.__contains__('P'):
                        screen.blit(self.b_pawn, (current_row[j][0]))
                    elif current_piece.__contains__('R'):
                        screen.blit(self.b_rook, (current_row[j][0]))
                    elif current_piece.__contains__('N'):
                        screen.blit(self.b_knight, (current_row[j][0]))
                    elif current_piece.__contains__('B'):
                        screen.blit(self.b_bishop, (current_row[j][0]))
                    elif current_piece.__contains__('Q'):
                        screen.blit(self.b_queen, (current_row[j][0]))
                    elif current_piece.__contains__('K'):
                        screen.blit(self.b_king, (current_row[j][0]))


class AI:
    def __init__(self):
        # Retrieve memory
        with open('best_moves.pickle', 'rb') as f:
            self.previous_finds = pickle.load(f)

        self.castled = [False, False]

    def move(self, color):
        fen = board_to_fen(main.board.gameboard, color)

        # Opening book
        if fen in opening_moves:
            move = opening_moves[fen][0]

        # Memory of previously found best moves
        elif fen in self.previous_finds:
            move = self.previous_finds[fen]

        # Minimax search
        else:
            move = self.find_best_move(color)

        # Checkmate
        if move is None:
            return

        main.board.gameboard = make_move(main.board.gameboard, move)

        main.board.represent_pieces()

        if color == 0:
            main.mover.turn = 1
        else:
            main.mover.turn = 0

    def find_best_move(self, color):
        ch = self.minimax(main.board.gameboard, 2, False, color)

        if ch[0] > 1000:
            print('Checkmate')
            return None

        minimax = self.minimax(main.board.gameboard, 4, False, color)
        best_move = minimax[1]
        print(print_move(best_move), minimax[0])

        # Add the move that was found to memory
        self.previous_finds[board_to_fen(main.board.gameboard, color)] = best_move

        # Save the dictionary to a file using pickle
        with open("best_moves.pickle", "wb") as f:
            pickle.dump(self.previous_finds, f)

        return best_move

    def minimax(self, board, depth, is_maximizing, color, alpha=-math.inf, beta=math.inf):
        best_move = None

        if depth == 0:  # or is game over
            return self.static_eval(board), None

        if is_maximizing:
            best_score = -math.inf

            next_color = 'w' if color == 'b' else 'b'

            possible_moves = get_moves(board, color)

            # Search at original depth - 1, then do a last search only for captures
            # if depth == 1:
            #     possible_moves = self.filter_captures(board, possible_moves)
            #
            #     if len(possible_moves) == 0:
            #         return self.static_eval(board), None

            ordered_moves = order_moves(board, possible_moves)

            for move in ordered_moves:
                # Removes invalid moves
                start = move[0]
                if main.board.gameboard[start[1]][start[0]] == '  ':
                    continue

                new_board = make_move(board, move)

                minimax = self.minimax(new_board, depth - 1, False, next_color, alpha, beta)

                score = minimax[0]

                if score > best_score:
                    best_score = score
                    best_move = move

                alpha = max(alpha, best_score)

                if beta <= alpha:
                    break

            return best_score, best_move

        else:
            best_score = math.inf

            next_color = 'w' if color == 'b' else 'b'

            possible_moves = get_moves(board, color)

            if depth == 1:
                possible_moves = self.filter_captures(board, possible_moves)

                if len(possible_moves) == 0:
                    return self.static_eval(board), None

            ordered_moves = order_moves(board, possible_moves)

            for move in ordered_moves:
                # Removes invalid moves
                start = move[0]
                if main.board.gameboard[start[1]][start[0]] == '  ':
                    continue

                new_board = make_move(board, move)

                minimax = self.minimax(new_board, depth - 1, True, next_color, alpha, beta)

                score = minimax[0]

                if score < best_score:
                    best_score = score
                    best_move = move

                beta = min(beta, best_score)

                if beta <= alpha:
                    break

            return best_score, best_move

    def filter_captures(self, board, moves):
        captures = []
        for move in moves:
            start = move[0]
            if board[start[1]][start[0]] == '  ':
                continue
            end = move[1]
            end_piece = board[end[1]][end[0]]
            if end_piece != '  ':
                captures.append(move)
        return captures

    def static_eval(self, board):
        # TODO add king safety

        piece_values = {'P': 1, 'N': 3, 'B': 3.3, 'R': 5, 'Q': 9, 'K': 1000}

        score = 2000

        # CASTLING

        # White
        if not self.castled[0]:
            if board[7][6] == 'wK' and board[7][5] == 'wR':
                self.castled[0] = True
            if board[7][2] == 'wK' and board[7][3] == 'wR':
                self.castled[0] = True
        else:
            score += 0.5

        # Black
        if not self.castled[1]:
            if board[0][6] == 'bK' and board[0][5] == 'bR':
                self.castled[1] = True
            if board[0][2] == 'bK' and board[0][3] == 'bR':
                self.castled[1] = True
        else:
            score -= 0.5

        for row in range(len(board)):
            for col in range(len(board[row])):
                piece = board[row][col]
                if piece == '  ':
                    continue  # Empty square

                value = piece_values[piece[1]]  # Get the value of the piece

                # WHITE
                if piece[0] == 'w':

                    # MATERIAL
                    score += value * 2

                    # PAWN STRUCTURE
                    if piece == 'wP':
                        # Isolated pawn
                        if (col == 0 or board[row][col - 1] == '  ') and (col == 7 or board[row][col + 1] == '  '):
                            score -= 0.1
                        # Doubled pawn
                        if row > 0 and board[row - 1][col] == 'wP':
                            score -= 0.1
                        # Passed pawn
                        passed = True
                        for r in range(row + 1, 8):
                            if board[r][col] != '  ':
                                passed = False
                                break
                        if passed:
                            score += 0.5

                        # Promotion understanding
                        if col == 7:
                            score += 9

                    # PIECE DEVELOPMENT
                    if piece != 'wP':
                        # col 0 = 0 points
                        if col == 1:
                            score += 0.05
                        elif col == 2:
                            score += 0.1
                        elif col == 3:
                            score += 0.2
                        elif col == 4:
                            score += 0.3
                        elif col == 5:
                            score += 0.4
                        elif col == 6:
                            score += 0.2
                        # col 7 = 0 points

                    # Center incentive for Knights
                    if piece == 'wN' and (row in [2, 3, 4, 5]) and (col in [2, 3, 4, 5]):
                        score += 0.05

                    # Big diagonal incentive
                    if piece == 'wB' and row == col:
                        score += 0.05

                    # ROOKS IN OPEN FILES
                    if piece == 'wR':
                        # check if the rook is in an open file (no pawns of either color in front)
                        open_file = True
                        for r in range(8):
                            if board[r][col] != '  ' and board[r][col][0] == 'wP':
                                open_file = False
                                break
                        if open_file:
                            score += 0.4

                    # DOUBLED ROOKS IN OPEN FILES
                    if piece == 'wR':
                        # check if there is another white rook in the same file
                        doubled_rook = False
                        for r in range(row + 1, 8):
                            if board[r][col] in ['wR', 'wQ']:
                                doubled_rook = True
                                break
                        if doubled_rook:
                            score += 0.1  # doubled rooks give 0.4 + 0.4 + 0.1 + 0.1 = 1

                    # PAWN CENTER
                    # Central pawns
                    if piece == 'wP' and col in [3, 4] and row in [3, 4]:
                        score += 0.2
                    # C and F pawns
                    if piece == 'wP' and col in [2, 5] and row in [2, 3, 4]:
                        score += 0.1

                    if piece == 'wK':
                        # Check for attacks on the king
                        if (row < 6 and col > 0 and board[row + 1][col - 1] == 'bP') or \
                                (row < 6 and col < 7 and board[row + 1][col + 1] == 'bP'):
                            score -= 0.3  # Penalty
                        if (row < 7 and board[row + 1][col] == 'bQ') or \
                                (row < 7 and col < 7 and board[row + 1][col + 1] == 'bB') or \
                                (row < 6 and col < 6 and board[row + 1][col + 2] == 'bN') or \
                                (row < 6 and col > 1 and board[row + 1][col - 2] == 'bN') or \
                                (row < 5 and col < 6 and board[row + 2][col + 1] == 'bN') or \
                                (row < 5 and col > 1 and board[row + 2][col - 2] == 'bN') or \
                                (row < 7 and col > 0 and board[row + 1][col - 1] == 'bK') or \
                                (row < 7 and col < 7 and board[row + 1][col + 1] == 'bK'):
                            score -= 0.3  # Penalty




                else:

                    # MATERIAL
                    score -= value * 2

                    # PAWN STRUCTURE
                    if piece == 'bP':
                        # Isolated pawn
                        if (col == 0 or board[row][col - 1] == '  ') and (col == 7 or board[row][col + 1] == '  '):
                            score += 0.1
                        # Doubled pawn
                        if row < 7 and board[row + 1][col] == 'bP':
                            score += 0.1
                        # Passed pawn
                        passed = True
                        for r in range(row - 1, -1, -1):
                            if board[r][col] != '  ':
                                passed = False
                                break
                        if passed:
                            score -= 0.5

                        if col == 0:
                            score -= 9

                    # PIECE DEVELOPMENT
                    if piece != 'bP':
                        # col 7 = 0 points
                        if col == 6:
                            score -= 0.05
                        elif col == 5:
                            score -= 0.1
                        elif col == 4:
                            score -= 0.2
                        elif col == 3:
                            score -= 0.3
                        elif col == 2:
                            score -= 0.4
                        elif col == 1:
                            score -= 0.2
                        # col 0 = 0 points

                    # Center incentive for Knights
                    if piece == 'bN' and (row in [2, 3, 4, 5]) and (col in [2, 3, 4, 5]):
                        score -= 0.05

                    # Big diagonal incentive
                    if piece == 'bB' and row == col:
                        score -= 0.05

                    # ROOKS IN OPEN FILES
                    if piece == 'bR':
                        # check if the rook is in an open file (no pawns of either color in front)
                        open_file = True
                        for r in range(8):
                            if board[r][col] != '  ' and board[r][col][0] == 'bP':
                                open_file = False
                                break
                        if open_file:
                            score -= 0.4

                    # DOUBLED ROOKS IN OPEN FILES
                    if piece == 'bR':
                        # check if there is another black rook in the same file
                        doubled_rook = False
                        for r in range(row - 1, -1, -1):
                            if board[r][col] in ['bR', 'bQ']:
                                doubled_rook = True
                                break
                        if doubled_rook:
                            score -= 0.1

                    # PAWN CENTER
                    # Central pawns
                    if piece == 'bP' and col in [3, 4] and row in [3, 4]:
                        score -= 0.2
                    # C and F pawns
                    if piece == 'bP' and col in [2, 5] and row in [2, 3, 4]:
                        score -= 0.1

                    # KING SAFETY
                    if piece == 'bK':

                        # set score to 0, there is no checkmate yet
                        score -= 2000

                        # Check for attacks on the king
                        if (row > 1 and col > 0 and board[row - 1][col - 1] == 'wP') or \
                                (row > 1 and col < 7 and board[row - 1][col + 1] == 'wP'):
                            score += 0.3  # Penalize for pawn attacks on king
                        if (row > 0 and board[row - 1][col] == 'wQ') or \
                                (row > 0 and col < 7 and board[row - 1][col + 1] == 'wB') or \
                                (row > 1 and col < 6 and board[row - 1][col + 2] == 'wN') or \
                                (row > 1 and col > 1 and board[row - 1][col - 2] == 'wN') or \
                                (row > 2 and col < 6 and board[row - 2][col + 1] == 'wN') or \
                                (row > 2 and col > 1 and board[row - 2][col - 2] == 'wN') or \
                                (row > 0 and col > 0 and board[row - 1][col - 1] == 'wK') or \
                                (row > 0 and col < 7 and board[row - 1][col + 1] == 'wK'):
                            score += 0.3  # Penalize for attacks on king

        score = round(score, 2)
        return score


class Mover:
    def __init__(self):
        self.start, self.end = -1, -1

        self.turn = 0

    def check_move(self):
        if self.start == -1 or self.end == -1:
            return True

        start_x = self.start[1]  # row (down -> up)
        start_y = self.start[0]  # column (left -> right)
        end_x = self.end[1]
        end_y = self.end[0]

        piece = main.board.gameboard[start_x][start_y]
        target = main.board.gameboard[end_x][end_y]

        promotion = False

        if piece.__contains__('P'):
            # TODO en pasant
            can_take = False

            # Take diagonally
            t1, t2 = ['  ', '  ']  # Initialize t1 and t2 to prevent bugs on A and H files
            if self.turn == 0:
                try:
                    t1 = main.board.gameboard[start_x - 1][start_y - 1]
                    t2 = main.board.gameboard[start_x - 1][start_y + 1]
                except:
                    pass
            else:
                try:
                    t1 = main.board.gameboard[start_x + 1][start_y - 1]
                    t2 = main.board.gameboard[start_x + 1][start_y + 1]
                except:
                    pass

            if t1 != '  ' or t2 != '  ':
                can_take = True

            # Don't move backwards
            if self.turn == 0:
                if end_x >= start_x:
                    return False
            else:
                if end_x <= start_x:
                    return False

            # Don't move sideways
            if can_take:
                if end_y not in [start_y - 1, start_y, start_y + 1]:
                    return False
            else:
                if start_y != end_y:
                    return False

            # Move one space, or two if hasn't moved
            if self.turn == 0:
                if start_x == 6:  # hasn't moved
                    if start_x not in [end_x + 1, end_x + 2]:
                        return False
                else:  # has moved
                    if end_x + 1 != start_x:
                        return False
            else:
                if start_x == 1:
                    if start_x not in [end_x - 1, end_x - 2]:
                        return False
                else:
                    if end_x - 1 != start_x:
                        return False

            # Don't move if piece in front
            if can_take:
                front = False  # initialize

                if start_y == end_y and target == '  ':
                    front = True  # it is able to go front

                if front is False:
                    if start_y == end_y:  # if tries go go front and can't, don't
                        return False

                    if self.turn == 0:
                        if not target.__contains__('b'):  # w can only eat b, vice versa
                            return False
                    else:
                        if not target.count('w'):
                            return False
            else:
                if target != '  ':
                    return False

            # Promotion
            if (self.turn == 0 and end_x == 0) or (self.turn == 1 and end_x == 7):
                promotion = True

        elif piece.__contains__('R'):
            if start_x == end_x:
                axis = 0  # horizontal
            elif start_y == end_y:
                axis = 1  # vertical
            else:
                axis = -1  # invalid

            if axis == 0:
                if start_y < end_y:
                    direction = 'r'
                else:
                    direction = 'l'
            elif axis == 1:
                if start_x > end_x:
                    direction = 'u'
                else:
                    direction = 'd'
            else:
                direction = -1

            # Only straight lines
            if axis == -1:
                return False

            # Don't jump pieces
            if straight_obstacles(direction, start_x, start_y, end_x, end_y, target, self.turn, main.board.gameboard):
                return False

            # Remove castling right
            if main.board.can_castle_k[self.turn] or main.board.can_castle_q:
                if start_y == 0:
                    main.board.can_castle_q[self.turn] = False
                if start_y == 7:
                    main.board.can_castle_k[self.turn] = False

        elif piece.__contains__('N'):
            if end_y not in [start_y - 2, start_y - 1, start_y + 1, start_y + 2]:
                return False

            if end_y == start_y - 2:
                if end_x not in [start_x - 1, start_x + 1]:
                    return False
            elif end_y == start_y - 1:
                if end_x not in [start_x - 2, start_x + 2]:
                    return False
            if end_y == start_y + 1:
                if end_x not in [start_x - 2, start_x + 2]:
                    return False
            elif end_y == start_y + 2:
                if end_x not in [start_x - 1, start_x + 1]:
                    return False

            # don't eat own pieces
            if self.turn == 0 and target.__contains__('w'):
                return False
            if self.turn == 1 and target.__contains__('b'):
                return False

        elif piece.__contains__('B'):
            diff_x = abs(start_x - end_x)
            diff_y = abs(start_y - end_y)

            if diff_x != diff_y:  # Only diagonal movements
                return False

            if diff_x == 0:  # Can't move into itself
                return False

            #  Up or down
            if end_x < start_x:
                vertical = 0  # upwards
            elif end_x > start_x:
                vertical = 1  # downwards
            else:
                vertical = -1

            # Get direction
            if vertical == 0:
                if start_y < end_y:
                    direction = 'ur'
                else:
                    direction = 'ul'
            elif vertical == 1:
                if start_y < end_y:
                    direction = 'dr'
                else:
                    direction = 'dl'
            else:
                direction = -1

            # Obstacle management
            if diagonal_obstacles(direction, start_x, start_y, self.turn, diff_x, main.board.gameboard):
                return False

        elif piece.__contains__('Q'):
            diff_x = abs(start_x - end_x)
            diff_y = abs(start_y - end_y)

            direction = ''  # TODO remove

            if start_x == end_x and start_y == end_y:  # Into itself
                return False

            if start_x > end_x:  # up
                if start_y > end_y:
                    direction = 'ul'
                elif start_y < end_y:
                    direction = 'ur'
                else:  # equal
                    direction = 'u'
            if start_x < end_x:  # down
                if start_y > end_y:
                    direction = 'dl'
                elif start_y < end_y:
                    direction = 'dr'
                else:  # equal
                    direction = 'd'
            if start_x == end_x:
                if start_y < end_y:
                    direction = 'r'
                else:
                    direction = 'l'

            # Diagonal movements
            if direction in ['ul', 'ur', 'dl', 'dr']:
                if diff_x != diff_y:
                    return False
                if diagonal_obstacles(direction, start_x, start_y, self.turn, diff_x, main.board.gameboard):
                    return False
            else:
                if straight_obstacles(direction, start_x, start_y, end_x, end_y, target, self.turn,
                                      main.board.gameboard):
                    return False

        elif piece.__contains__('K'):
            if end_x not in [start_x - 1, start_x, start_x + 1]:
                return False
            if end_y not in [start_y - 2, start_y - 1, start_y, start_y + 1, start_y + 2]:
                return False

            if self.turn == 0 and target.__contains__('w'):
                return False
            if self.turn == 1 and target.__contains__('b'):
                return False

            # Castling, Remove castling right
            if end_y in [start_y - 2, start_y + 2]:
                if end_y == start_y - 2:
                    if castle_unobstructed_q(self.turn, main.board.gameboard):
                        if main.board.can_castle_q[self.turn]:
                            castle_rook_q(self.turn, main.board.gameboard)
                            main.board.can_castle_q[self.turn] = False
                            main.board.can_castle_k[self.turn] = False
                        else:
                            return False
                    else:
                        return False
                elif end_y == start_y + 2:
                    if castle_unobstructed_k(self.turn, main.board.gameboard):
                        if main.board.can_castle_k[self.turn]:
                            castle_rook_k(self.turn, main.board.gameboard)
                            main.board.can_castle_q[self.turn] = False
                            main.board.can_castle_k[self.turn] = False
                        else:
                            return False
                    else:
                        return False

            else:
                main.board.can_castle_k[self.turn] = False
                main.board.can_castle_q[self.turn] = False

        self.move(promotion=promotion)

        return True

    def move(self, promotion=False):
        start_x = self.start[1]
        start_y = self.start[0]

        piece = main.board.gameboard[start_x][start_y]

        if piece == '  ':
            self.start, self.end = -1, -1
            return

        if self.start == self.end:
            return
        if self.start == -1:
            return
        else:
            if clicked_on(self.start, main.board.gameboard) == self.turn:  # check if he's trying to move his own piece
                if self.start != -1 and self.end != -1:
                    start_x = self.start[1]
                    start_y = self.start[0]
                    end_x = self.end[1]
                    end_y = self.end[0]

                    if promotion:
                        if self.turn == 0:
                            main.board.gameboard[end_x][end_y] = 'wQ'
                        else:
                            main.board.gameboard[end_x][end_y] = 'bQ'
                    else:
                        main.board.gameboard[end_x][end_y] = main.board.gameboard[start_x][start_y]

                main.board.gameboard[start_x][start_y] = '  '

                self.start, self.end = -1, -1

                if self.turn == 0:
                    self.turn = 1
                    color = 'b'
                else:
                    self.turn = 0
                    color = 'w'

                main.board.represent_pieces()

                if self.turn == main.ai_turn:
                    main.ai.move(color)


class Piece:
    def __init__(self, name, colour):
        self.colour = colour
        self.name = name

        if colour == 'w':
            self.id = 'W' + str(len(main.w_ids))
            main.w_ids.append(self.id)  # is it necessary to have them in main?
        else:
            self.id = 'B' + str(len(main.b_ids))
            main.b_ids.append(self.id)


def print_board(board):
    print('-------------------------------------------')
    for i in board:
        print(i, ',')
    print('-------------------------------------------')


def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print_board(main.board.gameboard)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            square = mouse_to_square(mouse[0], mouse[1])

            if main.mover.start == -1:
                main.mover.start = square
            elif main.mover.end == -1:
                main.mover.end = square
            else:
                main.mover.end = -1
                main.mover.start = square


screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
main = Main()
main.start()

while True:
    screen.fill((0, 0, 0))
    events()
    clock.tick(FPS)
    main.update()
    pygame.display.update()
