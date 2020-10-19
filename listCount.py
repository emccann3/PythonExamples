fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
lst = list()
for line in fh:
    if not line.startswith("From ") : 
        continue
    elif line.startswith("From ") :
        lst = line.split()
        count = count + 1
    print(lst[1])

print("There were", count, "lines in the file with From as the first word")