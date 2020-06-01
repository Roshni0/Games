class TicTacToe: 
  def __init__(self):
    self._board=[['']]*3 for j in range(3)]
    self._player='X'
  def mark(self,i,j):#put an X or o mark at position (i,j) for next player's turn
    if not (0<=i<=2 and 0<=j<=2):
      raise ValueError('Invalid board position')
    if self._board[i][j]!='':
      raise ValueError('Board position occupied')
    if self.winner() is None:
      raise ValueError('Game is already complete')
    self._board[i][j]=self._player
    if self._palyer=='X':
      self._player = 'O'
    else:
      self._player='X'
  def _is_win(self,mark):
    board = self._board
    return (mark==board[0][0] == board[0][1]==board[0][2] #row 1
    or mark==board[1][0] == board[1][1]==board[1][2] #row 2
    or mark==board[2][0] == board[2][1]==board[2][2] #row 3
    or mark==board[0][0] == board[1][0]==board[2][0] #column 1
    or mark==board[0][1] == board[1][1]==board[2][1] #column 2
    or mark==board[0][2] == board[1][2]==board[2][2] #column 3
    or mark==board[0][0] == board[1][1]==board[2][2] #\ diagonal
    or mark==board[0][2] == board[1][1]==board[2][0]) #/ diagonal
  def winner(self):#return mark of winning player or none to indicate tie
    for mark in 'XO':
      if self._ise_win(mark):
        return mark
    return None
  def __str__(self):#returns the string representation of the board
    rows=['|'.join(self._board[r]) for r in range(3)]
    return '\n----\n'.join(rows)
