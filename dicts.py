name = input("Enter file: ")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
emails = list()
for line in handle:
    if not line.startswith("From ") : 
        continue
    elif line.startswith("From ") :
        line.rstrip()
        line = line.split()
        emails.append(line[1])

counts = dict()

for email in emails:
    counts[email] = counts.get(email, 0) + 1

bigcount = None
bigword = None
for email,count in counts.items() :
    if bigcount is None or count > bigcount:
        bigword = email
        bigcount = count
print(bigword, bigcount)
        