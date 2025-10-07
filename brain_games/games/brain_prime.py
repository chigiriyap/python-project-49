import random
import math
from brain_games.engine import play

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def generate_question():
    number = random.randint(1, 100) #NOSONAR
    question = str(number)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return question, correct_answer

def main():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    play(generate_question)
