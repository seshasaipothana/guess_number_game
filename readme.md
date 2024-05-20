# Description about the game

Overview:
The Guess the Number game is a simple interactive game where the player must guess a randomly generated number between 1 and 100 (inclusive). The player selects a difficulty level which determines the number of attempts they are allowed.

Game Features:

The player chooses between two difficulty levels: "EASY" and "HARD".
"EASY" level grants 10 chances.
"HARD" level grants 5 chances.
A random number between 1 and 100 is generated using Python's random module.
The player is prompted to guess the number repetitively based on the allowed chances.
Feedback is provided for each guess:
"Too low" if the guess is lower than the random number.
"Too high" if the guess is higher than the random number.
"You guessed it correct" if the guess matches the random number, and the game reveals the correct number.
If the player cannot guess the number within the given chances, the game ends with a message: "You have run out of guesses, you lose." and shows the correct number.

Game Flow:

The game starts by asking the player to choose a difficulty level ("EASY" or "HARD").
Based on the selected difficulty, the player is allotted 10 or 5 chances to guess the number.
A random number between 1 and 100 is generated.
The player is repeatedly prompted to make a guess until they either guess correctly or exhaust their chances.
Appropriate feedback is given for each guess, and the game concludes with a success or failure message.
