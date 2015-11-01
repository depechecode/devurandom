import bs4
import requests

url = raw_input("Enter a website to extract the URL's from: ")

page = requests.get(url)
page.raise_for_status()

soup = bs4.BeautifulSoup(page.text)

for link in soup.find_all('script'):      #Lists out css links
    print(link.get('src'))
    print "<!------------------------------------!>"
    