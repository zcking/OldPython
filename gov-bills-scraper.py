import requests
from bs4 import BeautifulSoup

url = "https://www.congress.gov/resources/display/content/Most-Viewed+Bills"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
i = 0
howmany = 0
for bill in soup.find_all("td", {"class":"confluenceTd"}):
	try:
		print(bill.text)
	except:
		print("ERROR")
	i+=1
	howmany+=1
	if i == 3:
		print("\n")
		i = 0
	if howmany == 30:
		break