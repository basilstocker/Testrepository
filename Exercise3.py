import random
x = random.randint(1,101)
name = input("Choose a new name! ")

y = int(input("Hey {}, we are playing a guessing game together. Your goal is to find a number between 1 and 100.\nHave a guess! ".format(name)))
guesses = 1
while y != x:
    if y < x:
        print("Your guess ({}) was too low!".format(y))
        y = int(input("Have a new guess! "))
        guesses = guesses + 1
    else:
        print("Your guess ({}) was too high!".format(y))
        y = int(input("Have a new Guess! "))
        guesses = guesses + 1
if guesses == 1:
    a ='try'
else:
    a ='tries'
print("Wow {}, you achieved your life goal and guessed the random number correctly in only {} {}!!".format(name,guesses,a))
print("WWWW      WWWW      WWWW      OOOO      WWWW      WWWW      WWWW\n"
      " WWWW    WWWWWW    WWWW     OOOOOOOO     WWWW    WWWWWW    WWWW\n"
      "  WWWW  WWWWWWWW  WWWW    OOOO    OOOO    WWWW  WWWWWWWW  WWWW\n"
      "   WWWWWWWW  WWWWWWWW     OOOO    OOOO     WWWWWWWW  WWWWWWWW\n"
      "    WWWWWW    WWWWWW        OOOOOOOO        WWWWWW    WWWWWW\n"
      "     WWWW      WWWW           OOOO           WWWW      WWWW")