import requests, random
from threading import Thread

output = []
threads = []
threadc = 500
usernames = open('combo.txt','r').read().splitlines()

proxies = open('proxies.txt',encoding='UTF-8',errors='ignore').read().splitlines()
prox = [{'https':'http://'+proxy} for proxy in proxies]

def divide(stuff):
    return [stuff[i::threadc] for i in range(threadc)]

def getpast(users):
    for username in users:
        try:
            try:
                user,password = username.split(':',1)
            except: continue
            r = requests.get(f'http://api.roblox.com/users/get-by-username?username={user}',proxies=random.choice(prox)).json()
            if 'errorMessage' in r: continue
            output.append(r['Username']+':'+password+'\n')
        except Exception:
            pass

print('Started')
for i in range(threadc):
    threads.append(Thread(target=getpast,args=[divide(usernames)[i]]))
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

with open('updated.txt','a') as f:
    f.writelines(output)

input('Finished!')
