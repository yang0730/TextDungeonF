import game,time,save

print(' _____         _     ____                                     ')
print('|_   _|____  _| |_  |  _ \\ _   _ _ __   __ _  ___  ___  _ __  ')
print('  | |/ _ \\ \\/ / __| | | | | | | | \'_ \\ / _` |/ _ \\/ _ \\| \'_ \\') 
print('  | |  __/>  <| |_  | |_| | |_| | | | | (_| |  __/ (_) | | | |')       
print('  |_|\\___/_/\\_\\\\__| |____/ \\__,_|_| |_|\\__, |\\___|\\___/|_| |_|')        
print('                                        |___/              ')
time.sleep(3)
try:
  if save.db[save.username]:
    print('Welcome back, '+save.username)
    time.sleep(1)
except:
  print("Hello, "+save.username)
  time.sleep(1)
while 1:
  
  game.game()
