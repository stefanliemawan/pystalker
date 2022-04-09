from requests_html import HTMLSession
import requests
import os
import re

def getUrlsFromGoogle(name):
    name = name.replace(" ","")
    url = f"https://www.google.com/search?q={name}%20instagram"

    session = HTMLSession()
    response = session.get(url)
    urls = response.html.absolute_links

    instagram_urls = []

    for url in urls:
        if "instagram.com" in url:
            username = url.split("/")[3]
            if set(username).issubset(name):
                instagram_urls.append(url)
    
    return instagram_urls

def getImageUrls(instagram_url):
    session = HTMLSession()
    response = session.get(instagram_url)

    html = response.html.html
    keyword = r"https:\/\/scontent.+?(?=\")"

    img_urls = re.findall(keyword, html)

    img_urls = [
        img_url.replace("amp;","").replace("\\","").replace("u0026","&")
        for img_url in img_urls
        ]

    img_urls = list(filter(lambda x: "1080x1080" in x, img_urls))

    return img_urls

def downloadImages(username,img_urls):
    os.mkdir(username)
    for img_url in img_urls:
        filename = img_url.split("/")[5].split("?")[0]
        img = requests.get(img_url).content
        with open(f"{username}/{filename}","wb") as f:
            f.write(img)
    