import csv


def analyze_log(path_to_file: str):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
    try:
        with open(path_to_file) as file:
            array_data = []
            data_file = csv.reader(file)
            data = data_file
            for item in data:
                array_data.append(item)

        result1 = maria_most_ordered_dish(array_data)
        result2 = how_many_times_arnaldo_ordered_hamburguer(array_data)
        result3 = which_dishes_joao_never_ordered(array_data)
        result4 = which_days_joao_never_go_to_snake_bar(array_data)

        with open("data/mkt_campaign.txt", "w") as file:
            file.write(f"{result1}\n{result2}\n{result3}\n{result4}\n")

    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")


def maria_most_ordered_dish(data):
    dish_qtd_request = {}
    for item in data:
        if item[0] == "maria":
            if item[1] not in dish_qtd_request:
                dish_qtd_request[item[1]] = 1
            else:
                dish_qtd_request[item[1]] += 1
    return max(dish_qtd_request, key=dish_qtd_request.get)


def how_many_times_arnaldo_ordered_hamburguer(data):
    count = 0
    for item in data:
        if item[0] == "arnaldo" and item[1] == "hamburguer":
            count += 1
    return count


def which_dishes_joao_never_ordered(data):
    exist_dishes = set()
    dishes_ordered_by_joao = set()

    for item in data:
        exist_dishes.add(item[1])

    for item in data:
        if item[0] == "joao":
            dishes_ordered_by_joao.add(item[1])
    return exist_dishes - dishes_ordered_by_joao


def which_days_joao_never_go_to_snake_bar(data):
    available_days = set()
    days_joao_go_to_snake_bar = set()

    for item in data:
        available_days.add(item[2])

    for item in data:
        if item[0] == "joao":
            days_joao_go_to_snake_bar.add(item[2])
    return available_days - days_joao_go_to_snake_bar


# analyze_log("data/orders_1.csv")
