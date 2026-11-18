import os


class MMGame:

    def __init__(self, history=None, answer=None):

        if history is None:
            self.attempts = []
        else:
            self.attempts = history
        
        if answer is None:
            self.secret = (0,0,1,1)
        else:
            self.secret = answer
    
    def make_guess(self, guess):
        self.attempts.append(guess)

    def get_attempt_entry(self, index):
        return self.attempts[index]
    
    def get_answer(self):
        return list(self.secret)
    
    def row_feedback(self, row_num):
        checked = [False, False, False, False]
        list_of_mismatched = []
        matched = 0
        mismatched = 0
        
        # checking for matched
        for i in range(4):
            if self.secret[i] == int(self.attempts[row_num][i]):
                checked[i] = True
                matched += 1
            else:
                list_of_mismatched.append(i)

        # checking for mismatched
        for i in list_of_mismatched:
            for j in list_of_mismatched:
                if i != j and not checked[j] and int(self.attempts[row_num][i]) == self.secret[j]:
                    checked[j] = True
                    mismatched += 1
                    break 
        
        wrong = (4 - matched) - mismatched
        return (matched, mismatched, wrong)

class colour:
   PURPLE = '\033[1;35;48m'
   CYAN = '\033[1;36;48m'
   BOLD = '\033[1;37;48m'
   BLUE = '\033[1;34;48m'
   GREEN = '\033[1;32;48m'
   YELLOW = '\033[1;33;48m'
   RED = '\033[1;31;48m'
   BLACK = '\033[1;30;48m'
   END = '\033[1;37;0m'

class pins:
    RED = colour.RED + '⬤' + colour.END
    WHITE = '⬤'
    BLACK = colour.BLACK + '⬤' + colour.END


def make_row(game, row):
    data = list(game.get_attempt_entry(row))
    return "┃{}┃{}┃{}┃{}┃".format(*data)

def grade_row(game, row):
    result = game.row_feedback(row)
    output = result[0] * (pins.RED + " ") + (result[1] * (pins.WHITE + " ")) + (result[2] * (pins.BLACK + " "))
    return output[:-1]


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
        output.append(make_row(game, x) + f" {grade_row(game, x)}")
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
