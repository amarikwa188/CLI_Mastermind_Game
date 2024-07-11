import sys
from random import choices


def generate_code() -> list[str]:
    """
    Generate a 4 digit code.
    
    :return: a list of code digits.
    """
    letters: list[str] = ['R', 'G', 'B', 'Y', 'W', 'O']
    return choices(letters, k=4)


def generate_data(code: list[str], inp: list[str]) -> tuple[int]:
    """
    Determine the number of inputs in the correct and incorrect position in
    the code.

    :param code: the correct 4 digit code.
    :param inp: the player input.
    :return: a tuple containing (correct, incorrect) positions.
    """
    correct, incorrect = 0, 0

    correct_present = True
    while correct_present:
        correct_present = False
        for idx, guess in enumerate(inp):
            if code[idx] == guess and guess != '@':
                correct += 1
                correct_present = True
                inp[idx] = code[idx] = '@'
    
    for guess in inp:
        if guess in code and guess != '@':
            code[code.index(guess)] = '@'
            incorrect += 1
    
    return correct, incorrect
                    
            
if __name__ == "__main__":
    print("Mastermind Game")
    print("---------------")
    print("Welcome to Mastermind. Attempt to guess the 4 digit code... You have 10 tries.\n"
          "The colors that could make up the code are: R G B Y W O\n")
    
    tries: int = 0
    code: list[str] = generate_code()
    original_code: list[str] = code.copy()

    while tries < 10:
        while True:
            guess: str = input("Enter guess: ").upper().strip().replace(' ', '')

            invalid: bool = any(letter not in 'RGBYWO' for letter in guess)
            wrong_length: bool = len(guess) != 4
            if invalid:
                print("Invalid colors in guess. Select only from: R G B Y W O\n")
                continue
            elif wrong_length:
                print("Wrong length. Enter a 4 digit code.\n")
            else: break

        tries += 1
        inp: list[str] = list(guess)

        if code == inp:
            print(f"Correct! You guessed the code in {tries} {'try' if tries == 1 else 'tries'}!")
            sys.exit()

        data: tuple[int] = generate_data(code, inp)
        code = original_code.copy()

        result: str = f"\nCorrect Position: {data[0]} | Incorrect Position: {data[1]}\n"
        print(result)

    print(f"Wrong! You failed to guess the code in 10 tries.\nIt is... {' '.join(code)}")