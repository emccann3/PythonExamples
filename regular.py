import re

name = open('actual.txt', 'r')
sum = 0

for l in name:
    counts = re.findall('[0-9]+', l)
    for count in counts:
        sum = sum + int(count)

print (sum)