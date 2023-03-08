import sys


def txt_importer(path_file):
    try:
        if not path_file.endswith(".txt"):
            print("Formato inválido", file=sys.stderr)
        else:
            with open(path_file, "r") as file:
                text = file.read()
                text_list = text.split("\n")
                return text_list
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)


# print(txt_importer("staics/arquivo_teste.txt"))
