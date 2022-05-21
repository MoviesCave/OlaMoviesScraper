# Imports

import requests
from bs4 import BeautifulSoup
import urllib.parse as getDomain


# Function to run for getting the GdTot links


def magic():
    url = input("Media Homepage from OlaMovies - ")
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    links = soup.find_all(
        "a", {"class": "wp-block-button__link has-vivid-cyan-blue-to-vivid-purple-gradient-background has-background"})
    formattedLinks = []
    for link in links:
        eachLink = link.get('href')
        title = link.contents[0]
        formattedLinks.append(
            {
                "name": title,
                "link": "https://olamovies.uno" + eachLink
            }
        )

    for link in formattedLinks:

        def getLink():

            page = requests.get(link["link"])
            soup = BeautifulSoup(page.content, "html.parser")
            loan2host = soup.a.get('href')
            domain = getDomain.urlparse(loan2host).netloc
            if(domain == "tei.ai"):
                {
                    print(link["name"] + " - " + loan2host)
                }
            else:
                getLink()
        getLink()


magic()
