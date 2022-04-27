import requests
from bs4 import BeautifulSoup

# object/list of The Hacker New URLS
THN_URLS = {
    "base": "https://thehackernews.com/",
    "maxd": "https://thehackernews.com/search?updated-max=5000-01-01T22:40:00-08:00&max-results=30"
}

def get(optimal=False):
    global THN_URLS

    URL = THN_URLS["base"]
    if optimal == False:
        URL = THN_URLS["maxd"]

    # credit: https://realpython.com/beautiful-soup-web-scraper-python/
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    filtered_htmls = soup.find_all("div", class_="body-post clear")

    cdata = []
    for segment in filtered_htmls:

        line = str(segment).split("\n")

        # filter out article's url:
        url = line[1]
        url = url[url.find("https://"): url.find('\">')]

        # filter out article's title:
        title = line[5]
        title = title[title.find('<img alt="')+len('<img alt="'):title.find('" decoding="async')]

        # filter out article's published date:
        date = line[9]
        date = date[date.find('</i>')+len('</i>'):date.find('<span><i')]

        # filter out article's detail (some of it's detail):
        detail = line[11]
        detail = detail[detail.find('<div class="home-desc"> ')+len('<div class="home-desc"> '):detail.find('</div>')]

        cdata.append({"url": url, "title": title, "date": date, "details": detail})
    
    return cdata

