import sys

board = sys.stdin.readline()

board = board.replace('XXXX', 'AAAA')
board = board.replace('XX', 'BB')

print(-1) if 'X' in board else print(board)
