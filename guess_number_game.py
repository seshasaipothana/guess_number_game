import random


def random_number_generator():
    return random.randint(1, 100)


random_number = random_number_generator()
print("WELCOME TO NUMBER GUESSING GAME!")
print("I'M THINKING OF A NUMBER BETWEEN 1 AND 100")
print(f"PSST!!! The correct answer is {random_number}")

level = input("Choose a difficulty. Type 'easy' or 'hard' ")


def chances_given(level):
    if level == "easy":
        return 10
    elif level == "hard":
        return 5


def give_range(number, guessed_number):
    if number < guessed_number:
        return "too low"
    elif number > guessed_number:
        return "too high"
    elif number == guessed_number:
        return "match"


def number_game(game_level):
    chances = chances_given(game_level)
    guessed_number = random_number_generator()
    print(f"you have {chances} attempts remaining to guess the number.")
    while chances > 0:
        number = int(input("Make a guess "))
        result = give_range(number, guessed_number)
        if result == "match":
            return f"you got it! the answer was {guessed_number}."

        else:
            print(f"{result}\nguess again")

        chances -= 1
        print(f"you have {chances} attempts remaining to guess the number.")

    if chances == 0:
        return f"You have run out of guesses, you lose.\nThe number was {guessed_number}"


print(number_game(level))