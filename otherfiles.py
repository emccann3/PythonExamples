# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total=0
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    elif line.startswith("X-DSPAM-Confidence:") :
        spos=line.find(' ')
        fpos=line[spos:]
        ans=float(fpos)
        total=total+ans
        count = count + 1   
print("Average spam confidence:", total/count)

