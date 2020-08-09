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
apple_wsj = "https://www.wsj.com/market-data/quotes/AAPL" 

for i in range(len(all_ticker)):
    all_news = []
    all_time = []

    wsj_url = wsj + all_ticker[i]
    print(wsj_url)
    source_code = requests.get(apple_wsj).text
    soup = BeautifulSoup(source_code, "html.parser")
    wsj_headlines = soup.find_all()
    print(wsj_headlines)

    print("Ticker: ",all_ticker[i])
    for k in range(len(all_news)):
        print(all_time[k]+", "+all_news[k])
        


