from requests_html import HTMLSession
import re
import webbrowser

def getUrlsFromGoogle(name):
    name = name.replace(" ","")
    url = f"https://www.google.com/search?q={name}%20tiktok"
    
    session = HTMLSession()
    response = session.get(url)
    urls = response.html.absolute_links

    for url in urls:
        if "tiktok.com" in url:
            tiktok_username = url.split("/")[3].split("?")[-1][1:]
            if len(tiktok_username) > 3 and set(tiktok_username).issubset(name):
                tiktok_url =  f"https://tiktok.com/@{tiktok_username}"
                return tiktok_url, tiktok_username

    return None, None

def stalk(name):
    tiktok_url, tiktok_username = getUrlsFromGoogle(name)

    if tiktok_url:
        webbrowser.open_new_tab(tiktok_url)
