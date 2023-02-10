# from importer import Importer
import xmltodict

from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(path: str):
        if not path.endswith("xml"):
            raise ValueError("Arquivo inválido")
        else:
            with open(path) as file:
                result = xmltodict.parse(file.read())
                final_result = result["dataset"]["record"]
                return final_result
