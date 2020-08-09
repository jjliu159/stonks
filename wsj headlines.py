import requests
from bs4 import BeautifulSoup,SoupStrainer

stop = False

all_ticker = []


while stop == False:
    symbol = input(str("Enter ticker:"))
    if symbol == "end" or symbol == "":
        break;
    all_ticker.append(symbol.upper())

wsj = "https://www.wsj.com/market-data/quotes/" #wsj
#apple_wsj = "https://www.wsj.com/market-data/quotes/AAPL" #test
headers = {'User-Agent': 'Mozilla/5.0'}

for i in range(len(all_ticker)):
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
                all_time.append(res_time.get_text())
            res_headline = li.find("span", class_ = "headline") #gets the headlines
            if res_headline:
                res_title = res_headline.find("a").get_text()
                all_news.append(res_title)


    print("Ticker: ",all_ticker[i])
    for k in range(len(all_news)):
        print(all_time[k]+", "+all_news[k])
