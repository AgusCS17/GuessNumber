import art
import os
import random


EASY_LEVEL = 10
HARD_LEVEL = 5

def level():
    level = input("Choose the level. Type 'easy' or 'hard': ")

    if level == "easy":
        return EASY_LEVEL
    elif level == "hard":
        return HARD_LEVEL
  
    
def Check(guess, answer, turn):
    if guess > answer:
        print("Too High")
        return turn - 1
    elif guess < answer:
        print("Too Low")
        return turn - 1
    else:
        print("You have guess the right number!!!")

def game():
    
    print(art.logo)
    answer = random.randint(1,50)
    turn = level()
    print(answer)
    print("I'm Thinking a Number 1 to 50. Try to guess it!!!")
    guess = 0
    while guess != answer :
        print(f"You have {turn} more attemps to make a guess.")
        
        guess = int(input("Make a guess: "))
           
        turn = Check(guess, answer, turn)

        if turn == 0:
            print("You have no more attemps. You Lose!!!!")
            return
        elif guess != answer:
            print("Try Again")
            
        
game()