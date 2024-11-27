class Game :
  def __init__(self) -> None:
    self._board_ = [['~' for col in range(0,8)] for rows in range(0, 8)]
    self.print_board()

  def initialize_game(self):
   print('game star') 

  def print_board(self):
    '''
    Print the game cols and rows of the game board with idetation
    '''
    print('\n\n      TABLERO DE JUEGO')
    print('\n   1  2  3  4  5  6  7  8\n')
    for index, rows in enumerate(self._board_):
      print(f'{index}  {'  '.join(rows)}\n')


Game()