import pytest


@pytest.fixture(scope="module")
def news_mock():
    return [
        {
            "url": "https://blog.betrybe.com/novidades/noticia-bacana",
            "title": "Notícia bacana",
            "timestamp": "04/04/2021",
            "writer": "Eu",
            "reading_time": 4,
            "summary": "Algo muito bacana aconteceu",
            "category": "Ferramentas",
        },
        {
            "url": "https://blog.betrybe.com/novidades/noticia-bacana",
            "title": "Notícia bacana2",
            "timestamp": "04/04/2021",
            "writer": "Eu",
            "reading_time": 5,
            "summary": "Algo muito bacana aconteceu",
            "category": "Tecnologia",
        },
        {
            "url": "https://blog.betrybe.com/novidades/noticia-bacana",
            "title": "Notícia bacana3",
            "timestamp": "04/04/2021",
            "writer": "Eu",
            "reading_time": 10,
            "summary": "Algo muito bacana aconteceu",
            "category": "Ferramentas",
        },
    ]


@pytest.fixture(scope="module")
def group_news_for_available_mock():
    return {
        "readable": [
            {"chosen_news": [("Notícia bacana", 4)], "unfilled_time": 5},
            {"chosen_news": [("Notícia bacana2", 5)], "unfilled_time": 4},
        ],
        "unreadable": [("Notícia bacana3", 10)],
    }
