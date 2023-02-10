# Requisitos 11 e 12
from tech_news.analyzer.ratings import top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_category,
    search_by_date,
    search_by_title,
)
from tech_news.scraper import get_tech_news
import sys


def option0():
    option = input("Digite quantas notícias serão buscadas:")
    get_tech_news(option)


def option1():
    option = input("Digite o título:")
    search_by_title(option)


def option2():
    option = input("Digite a data no formato aaaa-mm-dd:")
    search_by_date(option)


def option3():
    option = input("Digite a categoria:")
    search_by_category(option)


def option4():
    top_5_categories()


def option5():
    print("Encerrando script")


ob = {
    "0": option0,
    "1": option1,
    "2": option2,
    "3": option3,
    "4": option4,
    "5": option5,
}


def return_input(n):
    if n == "0" or n == "1" or n == "2" or n == "3" or n == "4" or n == "5":
        ob[n]()
    else:
        return print("Opção inválida", file=sys.stderr)


def analyzer_menu():
    """Seu código deve vir aqui"""
    option = input(
        "Selecione uma das opções a seguir:\n"
        + " 0 - Popular o banco com notícias;\n"
        + " 1 - Buscar notícias por título;\n"
        + " 2 - Buscar notícias por data;\n"
        + " 3 - Buscar notícias por categoria;\n"
        + " 4 - Listar top 5 categorias;\n"
        + " 5 - Sair."
    )
    return_input(option)


# analyzer_menu()
