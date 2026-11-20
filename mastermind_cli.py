from mastermind import *


class colour:
   BLACK = '\033[0;30m'
   RED = '\033[0;31m'
   GREEN = '\033[0;32m'
   YELLOW = '\033[0;33m'
   AZURE = '\033[0;34m'
   PURPLE = '\033[38;5;54m'
   CYAN = '\033[0;36m'
   WHITE = '\033[0;37m'
   ORANGE = "\033[0;38;5;208m"
   END = '\033[0m'

class pins:
    WHITE = '⬤'
    BLACK = colour.BLACK + '⬤' + colour.END
    RED = colour.RED + '⬤' + colour.END
    GREEN = colour.GREEN + '⬤' + colour.END
    YELLOW = colour.YELLOW + '⬤' + colour.END
    AZURE = colour.AZURE + '⬤' + colour.END
    PURPLE = colour.PURPLE + '⬤' + colour.END
    CYAN = colour.CYAN + '⬤' + colour.END
    ORANGE = colour.ORANGE + '⬤' + colour.END

colour_list = [
        colour.RED, colour.GREEN, colour.YELLOW,
        colour.AZURE, colour.PURPLE, colour.CYAN,
        colour.ORANGE, colour.BLACK, colour.WHITE,
    ]

pin_list = [
    pins.RED, pins.GREEN, pins.YELLOW,
    pins.AZURE, pins.PURPLE, pins.CYAN,
    pins.ORANGE, pins.BLACK, pins.WHITE,
]

letter_to_number = {
    'r': '1', 'g': '2', 'y': '3',
    'a': '4', 'p': '5', 'c': '6',
    'o': '7', 'b': '8', 'w': '9',
}


def make_row(game, row, ui_format):
    if row == -1:
        data = game.get_answer()
    else:
        data = list(game.get_attempt_entry(row))
    
    match ui_format:
        case 0:
            pass
        case 1:
            for i in range(len(data)):
                data[i] = colour_list[int(data[i])-1] + str(data[i]) + colour.END
        case 2:
            for i in range(len(data)):
                data[i] = pin_list[int(data[i])-1]

    return " ┃{}┃{}┃{}┃{}┃".format(*data)

def grade_row(game, row):
    result = game.evaluation[row]
    output = result[0] * (pins.RED + " ") + (result[1] * (pins.WHITE + " ")) + (result[2] * (pins.BLACK + " "))
    return output[:-1]

def display_current_state(game, ui_format, game_length, reveal_secret=False):

    if reveal_secret:
        answer = make_row(game, -1, ui_format)
        print(
            " ┏━┳━┳━┳━┓\n" \
                    "{}  You {}\n" \
            " ┗━┻━┻━┻━┛".format(answer, ["lost!", "won!"][game.evaluation[-1][0] == 4]))
    else:
        print(
            " ┏━┳━┳━┳━┓\n" \
            " ┃?┃?┃?┃?┃\n" \
            " ┗━┻━┻━┻━┛"
        )

    output = [" ┏━┳━┳━┳━┓"]
    for _ in range(game_length - len(game.attempts)):
        output.append(" ┃ ┃ ┃ ┃ ┃")
        output.append(" ┣━╋━╋━╋━┫")

    for x in range(len(game.attempts)-1, -1, -1):
        output.append(make_row(game, x, ui_format) + f" {grade_row(game, x)}")
        output.append(" ┣━╋━╋━╋━┫")

    output[-1] = " ┗━┻━┻━┻━┛"

    for row in output:
        print(row)

def make_attempt(game, ui_format, game_length):
    os.system("clear")
    print("")

    while True:
        display_current_state(game, ui_format, game_length)
        guess = input("What is your guess?\n>>> ")

        if ui_format != 2:
            if len(guess) != 4 or not guess.isnumeric() or "0" in guess:
                os.system("clear")
                print("Not valid input try again")
            else:
                break
        else:
            if len(guess) != 4 or not all(letter in letter_to_number.keys() for letter in guess):
                os.system("clear")
                print("Not valid input try again")
            else:
                guess = "".join(letter_to_number[l] for l in guess)
                break

    game.make_guess(guess)

def play_game(format_choice, game_length):
    current_game = MMGame()

    for _ in range(game_length):
        make_attempt(current_game, format_choice, game_length)
        if current_game.evaluation[-1][0] == 4:
            break
    
    os.system("clear")
    print("")
    display_current_state(current_game, format_choice, game_length, reveal_secret=True)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--Format", type=int, choices=[0, 1, 2], default=1, help="Specify format")
    parser.add_argument("-l", "--Length", type=int, default=9, help="Game length")
    args = parser.parse_args()

    if args.Length <= 0:
        parser.error("game length must be a positive integer")

    play_game(args.Format, args.Length)
