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
    
    def get_answer(self):
        return list(self.secret)


def make_row(game, row):
    data = list(game.get_attempt_entry(row))
    return "┃{}┃{}┃{}┃{}┃".format(*data)

def display_current_state(game, reveal_secret=False):

    if reveal_secret:
        answer = game.get_answer()
        print(
            "┏━┳━┳━┳━┓\n" \
            "┃{}┃{}┃{}┃{}┃\n" \
            "┗━┻━┻━┻━┛\n".format(*answer))
    else:
        print(
            "┏━┳━┳━┳━┓\n" \
            "┃?┃?┃?┃?┃\n" \
            "┗━┻━┻━┻━┛\n"
        )

    output = ["┏━┳━┳━┳━┓"]
    for _ in range(9 - len(game.attempts)):
        output.append("┃ ┃ ┃ ┃ ┃")
        output.append("┣━╋━╋━╋━┫")

    for x in range(len(game.attempts)-1, -1, -1):
         output.append(make_row(game, x))
         output.append("┣━╋━╋━╋━┫")

    output[-1] = "┗━┻━┻━┻━┛\n"

    for row in output:
        print(row)

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

    for _ in range(9):
        make_attempt(current_game)
    
    os.system("clear")
    print("\n\n\n")
    display_current_state(current_game, True)


if __name__ == "__main__":
    play_game()
