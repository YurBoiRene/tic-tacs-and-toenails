#!/usr/bin/env python3
""" Authored by Lennon Anderson """

import copy


def chk_win(board):
  """Check if a player wins given a board.

  Arguments:
  board -- 3x3 board represeted as a 2d list.

  For board representation: each element is an integer [0,2].
  0 indicates empty square.
  1 indicates player 1 (X).
  2 indicates player 2 (O).
  """
  total_sum = 0
  ldiag_sum = [0, 0]
  rdiag_sum = [0, 0]
  for i in range(3):
    if board[i][i] != 0:
      idx = board[i][i] - 1
      ldiag_sum[idx] = ldiag_sum[idx] + 1
    new_i = 2 - i
    if board[i][new_i] != 0:
      idx = board[i][new_i] - 1
      rdiag_sum[idx] = rdiag_sum[idx] + 1


    vert_sum = [0, 0]
    hor_sum = [0, 0]
    #import pdb; pdb.set_trace()
    for k in range(3):
      if board[i][k] > 0:
        total_sum = total_sum + 1

      if board[i][k] != 0:
        idx = board[i][k] - 1
        hor_sum[idx] = hor_sum[idx] + 1
      if board[k][i] != 0:
        idx = board[k][i] - 1
        vert_sum[idx] = vert_sum[idx] + 1
    if vert_sum[0] == 3 or hor_sum[0] == 3:
      return 1
    elif vert_sum[1] == 3 or hor_sum[1] == 3:
      return 2

  if ldiag_sum[0] == 3 or rdiag_sum[0] == 3:
    return 1
  elif ldiag_sum[1] == 3 or rdiag_sum[1] == 3:
    return 2
  elif total_sum == 9:
    return 3
  else:
    return 0

def make_board():
  """Creates an empty board."""
  return [[0] * 3 for _ in range(3)]

def num2ttt(num):
  """Converts numberic element to its string representation."""
  if num == 0:
    return "   "
  elif num == 1:
    return " X "
  else:
    return " O "

def print_board(board):
  """Prints a board neatly."""
  hor_sep = '|'
  vert_sep = '-'
  board_width = 11
  board_str = [[num2ttt(elm) for elm in row] for row in board]
  # Lord please forgive me for what im about to do
  print(board_str[0][0], board_str[0][1], board_str[0][2], sep=hor_sep)
  print(vert_sep * board_width)
  print(board_str[1][0], board_str[1][1], board_str[1][2], sep=hor_sep)
  print(vert_sep * board_width)
  print(board_str[2][0], board_str[2][1], board_str[2][2], sep=hor_sep)

def do_move(board, player=1):
  """Do next move.

  Assumes nobody has won.
  Assumes it is *my* turn.
  """

  num_options = 0
  for row in range(3):
    for col in range(3):
      # Empty square
      if board[row][col] == 0:
        num_options = num_options + 1

def not_player(player):
  return 1 if player == 2 else 2

def prct_win(board, player=1, turn=1):
  num_options = 0
  total_pcnt = 0.0
  any_win = chk_win(board)
  if any_win != 0:
    if any_win == player:
      return 1
    else:
      return 0

  for row in range(3):
    for col in range(3):
      # Empty square
      if board[row][col] == 0:
        num_options = num_options + 1
        board[row][col] = turn
        total_pcnt = total_pcnt + prct_win(board, player=player, turn=not_player(turn))
        board[row][col] = 0
  return total_pcnt / num_options

def best_move(board, player=1, turn=1):
  moves = {}
  for row in range(3):
    for col in range(3):
      # Empty square
      if board[row][col] == 0:
        move = (row, col)
        board[row][col] = player
        prct = prct_win(board, player=player, turn=not_player(player))
        board[row][col] = 0
        moves[move] = prct

  print("Moves for board:")
  print_board(board)
  print(moves)
  print()
  best = max(moves, key=moves.get)
  return best


"""
board = make_board()
board[0][0] = 0
board[1][0] = 0
board[2][0] = 1
board[0][1] = 1
board[1][1] = 0
board[2][1] = 2
board[0][2] = 2
board[1][2] = 2
board[2][2] = 1
print_board(board)
print()

print(prct_win(board, player=1, turn=1))
print(best_move(board, player=1))
"""

board = make_board()
any_win = 0
while any_win == 0:
  print("Current board:")
  print_board(board)
  print("tattn's move")
  tattn_move = best_move(board, player=1)
  board[tattn_move[0]][tattn_move[1]] = 1
  print(f"tattn: I choose {tattn_move}, punk!")

  any_win = chk_win(board)
  if any_win > 0:
    break

  print("Current board:")
  print_board(board)
  print("Your move")
  your_move = input("> ")
  move = tuple([int(s) for s in your_move.split(',')])
  board[move[0]][move[1]] = 2
  any_win = chk_win(board)

print(f"{any_win} won!")
