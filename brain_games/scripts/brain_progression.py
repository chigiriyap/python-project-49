import random
from brain_games.engine import play

def generate_progression():
    start = random.randint(1, 20)
    length = random.randint(5, 10)  # длина прогрессии от 5 до 10
    step = random.randint(1, 10)
    progression = [start + i * step for i in range(length)]
    missing_index = random.randint(0, length - 1)
    correct_answer = progression[missing_index]
    progression_with_gap = progression.copy()
    progression_with_gap[missing_index] = '..'
    question = ' '.join(str(x) for x in progression_with_gap)
    return question, str(correct_answer)

def main():
    print('What number is missing in the progression?')
    play(generate_progression)

if __name__ == '__main__':
    main()
