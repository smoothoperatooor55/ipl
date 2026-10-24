import pandas
import json
data = pandas.read_excel("list.xlsx")
teamsBudget = {"CSK":12500,"MI":12500,"RCB":12500,"RR":12500,"DC":12500,"GT":12500,"LSG":12500,"SRH":12500,"KKR":12500,"PBKS":12500}
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
    if(team in teamsBudget):
      price = int(input("Enter price sold at: "))
      if(teamsBudget[team]>=price):
        teamsBudget[team]-=price
        print(playername,"sold to",team,"for",price)
        break;
      else: 
        print(team , "doesn't have enough money")
    else:
      print("Invalid Team")


def showbudget():
  for team, money in teamsBudget.items():
    print(team,": ",money,end="  ")
  print("\n")

for i in range(2,501):
  print("Player number: ",i-1)
  sell(i)
  showbudget()