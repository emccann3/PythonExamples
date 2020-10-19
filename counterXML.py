from urllib.request import urlopen
import xml.etree.ElementTree as ET

url = input("Enter Url: ")
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_471971.xml"
print ("Retrieving " + url)

xml = urlopen(url).read()
print ("Retrieved: " + str(len(xml)) + " characters")

et = ET.fromstring(xml)

counts =  et.findall('.//count')
print ("Count: " + str(len(counts)))

sum = 0

for count in counts:
    sum += int(count.text)

print ("Sum:" + str(sum))