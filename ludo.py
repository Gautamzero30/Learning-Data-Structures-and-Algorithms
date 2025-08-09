import chess
import chess.engine

# Create a chess board (start position)
board = chess.Board()

# Path to Stockfish engine (you need to have stockfish installed)
engine = chess.engine.SimpleEngine.popen_uci("/path/to/stockfish")

# Print board
print(board)

# Ask Stockfish for the best move
result = engine.play(board, chess.engine.Limit(time=1.0))

print("Best move:", result.move)

engine.quit()
