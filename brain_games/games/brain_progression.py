import random
from brain_games.engine import play

def generate_progression():
    start = random.randint(1, 20) #NOSONAR
    length = random.randint(5, 10) #NOSONAR
    step = random.randint(1, 10) #NOSONAR
    progression = [start + i * step for i in range(length)]
    missing_index = random.randint(0, length - 1) #NOSONAR
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
