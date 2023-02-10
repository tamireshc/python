from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        19,
        "Book",
        "TamiresSA",
        "19/10/1987",
        "19/10/2023",
        "1987",
        "ao abrigo de luz",
    )
    assert (
        str(repr(product))
        == "O produto Book fabricado em 19/10/1987 por TamiresSA com"
        + " validade até 19/10/2023 precisa ser armazenado ao abrigo de luz."
    )
