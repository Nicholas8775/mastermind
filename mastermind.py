import os


class MMGame:

    def __init__(self, history=None, answer=None):

        if history is None:
            self.attempts = []
        else:
            self.attempts = history
        
        if answer is None:
            self.secret = (0,0,0,0)
        else:
            self.secret = answer
    
    def make_guess(self, guess):
        self.attempts.append(guess)

    def get_attempt_entry(self, index):
        return self.attempts[index]


def make_row(game, row):
    return game.get_attempt_entry(row)

def display_current_state(game):
    if (len(game.attempts) == 0):
        print("-- empty --")
    else:
        print(make_row(game, -1))

def make_attempt(game):
    os.system("clear")
    print("")

    while True:
        print("\n\n")
        display_current_state(game)
        print("\n")
        guess = input("What is your guess?\n>>> ")

        if len(guess) != 4 or not guess.isnumeric():
            os.system("clear")
            print("Not valid input try again")
        else:
            break

    game.make_guess(guess)

def play_game():
    current_game = MMGame()

    while True:
        make_attempt(current_game)


if __name__ == "__main__":
    play_game()
