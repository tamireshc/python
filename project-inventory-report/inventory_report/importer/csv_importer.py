# from importer import Importer
import csv

from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(path: str):
        if not path.endswith("csv"):
            raise ValueError("Arquivo inválido")
        else:
            with open(path, mode="r") as file:
                result = []

                data_reader = csv.reader(file)
                header, *data = data_reader
                for row in data:
                    report = {}
                    # print(row)
                    for i, head in enumerate(header):
                        report[head] = row[i]
                    result.append(report)
                return result
