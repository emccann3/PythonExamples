from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input('Enter: ')

html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
tag = soup("span")
sum=0
count=0
for i in tag:
	x=int(i.text)
	count+=1
	sum = sum + x
print (count)
print (sum)