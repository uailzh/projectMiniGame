import random

# Define the possible colors, number of tries, and the length of the secret code
COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 4

# Function to generate a random secret code
def generate_code():
    code = []

    # Generate a code with the specified length using random colors
    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)

    return code

# Function to take user input for a guess
def guess_code():
    while True:
        # Take input, convert to uppercase, and split by spaces to get individual colors
        guess = input("Guess: ").upper().split(" ")

        # Check if the guess has the correct length
        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors")
            continue

        # Check if each color in the guess is a valid color
        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}. Try again")
                break
        else:
            # Break out of the loop if the guess is valid
            break

    return guess

# Function to check the correctness of a guess against the real code
def check_code(guess, real_code):
    colors_count = {}  # Using a dictionary to count occurrences of each color
    correct_position = 0
    incorrect_position = 0

    # Count occurrences of each color in the real code
    for color in real_code:
        if color not in colors_count:
            colors_count[color] = 0
        colors_count[color] += 1

    # Check for correct positions in the guess using the zip function
    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_position += 1
            colors_count[guess_color] -= 1

    # Check for incorrect positions in the guess using the zip function
    for guess_color, real_color in zip(guess, real_code):
        if guess_color in colors_count and colors_count[guess_color] > 0:
            incorrect_position += 1
            colors_count[guess_color] -= 1

    return correct_position, incorrect_position

# Main game function
def game():
    print(f"Welcome to mastermind! You have {TRIES} tries.")
    print("The valid colors are", *COLORS)

    # Generate the secret code
    code = generate_code()

    # Allow the player to make guesses within the specified number of tries
    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        # Check if the player guessed the code correctly
        if correct_pos == CODE_LENGTH:
            print(f"You won the game! You guessed the code in {attempts} attempts")
            break

        # Provide feedback on the correctness of the guess
        print(f"Correct position: {correct_pos} | Incorrect position: {incorrect_pos}")

    else:
        # If the loop completes without breaking, the player ran out of tries
        print("You ran out of tries")

# Start the game
game()
