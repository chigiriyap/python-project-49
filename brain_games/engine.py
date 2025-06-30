def play(game):
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Answer the following questions:")

    for _ in range(3):
        question, correct_answer = game()
        print(f"Question: {question}")
        answer = input("Your answer: ")

        if answer == str(correct_answer):
            print("Correct!")
        else:
            print(f"'{answer}' is wrong. The correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
