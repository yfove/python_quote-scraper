from bs4 import BeautifulSoup
import requests
from time import sleep


# url = "http://quotes.toscrape.com"
# response = requests.get(url).text
# soup = BeautifulSoup(response, 'html.parser')
# quotes = soup.select('.quote')
# arr = []

# for quote in quotes:
#     quote_text = quote.select('.text')[0].get_text()
#     # quote text is located inside a span with class of text
#     author = quote.select('author')[0].get_text()
#     # author name in a small tag with class author
#     arr.append({
#         'quote':quote_text,
#         "author":author
#     })

# print(arr)

def fetch_quotes():
    website_url = "http://quotes.toscrape.com"
    response = requests.get(website_url).text
    soup = BeautifulSoup(response, 'html.parser')
    arr = []
    next_page_url = soup.select('.next')
    while next_page_url:
        quotes = soup.select('.quote')
        for quote in quotes:
            quote_text = quote.select('.text')[0].get_text()
            author = quote.select('.author')[0].get_text()
            arr.append({
                "quote": quote_text,
                "author": author
            })
        try: 
        # lets you test a block of code for errors. Except lets you handle the error
        # else lets you execute the code when there is not error
        # finally lets you execute code regardless
            next_page_url = soup.select('.next')[0].select('a')[0]['href']
            sleep(1)
            # method to suspend execution of a program for 1 second
        except IndexError:
            next_page_url = None
    return arr

my_arr = fetch_quotes()
print(my_arr)

