import requests
from bs4 import BeautifulSoup,SoupStrainer


stop = False

all_ticker = []


while stop == False:
    symbol = input(str("Enter ticker:"))
    if symbol == "end" or symbol == "":
        break;
    all_ticker.append(symbol.upper())

cnbc = "https://www.cnbc.com/quotes/?symbol=" #cnbc

for i in range(len(all_ticker)):
    all_news = []
    all_time = []
    
    cnbc_url = cnbc + all_ticker[i]
    source_code = requests.get(cnbc_url).text
    soup = BeautifulSoup(source_code, "lxml")
    cnbc_headlines = soup.find_all("div",class_ = "subsection assets", id="quote_latest_from_cnbc_summary")

    for headlines in cnbc_headlines:
        subtitles = headlines.find_all("div", class_ = "assets")
        for subtitle in subtitles:
            title = subtitle.find("span").get_text()
            time = subtitle.find("span", class_ = "note").get_text()
            if title != "":
                all_news.append(title)
                all_time.append(time)
