secret_letter = 25
guess = 0
guess_count = 0
guess_limit = 5
out_of_guess = False

while guess != secret_letter and not out_of_guess:
    if guess_count < guess_limit:
        guess = int(input("Enter a number: "))
        guess_count += 1

    else:
        out_of_guess = True
        print("Out of guesses")

if guess == secret_letter:
    print("You guessed the correct number")

else:
    print("You are out of guesses")
