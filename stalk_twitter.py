from requests_html import HTMLSession
import re
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

def getTweets(twitter_url, twitter_username):
    session = HTMLSession()
    response = session.get(twitter_url)

    html = response.html.html
    keyword = rf"https:\/\/twitter.com/{twitter_username}/status/.+?(?=\")"

    tweet_urls = re.findall(keyword, html)

    for tweet_url in tweet_urls:
        response = session.get(tweet_url)
        response.html.render()
        print(response.html.search("tonight's"))
        break

def main():
    name = str(input("What is your target full name?\n")).lower()
    twitter_url, twitter_username = getUrlsFromGoogle(name)

    webbrowser.open_new_tab(twitter_url)

    # tweets = getTweets(twitter_url, twitter_username)


main()