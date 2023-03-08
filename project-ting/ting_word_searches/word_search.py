from ting_file_management.queue import Queue


def exists_word(word: str, instance: Queue):
    return_list = []
    dict_item = {}

    for item in instance.queue:
        line_of_occurrence = []
        for index, element in enumerate(item["linhas_do_arquivo"]):
            # print(element)
            if word.lower() in element.lower():
                line_of_occurrence.append({"linha": index + 1})
        # print("item", line_of_occurrence)
        if len(line_of_occurrence) > 0:
            dict_item["palavra"] = word
            dict_item["arquivo"] = item["nome_do_arquivo"]
            dict_item["ocorrencias"] = line_of_occurrence
            # print(dict_item)
            return_list.append(dict_item)
    return return_list


def search_by_word(word, instance):
    return_list = []
    dict_item = {}

    for item in instance.queue:
        line_of_occurrence = []
        for index, element in enumerate(item["linhas_do_arquivo"]):
            # print(element)
            if word.lower() in element.lower():
                line_of_occurrence.append(
                    {"linha": index + 1, "conteudo": element}
                )
        # print("item", line_of_occurrence)
        if len(line_of_occurrence) > 0:
            dict_item["palavra"] = word
            dict_item["arquivo"] = item["nome_do_arquivo"]
            dict_item["ocorrencias"] = line_of_occurrence
            # print(dict_item)
            return_list.append(dict_item)
    return return_list


# project = Queue()
# process("statics/nome_pedro.txt", project)
# print(exists_word("pedro", project))
