
import random
name = input("what is your name ? ")
print("Good Luck!",name)
#possible words 
words =['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
#choose the word 
word=random.choice(words)
#Prompting the User to Guess
print("Guess the characters")
# Initializing Guesses and Turns
guesses=''
turns= 12 
while turns>0:
    failed=0
for char in word:
    if char in guesses:
        print(char, end=" ")
    else:
        print("_",end=" ")
        failed += 1
    if failed==0:
        print("Congrats!,you win")
        print("The word is: ",word)
        break
    guess=input("guess the charcter")
    guesses+=guess
    if guess not in word:
        turns -=1
        print("wrong")
        print("you have",+turns,'more guesses')
    if turns==0:
        print("You loose")


