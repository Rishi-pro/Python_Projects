#this would ask python for a random thing
import random
#secret would be the number computer would import from the random
secret= random.randint(1,10)
# ask user to guess the number

guess= int(input('guess the number from between 1 to 10: '))
#this creates a situiation if user does guess or does not guess
if guess==secret:
    print('woah! you guessed the number')
else:
    print('you did not guess the number/nthe correct number was',secret)
