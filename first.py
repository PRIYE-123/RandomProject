#Binary search 
import random
print("Hi , welcome to the game .let's start")
#step 1 : Enter the range that is lower and upper bound 
low=int(input("enter the highrt bound:"))
high=int(input("enter the higher bound:"))
print("condition is you have only 7 chances, let's start")
num=random.randint(low, high)
ch=7  #chances 
gc=0  #global counter
while gc<ch:
    gc+=1
    guess=int(input('enter your guess: '))
    if guess==num:
        print("correct!the number is {num},you guessed it in {gc)} attempt")
        break
    elif gc>=7 and guess != num:
        print("sorry ! the number was {num}, better luck next time.")
    elif guess > num:
        print("too high")
    elif guess < num:
        print("too low")
  