import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession

url = "https://www.google.com/search?q=erlina%20tivania"

session = HTMLSession()
response = session.get(url)
links = response.html.absolute_links
links = list(filter(lambda x: "google.com" not in x, links))
print(links)
# html = response.html.html