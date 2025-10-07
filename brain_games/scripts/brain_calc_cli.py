from brain_games.engine import play
from brain_games.games import brain_calc


def main():
    print("What is the result of the expression?")
    play(brain_calc.generate_question)


if __name__ == '__main__':
    main()
