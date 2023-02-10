# from simple_report import SimpleReport, FilterData

from inventory_report.reports.simple_report import SimpleReport, FilterData

# teste = [
#     {
#         "id": 1,
#         "nome_do_produto": "CADEIRA",
#         "nome_da_empresa": "Forces",
#         "data_de_fabricacao": "2022-04-04",
#         "data_de_validade": "2023-05-28",
#         "numero_de_serie": "FR48",
#         "instrucoes_de_armazenamento": "Conservar em local fresco",
#     },
#     {
#         "id": 2,
#         "nome_do_produto": "CADEIRA",
#         "nome_da_empresa": "Nature",
#         "data_de_fabricacao": "2018-04-04",
#         "data_de_validade": "2024-02-09",
#         "numero_de_serie": "FR48",
#         "instrucoes_de_armazenamento": "Conservar em local fresco",
#     },
#     {
#         "id": 3,
#         "nome_do_produto": "CADEIRA",
#         "nome_da_empresa": "Forces",
#         "data_de_fabricacao": "2021-04-04",
#         "data_de_validade": "2021-02-09",
#         "numero_de_serie": "FR48",
#         "instrucoes_de_armazenamento": "Conservar em local fresco",
#     },
# ]


class FilterCompleteData(FilterData):
    @staticmethod
    def get_stock_by_company(list_items: list[dict]):
        dict_company = {}
        frase = ""
        for item in list_items:
            if item["nome_da_empresa"] not in dict_company:
                dict_company[item["nome_da_empresa"]] = 1
            else:
                dict_company[item["nome_da_empresa"]] += 1

        ordenado = {
            k: v
            for k, v in sorted(
                dict_company.items(), key=lambda item: item[1], reverse=True
            )
        }

        for item in ordenado.items():
            frase += f"- {item[0]}: {item[1]}\n"

        return frase


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(list_items: list[dict]):
        oldest_date = FilterData.get_oldest_date(list_items)
        closest_date = FilterData.get_closest_date_validate(list_items)
        company_bigger_stock = FilterData.get_company_bigger_stock(list_items)
        qtd_items_by_company = FilterCompleteData.get_stock_by_company(
            list_items
        )

        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {closest_date}\n"
            f"Empresa com mais produtos: {company_bigger_stock}\n"
            f"Produtos estocados por empresa:\n"
            f"{qtd_items_by_company}"
        )


# print(CompleteReport.generate(teste))
