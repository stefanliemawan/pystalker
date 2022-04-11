import stalk_instagram
import stalk_twitter
import stalk_tiktok

def main():
    name = str(input("What is your target full name?\n")).lower()
    stalk_tiktok.stalk(name)
    stalk_twitter.stalk(name)
    stalk_instagram.stalk(name)

main()
