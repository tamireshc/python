from datetime import datetime


class FilterData:
    @staticmethod
    def get_oldest_date(list_items: list[dict]):
        oldest_date = ""
        count_oldest_date = 0

        for item in list_items:
            if (
                (
                    datetime.now()
                    - datetime.strptime(item["data_de_fabricacao"], "%Y-%m-%d")
                ).days
            ) > count_oldest_date:
                oldest_date = item["data_de_fabricacao"]
                count_oldest_date = (
                    datetime.now()
                    - datetime.strptime(item["data_de_fabricacao"], "%Y-%m-%d")
                ).days
        return oldest_date

    @staticmethod
    def get_closest_date_validate(list_items: list[dict]):
        list_closet_days_complete = []
        list_closet_days_just_positives = []
        closest_date = ""
        index = 0
        for item in list_items:
            list_closet_days_complete.append(
                (
                    datetime.strptime(item["data_de_validade"], "%Y-%m-%d")
                    - datetime.now()
                ).days
            )
            if (
                (
                    datetime.strptime(item["data_de_validade"], "%Y-%m-%d")
                    - datetime.now()
                ).days
            ) > 0:
                list_closet_days_just_positives.append(
                    (
                        datetime.strptime(item["data_de_validade"], "%Y-%m-%d")
                        - datetime.now()
                    ).days
                )
                max_value = min(list_closet_days_just_positives)
                index = list_closet_days_complete.index(max_value)
                closest_date = list_items[index]["data_de_validade"]
        return closest_date

    @staticmethod
    def get_company_bigger_stock(list_items: list[dict]):
        dict_company = {}
        count = 0
        big_company = ""
        for item in list_items:
            if item["nome_da_empresa"] not in dict_company:
                dict_company[item["nome_da_empresa"]] = 1
            else:
                dict_company[item["nome_da_empresa"]] += 1

        for item in dict_company.items():
            if item[1] > count:
                big_company = item[0]
                count = item[1]
            else:
                pass
        return big_company


class SimpleReport:
    @staticmethod
    def generate(list_items: list[dict]):
        oldest_date = FilterData.get_oldest_date(list_items)
        closest_date = FilterData.get_closest_date_validate(list_items)
        company_bigger_stock = FilterData.get_company_bigger_stock(list_items)

        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {closest_date}\n"
            f"Empresa com mais produtos: {company_bigger_stock}"
        )


# print(SimpleReport.generate(teste))
# print((datetime.now() - datetime.strptime("2022-04-04", "%Y-%m-%d")).days)
