from inventory_report.inventory.product import Product


def test_cria_produto():
    produto_teste = Product(
        19,
        "Book",
        "TamiresSA",
        "19/10/1987",
        "19/10/2023",
        "1987",
        "mantenha aquecido",
    )

    assert produto_teste.id == 19
    assert produto_teste.nome_do_produto == "Book"
    assert produto_teste.nome_da_empresa == "TamiresSA"
    assert produto_teste.data_de_fabricacao == "19/10/1987"
    assert produto_teste.data_de_validade == "19/10/2023"
    assert produto_teste.numero_de_serie == "1987"
    assert produto_teste.instrucoes_de_armazenamento == "mantenha aquecido"
