#coin flip game 2021 v1 12th May 2021 

#coin flip variables

import sys
import random


twoPennyCoin = 300
fivePennyCoin = 500
tenPennyCoin = 750
twentyPennyCoin = 900
fiftyPennyCoin = 1100
onePoundCoin = 1300
twoPoundCoin = 1500


#login system
import os, time, random
from replit import db

def clear():
  os.system('clear')
  time.sleep(1)


def coinFlip():
  global winStreak
  global score
  global lives
  lives = 10
  score = 0
  winStreak = 0
  heads = False
  tails = False
  hort = input ("Heads or Tails? ")
  if hort.lower() == "heads":
    heads = True
  elif hort.lower() == "tails":
    tails = True
  else:
    print("Invalid")
    sys.exit()
    #
  flipResult = random.randint(1,2)
  if flipResult == 1 and heads == True:
    time.sleep(3)
    winStreak = winStreak + 1
    score = score + 100
    print("Correct! The result was heads! You have been awarded 100 coins!")
    print("Winstreak: ", winStreak)
  if flipResult == 2 and heads == True:
    time.sleep(3)
    winStreak = winStreak + 0 
    score = score + 50
    print("Unlucky, the result wasn't heads, however here is 50 coins!")
    print("Winstreak: ", winStreak)
    lives = lives - 1
    print("Lives Remaining: ", lives)
  if flipResult == 1 and tails == True:
    time.sleep(3)
    winStreak = winStreak + 1
    score = score + 100
    print("Correct! The result was heads! You have been awarded 100 coins!")
    print("Winstreak: ", winStreak)
  if flipResult == 2 and tails == True:
    time.sleep(3)
    winStreak = winStreak + 0 
    score = score + 50
    print("Unlucky, the result wasn't heads, however here is 50 coins!")
    print("Winstreak: ", winStreak)
    lives = lives - 1
    print("Lives Remaining: ", lives)
  return lives













































def LS():
  loggedin = 0

  ls = input("Do You Want To\n[1] Sign Up\n[2] Login\n[3] Continue Without Login\n")
  if ls == "1":
    susername = input("Username: ")
    spassword = input("Password: ")
    db[susername] = spassword
    print("Successfully Logged In!")
    LS()
  elif ls == "2":
    username = input("Username: ")
    password = input("Password: ")
    allUsernames = db.keys()
    if username in allUsernames:
      realpassword = db[username]
      if password == realpassword:
        print("Log In Successful!")
        loggedin = 1
        time.sleep(1)
        clear()
        coinFlip()
































      else:
        print("Password Is Wrong!")
        time.sleep(1)
        clear()
    else:
      print("Username Not Found!")
      time.sleep(1)
      clear()
  elif ls == "3":
    loggedin = 0
    guestusername = "Guest" + str(random.randint(0, 999))
    print("Your Username Is " + guestusername)
  else:
    print("Not An Option!")
LS()
#
#
#
#
#

