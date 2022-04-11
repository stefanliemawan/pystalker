from requests_html import HTMLSession
import requests
import os
import re
import webbrowser

def getUrlsFromGoogle(name):
    name = name.replace(" ","")
    url = f"https://www.google.com/search?q={name}%20instagram"

    session = HTMLSession()
    response = session.get(url)
    urls = response.html.absolute_links

    for url in urls:
        if "instagram.com" in url:
            username = url.split("/")[3]
            if len(username) > 3 and set(username).issubset(name):
                return url
        

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
    os.mkdir(f"./instagram_{username}")
    for img_url in img_urls:
        filename = img_url.split("/")[5].split("?")[0]
        img = requests.get(img_url).content
        with open(f"./instagram_{username}/{filename}","wb") as f:
            f.write(img)
    
def main():
    name = str(input("What is your target full name?\n")).lower()
    instagram_url = getUrlsFromGoogle(name)

    webbrowser.open_new_tab(instagram_url)
    username = instagram_url.split("/")[3]

    img_urls = getImageUrls(instagram_url)

    print(f"Downloading files from {username} instagram...")
    downloadImages(username,img_urls)
    print("Done!\n")

main()