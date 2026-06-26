from django.conf import settings
from newsapi import NewsApiClient
from newsapi.newsapi_exception import NewsAPIException


def _get_api_key() -> str:
    api_key = (getattr(settings, "NEWS_API_KEY", "") or "").strip().strip('"').strip("'")
    if not api_key:
        raise ValueError("NEWS_API_KEY is not set.")
    return api_key


def get_news_client() -> NewsApiClient:
    return NewsApiClient(api_key=_get_api_key())


def get_category_articles(category: str, country: str = "us") -> list[dict]:
    client = get_news_client()
    try:
        response = client.get_top_headlines(category=category, country=country)
    except NewsAPIException as e:
        raise RuntimeError(f"NewsAPI error: {e}") from e
    return response.get("articles", [])

#test for API connectivity
        #response = client.get_top_headlines(q="news") 
    #except NewsAPIException as e:
        #raise RuntimeError(f"NewsAPI error: {e}") from e
    #return response.get("articles", [])