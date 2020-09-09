import wsj_headlines
import cnbc_headlines
import display_news
import textbox

stop = False

all_ticker = []

while stop == False:
    symbol = input(str("Enter ticker:"))
    if symbol == "end" or symbol == "":
        break
    all_ticker.append(symbol.upper())

wsj_news,wsj_news_links = wsj_headlines.grab(all_ticker)

cnbc_news,cnbc_news_links = cnbc_headlines.grab(all_ticker)

print(wsj_news,wsj_news_links)

all_news,company_name,all_news_link = [], [], []
all_news.append(wsj_news)
all_news.append(cnbc_news)
all_news_link.append(wsj_news_links)
all_news_link.append(cnbc_news_links)
company_name.append("Wall Street Journal")
company_name.append("CNBC")

print(all_news_link,all_news,company_name)

textbox.text(all_news,company_name,all_news_link)
