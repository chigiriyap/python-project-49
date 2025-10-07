from brain_games.engine import play
from brain_games.games import brain_calc

def main():
    play(brain_calc.generate_question)

if __name__ == '__main__':
    main()
