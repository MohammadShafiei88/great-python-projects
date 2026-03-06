from random import randint

min_thresh, max_thresh = 1, 10
random_num = randint(min_thresh, max_thresh)
print(f"Guess an integer between {min_thresh} and {max_thresh}")

while True:
    try:
        guess = int(input("Guess a number: "))
    except ValueError as e:
        print("please enter a valid number")
        continue

    if guess < random_num:
        print("Guess was too low")
    elif guess > random_num:
        print("Guess was too high")
    else:
        print("Guess was correct!!!")
        break