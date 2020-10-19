name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)

count = dict()

for line in fh:
    if line.startswith("From "):
        time = line.split()[5].split(":")
        count [time[0]] = count.get(time[0], 0) + 1

lst = list()

for k, v in count.items():
    lst.append((k, v))
lst.sort()

for hour, count in lst:
    print (hour, count)