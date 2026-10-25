import pandas
import json
import sys
data = pandas.read_excel("list.xlsx")
with open("players.json","r") as players:
  teamsPlayers = json.load(players)
def sell(number):
  playername=data.iat[number,2]
  print("Selling ",playername)
  while True:
    team = input("Enter team: ")
    if(team=="U"):
      print(playername,"unsold")
      break;
    if(team in teamsPlayers.keys()):
      price = int(input("Enter price sold at: "))
      if(teamsPlayers[team][0]>=price):
        teamsPlayers[team][0]-=price
        print(playername,"sold to",team,"for",price)
        teamsPlayers[team][1].append(playername)
        break;
      else: 
        print(team , "doesn't have enough money")
    else:
      print("Invalid Team")
def reset():
  resetlist={"CSK":[12500,[]],"MI":[12500,[]],"RCB":[12500,[]],"RR":[12500,[]],"DC":[12500,[]],"GT":[12500,[]],"LSG":[12500,[]],"SRH":[12500,[]],"KKR":[12500,[]],"PBKS":[12500,[]],"index":1}
  with open("players.json","w") as players:
    json.dump(resetlist, players, indent=4)
  exit()
def savePlayers(i):
  teamsPlayers["index"]=i;
  with open("players.json","w") as players:
    json.dump(teamsPlayers, players, indent=4)
def showbudget():
  for team, money in teamsPlayers.items():
    if type(money)==type(0):
      continue
    print(team,": ",money[0],end="  ")
  print("\n")
def showPlayers():
  for team,players in teamsPlayers.items():
    if type(players)==type(1):
      continue
    print(team,": ",*(players[1]))
  exit()
    
try:
  if sys.argv[1]=="reset":
    reset();
  elif sys.argv[1]=="show":
    showPlayers()
except IndexError as err:
  pass

start = teamsPlayers["index"]+1
for i in range(start,501):
  print("Player number: ",i-1)
  sell(i)
  showbudget()
  savePlayers(i)