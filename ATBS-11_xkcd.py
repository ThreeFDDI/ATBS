#! /usr/local/bin/python3

# download ALL the xkcd

import requests, bs4, os

# starting url for download
url = "http://xkcd.com"

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
    
    # Find the URL of the comic image
    comicElem = soup.select('#comic img')
    
    # error if no comic image found
    if comicElem == []:
        print("Could not find comic image.")
    
    # try to download comic image
    else:
        try:
            # create current comic url from soup select
            comicURL = "http:" + comicElem[0].get("src")
            
            # download image
            print(f"Downloading image {comicURL}...")
            res = requests.get(comicURL)
            
            # raise exception for error codes
            res.raise_for_status()

        # skip pages without a comic
        except requests.exceptions.MissingSchema:

            # get link for Prev button
            prevLink = soup.select('a[rel="prev"]')[0]
            
            # set url to go to previous page
            url = "http://xkcd.com" + prevLink.get("href")
            continue
    
    # Save the image to ATBS/ATBS-11_xkcd directory
    imageFile = open(os.path.join("ATBS/ATBS-11_xkcd", os.path.basename(comicURL)), "wb")
    
    # do magic
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    
    # close image file
    imageFile.close()

    # get link for Prev button
    prevLink = soup.select('a[rel="prev"]')[0]
    
    # set url to go to previous page
    url = "http://xkcd.com" + prevLink.get("href")

    continue

print("Done.")