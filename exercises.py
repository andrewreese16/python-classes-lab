class Game:
  def __init__(self):
    self.turn = 'X'
    self.tie = False
    self.winner = None
    self.board = {
      'a1': None, 'b1': None, 'c1': None,
      'a2': None, 'b2': None, 'c2': None,
      'a3': None, 'b3': None, 'c3': None
    }
  
  def play_game(self):
    print("=== Welcome to Tic-Tac-Toe! ===")
    while not self.winner and not self.tie:
      self.render()
      move = self.get_move()
      self.make_move(move)
      self.check_for_winner()
      self.check_for_tie()
      self.switch_turn()
    self.render_endgame()

  def render(self):
    self.print_board()
    self.print_message()

  def print_board(self):
    b = self.board
    print(f"""
          A   B   C
        1) {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
          ----------
        2) {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
          ----------
        3) {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)
  
  def print_message(self):
    if self.winner:
      print(f"{self.winner} wins the game")
    elif self.tie:
      print("It's a tie")
    else:
      print(f"It's player {self.turn}'s turn")
  
  def get_move(self):
    while True:
      move = input("Enter a valid move (ex: A1): ").lower()
      if move in self.board and not self.board[move]:
        return move
      print("Invalid move.")

  def make_move(self, move):
    self.board[move] = self.turn

  def check_for_winner(self):
    winning_combinations = [
      ['a1', 'b1', 'c1'], ['a2', 'b2', 'c2'], ['a3', 'b3', 'c3'],
      ['a1', 'a2', 'a3'], ['b1', 'b2', 'b3'], ['c1', 'c2', 'c3'],
      ['a1', 'b2', 'c3'], ['a3', 'b2', 'c1']
    ]
    for combo in winning_combinations:
      if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] and self.board[combo[0]] is not None:
        self.winner = self.turn
        break

  def check_for_tie(self):
    if not self.winner and all(self.board[pos] is not None for pos in self.board):
      self.tie = True

  def switch_turn(self):
    self.turn = '0' if self.turn == 'X' else 'X'

  def render_endgame(self):
    if self.winner:
      print(f"Congrats, Player {self.winner}!")
    else:
      print("It's a tie.")

if __name__ == "__main__":
  game_instance = Game()
  game_instance.play_game()