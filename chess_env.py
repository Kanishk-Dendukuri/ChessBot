import chess
import random
import numpy as np

piece_to_ascii = {
    'P': '♟', 'p': '♙',  # Pawn
    'N': '♞', 'n': '♘',  # Knight
    'B': '♝', 'b': '♗',  # Bishop
    'R': '♜', 'r': '♖',  # Rook
    'Q': '♛', 'q': '♕',  # Queen
    'K': '♚', 'k': '♔',  # King
    '.': '·',             # Empty square
}

board = str(chess.Board())

for piece, ascii_char in piece_to_ascii.items():
    board = board.replace(piece, ascii_char)

print(board)
