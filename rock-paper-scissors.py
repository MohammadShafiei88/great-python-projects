import random
import sys

class RPS:
    def __init__(self):
        print('Welcome to RPS 2026!')

        self.moves: dict = {'rock': '🪨', 'paper': '📜', 'scissors': '✂️'}
        self.valid_moves: list[str] = list(self.moves.keys())
        self.your_score: int = 0
        self.ai_score: int = 0

    def play_game(self):

        user_move: str = input('rock, paper , or scissors: ').lower()

        if user_move == 'exit':
            print('Thanks for playing!')
            if self.your_score > self.ai_score:
                print('You won the whole game!')
            elif self.your_score == self.ai_score:
                print('It is a tie!')
            else:
                print('You lost the whole game!')
            sys.exit()

        if user_move not in self.valid_moves:
            print('Invalid move!')
            return self.play_game()

        ai_move: str = random.choice(self.valid_moves)

        self.display_moves(user_move, ai_move)
        self.check_move(user_move, ai_move)

    def display_moves(self, user_move: str, ai_move: str):
        print('******************')
        print(f'Your move: {self.moves[user_move]}')
        print(f'AI move: {self.moves[ai_move]}')
        print('******************')

    def check_move(self, user_move: str, ai_move: str):
        if user_move == ai_move:
            print('It is a tie!')
            print(f'Your score:{self.your_score}', f'AI score:{self.ai_score}')
        elif user_move == 'rock' and ai_move == 'scissors':
            print('You win!')
            self.your_score += 1
            print(f'Your score:{self.your_score}', f'AI score:{self.ai_score}')
        elif user_move == 'paper' and ai_move == 'rock':
            print('You win!')
            self.your_score += 1
            print(f'Your score:{self.your_score}', f'AI score:{self.ai_score}')
        elif user_move == 'scissors' and ai_move == 'paper':
            print('You win!')
            self.your_score += 1
            print(f'Your score:{self.your_score}', f'AI score:{self.ai_score}')
        else:
            print('AI wins...')
            self.ai_score += 1
            print(f'Your score:{self.your_score}', f'AI score:{self.ai_score}')

if __name__ == '__main__':
    rps = RPS()

    while True:
        rps.play_game()


