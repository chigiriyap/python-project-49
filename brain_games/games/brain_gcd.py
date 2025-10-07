import math
import random

from brain_games.engine import play


def generate_question():
    num1 = random.randint(1, 100)  # NOSONAR
    num2 = random.randint(1, 100)  # NOSONAR
    question = f"{num1} {num2}"
    answer = str(math.gcd(num1, num2))
    return question, answer


def main():
    print("Find the greatest common divisor of given numbers.")
    play(generate_question)


if __name__ == '__main__':
    main()
