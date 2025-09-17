## web scraping : Web scraping is the process of automatically extracting data from websites. It typically involves:
##Sending HTTP requests to web pages.
##Downloading the HTML content.
##Parsing the HTML to find and extract specific information (such as text, links, images, tables, etc.).
##Saving or processing the extracted data for further use.
##In Python, popular libraries for web scraping include requests (for fetching web pages) and BeautifulSoup or lxml (for parsing HTML). Web scraping is widely used for data collection, price monitoring, research, and more, but always check a website’s terms of service before scraping.

## https://python.langchain.com/docs/introduction/

## https://python.langchain.com/docs/concepts/

## https://python.langchain.com/docs/tutorials/

import threading 
import requests
import bs4
from bs4 import BeautifulSoup

urls =['https://python.langchain.com/docs/introduction/',
       'https://python.langchain.com/docs/concepts/',
       'https://python.langchain.com/docs/tutorials/']

def fetch(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f'Fetched{len(soup.text)} characters from {url}')

threads = []
for url in urls:
    thread = threading.Thread(target=fetch, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All web pages fetched")


