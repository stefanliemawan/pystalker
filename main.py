import stalk_name
import stalk_instagram

def main():
    name = "erlina tivania"

    urls_from_google = stalk_name.getUrlsFromGoogle(name)
    print(urls_from_google)

    instagram_urls_from_google = stalk_instagram.getUrlsFromGoogle(name)
    print(instagram_urls_from_google)

    for instagram_url in instagram_urls_from_google:
        username = instagram_url.split("/")[3]
        img_urls = stalk_instagram.getImageUrls(instagram_url)
        stalk_instagram.downloadImages(username,img_urls)


main()