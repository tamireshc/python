import pytest
from unittest.mock import patch

from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501
from tech_news.analyzer import reading_plan


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


def test_reading_plan_group_news(news_mock, group_news_for_available_mock):
    with pytest.raises(
        ValueError, match="Valor 'available_time' deve ser maior que zero"
    ):
        ReadingPlanService.group_news_for_available_time(-1)

    with patch.object(
        reading_plan,
        "find_news",
        return_value=news_mock,
    ):
        result = ReadingPlanService.group_news_for_available_time(9)
        assert result == group_news_for_available_mock
