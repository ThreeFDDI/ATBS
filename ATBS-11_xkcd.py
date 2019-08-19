#! /usr/local/bin/python3

# download ALL the xkcd

import requests, bs4, os

# starting url for download
url = 'http://xkcd.com'

# folder structure for comics
os.makedirs("ATBS-11_xkcd", exist_ok=True)

while not url.endswith("#"):
    url = 'http://xkcd.com/#'
    continue

    # TODO download page

    # TODO find the next URL

    # TODO download the image

    # TODO get the prev button's url





print("Done.")