from django.shortcuts import render
from . import scraper, weather
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
    dateNow = str(f'{date.day}.{date.month}.{date.year}')

    # retrieving the weather
    weatherNow = weather.Weather()

    return render(request, 'index.html', {
        'news': newsData,
        'newssource': newsSource,
        'date': dateNow,
        'weather': weatherNow,
        'carouselNews': carouselData,
        })


