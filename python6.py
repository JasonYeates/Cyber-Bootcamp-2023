# Bob wants to create a guessing number game! 
# Rule 1: Numbers have to be between 1 and 20
# Rule 2: Program must run until the correct number is guessed
# Rule 3: When guessed right, print out how many tries to guess the 
# right number. Example: "Yes! You guessed it in ___ guesses."
# Rule 4: The program will tell you if your number needs to be HIGHER
# or LOWER 
# until the number is guessed correctly and the program ENDS.
# Remeber to import the random function
#Bonus objective can you put it into a loop to make the game end after 3 turns?

import random
R=random.randint(1,20)
t=1
while 1==1: #t<4:
    N=int(input("pick a number"))
    print (t)
    print (R)
    if (N == R): #or (t==3):
        print ("you guessed it in",t,"guesses")
        break
    elif R > N:
        print ("too low")
        print ("try again")
        t=t+1
    elif R < N:
        print ("too high")
        print ("try agian")
        t=t+1