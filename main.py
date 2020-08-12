import wsj_headlines
import cnbc_headlines
import display_news
import textbox

stop = False

all_ticker = []

while stop == False:
    symbol = input(str("Enter ticker:"))
    if symbol == "end" or symbol == "":
        break;
    all_ticker.append(symbol.upper())

wsj_news = wsj_headlines.grab(all_ticker)
cnbc_news = cnbc_headlines.grab(all_ticker)

all_news,company_name = [], []
all_news.append(wsj_news)
all_news.append(cnbc_news)
company_name.append("Wall Street Journal")
company_name.append("CNBC")

textbox.text(all_news,company_name)
