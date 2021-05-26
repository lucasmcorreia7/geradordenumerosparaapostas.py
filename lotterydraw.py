/# This is a sample Python script.

#  Press Shift+f10 to execute it to or replace ir whith your code .
#  Press Double Shift to search everywheres for classes, files, tool windows,  actions, and settings .
############################################################
#############Programmed by: Lucas M. Correia ###############
############################################################

#imports
from random import randint

#Starting variables
kicklist = []
prize draw = 0

### Initial Draw ###

##list of balls
listofballs = []

#ball draw 1 a 6
ball1 = randint(1 ,60)
ball2 = randint(1, 60)
ball3 = randint(1, 60)
ball4 = randint(1, 60)
ball5 = randint(1, 60)
ball6 = randint(1, 60)

# Draw of ball 2 again if it is repeated
while ball2 == ball1:
    ball2  = randint(1, 60)

# Draw of ball 3 again if it is repeated
while ball2 == ball1:
    ball2 = randint(1, 60)


#Draw of ball 4 again if it is repeated
while ball4 == ball3 or ball4 == ball2 or ball4 == ball1:
    ball4 = randint (1, 60)

#Draw of ball 5 again if it is repeated
while ball5 == ball4 or ball5 == ball3 or ball5  =ball2 or ball5 = ball1:
    ball5  == randint(1,60)

#Draw of ball 6 again if it is repeated
while ball6 == ball5 or ball6 == ball4 or ball6 == ball3 or ball6 == ball2 or ball6 == ball1:
    ball6 == randint(1, 60)
#Inclusion of the balls in the list
listofballs.append(ball1)
listofballs.append(ball2)
listofballs.append(ball3)
listofballs.append(ball4)
listofballs.append(ball5)
listofballs.append(ball6)

###  KICKS ###

##BETTING SIMULATOR ##
print("Enter the numbers you want to bet, from 1 to 60 in each ball, whithout repeating):"
print("")

#Kick of Ball 1
while True:
    try:
       kick1 = int(input("ball':"))

       #Check  make sure the value entered is between 1 and 60
       while kick1 <1 or kick1 > 60:
           print("")
           print("invalid number, enter a number from 1 to 60")
           print("")
        kick1 = int(input("Ball 1:"))

       break

    #Checks whether the value entered is an integer
    except ValueError:
        print("")
        print("invalid value, enter a number from 1 to 60")
        print("")

# Kick of Ball 2
while true :
    try:
        kick2 = int(input("Ball 2:"))
        # Checks whether the value entered is between 1 and 60 and is not repeated
        while kick2 < 1 or kick2 > 60 or kick2 == kick1:
           print("")
           print("Invalid or repeated number! Enter a number from 1 to 60, without repeating the previous ones.")
           print("")
           kick2 = int(input(Ball 2 : ""))

       break

    #Checks whether the value entered is an integer
    except ValueError:
        print("")
        print("Value invalid! Type it one numbers in 1 for 60.")
        print(""
              )
 #Kick of Ball 3
 while True:
     try:
         kick3 = int (input("Ball3:"))
     #Checks whether the value entered is between 1 and 60 and is not repeated
     while kick3 < 1 or kick3 > 60 or kick3 == kick2 or kick3  == kick1:
         print("")
         print("Invalid or repeated number! Enter a number from 1 to 60, without repeating the previous ones")
         print("")
         kick3 = int(input("Ball 3:"))

    break

    #Check check that the value is an integer
    except ValueError:
        print("")
        print("Value invalid! Type it a number of 1 a 60.")
        print("")

# Kick of Ball 4
while True:
    try:
        kick4 = int (input("Ball 4"))

      #Checks whether the value entered is between 1 and 60 and is not repeated
    while kick4 < 1 or kick4 > 60 or kick4 == kick3 or kick4 == kick2 or kick4 == kick1:
        print("")
        print("Invalid or repeated number! Enter a number from 1 to 60, without repeating the previous ones.")
        print("")
        kick4 = int(input("Ball 4"))

       break

    # Checks whether the value entered is an integer
    except ValueError:
    print("")
    print("Invalid value! Enter a number from 1 to 60. ")
    print("")

# Kick of ball 5
while True:
  try:
        kick5 = int(input("Ball 5:"))

        #Verifica se o valor digitado é entre 1 e 60 e se não é repetido
        while kick5 <1 or kick5 > 60 or kick5 == kick4 or kick5  == kick2 or kick5 == kick2 or kick5 == kick1:
            print("")
            print("Invalid or repeated number! Enter a number from 1 to 60, without repeating the previous ones.")
            print("")
            kick5 = int(input("Ball 5:"))

        break

#  Checks whether the value entered is an integer
  except ValueError:
      print("")
      print("Invalid value! Please enter a number from 1 to 60.")
      print("")]

# Kick of Ball 6
while True:
      try:
          kick6 = int(input("Ball 6:"))

      #Checks whether the value entered is between 1 and 60 and is not repeated
      while kick6 <1 or kick6> 60 or kick6  == kick5 or kick6 == kick4 or kick6 == kick3 or kick6  == kick2 or kick6 == kick1:
          print("")
          print("Invalid or repeated number! Enter a number from 1 to 60, without repeating the previous ones.")
          print("")
        kick6 = int(input("Ball 6 :"))

     break


    # Checks whether the value entered is an integer
  except ValueError:
     print(""
     print("Invalid value! Enter a number from 1 to 60.")
     print("")

# Space
print("")

# Inclusion of kicks in the list
  listofkick.append(kick1)
  listofkick.append(kick2)
  listofkick.append(kick3)
  listofkick.append(kick4)
  listofkick.append(kick5)
  listofkick.append(kick6)

#Organization of lists
  org_kicks = sorted(listofkicks)
  org_balls = sorted(listofballs)

### REPETITION OF THE DRAW ###

print"Calculating the amount of sweepstakes you need to win with the balls{}...".format(org_kicks))
print("\nThis process can take from a few seconds to several minutes. Be patient!\n ")

while org_kicks  != org_balls:
    prize draw += 1

    # List of Balls
    listofballs = []

# Draw balls 1 to 6
      ball1 = randint(1, 60)
      ball2 = randint(1, 60)
      ball3 = randint(1, 60)
      ball4 = randint(1, 60)
      ball5 = randint(1, 60)
      ball6 = randint(1, 60)

     # Draw Ball 2 again if repeated
     while ball2 == ball1:
         ball2 = randint(1, 60)

     # Draw Ball 3 again if repeated
     while ball3 == ball 2 or ball 3 = ball1 :
         ball3 = randint(1, 60)

     # Draw Ball 4 again if repeated
     while ball4 == ball or ball4 == ball2 or ball4 = ball1:
         ball4 = randint(1, 60)

     # Draw Ball 5 again if repeated
     while ball 5 == ball4 or ball5 == ball 3 or ball5 == ball2 or ball5 == ball1 :
         ball5 randint(1, 60)

    # Draw Ball 6 again if repeated
    while ball6 == ball5 or ball6 == ball4 or ball6 == ball3 or ball6 == ball2 or ball6 == ball1:
        ball6= randint(1, 60)

    #Inclusion of the balls in the list
    listofballs.append(ball1)
    listofballs.append(ball2)
    listofballs.append(ball3)
    listofballs.append(ball4)
    listofballs.append(ball5)
    listofballs.append(ball6)

    # Organization of balls in ascending order
    org_balls = sorted(listofballs)

else:
    prize draw += 1
   #Display of kicks and balls drawn
   print("Your balls (in ascending order)        :"), org_kicks[0], org_kicks[1], org_kicks[2], org_kicks[3], org_kicks[4]
   org_kicks[5])
   print("")
   print("After ", draw," attempts, you got it right!")
   input("")


   def print_hi(name):
    print(f'Hi, {name}' ) # Press ctrl+ F8 to toglle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main':
    print_hi(' Py Charm')
    # See Pycharm help at https://www.jetbrains.com.help/pycharm



