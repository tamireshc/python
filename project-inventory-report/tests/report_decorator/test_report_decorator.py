from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport

mock = [
    {
        "id": 1,
        "nome_do_produto": "CADEIRA",
        "nome_da_empresa": "Forces",
        "data_de_fabricacao": "2022-04-04",
        "data_de_validade": "2023-05-28",
        "numero_de_serie": "FR48",
        "instrucoes_de_armazenamento": "Conservar em local fresco",
    },
    {
        "id": 2,
        "nome_do_produto": "CADEIRA",
        "nome_da_empresa": "Nature",
        "data_de_fabricacao": "2018-04-04",
        "data_de_validade": "2024-02-09",
        "numero_de_serie": "FR48",
        "instrucoes_de_armazenamento": "Conservar em local fresco",
    },
    {
        "id": 3,
        "nome_do_produto": "CADEIRA",
        "nome_da_empresa": "Forces",
        "data_de_fabricacao": "2021-04-04",
        "data_de_validade": "2021-02-09",
        "numero_de_serie": "FR48",
        "instrucoes_de_armazenamento": "Conservar em local fresco",
    },
]


def test_decorar_relatorio():
    # color_report = ColoredReport(SimpleReport).generate(mock)
    assert (
        ColoredReport(SimpleReport).generate(mock)
        == "\033[32mData de fabricação mais antiga:\033[0m \033[36m2018-04-04"
        + "\033[0m\n"
        + "\033[32mData de validade mais próxima:\033[0m \033[36m2023-05-28"
        + "\033[0m\n"
        + "\033[32mEmpresa com mais produtos:\033[0m \033[31mForces"
        + "\033[0m"
    )
