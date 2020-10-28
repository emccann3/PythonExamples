import time
from datetime import datetime as dt 

host_path = "/etc/hosts"
redirect = "127.0.0.1"

website_list = []
blocker = input("What website would you like to block?: ")
website_list.append(blocker)
alt = input("Is there an altenative address to add?: ")

if alt is not 'No' or 'no' or 'n':
    website_list.append(alt)

while True: 
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt(dt.now().year, dt.now().month, dt.now().day, 18):
        with open(host_path, "r+") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else: 
                    file.write(redirect + " " + website + "\n")
        print("All the listed websites are blocked")
        break 
    else:
        with open(host_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                    
            file.truncate()
        print("Websites are unblocked!! Have fun!!")
        break