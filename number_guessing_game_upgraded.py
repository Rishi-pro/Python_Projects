#SO THIS IS GOING TO BE THE NEXT VERSION OF THE GUESS GAME
import random 
secret= random.randint(1,20)
chances= 3 #so this would be the major change in this program
while chances>0:
    guess= int(input('guess the number between 1 to 20: '))
    if guess==secret:
        print('woah! you guessed it right')
        break
    else:
        print("you couldn't guess the numebr correctly TRY AGAIN!")
        chances -= 1
        
