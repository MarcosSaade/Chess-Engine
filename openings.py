import random
from functions import x0_to_move

opening_moves = {
    # ------------------------- #

    # 1.e4
    'rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b': [
        (x0_to_move(('c7', 'c5')), 1),
        (x0_to_move(('e7', 'e5')), 1),
        (x0_to_move(('d7', 'd6')), 1),
        (x0_to_move(('g7', 'g6')), 1),
        (x0_to_move(('g8', 'f6')), 1),
        (x0_to_move(('b8', 'c6')), 1),
        (x0_to_move(('d7', 'd5')), 1),
    ],

    # ------------------------- #

    ### SICILIAN ###

    # 2. Nf3
    'rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R b': [
        (x0_to_move(('g7', 'g6')), 1)  # Hyperaccelerated dragon
    ],

    # Hyperacceletrated dragon

    # ------------------------- #

    # 3.Nxd4
    # Hyperaccelerated dragon, 2d4. cxd4. 3.Nxd4.
    'rnbqkbnr/pp1ppp1p/6p1/8/3NP3/8/PPP2PPP/RNBQKB1R b': [
        (x0_to_move(('f8', 'g7')), 1),
        (x0_to_move(('b8', 'c6')), 1),
    ],

    # 3.Nxd4 Bg7
    # Hyperaccelerated dragon, 2d4. cxd4. 3.Nxd4. Bg7 4.Nc6
    'rnbqk1nr/pp1pppbp/6p1/8/3NP3/2N5/PPP2PPP/R1BQKB1R b': [
        (x0_to_move(('b8', 'c6')), 1),
    ],

    # Hyperaccelerated dragon, 2d4. cxd4. 3.Nxd4. Bg7 4.c4
    'rnbqk1nr/pp1pppbp/6p1/8/2PNP3/8/PP3PPP/RNBQKB1R b': [
        (x0_to_move(('b8', 'c6')), 1),
    ],

    # Nxd4 Nc6
    # Hyperaccelerated dragon, 2d4. cxd4. 3.Nxd4. Nc6 4.Nc3
    'r1bqkbnr/pp1ppp1p/2n3p1/8/3NP3/2N5/PPP2PPP/R1BQKB1R b': [
        (x0_to_move(('f8', 'g7')), 1),
    ],

    # Hyperaccelerated dragon, 2d4. cxd4. 3.Nxd4. Nc6 4.c4
    'r1bqkbnr/pp1ppp1p/2n3p1/8/2PNP3/8/PP3PPP/RNBQKB1R b': [
        (x0_to_move(('f8', 'g7')), 1),
    ],

    # ------------------------- #

    # 3.Qxd4
    # Hyperaccelerated dragon, 2d4. cxd4. 3.Qxd4.
    'rnbqkbnr/pp1ppp1p/6p1/8/3QP3/5N2/PPP2PPP/RNB1KB1R b': [
        (x0_to_move(('g8', 'f6')), 1),
    ],

    # Hyperaccelerated dragon, 2d4. cxd4. 3.Qxd4. Nf6 4.e5
    'rnbqkb1r/pp1ppp1p/5np1/4P3/3Q4/5N2/PPP2PPP/RNB1KB1R b': [
        (x0_to_move(('b8', 'c6')), 1),
    ],

    # Hyperaccelerated dragon, 2d4. cxd4. Qxd4. 3.Nf6 Nc3
    'rnbqkb1r/pp1ppp1p/5np1/8/3QP3/2N2N2/PPP2PPP/R1B1KB1R b': [
        (x0_to_move(('b8', 'c6')), 1),
    ],

    # ------------------------- #

    # 2. CLOSED SICILIAN (2.Nc3)
    'rnbqkbnr/pp1ppppp/8/2p5/4P3/2N5/PPPP1PPP/R1BQKBNR b': [
        (x0_to_move(('b8', 'c6')), 1)
    ],

    # 2. Closed sicilian, traditional line, 3Nf3.
    'r1bqkbnr/pp1ppppp/2n5/2p5/4P3/2N2N2/PPPP1PPP/R1BQKB1R b': [
        (x0_to_move(('e7', 'e6')), 1),
        (x0_to_move(('g7', 'g6')), 1)
    ],

    # ------------------------- #

    # e5.

    # ------------------------- #

    # KINGS KNIGHT

    # 1.e4 e5. 2.Nf3 (Kings Knight)
    'rnbqkbnr/pppp1ppp/8/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R b': [
        (x0_to_move(('b8', 'c6')), 1),
        (x0_to_move(('g8', 'f6')), 1),
        (x0_to_move(('d7', 'd6')), 1),
    ],

    # ------------------------- #

    # ITALIAN
    'r1bqkbnr/pppp1ppp/2n5/4p3/2B1P3/5N2/PPPP1PPP/RNBQK2R b': [
        (x0_to_move(('f8', 'c5')), 1),
    ],

    # 2...Bc5, Giuoco piano
    'r1bqk1nr/pppp1ppp/2n5/2b1p3/2B1P3/2P2N2/PP1P1PPP/RNBQK2R b': [
        (x0_to_move(('g8', 'f6')), 1),
    ],

    # ------------------------- #

    # 1.e4 e5. 2.Nc3 (Viena)
    'rnbqkbnr/pppp1ppp/8/4p3/4P3/2N5/PPPP1PPP/R1BQKBNR b': [
        (x0_to_move(('b8', 'c6')), 1),
        (x0_to_move(('g8', 'f6')), 1),
        (x0_to_move(('f8', 'c5')), 1),
    ],

    # ------------------------- #

    # Pirc
    # 2.d4
    'rnbqkbnr/ppp1pppp/3p4/8/3PP3/8/PPP2PPP/RNBQKBNR b': [
        (x0_to_move(('g8', 'f6')), 1),
        (x0_to_move(('g7', 'g6')), 1),
        (x0_to_move(('c7', 'c6')), 1),
    ],

    # ------------------------- #

    # Modern
    # 2.d4
    'rnbqkb1r/pppppppp/5n2/4P3/8/8/PPPP1PPP/RNBQKBNR b': [
        (x0_to_move(('f6', 'd5')), 1),
    ],

    # ------------------------- #

    # Alekhine
    # 2. e5
    'rnbqkb1r/pppppppp/5n2/4P3/8/8/PPPP1PPP/RNBQKBNR b ': [
        (x0_to_move(('f8', 'g7')), 1),
        (x0_to_move(('d5', 'd6')), 1),
        (x0_to_move(('g5', 'g6')), 1),
    ],

    # ------------------------- #

    # Nizmowich
    # 2.Nf3
    'r1bqkbnr/pppppppp/2n5/8/4P3/5N2/PPPP1PPP/RNBQKB1R b': [
        (x0_to_move(('e7', 'e5')), 1),
        (x0_to_move(('d7', 'd6')), 1),
    ],

    # ------------------------- #

    # 2.d4

    'r1bqkbnr/pppppppp/2n5/8/3PP3/8/PPP2PPP/RNBQKBNR b':
        [
            (x0_to_move(('d7', 'd5')), 1),
            (x0_to_move(('e7', 'e6')), 1),

        ],

    # ------------------------- #

    # ------------------------- #

    # QUEENS PAWN OPENING
    'rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR b': [
        (x0_to_move(('g8', 'f6')), 1),
        (x0_to_move(('d7', 'd5')), 1),
        (x0_to_move(('e7', 'e6')), 1),
        (x0_to_move(('d7', 'd6')), 1),
    ],

    # ------------------------- #

    # Queens gambit
    # 1.d4 d5 2. c5
    'rnbqkbnr/ppp1pppp/8/3p4/2PP4/8/PP2PPPP/RNBQKBNR b': [
        (x0_to_move(('c7', 'c6')), 1),
        (x0_to_move(('e7', 'e6')), 1),
    ],

    # ------------------------- #

    # Slav, Modern Line (2. Nf3)
    'rnbqkbnr/pp2pppp/2p5/3p4/2PP4/5N2/PP2PPPP/RNBQKB1R b': [
        (x0_to_move(('g8', 'f6')), 1),
    ],

    # Slav 2.Nc3
    'rnbqkbnr/pp2pppp/2p5/3p4/2PP4/2N5/PP2PPPP/R1BQKBNR b': [
        (x0_to_move(('g8', 'f6')), 1),
    ],

    # Slav 2.cxd5
    'rnbqkbnr/pp2pppp/2p5/3P4/3P4/8/PP2PPPP/RNBQKBNR b': [
        (x0_to_move(('c6', 'd5')), 1),
    ],

    # ------------------------- #

    # Queens gambit declined

    # ------------------------- #

    # 2. Nc3
    'rnbqkbnr/ppp2ppp/4p3/3p4/2PP4/2N5/PP2PPPP/R1BQKBNR b': [
        (x0_to_move(('g8', 'f6')), 1),
        (x0_to_move(('c7', 'c6')), 1),
    ],

    # 2. Nc3 Nf6 3.Bg5
    'rnbqkb1r/ppp2ppp/4pn2/3p2B1/2PP4/2N5/PP2PPPP/R2QKBNR b': [
        (x0_to_move(('f8', 'e7')), 1),
        (x0_to_move(('b8', 'd7')), 1),
    ],

    # 2. Nc3 Nf6 3.cxd5
    'rnbqkb1r/ppp2ppp/4pn2/3P4/3P4/2N5/PP2PPPP/R1BQKBNR b': [
        (x0_to_move(('e6', 'd5')), 1),
    ],

    # ------------------------- #

    # Semi Slav

    # 2. Nc3 c6 3.Nf3
    'rnbqkbnr/pp3ppp/2p1p3/3p4/2PP4/2N2N2/PP2PPPP/R1BQKB1R b': [
        (x0_to_move(('g8', 'f6')), 1),
    ],

    # 2. Nc3 c6 3.Nf3 Nf6 4.e3
    'rnbqkb1r/pp3ppp/2p1pn2/3p4/2PP4/2N1PN2/PP3PPP/R1BQKB1R b': [
        (x0_to_move(('b8', 'd7')), 1),
    ],

    # 2. Nc3 c6 3.Nf3 Nf6 4.Bg5
    'rnbqkb1r/pp3ppp/2p1pn2/3p2B1/2PP4/2N2N2/PP2PPPP/R2QKB1R b': [
        (x0_to_move(('b8', 'd7')), 1),
        (x0_to_move(('h7', 'h6')), 1),
    ],

    # ------------------------- #

    # d4, kings knight

    # ------------------------- #

    # 1.d4 d5 2. Nf3.
    'rnbqkbnr/ppp1pppp/8/3p4/3P4/5N2/PPP1PPPP/RNBQKB1R b': [
        (x0_to_move(('g8', 'f6')), 1),
        (x0_to_move(('e7', 'e6')), 1),
    ],

    # 1.d4 d5 2.Nf3 Nf6 3.c4
    'rnbqkb1r/ppp1pppp/5n2/3p4/2PP4/5N2/PP2PPPP/RNBQKB1R b': [
        (x0_to_move(('e7', 'e6')), 1),
        (x0_to_move(('c7', 'c6')), 1),
    ],

    # 1.d4 d5 2.Nf3 Nf6 3.c4
    'rnbqkb1r/ppp1pppp/5n2/3p4/3P1B2/5N2/PPP1PPPP/RN1QKB1R b': [
        (x0_to_move(('e7', 'e6')), 1),
        (x0_to_move(('c7', 'c5')), 1),
    ],

    # 1.d4 d5 2. Nf3. e6 3.c4
    'rnbqkbnr/ppp2ppp/4p3/3p4/2PP4/5N2/PP2PPPP/RNBQKB1R b': [
        (x0_to_move(('g8', 'f6')), 1),
        (x0_to_move(('c7', 'c6')), 1),
    ],

    # 1.d4 d5 2. Nf3. e6 3.e3
    'rnbqkbnr/ppp2ppp/4p3/3p4/3P4/4PN2/PPP2PPP/RNBQKB1R b': [
        (x0_to_move(('g8', 'f6')), 1),
    ],

    # 1.d4 d5 2. Nf3. e6 3.Bf4
    'rnbqkbnr/ppp2ppp/4p3/3p4/3P1B2/5N2/PPP1PPPP/RN1QKB1R b': [
        (x0_to_move(('g8', 'f6')), 1),
        (x0_to_move(('f8', 'd6')), 1),
    ],

    # ------------------------- #

    # London
    # 1.d4 d5 2. Bf4.
    'rnbqkbnr/ppp1pppp/8/3p4/3P1B2/8/PPP1PPPP/RN1QKBNR b': [
        (x0_to_move(('g8', 'f6')), 1),
        (x0_to_move(('c7', 'c5')), 1),
        (x0_to_move(('e7', 'e6')), 1),
    ],

    # ------------------------- #

    # ENGLISH
    # 1.c4

    # ------------------------- #

    'rnbqkbnr/pppppppp/8/8/2P5/8/PP1PPPPP/RNBQKBNR b': [
        (x0_to_move(('e7', 'e5')), 1),
        (x0_to_move(('c7', 'c5')), 1),
    ],

    # ------------------------- #

    # Reversed sicilian

    # 2.Nc3
    'rnbqkbnr/pppp1ppp/8/4p3/2P5/2N5/PP1PPPPP/R1BQKBNR b': [
        (x0_to_move(('g8', 'f6')), 1),
    ],

    # Reversed sicilian, 2.g3
    'rnbqkbnr/pppp1ppp/8/4p3/2P5/6P1/PP1PPP1P/RNBQKBNR b': [
        (x0_to_move(('g8', 'f6')), 1),
    ],

    # Reversed sicilian, 2.g3 Nf6 3.Bg3
    'rnbqkb1r/pppp1ppp/5n2/4p3/2P5/6P1/PP1PPPBP/RNBQK1NR b': [
        (x0_to_move(('d7', 'd5')), 1),
    ],

    # Reversed sicilian, 2.g3 Nf6 3.Nc3
    'rnbqkb1r/pppp1ppp/5n2/4p3/2P5/2N3P1/PP1PPP1P/R1BQKBNR b': [
        (x0_to_move(('d7', 'd5')), 1),
    ],

    # ------------------------- #

    # Symetrical

    # 2.Nf3
    'rnbqkbnr/pp1ppppp/8/2p5/2P5/5N2/PP1PPPPP/RNBQKB1R b': [
        (x0_to_move(('g8', 'f6')), 1),
    ],

    # Symetrical, 2.Nf3 Nf6 3.Nc3
    'rnbqkb1r/pp1ppppp/5n2/2p5/2P5/2N2N2/PP1PPPPP/R1BQKB1R b': [
        (x0_to_move(('b8', 'c6')), 1),
    ],

    # Symetrical, 2.Nc3
    'rnbqkbnr/pp1ppppp/8/2p5/2P5/2N5/PP1PPPPP/R1BQKBNR b': [
        (x0_to_move(('g8', 'f6')), 1),
        (x0_to_move(('b8', 'c6')), 1),
    ],

    # Symetrical, 2.g3
    'rnbqkbnr/pp1ppppp/8/2p5/2P5/6P1/PP1PPP1P/RNBQKBNR b': [
        (x0_to_move(('g7', 'g6')), 1),
        (x0_to_move(('b8', 'c6')), 1),
    ],

}

# Assign a random choice to each dictionary value
opening_moves = {key: random.choices(value, weights=[w for _, w in value])[0] for key, value in opening_moves.items()}
