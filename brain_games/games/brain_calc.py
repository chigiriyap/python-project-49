import random

def generate_question():
    operators = ['+', '-', '*']
    num1 = random.randint(1, 20) #NOSONAR
    num2 = random.randint(1, 20) #NOSONAR
    operator = random.choice(operators) #NOSONAR

    question = f"{num1} {operator} {num2}"

    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2

    return question, answer
