import random

# EmirXK


# the program is coded so you can add as many words as you want
# the words have no character limit


words = ["orman",
         "hastane",
         "defter",
         "kosova",
         "ayran",
         "elbise",
         "balik",
         "manisa",
         "osmanli",
         "muvaffakiyetsizlestiricilestiremediklerimizdenmissinizcesine",
         "kelime",
         "avustralya",
         "playstation",
         "makedonya"]

limit = len(words)

rand_num = random.randint(0, limit-1)

length = len(words[rand_num])

check = [0] * length

k = 0

i = 0
while i < length:
    check[i] = 0
    i += 1
i = 0

lives_num = length * 2
print("Lives_num: " + str(lives_num))
print("\n")

num_correct = 0
temp = 0
guess = ''

WIN = False

while num_correct < length:
    print("\033[1;00m")
    if lives_num <= 0:
        break

    while i < length:
        if check[i] == 1:
            print(words[rand_num][i], end="")
        else:
            print("-", end="")
        i += 1

    print("\n")

    guess = input("Enter a guess letter: ")
    i = 0

    if guess == words[rand_num]:
        WIN = True
        break

    temp = num_correct
    k = 0
    while i < length:
        if guess == words[rand_num][i] and check[i] != 1:
            while k < 1:
                print("'" + guess + "'" + " is a right guess")
                k += 1
            num_correct += 1
            check[i] = 1
        i += 1

    if num_correct == temp:
        print("Wrong guess, ", end="")
        lives_num -= 1
        print("Lives: " + str(lives_num))

    i = 0
    print("\n")


if num_correct == length or WIN:
    print("You win, the word is: ", end="")
    print("\033[1;36m" + str(words[rand_num]))
else:
    print("Sorry, you lost. The word was: ", end="")
    print("\033[1;36m" + str(words[rand_num]))
