import random

upper_Range=input("Enter you upper range value>>>")

if upper_Range.isdigit():
    upper_Range=int(upper_Range)

    if upper_Range <=0:
        print("please enter positive number")
        quit()
else:
    print("Please enter a valid number next time")
    quit()


random_number=random.randint(0,upper_Range)
guess=0

while True:
    guess +=1
    user_guess=input("Type your guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in", guess, "guesses")


