from requests_html import HTMLSession

def getUrlsFromGoogle(name):
    name = name.replace(" ","%20")
    url = f"https://www.google.com/search?q={name}"

    session = HTMLSession()
    response = session.get(url)
    urls = response.html.absolute_links
    urls = list(filter(lambda x: "google.com" not in x, urls))
    
    return urls

def main():
    name = "madison beer"

    urls_from_google = getUrlsFromGoogle(name)
    print(urls_from_google)

main()