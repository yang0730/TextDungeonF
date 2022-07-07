import os,player
from replit import db
username = os.environ['REPL_OWNER']
#load
#[0,100,50,1,1,1,0,0]
def load():
  try:
    if db[username] :
      data = db[username].strip(',')
      for i in range(8):
        player.Status.append(data[i])
      for i in range(6):
        player.CounteredMob.append(data[i+8])
      player.inBattle = True if data[14] == 1 else False
      player.CurLv = data[15]
      player.CurRoom = data[16]
      for i in range(3):
        player.Buffs[i].append(data[i+17])
      for i in range(10):
        player.Equipment.append(data[i+20])
      for i in range(30,len(data),2):
        player.Inventory.append([data[i],data[i+1]])
    else:
      player.Status=[0,100,50,1,1,1,0,0]
      player.CounteredMob=[]
      player.inBattle = False
      player.CurLv = 0
      player.CurRoom = 'Spawn'
      player.Buffs = [0,0,0]
      player.Equipment = [0,0,0,0,0,0,0,0,0,0]
      player.Inventory = [[1,1]]
  except:
    pass

#save

def save():
  savestr=''
  for i in player.Status:
    savestr += i+','
  for i in player.CounteredMob:
    savestr+=i+','
  if player.inBattle:
    savestr+='1,'  
  else: 
    savestr+='0,'
  savestr+=player.CurLv+','
  savestr+= player.CurRoom+','
  for i in player.Buffs:
    savestr+=i+','
  for i in player.Equipment:
    savestr+=i+','
  for i in player.Inventory:
    for j in i:
      savestr+=j+','
  savestr = savestr[:-1]
  db[username] = savestr
  