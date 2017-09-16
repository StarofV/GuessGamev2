import time 
from os import name
from os import system as console
from random import randint
print(r''' __      __       .__                                  __             __  .__                                                 .__                                                
#   __      __       .__                               
#  /  \    /  \ ____ |  |   ____  ____   _____   ____  
#  \   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \ 
#   \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/ 
#    \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >
#         \/       \/          \/            \/     \/
Woahhh! Guess game v2? Made by me and Yuki(Yuki didn't make v2).. add me in discord Rick sanchez#5068''')

def delay(x):
  time.sleep(x)

def clear():
  console('cls' if name == "nt" else "clear")


def another(x):
    guessit = randint(1, x)
    
    guess = None
    
    print("Enter your guess between 1 and %d\n" % x)
    
    while guess != guessit:
      try:
        guess = int(input())
        print("Lower" if guess > guessit else "Higher")  
        
        
        if guess == guessit:
          print("You made it into the next level!")
          delay(1)
          clear()
          another(x + 10)
      except ValueError:
        print("Enter a number..")
          
if __name__ == '__main__':
  another(10) # start of the generated number by 10.
