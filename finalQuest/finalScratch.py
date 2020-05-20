def initialGame():

   started = False
   while not started:
      print("\n\t\t\tWelcome to my game human:")
      ans = input("\t\t\tWould you like to go first? (y/n)")
      if ans.upper() == "Y":
         firstPlayerHuman = True
         print("\n\t\t\tThe human has choosen to go first. Good luck!!\n\n")
         started = True
      elif ans.upper() == "N":
         firstPlayerHuman = False
         print("\n\t\t\tThe human has choosen to go second. Good luck!!\n\n")
         started = True
      else:
         print("\n\t\t\tPlease answer 'y' or 'n' only.")
         started = False

   return(firstPlayerHuman)
###################################################################################################


###################################################################################################
def refHumanScreen(gameCounter):
   goodUserInput = False

   while not goodUserInput:
      numbers = input("Human please enter your next 1,2, or 3 integer numbers in the remaining sequence? ")
      numList = numbers.split(",")

      #Check to see if there are more than 3 numbers entered
      if len(numList) > 3:
         num_invalid = True
      else:
         num_invalid = False

      #Check to see if any of the values entered are not integer numbers
      if not num_invalid:
         for i in range(len(numList)):
            try:
               numList[i] = int(numList[i])
            except:
               num_invalid = True
               break

      #Sort the user entry
      if not num_invalid:
         numList.sort()

         #Check to see the user entered the next in the sequence and the last
         #If the user entry is valid update the game counter to his last entry.
         if (numList[0] != gameCounter) or (numList[-1] != gameCounter + len(numList) -1 ):
            num_invalid = True
         else:
            goodUserInput = True

   #Check to see if you lost
   if numList[-1] >= 21:
      lost = True
   else:
      lost = False

   return(lost,numList[-1]+1)
###################################################################################################
      


###################################################################################################
def refComputerScreen(gameCounter):
   nums2Generate = random.randint(1,3)

   numList = []
   for i in range(nums2Generate):
      numList.append(gameCounter + i)

    #Check to see if you lost
   if numList[-1] >= 21:
      lost = True
      return(lost,-1)
   else:
      lost = False

   #Convert the computer number list to text for printing
   nstring = ""
   for i in range(len(numList)):
      nstring += str(numList[i])
      nstring += ","

   #Remove the last comma
   sc = len(nstring)-1
   nstring = nstring[:sc]

   print("Human, here is", nums2Generate, "more numbers in the sequence for you: ", end = "")
   print(nstring)

  
   
   #Update the Game counter and return it
   return(lost,numList[-1]+1)

###################################################################################################               
     

###################################################################################################
def start():
   firstPlayerHuman = initialGame()
   gameCounter = 1
   gameEnd = False

   #Start Game of with human player first
   if firstPlayerHuman:
      while not gameEnd:
         lost, gameCounter = refHumanScreen(gameCounter)
         if lost:
            print("You lost!")
            gameEnd = True
         else:
            lost, gameCounter = refComputerScreen(gameCounter)
            if lost:
               print("You won!")
               gameEnd = True

   #Start Game of with Computer player first
   else:
      while not gameEnd:
         lost, gameCounter = refComputerScreen(gameCounter)
         if lost:
            print("You won!")
            gameEnd = True
         else:
            lost, gameCounter = refHumanScreen(gameCounter)
            if lost:
               print("You lost!")
               gameEnd = True
###################################################################################################


if __name__ == "__main__":
   import random
   start()
