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
            instagram_username = url.split("/")[3]
            if len(instagram_username) > 3 and set(instagram_username).issubset(name):
                instagram_url = f"https://www.instagram.com/{instagram_username}"
                return instagram_url, instagram_username
        

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

def downloadImages(instagram_username, img_urls):
    os.mkdir(f"./instagram_{instagram_username}")
    for img_url in img_urls:
        filename = img_url.split("/")[5].split("?")[0]
        img = requests.get(img_url).content
        with open(f"./instagram_{instagram_username}/{filename}","wb") as f:
            f.write(img)
    
def main():
    name = str(input("What is your target full name?\n")).lower()
    instagram_url, instagram_username = getUrlsFromGoogle(name)

    webbrowser.open_new_tab(instagram_url)

    img_urls = getImageUrls(instagram_url)

    print(f"Downloading files from {instagram_username} instagram...")
    downloadImages(instagram_username,img_urls)
    print("Done!\n")

main()