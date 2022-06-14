# Monkey Island

## 
class players:
  def __init__(self, name, position = 0, dead = False):
    self.name = name
    self.position = position
    self.dead = dead
  
  def __repr__(self):
    name = self.name
    pos = str(self.position)
    if self.dead == True: 
      print("{} is dead".format(name))
    else:
      print("{} is in posistion {}".format(name, pos))

  def loose(self):
    self.position = 0
    print("{} lost".format(self.name))

  def win(self):
    self.position += 1
    if self.position == 3:
      print("{} wins".format(self.name))
    else:
      print("{} is in posistion {}".format(self.name, self.position))

## create players
player1 = players("Guybrush Threepwood")
player2 = players("Danny")

class insult:
  def __init__(self, curse, re1, re2, win_no = 1, responces = {}):
    self.curse = curse
    self.responce1 = re1
    self.responce2 = re2
    self.win_no = win_no
    self.responces = {1:re1 , 2:re2}

  def __repr__(self):
    return self.responces

  def check(self):
    if self.win_no == 1:
      print('curse is "{}". The winning curse is "{}". The loosing curse is "{}".'.format(self.curse, self.responce1, self.responce2))
    else: 
      print('curse is "{}". The winning curse is "{}". The loosing curse is "{}".'.format(self.curse, self.responce2, self.responce1))

  def attack(self,player1, player2):
    print('{} said "{}". {}, what is your responce. 1 "{}" or 2 "{}"'.format(player1.name, self.curse, player2.name, self.responce1, self.responce2))
    choice = input("please pick 1 or 2?")
    while choice != "1" and choice != "2":
      choice = input("Sorry, please pick 1 or 2?")
    if choice == "1":
      player1.loose()
    else:
      player1.win()

curse1 = insult("You fight like a dairy Farmer!", "How appropriate. You fight like a cow!", "I am rubber you are glue" )
curse2 = insult("I once owned a dog that was smarter than you", "You run THAT fast", "He must have taught you everything you know", 2)
curse3 = insult("En Garde!  Touche!", "Oh, that is so cliche.", "Is that your face? I thought it was your backside.")

curse1.attack(player1, player2)
