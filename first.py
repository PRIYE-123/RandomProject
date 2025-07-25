#from array import array
#arr = array('i',[1,2,3,4])
#list are built-in , we dont need to import themand array
#means same tupe of element but the list , is not same it can be different one 
#module 
#import math
#print(math.sqrt(7))
#package is a collection of related modules in the directory .
#ex numpy 
#xrange and range()
#range func behaved as s xrange in py 3 , funct that is usedto iterate 
#a certain number of times in for loops in python .
#dictionary comprehension 
#import logging
#logging.basicConfig(level=logging.DEBUG)
#logging.debug("This is a debug message")
#a="Rishu loves anup's eye"
##substg=a[4:1:1]
#print(substring)rin
#import time
#currenttime=time.localtime(time.time())
#rint(currenttime)
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
  