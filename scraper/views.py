from django.shortcuts import render
from . import scraper, weather, cryptusd
import datetime

# Create your views here.
def index(request):
    # retrieving the news
    newsData = scraper.newsScraper('title', 'https://feeds.feedburner.com/euronews/en/home/')
    newsSource = newsData[0][:-4]
    newsData = newsData[1:]
    
    # retrieving the image and news for carousel
    carouselData = scraper.imgScraper('img', 'https://www.euronews.com/')

    # getting the date now
    date = datetime.datetime.now()
    dateNow = str(date.strftime("%d.%B.%Y"))

    # retrieving the weather
    weatherNow = weather.Weather()

    # retrieving the cryptos' quote
    try:
        cryptosusd_data = cryptusd.crypto_scraper()
    except:
        cryptosusd_data = {}


    return render(request, 'index.html', {
        'news': newsData,
        'newssource': newsSource,
        'date': dateNow,
        'weather': weatherNow,
        'carouselNews': carouselData,
        'cryptosUsdData': cryptosusd_data,
        })


