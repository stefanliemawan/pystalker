from requests_html import HTMLSession
import webbrowser

def getUrlsFromGoogle(name):
    name = name.replace(" ","")
    url = f"https://www.google.com/search?q={name}%20twitter"

    session = HTMLSession()
    response = session.get(url)
    urls = response.html.absolute_links

    for url in urls:
        if "twitter.com" in url:
            twitter_username = url.split("/")[3].split("?")[0]
            if len(twitter_username) > 3 and set(twitter_username).issubset(name):
                twitter_url = f"https://twitter.com/{twitter_username}"
                return twitter_url, twitter_username

    return None, None

def stalk(name):
    twitter_url, twitter_username = getUrlsFromGoogle(name)

    if twitter_url:
        webbrowser.open_new_tab(twitter_url)

    # tweets = getTweets(twitter_url, twitter_username)

