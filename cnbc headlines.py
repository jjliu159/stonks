import requests
from bs4 import BeautifulSoup,SoupStrainer

cnbc_news = []

cnbc = "https://www.cnbc.com/quotes/?symbol=" #cnbc

def grab(all_ticker):
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
                    if "hr" in time: #check for most recent, the same day
                        all_news.append(title)
                        all_time.append(time)

    for k in range(len(all_news)):
        cnbc_news.append((all_time[k]+", "+all_news[k]))

    return cnbc_news
