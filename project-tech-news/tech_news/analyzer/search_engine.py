# Requisito 7
from tech_news.database import find_news
from datetime import datetime


def search_by_title(title: str):
    """Seu código deve vir aqui"""
    news = find_news()
    news_by_title = []
    for new in news:
        if title.lower() in new["title"].lower():
            news_by_title.append((new["title"], new["url"]))
    return news_by_title


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        date_from_str_date = datetime.strptime(date, "%Y-%m-%d").date()
        converter_date_to_format = date_from_str_date.strftime("%d/%m/%Y")
        news = find_news()
        news_by_date = []
        for new in news:
            if converter_date_to_format in new["timestamp"]:
                news_by_date.append((new["title"], new["url"]))
        return news_by_date
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category: str):
    """Seu código deve vir aqui"""
    news = find_news()
    news_by_category = []
    for new in news:
        if category.lower() in new["category"].lower():
            news_by_category.append((new["title"], new["url"]))
    return news_by_category


# print(search_by_title("software"))
# print(search_by_category("novidades"))
#
