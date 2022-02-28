import random

counter = 0
randNum = random.randint(1, 100)
WIN = 0
att = 8
print("Enter a number and use the hints given by the game to guess the random number."
      "\nYou should be able to win every time if you use the right strategy."
      "\nGood luck!\n")


while counter < att:
    guess = int(input("Enter a number: "))
    if guess > randNum:
        print("Guess lower")
    elif guess < randNum:
        print("Guess higher")
    else:
        WIN = 1
        break
    counter += 1
    lives = att - counter
    print("lives left: " + str(lives))


if WIN == 1:
    print("The number is: " + str(randNum) + "\nYou win!")
else:
    print("You lost, the number was: " + str(randNum))
