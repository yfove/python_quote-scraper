from bs4 import BeautifulSoup
import requests
from time import sleep


url = "http://quotes.toscrape.com"
response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')
quotes = soup.select('.quote')
arr = []

for quote in quotes:
    quote_text = quote.select('.text')[0].get_text()
    # quote text is located inside a span with class of text
    author = quote.select('author')[0].get_text()
    # author name in a small tag with class author
    arr.append({
        'quote':quote_text,
        "author":author
    })

print(arr)


print(my_arr)

