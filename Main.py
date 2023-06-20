import sys,time
import random

def sprint(str):
  for c in str + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(3./90)

def theDoubleCross():
  sprint("It seems it is time to eat, for I am a Spider and you are the treat")
  directions = ["Wait", "Fly"]
  userInput = ""
  while userInput not in directions:
    sprint("Options: Wait/Fly")
    userInput = input()
    if userInput == "Wait":
      sprint("Good little fly, you know your place")
      break
      return
    elif userInput == "Fly":
      sprint("You dissapoint me fly, you should know your place")
      sprint("Roll three die, two of the same number and you survive")
      die1 = random.randint(1,6)
      die2 = random.randint(1,6)
      die3 = random.randint(1,6)
      print("Die 1=",die1, "Die 2=",die2, "Die 3=",die3,)

      if die1 == die2:
        sprint("You are a very lucky fly")
        sprint("You live to fight another day")
        break
        return
      if die1 == die3:
        sprint("You are a very lucky fly")
        sprint("You live to fight another day")
        break
        return
      if die2 == die1:
        sprint("You are a very lucky fly")
        sprint("You live to fight another day")
        break
        return
      if die2 == die3:
        sprint("You are a very lucky fly")
        sprint("You live to fight another day")
        break
        return
      if die3 == die1:
        sprint("You are a very lucky fly")
        sprint("You live to fight another day")
        break
        return
      if die3 == die2:
        sprint("You are a very lucky fly")
        sprint("You live to fight another day")
        break
        return
      else:
        sprint("DINNER TIME!!")
        sprint("Your luck ran out, the spider caught the fly")
        break
        return

def question3():
  directions = ["Answer","Refuse"]
  sprint("Answer me one more riddle, and I shall let you go free")
  userInput = ""
  while userInput not in directions:
    sprint("Options: Answer/Refuse")
    userInput = input()
    if userInput == "Answer":
      sprint("Good choice little fly, and so we go again...")
      sprint("What does man love more than life, hate more than death or mortal strife; that which contented men desire; the poor have, the rich require; the miser spends, the spendthrift saves, and all men carry to their graves?")
      sprint("Options: Money, Time, Nothing")
      userInput = input()
      if userInput == "Nothing":
        sprint("Are you just a fly? It would almost be a shame to eat you")
        theDoubleCross()
      else:
        sprint("Bad luck little fly, time to die")
        break
        return
    elif userInput =="Refuse":
        print(figlet_format("Wrong choice im afraid little fly, now I must eat you....", font = "sblood"))
    break
    return

def question2():
  directions = ["Answer","Refuse"]
  sprint("Answer me two more riddles, and I shall let you go free")
  userInput = ""
  while userInput not in directions:
    sprint("Options: Answer/Refuse")
    userInput = input()
    if userInput == "Answer":
      sprint("Good choice little fly, and so we go again...")
      sprint("What breaks but never falls, and what falls but never breaks?")
      sprint("Options: Seasons, Gravity, Day and Night")
      userInput = input()
      if userInput == "Day and Night":
        sprint("Right again, you might just survive after all")
        question3()
      else:
        sprint("Bad luck little fly, time to die")
        break
        return
    elif userInput =="Refuse":
      sprint("Wrong choice im afraid little fly, now I must eat you....")
    break
    return

def theRiddle():
  directions = ["Answer","Refuse"]
  sprint("Answer me three riddles, and I shall let you go free")
  userInput = ""
  while userInput not in directions:
    sprint("Options: Answer/Refuse")
    userInput = input()
    if userInput == "Answer":
      sprint("Good choice little fly, and so we begin...")
      sprint("What is so fragile that saying its name breaks it?")
      sprint("Options: Vase, Silence, Sleep")
      userInput = input()
      if userInput == "Silence":
        sprint("Clever little Fly")
        question2()
      else:
        sprint("Bad luck little fly, time to die")
        break
        return
    elif userInput == "Refuse":
      sprint("Wrong choice im afraid little fly, now I must eat you....")
    break
    return

def theSpider():
  directions = ["Agree","Disagree"]
  sprint("What do I have here? It seems someone has joined me for dinner")
  userInput = ""
  while userInput not in directions:
    sprint("Options: Agree/Disagree")
    userInput = input()
    if userInput == "Agree":
      sprint("You will join me for dinner, how lovely. Tell me little fly do you enjoy riddles?")
      theRiddle()
    elif userInput == "Disagree":
      sprint("How rude of you fly, you dissapoint me")
      theDoubleCross()
    else:
      sprint("Please copy exact spelling")

def theWeb():
  directions = ["Struggle", "Stay still"]
  sprint("What do you do little fly?")
  userInput = ""
  while userInput not in directions:
    sprint("Options: Struggle/Stay still")
    userInput = input()
    if userInput == "Struggle":
      theSpider()
    elif userInput == "Stay still":
      print("You have accepted your fate, you sense the vibrations of your end approaching.....and darkness")
      return
      break
    else:
      sprint("Please copy exact spelling")

if __name__ == "__main__":
  while True:
      print("The Spider to the Fly")
      sprint("Welcome said the Spider to the Fly")
      sprint("You are the fly, you have landed in her web")
      sprint("Can you answer her riddles, and avoid being eaten?")
      sprint("Answer wisely, your life depends on it")
      sprint("What is your name, little Fly?: ")
      player_name = input()
      sprint("Good luck, " +player_name+ ".")
      theWeb()