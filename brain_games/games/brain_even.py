from brain_games.engine import play

def generate_question():
    import random
    number = random.randint(1, 100) #NOSONAR
    is_even = (number % 2 == 0)
    correct_answer = 'yes' if is_even else 'no'
    return str(number), correct_answer

def main():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    play(generate_question)

if __name__ == '__main__':
    main()
