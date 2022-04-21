<h1 align="center">The Hacker News API</h1>
<p align="center">
  <img width="1000" src="./assets/logo.png">
</p>


## About:
- The Hacker News (THN) is a cybersecurity news platform.
- THN is a news platform that me and a lot of people use to get news on the latest cyber security news, but THN does not have an official API. THN does post regular updates on their Twitter account so you could use the Twitter API to get news from THN but that Twitter API is a bit complicated to use.
- Due to this, I made this basic API that scraps information from THN's website.
- Currently this THN api only has a GET feature which grabs the latest news posted on The Hacker News (THN) website.
  - The GET feature grabs the following information from a single article: title, date published, link to article, and a short description of the article. 

## Notes:
- Due to this API relying on web scrapping; if THN changes their website then the scrapping function for the GET feature might fail to scrap proper article information from the offical THN website. Due to this, this API needs to be maintained regularly.
- After using this API for about 2 months, I only had to fix the scrapping algorithm twice. These bug fixes only took less then half an hour each to fix. Due, at the moment, maintaining this API is not too beig of an issue. 

## Issues:
- THN scraps an article's title, date published, and link to article perfectly. But it struggles with scrapping the description for an article. Well scrapping the description of the article, the api leaves behind some html codes in the description text.

## Requirements:
- python3:
    - pip install beautifulsoup4
    - pip install requests
- services:
    - website: https://thehackernews.com/

## Sources:
- https://thehackernews.com/
- https://realpython.com/beautiful-soup-web-scraper-python/


