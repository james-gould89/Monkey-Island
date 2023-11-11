# Monkey Island

## dictionary of 6 no. of insults and correct responces
insults_and_responces = {"You fight like a dairy Farmer!":"How appropriate. You fight like a cow!","I once owned a dog that was smarter than you":"He must have taught you everything you know", "En Garde!  Touche!":"Oh, that is so cliche.","Now I know what filth and stupidity really are.":"I'm glad to hear you attended your family reunion.","You are a pain in the backside, sir!":"Your hemorrhoids are flaring up again, eh?", "I hope you have a boat ready for a quick escape.":"Why, did you want to borrow one?"}
insults = [insult for insult in insults_and_responces.keys()]
responces = [responce for responce in insults_and_responces.values()]

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
player2 = players("Le Chuck")

def pick_option(choices):
  for i in range(len(choices)):
    print("{}. {}\n".format(str(i+1), choices[i]))
  idx_choice = len(choices)+1
  while idx_choice not in range(len(choices)):
    idx_choice = int(input("please pick 1 - {} ? \n".format(len(choices))))-1
  return choices[idx_choice]

def attack(player1, player2, insult):
  print('''{} said
"{}". 

{}, 
what is your responce?  
    '''.format(player1.name, insult, player2.name))
  responce = pick_option(responces)
  if responce == insults_and_responces[insult]:
    player1.loose()
    choose_attack(player2, player1)
  else:
    player1.win()
    if player1.position < 3:
      choose_attack(player1, player2)
      # else replay()

def choose_attack(player1, player2):
  print('''
{},

It is your turn to choose an insult, 
please choose one of the following:

 '''. format(player1.name))
  insult=pick_option(insults)
  attack(player1, player2,insult)


def StartGame():
  print("""
                 ___      _    _   _  _  _   _ ___    _   _
                  |  |_| |_   (_` |_ /  |_) |_  |    / \ |_
                  |  | | |_   ._) |_ \_ | \ |_  |    \_/ |
___        ___      _     ___         ___ ___      ___  _______ ___       ___
\  \      /  /   ,'___`.  `. `.       \ / \ /    ,' ,' |  _____\`. `.   ,' ,'
|   \    /   |  / /   \ \  |   `.     | | | |  ,' ,'   | |        `. `.' ,'
|    \  /    | | |     | | | |`. `.   | | | |,' ,'     | |_,|       `. ,'
|  |\ \/ /|  | | |     | | | |  `. `. | | |   , `.     |  _ |        | |
|  | \  / |  |  \ \___/ /  | |    `. `| | | ,' `. `.   | | `'        | |
|  |  \/  |  |   `.___,'   /_\      `.  | /_\    `. `. | `--.._;|    | |
|  |      /  \   _   _,----._, .---.  `.|        /\````'---_..__|    | |
|  |      \  / ,' | / ,-'''-.|  \ /             /  \      \  \   ___ _-|
/  \       \/  |  | | |      '  | |            / /\ \     |   \  \ / \`'--._
\  /           |  | \ `-.__     | |           / /  \ \    | |\ \ | | | |`-._`-.
 \/            |  |  `-.__ `-.  | |          / /____\ \   | | \ \| | | |    `. \ 
               |  |        \ |  | |____,'|  / ,------. \  | |  \ ' | | |     | |
               |  | |`-....' /  '--------' '-'        \_\ /_\   \  | | |     | |
               |  | ''------'                                    \ | /_`-....' /
               |  |                                               \|    '-----'
               /  \ 
          jrei \  /
                \/
                
╔╦╗┬ ┬┬┌─┐  ┬┌─┐  ╔╦╗┌─┐┌┐┌┬┌─┌─┐┬ ┬  ╦┌─┐┬  ┌─┐┌┐┌┌┬┐   
 ║ ├─┤│└─┐  │└─┐  ║║║│ ││││├┴┐├┤ └┬┘  ║└─┐│  ├─┤│││ ││   
 ╩ ┴ ┴┴└─┘  ┴└─┘  ╩ ╩└─┘┘└┘┴ ┴└─┘ ┴   ╩└─┘┴─┘┴ ┴┘└┘─┴┘   
     ╔═╗┌┐┌┌┬┐  ╔╦╗┬ ┬┌─┐  ╦  ┌─┐┌─┐┌┬┐  ╔═╗┬ ┬┌─┐
     ╠═╣│││ ││   ║ ├─┤├┤   ║  │ │└─┐ │   ║  │ │├─┘
     ╩ ╩┘└┘─┴┘   ╩ ┴ ┴└─┘  ╩═╝└─┘└─┘ ┴   ╚═╝└─┘┴  

   {} and {} have both lost thier cup and think it has been stolen. 
   You must both dule till the other wins. 
   
   Use your best insults to win. 
   You need to successuflly insult your opponent 3 times in a row to win.
   
   {} you will play go first!!
   """. format(player1.name, player2.name, player1.name))
  
  temp = input("please press any key to continue")

  choose_attack(player1, player2)

##choose_attack(player1, player2)
StartGame()
##curse1.attack(player1, player2)
