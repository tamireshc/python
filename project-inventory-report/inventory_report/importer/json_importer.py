# from importer import Importer
import json

from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(path: str):
        if not path.endswith("json"):
            raise ValueError("Arquivo inválido")
        else:
            with open(path, mode="r") as file:
                result = json.load(file)
                return result
