from random import randint
guesses = 0
print("number from 1 to 10 has been chosen.")
number = randint(1,10)
while True:
    guesses += 1
    x = int(input("Guess the number: "))
    if x == number:
        print('correct')
        break
    elif x > number:
        print('too high')
    elif x < number:
        print('too low')
print(f'It took {guesses} guesses')