import requests
from bs4 import BeautifulSoup


def metar_get(aic):

    url = "https://www.aviationweather.gov/metar/data?ids=" + aic + "&format=raw&date=&hours=0"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="awc_main_content_wrap")

    rawmetar = results.find("code")
    metar = str(rawmetar)[6:]
    metar = str(metar)[:-7]

    return metar

