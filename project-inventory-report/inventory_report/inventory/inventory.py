from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def read_data_csv(path: str, type: str):
        if type == "simples":
            return SimpleReport.generate(CsvImporter.import_data(path))
        else:
            return CompleteReport.generate(CsvImporter.import_data(path))

    @staticmethod
    def read_data_json(path: str, type: str):
        if type == "simples":
            return SimpleReport.generate(JsonImporter.import_data(path))
        else:
            return CompleteReport.generate(JsonImporter.import_data(path))

    @staticmethod
    def read_data_xml(path: str, type: str):
        if type == "simples":
            return SimpleReport.generate(XmlImporter.import_data(path))
        else:
            return CompleteReport.generate(XmlImporter.import_data(path))

    @staticmethod
    def import_data(path: str, type):
        if path.endswith("csv"):
            return Inventory.read_data_csv(path, type)
        if path.endswith("json"):
            return Inventory.read_data_json(path, type)
        if path.endswith("xml"):
            return Inventory.read_data_xml(path, type)


# print(Inventory.import_data
# ("inventory_report/data/inventory.csv", "simples"))
