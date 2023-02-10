from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter

from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport

import sys


def csv_converter():
    if sys.argv[2] == "simples":
        print(
            SimpleReport.generate(CsvImporter.import_data(sys.argv[1])), end=""
        )
    else:
        print(
            CompleteReport.generate(CsvImporter.import_data(sys.argv[1])),
            end="",
        )


def json_converter():
    if sys.argv[2] == "simples":
        print(
            SimpleReport.generate(JsonImporter.import_data(sys.argv[1])),
            end="",
        )
    else:
        print(
            CompleteReport.generate(JsonImporter.import_data(sys.argv[1])),
            end="",
        )


def xml_converter():
    if sys.argv[2] == "simples":
        print(
            SimpleReport.generate(XmlImporter.import_data(sys.argv[1])),
            end="",
        )
    else:
        print(
            CompleteReport.generate(XmlImporter.import_data(sys.argv[1])),
            end="",
        )


def main():
    if len(sys.argv) < 3:
        return print("Verifique os argumentos", file=sys.stderr)
    elif sys.argv[1].endswith("csv"):
        csv_converter()
    elif sys.argv[1].endswith("json"):
        json_converter()
    elif sys.argv[1].endswith("xml"):
        xml_converter()
