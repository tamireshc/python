import time
from parsel import Selector
import requests
from requests.exceptions import HTTPError, MissingSchema
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    time.sleep(1)
    try:
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )
        if response.status_code != 200:
            return None
        else:
            return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""
    try:
        seletor = Selector(html_content)
        urls = seletor.css(".entry-title a::attr(href)").getall()
        return urls
    except (HTTPError, MissingSchema):
        return []


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    seletor = Selector(html_content)
    url_next = seletor.css(".next::attr(href)").get()
    return url_next


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    seletor = Selector(html_content)
    dict_news = {}
    sumary = ""
    first_p = seletor.css(
        "div.entry-content > p:first-of-type *::text"
    ).getall()

    for item in first_p:
        sumary += item

    dict_news["url"] = seletor.css(
        "div.pk-share-buttons-wrap::attr(data-share-url)"
    ).get()
    dict_news["title"] = seletor.css(".entry-title::text").get().strip()
    dict_news["timestamp"] = seletor.css(".meta-date::text").get()
    dict_news["writer"] = seletor.css("span.author > a::text").get()
    dict_news["reading_time"] = int(
        seletor.css("li.meta-reading-time::text").get().split()[0]
    )
    dict_news["summary"] = sumary.strip()

    dict_news["category"] = seletor.css(
        "div.meta-category a span.label::text"
    ).get()

    return dict_news


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    URL_BASE = "https://blog.betrybe.com"
    result = []
    while URL_BASE and len(result) < amount:
        response = fetch(URL_BASE)
        urls = scrape_updates(response)
        for url in urls:
            if len(result) < amount:
                notice = scrape_news(fetch(url))
                result.append(notice)
            else:
                ...
        URL_BASE = scrape_next_page_link(response)
    create_news(result)
    return result


# print(scrape_updates(fetch("")))
# print(fetch("https://blog.betrybe.cm/"))
# print(scrape_next_page_link(fetch("https://blog.betrybe.com/")))
# print(
#     scrape_news(
#         fetch(
#             "https://blog.betrybe.com/noticias/bill-gates-e-cetico-sobre-criptomoedas-e-nfts-entenda-o-motivo/"
#         )
#     )
# # )
# print(get_tech_news(13))
