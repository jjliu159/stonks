import requests
from bs4 import BeautifulSoup,SoupStrainer

wsj_news = []
hyper_link = []

wsj = "https://www.wsj.com/market-data/quotes/" #wsj
headers = {'User-Agent': 'Mozilla/5.0'} #need header so that it doesnt return page error for wsj

def grab(all_ticker):
    for i in range(len(all_ticker)): #Wall Street Journal
        all_news = []
        all_time = []

        wsj_url = wsj + all_ticker[i]
        source_code = requests.get(wsj_url,headers=headers).text
        soup = BeautifulSoup(source_code, "lxml")
        wsj_headlines = soup.find_all("div", class_ = "contentFrame")

        for headlines in wsj_headlines:
            li_headlines = headlines.find_all("li")
            for li in li_headlines:
                res_time = li.find("li", class_ = "cr_dateStamp")#get the text from time <li>
                if res_time:
                    if "hour" in res_time.get_text(): #check for most recent, the same day, wsj has difference between hour and hours
                        all_time.append(res_time.get_text())
                        res_headline = li.find("span", class_ = "headline") #gets the headlines

                        res_find_link = res_headline.find("a")
                        res_link = res_find_link.get("href")

                        hyper_link.append(res_link)
                        if res_headline:
                            res_title = res_headline.find("a").get_text()
                            all_news.append(res_title)

    for k in range(len(all_news)):
        wsj_news.append((all_time[k]+", "+all_news[k]))
    return wsj_news,hyper_link
