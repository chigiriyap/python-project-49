import random 

def main():
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    
    correct_answer_in_row = 0

    while correct_answer_in_row < 3:
	number = random.randint(1, 100)
	print(f'Question: {number}')
	user_answer = input('Your answer: ')

	is_even = (number % 2 == 0)
	correct_answer = 'yes' if is_even else 'no'

	if user_answer != correct_answer:
	    print(f'"{user_answer}" is wrong answer ;(. Correct answer was "{correct_answer}".')
	    print(f"Let's try again, {name}!")
	    return
        else:
	    print('Correct!')
	    correct_answer_in_row += 1

    print(f'Congratulations, {name}!')

if __name__ == '__main__':
    main()
