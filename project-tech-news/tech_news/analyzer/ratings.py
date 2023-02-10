# Requisito 10
from tech_news.database import find_news


def top_5_categories():
    """Seu código deve vir aqui"""
    news = find_news()
    top_5_categories = []
    count_amount_categories = {}
    for new in news:
        if new["category"] not in count_amount_categories:
            count_amount_categories[new["category"]] = 1
        else:
            count_amount_categories[new["category"]] += 1

    keys_count_amout_categories = list(count_amount_categories.keys())
    keys_count_amout_categories.sort()
    sorted_dict_keys = {
        i: count_amount_categories[i] for i in keys_count_amout_categories
    }
    # https://horadecodar.com.br/2020/06/28/como-ordenar-um-dicionario-pelo-valor-no-python/
    count_amount_categories_reverse_order = {
        k: v
        for k, v in sorted(
            sorted_dict_keys.items(),
            key=lambda item: item[1],
            reverse=True,
        )
    }
    for category in count_amount_categories_reverse_order.keys():
        top_5_categories.append(category)

    if len(top_5_categories) > 5:
        return top_5_categories[0:5]
    else:
        return top_5_categories


print(top_5_categories())

# {'Ferramentas': 3, 'Categoria_0': 2, 'Novidades': 2,
# 'Categoria_7': 2, 'Categoria_9': 1}
