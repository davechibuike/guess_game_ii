#guess_game

guess_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess > "))
    guess_count += 1

    if guess == guess_number:
        print("You WIn")
        break

else:
    print(f" You fail, The correct Guess is {guess_number} ")

print("thanks for playing !!")