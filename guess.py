import random

def play_game(player_name):
    secret_number = random.randint(1, 100)
    attempts = 0

    print(f"\n{player_name}, it's your turn.")
    print("I have selected a number between 1 and 100. Try to guess it.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low.")
            elif guess > secret_number:
                print("Too high.")
            else:
                print(f"Correct! {player_name}, you guessed the number in {attempts} attempts.")
                return attempts

        except ValueError:
            print("Please enter a valid number.")

print("Welcome to the 2-Player Number Guessing Game.")
print("Each player will take a turn to guess a secret number.\n")

player1 = input("Enter Player 1 name: ")
player2 = input("Enter Player 2 name: ")

print(f"\n{player1}, you're up first.")
player1_attempts = play_game(player1)

print(f"\n{player2}, it's your turn now.")
player2_attempts = play_game(player2)

print("\nResults:")
print(f"{player1} took {player1_attempts} attempts.")
print(f"{player2} took {player2_attempts} attempts.")

if player1_attempts < player2_attempts:
    print(f"{player1} wins.")
elif player2_attempts < player1_attempts:
    print(f"{player2} wins.")
else:
    print("It's a tie.")

print("\nThank you for playing the 2-Player Number Guessing Game.")
