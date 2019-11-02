import random

n = random.randint(1, 99)
print(n)
guess = int(input("Guess the number I have in my mind. \nEnter an integer from 1 to 99: "))
while n != guess:
    print
    if guess < n:
        print("ur Yguess is low. Try again.")
        guess = int(input("Enter an integer from 1 to 99: "))
    elif guess > n:
        print("Your guess is high. Try again.")
        guess = int(input("Enter an integer from 1 to 99: "))
    else:
        print("You guessed it!")
        break
    print
    
