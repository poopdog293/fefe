import os 
import threading
import requests, random, keep_alive
from bs4 import BeautifulSoup
from dhooks import Webhook

print("Online")
keep_alive.keep_alive()
hook = "YOUR_WEBHOOK_HERE"
#put your webhook here make sure you keep the quotes
while True:
    id = random.randint(5000000, 8500000)

    r = requests.get(f"https://www.roblox.com/groups/group.aspx?gid={id}") 
    if 'owned' not in r.text: # from the html
        re = requests.get(f"https://groups.roblox.com/v1/groups/{id}")
        print(re)
        if 'isLocked' not in re.text and 'owner' in re.text:
            if re.json()['publicEntryAllowed'] == True and re.json()['owner'] == None:
                hook.send(f'https://www.roblox.com/groups/group.aspx?gid={id}')
            else:
                print(f"\033[91m[ INVALID ] > {id}\033[39m")
