import bs4
import requests, time

url = raw_input("Enter a website to extract the URL's from: ")

page = requests.get(url)
page.raise_for_status()

soup = bs4.BeautifulSoup(page.text)

for link in soup.find_all('script'):      #Lists out js links
    print(link.get('src'))
    print "<!------------------------------------!>"

print "*"    
print "Searching for API Endpoints.."
time.sleep(5)




