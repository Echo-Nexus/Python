import random as ran

isPlaying = True
userInput = int(input("Guess the number : "))
round = 1

while (isPlaying) :
  num = ran.randint(1, 100)
  count = 1

  while(userInput != num):
      if( userInput > num ) :
        print("\nToo High !!!")
        userInput = int(input("Try again : "))
        count += 1
      elif( userInput < num ) :
        print("\nToo Low !!! ")
        userInput = int(input("Try again : "))
        count += 1

  if(userInput == num):
    print("\nYou guessed the correct number in ", count, "attempts...")
    print("\nDo you want to play again ? (Y/N) : ")
    playAgain = input()
    print("\n")

    if(playAgain == "Y" or playAgain == "y"):
        isPlaying = True
        userInput = int(input("Guess the number : "))
        round += 1
    else:
        isPlaying = False
        print(f"You played {round} rounds. Thanks for playing...")