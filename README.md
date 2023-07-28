# Number Guessing Game

This is a simple number guessing game implemented in Python. The game prompts the player to think of a number within a specified range and then attempts to guess the number using the "higher", "lower", or "yes" responses.

## How to Play

1. Run the Python script in your Python environment.
2. The program will welcome you to the game and ask you to think of a number.
3. Provide the lower and upper range within which your chosen number lies.
4. The game will make initial random guesses within the specified range.
5. Respond to each guess with "higher" if your number is greater, "lower" if your number is smaller, or "yes" if the guess is correct.
6. The game will adjust its range based on your responses and continue guessing until it finds your number.

## Implementation Details

- The game uses the `random` module to make random guesses within the specified range.
- The player provides feedback using the "higher", "lower", or "yes" responses to guide the game in guessing the correct number.
- The game will terminate and print a goodbye message once the correct number is guessed.
