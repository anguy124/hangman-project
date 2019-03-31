__author__ = 'anguyen'
import random

#open the file
file = open("capitals.txt", "r")
line = random.choice(open("capitals.txt").readlines())
print(line)

#turn string into a list
convert = list(line)
convert.remove("\n")
temp = list(line)
temp.remove("\n")

#gets rid of the commas
for i in range(len(temp)):
    if str.isalpha(temp[i]):
        temp[i] = "_"
tempPrint = "".join(temp)
print(tempPrint)

gameOver = False

#guess the letter
#while i in range(len(convert)):
while gameOver is False:
    guess = input(" \n Enter a letter to guess the name: \n")
    if guess not in convert:
        print(guess+ " is not in the answer\n")
    else:
        print(guess + " is in the answer")
#if the guess matches the letter in the line reveal it

    for i in range(len(convert)):
        if guess in convert[i]:
            temp[i] = guess
            tempPrint = "".join(temp)
    print(tempPrint)
    if temp == convert:
        print("Congratulations you won!!!")
        gameOver = True
file.close()










