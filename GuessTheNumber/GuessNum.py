import random

number = random.randint(1, 10)
tries = 1
win = False 
print("Hello!")
name = input("What is your name? ")
print("Hello", name + ".", )

question = input("Would you like to play a game? [Y/N] ")
if question.lower() == "y":
    print("I'm thinking of a number between 1 & 10")
while not win:     
    guess = int(input("Have a guess: "))
    tries = tries + 1
    if guess == number:
        win = True
    elif guess < number:
        print("My number is higher")
    elif guess > number:
        print("My number is lower")
print("Congrats, you guessed correctly. The number was indeed ".format(number))
print("it had taken you.format(tries-1).tries")
