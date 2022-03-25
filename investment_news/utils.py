import datetime
from pprint import pprint
import re
from typing import Dict, List
from .models import BusinessNews
import requests
from django.conf import settings

API_KEY = settings.NEWS_API_KEY

REGEX_TO_REMOVE_CHARS = '\[\+(.*?) chars\]'
def fetch_business_news_from_news_api(date =None):
    if not date:
        date = datetime.date.today() - datetime.timedelta(days=1)
        print(date)
    url = (f'https://newsapi.org/v2/top-headlines?'
    'sources=the-wall-street-journal,business-insider,business-insider-uk,fortune'
    f'&from={date.isoformat()}'
    '&sortBy=popularity'
    f'&apiKey={API_KEY}')
    response = requests.get(url)
    
    return response.json()

def put_business_news_results_in_database(results: Dict):
    articles:List  = results['articles']
    for article in articles:
        news = BusinessNews.objects.get_or_create(
            author = article['author'],
            title = article['title'],
            source = article['source']['name'],
            description = article['description'],
            content =re.sub(REGEX_TO_REMOVE_CHARS, "",article['content']),
            url = article['url'],
            url_to_image = article['urlToImage'],
            published_at = article['publishedAt'],
        )[0]
        

def run():
    put_business_news_results_in_database(fetch_business_news_from_news_api())