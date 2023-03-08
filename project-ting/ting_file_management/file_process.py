import sys
from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file, instance: Queue):
    for item in instance.queue:
        if item["nome_do_arquivo"] == path_file:
            return

    list_text = txt_importer(path_file)
    dict_with_list_text = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(list_text),
        "linhas_do_arquivo": list_text,
    }
    instance.enqueue(dict_with_list_text)
    print(dict_with_list_text)


def remove(instance: Queue):
    if len(instance) == 0:
        print("Não há elementos")
        return
    first_element_in_queue_path_file = instance.search(0)["nome_do_arquivo"]
    instance.dequeue()
    print(f"Arquivo {first_element_in_queue_path_file} removido com sucesso")


def file_metadata(instance: Queue, position):
    if position > len(instance.queue) - 1 or position < 0:
        print("Posição inválida", file=sys.stderr)
        return
    print(instance.search(position))
