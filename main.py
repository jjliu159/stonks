import wsj_headlines
import cnbc_headlines
import display_news

stop = False

all_ticker = []

while stop == False:
    symbol = input(str("Enter ticker:"))
    if symbol == "end" or symbol == "":
        break;
    all_ticker.append(symbol.upper())

wsj_news = wsj_headlines.grab(all_ticker)
cnbc_news = cnbc_headlines.grab(all_ticker)

display_news.display(wsj_news)
display_news.display(cnbc_news)

