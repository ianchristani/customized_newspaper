from bs4 import BeautifulSoup
from urllib.request import urlopen
import itertools

# newsscraper routine
def newsScraper(tag, url):
  contentList = []
  with urlopen(url) as pg:
    soup = BeautifulSoup(pg,'html.parser')
    contentBObj = soup.find_all(tag)

    # stringfying the items
    for item in contentBObj:
      item = str(item)
      contentList.append(item)
    
    # treating the news content
    if contentList[0][:7] == '<title>':
      content = []
      del contentList[0]
      for n in contentList:
        n = n[7:-8]
        content.append(n)     
    
    return content


# news and image scraper routine
def imgScraper(tag, url):
  contentDict = {}
  with urlopen(url) as pg:
    filtering = [
      'Facebook', 'Instagram', 'Dailymotion', 'VK', 'Linkedin', 'Youtube', 'Flipboard', 'Twitter', 'Quote open', 'Quote close',
      'services apps', 'services widgets', 'services games', ' ', 'musica', 'Cinema', 'no comment', 'Culture', 'Advertisement',
      'explore'
    ]
    
    soup = BeautifulSoup(pg,'html.parser')
    contentBObj = soup.find_all(tag)
    
    for newsAndimage in contentBObj:
      if newsAndimage['alt'] not in filtering:
        contentDict.update({newsAndimage['alt']: newsAndimage['src']})

    contentDict = dict(itertools.islice(contentDict.items(),0 ,4))
    return contentDict