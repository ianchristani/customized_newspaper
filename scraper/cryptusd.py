from bs4 import BeautifulSoup
from urllib.request import urlopen

# btcusd routine
def crypto_scraper():
  cryptusd = []
  
  cryptos = {'BTC':'https://www.binance.com/en/price/bitcoin',
  'ETH':'https://www.binance.com/en/price/ethereum',  
  'XRP':'https://www.binance.com/en/price/xrp'
  }

  for crpt, url in cryptos.items():

    with urlopen(url) as pg:      
      soup = BeautifulSoup(pg,'html.parser')

      quoteObj = soup.find_all(class_= 'css-12ujz79', limit=1)
      quoteObj = quoteObj[0].contents[0]

      try:
        varObj = soup.find_all(class_= 'css-4j2do9', limit=1)
        varObj = varObj[0].contents[0]
      except:
        varObj = soup.find_all(class_= 'css-12i542z', limit=1)
        varObj = varObj[0].contents[0]
      
      crpt = {'quote': quoteObj, 'var': varObj}
      cryptusd.append(crpt)
      
  
  return cryptusd
