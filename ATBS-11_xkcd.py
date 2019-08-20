#! /usr/local/bin/python3

# download ALL the xkcd

import requests, bs4, os

# starting url for download
url = 'http://xkcd.com'

# folder structure for comics
os.makedirs("ATBS/ATBS-11_xkcd", exist_ok=True)

while not url.endswith("#"):

    # download the page
    print(f"Downloading page {url}...")
    # HTTP GET for url
    res = requests.get(url)
    # raise exception for error codes
    res.raise_for_status()

    # soup it up
    soup = bs4.BeautifulSoup(res.text, features="lxml")

    #print(soup)

    # Find the URL of the comic image
    comicElem = soup.select('#comic img')

    print(comicElem)


    # TODO find the next URL

    # TODO download the image

    # TODO get the prev button's url
    url = 'http://xkcd.com/#'
    continue





print("Done.")