import random
number = random.randint(1, 10)
while(1):
    guess = input('Please Guess the number between 1-10 :')
    if (int(guess)!= number):
        print("Not correct Please try again ")
    else:
        print("Correct Number")
        exit(0)
