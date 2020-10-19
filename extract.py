from urllib.request import urlopen
import json

url = input("Enter url: ")
print("Retrieving ", url)
data = urlopen(url).read().decode('utf-8')
print('Retrieved', len(data), 'characters')
json_obj = json.loads(data)

sum = 0
total = 0

for comment in json_obj["comments"]:
    sum += int(comment["count"])
    total += 1

print('Count:', total)
print('Sum:', sum)