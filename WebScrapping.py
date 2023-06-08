import requests
import bs4
#report = requests.get("www.amazon.com")
res = requests.get("http://quotes.toscrape.com/")
res.text
soup = bs4.BeautifulSoup(res.text,'lxml')
soup.select(".author")
authors = set()
for name in soup.select(".author"):
    authors.add(name.text)

quotes = []
for quote in soup.select(".text"):
    quotes.append(quote.text)

soup = bs4.BeautifulSoup(res.text,'lxml')
soup.select('.tag-item')
for item in soup.select(".tag-item"):
    print(item.text)