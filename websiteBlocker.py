from datetime import datetime as dt
import time

host_temp ="hosts"
host_path = "C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

websites= ["www.facebook.com","facebook.com", "www.instagram.com", "instagram.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,21):
        print ("Working hours...")
        with open(host_path,'r+') as file:
            content=file.read()
            for site in websites:
                if site in content:
                    pass
                else:
                    file.write(redirect+" "+site+"\n")
    else: 
         with open(host_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(site in line for site in websites):
                    file.write(line)
            file.truncate()
    print("Fun hours...")
    time.sleep(5)